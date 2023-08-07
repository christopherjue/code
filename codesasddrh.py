import sounddevice as sd
import numpy as np
import pygame

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Note frequencies (Hz)
NOTE_FREQUENCIES = {
    pygame.K_a: 261.63,  # C4
    pygame.K_s: 293.66,  # D4
    pygame.K_d: 329.63,  # E4
    pygame.K_f: 349.23,  # F4
    pygame.K_g: 392.00,  # G4
    pygame.K_h: 440.00,  # A4
    pygame.K_j: 493.88,  # B4
    pygame.K_k: 523.25,  # C5
    pygame.K_l: 587.33,  # D5
    pygame.K_SEMICOLON: 659.25,  # E5
    pygame.K_QUOTE: 698.46,  # F5
    pygame.K_LEFTBRACKET: 783.99,  # G5
    pygame.K_RIGHTBRACKET: 880.00,  # A5
    pygame.K_BACKSLASH: 987.77,  # B5
    pygame.K_z: 1046.50,  # C6
    pygame.K_x: 1174.66,  # D6
    pygame.K_c: 1318.51,  # E6
    pygame.K_v: 1396.91,  # F6
    pygame.K_b: 1567.98,  # G6
    pygame.K_n: 1760.00,  # A6
    pygame.K_m: 1975.53  # B6
}

# Keyboard layout
KEYS_LAYOUT = [
    (pygame.K_z, "C4"), (pygame.K_x, "D4"), (pygame.K_c, "E4"), (pygame.K_v, "F4"),
    (pygame.K_b, "G4"), (pygame.K_n, "A4"), (pygame.K_m, "B4"), (pygame.K_a, "C5"),
    (pygame.K_s, "D5"), (pygame.K_d, "E5"), (pygame.K_f, "F5"), (pygame.K_g, "G5"),
    (pygame.K_h, "A5"), (pygame.K_j, "B5"), (pygame.K_k, "C6"), (pygame.K_l, "D6"),
    (pygame.K_SEMICOLON, "E6"), (pygame.K_QUOTE, "F6"), (pygame.K_LEFTBRACKET, "G6"),
    (pygame.K_RIGHTBRACKET, "A6"), (pygame.K_BACKSLASH, "B6")
]

# Set up the piano keys
key_width = WIDTH // len(KEYS_LAYOUT)
keys = []
for i, (key, note) in enumerate(KEYS_LAYOUT):
    key_rect = pygame.Rect(i * key_width, HEIGHT // 2, key_width, HEIGHT // 2)
    key_data = (key_rect, key, note)
    keys.append(key_data)

# Active keys dictionary
active_keys = {}

# Set up sound parameters
duration = 1.0  # Note duration in seconds
sampling_rate = 44100  # Audio sampling rate
t = np.linspace(0, duration, int(duration * sampling_rate), False)

# Generate audio samples for each note frequency
note_samples = {}
for key, frequency in NOTE_FREQUENCIES.items():
    note_samples[key] = np.sin(frequency * 2 * np.pi * t)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in NOTE_FREQUENCIES:
                # Play the note when a key is pressed
                samples = note_samples[event.key]
                sd.play(samples, sampling_rate, blocking=False)
                active_keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in active_keys:
                # Stop playing the note when a key is released
                del active_keys[event.key]
                if len(active_keys) == 0:
                    sd.stop()

    # Update the display
    window.fill(WHITE)
    for key_rect, key, note in keys:
        color = GRAY if key in active_keys else BLACK
        pygame.draw.rect(window, color, key_rect)
        pygame.draw.rect(window, WHITE, key_rect, 1)
        label = pygame.font.SysFont(None, 20).render(note, True, BLACK)
        label_rect = label.get_rect(center=key_rect.center)
        window.blit(label, label_rect)

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
