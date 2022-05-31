#from AppClass import App
import pygame
import os 
import serial
import json

def servo(servoValues):
    arduinoData.write(str.encode(servoValues))

#connect to serial arduino
portName = "COM1"
arduinoData = serial.Serial(portName, 9600)

#pygame initialization
pygame.init()

#PS4 controller initialization
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

    # Reading in PS4 buttons
with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)

# 0: Left-analog Horz 1: Left-analog Vertical 2: Right-analog Horz
# 3: Right-analog Vertical 4: Left Trigger 5: Right Trigger
analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: 1}

#opening file to read data from controller
is_close = False
f = open("control_values.txt", "a")
count = 0 #reset counter

#controller values
HLA = "00"
VLA = "00"
HRA = "00"
rt = "00"

#initalize App
#GUI = App()

velocity = 0.0
altitude = 0.0
time_from_destination = 0.0
time_elapsed = 0.0
distance_traveled = 0.0
battery_left = 1.0

a = 525
b = 685

a1 = 30
b1 = 40
while True:
    # GUI.background()
    # GUI.update()
    # # Gaining PS4 Controller access
    
    # GUI.display_stat("Time Elpased:", a, a1 + b1 * 0)
    # GUI.display_stat(time_elapsed, b, a1 + b1 * 0)

    # GUI.display_stat("Average Velocity:", a, 70)
    # GUI.display_stat(velocity, b, 70)

    # GUI.display_stat("Distance Traveled:", a, 110)
    # GUI.display_stat(distance_traveled, b, 110)

    # GUI.display_stat("Altitude:", a, 190)
    # GUI.display_stat(altitude, b, 190)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['triangle']:
                count += 1
        # PS4 Buttons
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['x']:
                f.close()
                is_close = True
                print("\nx")

        if count % 2 == 1:
            HLA = "00"
            VLA = "00"
            HRA = "00"
            rt = "00"            
            #add a heads up display saying in saftey mode

            break

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['circle']:
                print("\ncircle")



        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['triangle']:
                pass
                # servo_off()
                # print("two")

        if event.type == pygame.JOYAXISMOTION:
            # Initialising Controller values


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

            # analog_keys[4] is left trigger for Windows and right trigger for the Mac
            # analog_keys[4] is left trigger for Windows and right trigger for the Mac          
            
            if -1 < analog_keys[5] < 1:
                RT = int(round(analog_keys[5], 2) * 10) + 10

                if RT == 1:
                    RT = 0

                if RT > 19:
                    RT = 19
                    rt = str(RT)
        
                rt = str(RT)
                if RT <= 9:
                    rt = "0"+str(RT)

                # Final output
            value = HLA + VLA + HRA + rt
            if is_close == False:
                f.write(value)
                f.write("\n")
            print(value)
            servo(value)
    #pygame.display.update()
