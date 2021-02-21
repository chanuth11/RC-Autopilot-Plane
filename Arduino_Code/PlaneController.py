import pygame
import json
import os
import serial

# Arduino Setup


arduinoData = serial.Serial('com3', 9600)


def led_on():
    arduinoData.write(str.encode('1'))


def led_of():
    arduinoData.write(str.encode('0'))


def servo(value):
    arduinoData.write(str.encode(value))


# Initialize the pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# Initialize Controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

# Reading in PS4 buttons
with open(os.path.join("ps4keys.json"), "r+") as file:
    button_keys = json.load(file)

# 0: Left-analog Horz 1: Left-analog Vertical 2: Right-analog Horz
# 3: Right-analog Vertical 4: Left Trigger 5: Right Trigger
analog_keys = {0: 0, 1: 0, 3: 0, 4: -1, 5: 1}

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    pygame.time.delay(100)
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['x']:
                led_on()

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['circle']:
                led_of()

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['triangle']:
                pass

        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['triangle']:
                pass
                # servo_off()
                # print("two")

        if event.type == pygame.JOYAXISMOTION:
            # Horizontal Left Analog
            analog_keys[event.axis] = event.value
            if (abs(analog_keys[0])) > 0:
                if analog_keys[0] < -.1:
                    x = int(round(analog_keys[0], 2) * 100)
                    servo_output = ' '
                    if x < -90:
                        servo_output = '1'
                    elif x < -80:
                        servo_output = '2'
                    elif x < -70:
                        servo_output = '3'
                    elif x < -60:
                        servo_output = '4'
                    elif x < -50:
                        servo_output = '5'
                    elif x < -40:
                        servo_output = '6'
                    elif x < -30:
                        servo_output = '7'
                    elif x < -20:
                        servo_output = '8'
                    elif x < -10:
                        servo_output = '9'
                    # elif x < -60:
                    #     servo_output = '6'
                    # elif x < -70:
                    #     servo_output = '7'
                    # elif x < -80:
                    #     output = '8'
                    # elif x < -90:
                    #     servo_output = '9'
                    # print(servo_output)
                    servo(servo_output)
                if analog_keys[0] > 0.1:
                    x = int(round(analog_keys[0], 2) * 100)
                    print(x)
                    servo_output = ' '
                    if x > 90:
                        servo_output = 'A'
                    elif x > 80:
                        servo_output = 'B'
                    elif x > 70:
                        servo_output = 'C'
                    elif x > 60:
                        servo_output = 'D'
                    elif x > 50:
                        servo_output = 'E'
                    elif x > 40:
                        servo_output = 'F'



                    # print(servo_outputVert)
                    servo(servo_output)
            # Vertical Analog
            if (abs(analog_keys[1])) > .4:
                if analog_keys[1] < -.7:
                    playerY_change = -0.1
                    print("Up")
                else:
                    playerY_change = 0
                if analog_keys[1] > .7:
                    playerY_change = 0.1
                    print("Down")
                else:
                    playerY_change = 0
            if analog_keys[5] > 0:
                x = int(round(analog_keys[5], 2) * 100)
                output = ' '
                if x > 6:
                    output = '1'
                if x > 12:
                    output = '2'
                if x > 18:
                    output = '3'
                if x > 24:
                    output = '4'
                if x > 30:
                    output = '5'
                if x > 36:
                    output = '6'
                if x > 48:
                    output = '7'
                if x > 54:
                    output = '8'
                if x > 60:
                    output = '9'
                if x > 66:
                    output = 'A'
                if x > 72:
                    output = 'B'
                if x > 78:
                    output = 'C'
                if x > 83:
                    output = 'D'
                if x > 87:
                    output = 'E'
                if x > 91:
                    output = 'F'
                if x > 95:
                    output = 'G'
                servo(output)

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
