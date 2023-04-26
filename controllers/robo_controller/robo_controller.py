from controller import Robot, Keyboard, Motion

robot = Robot()
timestep = 32
key = -1
keyboard= Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')

print("Press up")

while robot.step(timestep!= -1):
    key = Keyboard.getKey()
    
    if key == Keyboard.UP:
        wave.play()


