import time
import pydirectinput

x_back_to_game = 100  # Adjust x-coordinate for the "Back to Game" button
y_back_to_game = 100  # Adjust y-coordinate for the "Back to Game" button

def bridge_forward():
    for _ in range(10):
        pydirectinput.keyDown('w')
        time.sleep(0.05)
        pydirectinput.keyUp('w')
        time.sleep(0.05)

def bridge_backward():
    for _ in range(10):
        pydirectinput.keyDown('s')
        time.sleep(0.05)
        pydirectinput.keyUp('s')
        time.sleep(0.05)

def jump():
    pydirectinput.keyDown('space')
    time.sleep(0.2)  # Adjust the duration as needed
    pydirectinput.keyUp('space')

def place_blocks():
    for _ in range(10):
        pydirectinput.mouseDown()
        time.sleep(0.05)
        pydirectinput.mouseUp()
        time.sleep(0.05)

# Example: Esc key to "Back to Game"
def back_to_game():
    pydirectinput.press('esc')
    time.sleep(0.5)  # Adjust the delay based on game responsiveness
    pydirectinput.click(x_back_to_game, y_back_to_game)  # Click "Back to Game" button

# Perform the actions
back_to_game()  # Press Esc and click "Back to Game"
time.sleep(2)  # Give time for the game to load

bridge_backward()  # Move backward
bridge_forward()  # Move forward
jump()  # Jump
bridge_backward()  # Move backward
place_blocks()  # Place blocks
bridge_forward()  # Move forward










