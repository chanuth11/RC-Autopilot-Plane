import pygame
import json
import os
import serial
import time
# Arduino Setup


arduinoData = serial.Serial('com3', 9600)


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

            HLA1 = "00"
            HLA2 = "00"
            VLA1 = "00"
            VLA2 = "00"
            HRA1 = "00"
            HRA2 = "00"
            RT = "00"

            analog_keys[event.axis] = event.value

            # Horizontal Left Analog - Ailerons
            if (abs(analog_keys[0])) > 0:
                if analog_keys[0] < -.1:
                    HLA1 = int(round(analog_keys[0], 2) * -100)
                    if HLA1 > 99:
                        HLA1 = 99
                if analog_keys[0] > 0.1:
                    HLA2 = int(round(analog_keys[0], 2) * 100)
                    if HLA2 > 99:
                        HLA2 = 99
            # Vertical Left Analog - Elevator
            if (abs(analog_keys[1])) > 0.1:
                if analog_keys[1] < -.1:
                    VLA1 = int(round(analog_keys[1], 2) * -100)
                    if VLA1 > 99:
                        VLA1 = 99
                if analog_keys[1] > 0.1:
                    VLA2 = int(round(analog_keys[1], 2) * 100)
                    if VLA2 > 99:
                        VLA2 = 99
            # Horz Right Analog - Rutter
            if (abs(analog_keys[2])) > 0.1:
                if analog_keys[2] < -.1:
                    HRA1 = int(round(analog_keys[2], 2) * -100)
                    if HRA1 > 99:
                        HRA1 = 99
                if analog_keys[2] > 0.1:
                    HRA2 = int(round(analog_keys[2], 2) * 100)
                    if HRA2 > 99:
                        HRA2 = 99
            # Right Trigger - DC Motor
            if analog_keys[5] > 0:
                RT = int(round(analog_keys[5], 2) * 100)
                if RT > 99:
                    RT = 99

            value = str(HLA1) + str(HLA2) + str(VLA1) + str(VLA2) + str(HRA1) + str(HRA2) + str(RT)
            print(value)
            output(value)

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
