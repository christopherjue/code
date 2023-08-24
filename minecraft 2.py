#auto mine bot
import pydirectinput as p
import time





def mineblock():
     p.mouseDown()
     print("mining")
     time.sleep(1)
     p.mouseUp()


def walkforward():
     print("walking")
     p.keyDown('shift')
     p.keyDown('w')
     time.sleep(1)
     p.keyUp('w')
     time.sleep(0.5)
     p.keyUp('shift')
     time.sleep(0.5)

#program begin
#counter
counter=0

#resume game
p.click(2500,500)
time.sleep(1)

while counter < 1:
     mineblock()
     p.moveRel(0,-300)
     mineblock()
     p.moveRel(0, 300)
     walkforward()
     counter += 1

print("done")