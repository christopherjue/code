import pydirectinput as p
import time

p.click(2000, 1100)
time.sleep(1)

p.mouseDown()
time.sleep(1)
p.mouseUp()


p.move (0,250)


print("done")