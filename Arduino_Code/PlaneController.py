import pygame
import json
import os
import serial

# Arduino Setup


arduinoData = serial.Serial('com8', 9600)


def led_on():
    arduinoData.write(str.encode('1'))


def led_of():
    arduinoData.write(str.encode('0'))

def motor(value):
    arduinoData.write(str.encode(value))

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
analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: 1}

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
                    servo(servo_output)
                if analog_keys[0] > 0.1:
                    x = int(round(analog_keys[0], 2) * 100)
                    servo_output = ' '
                    if x > 90:
                        servo_output = 'J'
                    elif x > 80:
                        servo_output = 'K'
                    elif x > 70:
                        servo_output = 'L'
                    elif x > 60:
                        servo_output = 'M'
                    elif x > 50:
                        servo_output = 'N'
                    elif x > 40:
                        servo_output = 'O'

                    servo(servo_output)
            # Vertical Left Analog - Elevator
            if (abs(analog_keys[1])) > 0.1:
                if analog_keys[1] < -.1:
                    x = int(round(analog_keys[1], 2) * 100)
                    servo_output = ' '
                    if x < -90:
                        servo_output = 'Q'
                    elif x < -80:
                        servo_output = 'R'
                    elif x < -70:
                        servo_output = 'S'
                    elif x < -60:
                        servo_output = 'T'
                    elif x < -50:
                        servo_output = 'U'
                    elif x < -40:
                        servo_output = 'V'
                    elif x < -30:
                        servo_output = 'W'
                    elif x < -20:
                        servo_output = 'X'
                    servo(servo_output)
                    print(servo_output)
                if analog_keys[1] > 0.1:
                    x = int(round(analog_keys[1], 2) * 100)
                    servo_output = ' '
                    if x > 90:
                        servo_output = 'Y'
                    elif x > 80:
                        servo_output = 'Z'
                    elif x > 70:
                        servo_output = ','
                    elif x > 60:
                        servo_output = ';'
                    elif x > 50:
                        servo_output = '{'
                    elif x > 40:
                        servo_output = '}'
                    servo(servo_output)
                    print(servo_output)
            elif (abs(analog_keys[1])) < 0.1:
                output = '='
                motor(output)
                # Horizontal Right Analog - Rudder
            if (abs(analog_keys[3])) > 0.1:

                if analog_keys[3] < -.1:
                    x = int(round(analog_keys[3], 2) * 100)
                    servo_output = ' '
                    if x < -90:
                        servo_output = '!'
                    elif x < -80:
                        servo_output = '@'
                    elif x < -70:
                        servo_output = '#'
                    elif x < -60:
                        servo_output = '$'
                    elif x < -50:
                        servo_output = '%'
                    elif x < -40:
                        servo_output = '^'
                    elif x < -30:
                        servo_output = '&'
                    elif x < -20:
                        servo_output = '*'
                    elif x < -10:
                        servo_output = '('
                    servo(servo_output)
                    print(servo_output)
                if analog_keys[3] > 0.1:
                    x = int(round(analog_keys[3], 2) * 100)
                    servo_output = ' '
                    if x > 90:
                        servo_output = ')'
                    elif x > 80:
                        servo_output = '-'
                    elif x > 70:
                        servo_output = '+'
                    elif x > 60:
                        servo_output = '/'
                    elif x > 50:
                        servo_output = '['
                    elif x > 40:
                        servo_output = ']'
                    servo(servo_output)
                    print(servo_output)
            elif (abs(analog_keys[3])) < 0.1:
                output = 'z'
                servo(output)

            # Right Trigger - Motor
            if analog_keys[5] > 0:
                x = int(round(analog_keys[5], 2) * 100)
                output = ' '
                if x > 10:
                    output = '0'
                if x > 20:
                    output = 'A'
                if x > 30:
                    output = 'B'
                if x > 40:
                    output = 'C'
                if x > 50:
                    output = 'D'
                if x > 60:
                    output = 'E'
                if x > 70:
                    output = 'F'
                if x > 80:
                    output = 'G'
                if x > 90:
                    output = 'H'
                if x > 95:
                    output = 'I'
                motor(output)
            elif analog_keys[5] < 0:
                output = 'P'
                motor(output)

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
