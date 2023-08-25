import time
import pydirectinput

def god_bridge():
    # Adjust these values to match your screen resolution and sensitivity
    bridge_length = 5  # Number of blocks to bridge
    bridge_delay = 0.1  # Time delay between block placements (in seconds)
    bridge_height = 2  # Height of the bridge (use 2 for god bridging)
    move_distance = 30  # Distance to move forward while bridging
    
    # Position the cursor at the edge of the block
    pydirectinput.moveRel(x=10, y=10)
    
    for _ in range(bridge_length):
        # Place a block and wait
        pydirectinput.mouseDown()
        time.sleep(bridge_delay)
        pydirectinput.mouseUp()
        time.sleep(bridge_delay)
        
        # Move forward
        pydirectinput.keyDown('w')
        time.sleep(bridge_delay * 2)  # Adjust this if needed
        pydirectinput.keyUp('w')
        time.sleep(bridge_delay)
    
    # Move up for the god bridge
    pydirectinput.keyDown('space')
    time.sleep(bridge_height * bridge_delay)
    pydirectinput.keyUp('space')
    
    # Move forward to complete the bridge
    pydirectinput.keyDown('w')
    time.sleep(move_distance * bridge_delay)
    pydirectinput.keyUp('w')

def click_back_to_game():
    # You'll need to find the exact coordinates of the "Back to Game" button on your screen
    back_to_game_button_x = 100
    back_to_game_button_y = 100
    
    # Move the cursor and click the button
    pydirectinput.moveTo(back_to_game_button_x, back_to_game_button_y)
    pydirectinput.click()

# Wait a few seconds before starting the process
time.sleep(5)

# Call the functions to perform god bridging and click "Back to Game"
god_bridge()
click_back_to_game()
