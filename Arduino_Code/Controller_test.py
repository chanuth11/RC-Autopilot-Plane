import pygame
import json
import os
import serial
import time
# Arduino Setup


arduinoData = serial.Serial('com5', 9600)


def led_on():
    arduinoData.write(str.encode('1'))


def led_of():
    arduinoData.write(str.encode('0'))


def output(value):
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

            HLA = "00"
            VLA = "00"
            HRA = "00"
            RT = "00"

            analog_keys[event.axis] = event.value

            # Horizontal Left Analog - Ailerons
            if (abs(analog_keys[0])) > 0:
                if analog_keys[0] < -.1:
                    HLA = int(round(analog_keys[0], 2) * -10)
                    if HLA > 9:
                        HLA = 9
                    HLA = "0" + str(HLA)
                if analog_keys[0] > 0.1:
                    HLA = int(round(analog_keys[0], 2) * 10) + 10
                    if HLA > 19:
                        HLA = 19
                    HLA = str(HLA)
            # Vertical Left Analog - Elevator
            if (abs(analog_keys[1])) > 0.1:
                if analog_keys[1] < -.1:
                    VLA = int(round(analog_keys[1], 2) * -10)
                    if VLA > 9:
                        VLA = 9
                    VLA = "0" + str(VLA)
                if analog_keys[1] > 0.1:
                    VLA = int(round(analog_keys[1], 2) * 10) + 10
                    if VLA > 19:
                        VLA = 19
                    VLA = str(VLA)
            # Horz Right Analog - Rutter`
            if (abs(analog_keys[2])) > 0.1:
                if analog_keys[2] < -.1:
                    HRA = int(round(analog_keys[2], 2) * -10)
                    if HRA > 9:
                        HRA = 9
                    HRA = "0" + str(HRA)
                if analog_keys[2] > 0.1:
                    HRA = int(round(analog_keys[2], 2) * 10) + 10
                    if HRA > 19:
                        HRA = 19
                    HRA = str(HRA)
            # Right Trigger - DC Motor
            if analog_keys[5] > 0:
                RT = int(round(analog_keys[5], 2) * 100)
                if RT > 99:
                    RT = 99
                RT = str(RT)

            value = HLA + VLA + HRA + RT
            output(value)
            print(value)
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
