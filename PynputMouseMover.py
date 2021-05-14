from pynput.keyboard import Listener, Key
from pynput.mouse import Controller
import math
import time


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False


def square(mouseCon, r, l, u, d, speed, displacementX, displacementY, currentPosition, startPosition):
    global up
    global down
    global left
    global right
    startX = startPosition[0]
    startY = startPosition[1]
    # pretty self explanatory really, updates mouse position. that's it
    currentX = currentPosition[0]
    currentY = currentPosition[1]
    if r:
        mouseCon.move(speed, 0)
        if currentX > startX + displacementX:
            right = False
            down = True

    elif l:
        mouseCon.move(-speed, 0)
        if currentX < startX:
            left = False
            up = True

    elif d:
        mouseCon.move(0, speed)
        if currentY > startY + displacementY:
            down = False
            left = True

    elif u:
        mouseCon.move(0, -speed)
        if currentY < startY:
            up = False
            right = True


def circle(mouseCon, startPosition, radius, degree, speed):
    startX = startPosition[0]
    startY = startPosition[1]
    X = startX + radius * math.cos(math.radians(degree))
    Y = startY + radius * math.sin(math.radians(degree))
    mouseCon.position = (X, Y)
    degree += speed
    if degree > 360:
        degree = 0
    return degree


def main():

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()

    print("Get your mouse in position!")
    time.sleep(1.5)
    print("Are you ready?")
    time.sleep(1.5)
    print("Here we go")
    time.sleep(.5)

    mouseCon = Controller()
    startPosition = mouseCon.position

    currentPosition = (startPosition[0], startPosition[1])


    displacementX = 1400
    displacementY = 700
    speed = 4
    radius = 450
    degree = 0

    # pressing escape will stop this loop
    while listener.running:

        # comment out which one you dont want to use
        square(mouseCon, right, left, up, down, speed, displacementX, displacementY, currentPosition, startPosition)
        # degree = circle(mouseCon, startPosition, radius, degree, speed)

        # end of loop logic
        currentPosition = mouseCon.position
        time.sleep(0.001)


# global boolean statements because it is 2am and i cannot be bothered to fix so be quiet future keegan >:P
right = True
down = False
left = False
up = False

if __name__ == "__main__":
    main()
