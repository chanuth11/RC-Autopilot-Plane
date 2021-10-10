# RC Autopilot Plane

Why we are doing this project: [Project Overview](https://docs.google.com/document/d/1GXb-hj0h31oRvuv6bn0ZbQ69HOYbUhehtujObRabfnY/edit?usp=sharing)

## Videos and Current Progress: 

https://docs.google.com/document/d/124PLKt3WayUlCQaWhQOHeGj22U9F4H3z6Gp6ViLzv4w/edit?usp=sharing

Plan for Winter Break: 
https://docs.google.com/document/d/1lroXHf4Y8rhPDGnO8ytmJ74nIkBuzvZ1OpPVsnde-J4/edit?usp=sharing

### Hardware

|                     | Transmitter Components | Receiver Components |
| ------------------- | ---------------------- | ------------------- |
| Soldered Components |  | <ul><li>nRF24L01 Breakout Adapter</li><li>Power MB V2 Voltage</li><li>Regulator/Power Supply</li><li>Arduino Nano iot 33</li><li>Servos x 4</li><li>Motor driver</li><li>PCB</li></ul> |
| Connected Components | <ul><li>Arduino UNO</li><li>nRF24L01 Breakout Adapter</li><li>nRF24L01 + PA transmitter</li></ul> | <ul><li>nRF24L01 + PA receiver to nRF24L01 Breakout Adapter</li><li>Connected 3.7 drone dc motors x 2 to motor driver</li><li>Connected 7.4V 5200mah LIPO battery to Power MB V2</li></ul> |

 **Receiver Schematic**
![receiver schematic](https://user-images.githubusercontent.com/57009205/115151764-533e3600-a03c-11eb-8dd1-f1ec7b6fffcc.png)

 **New Wing Design**
 
![newdesign](https://user-images.githubusercontent.com/57009205/127687287-eb4fee48-6a85-4cea-a978-d29f71f33d39.png)

### Software

**Current Application:** https://www.dropbox.com/s/v0275ro6g6j7pxt/Plane_Visualizer_2021-07-11_18-41-11.mp4?dl=0

The desktop application designed in PyGame functions as a visualizer to plot the position of the plane relative to the position of the destination -> marked as an x a the origin. The scale is 250 m in each direction from the origin. Multiple stats are displayed on the application. Currently, the stats that are working are Time Elapsed and Bearing Angle. The other stats need functions to be calculated. The position of the plane updates every time a signal is received through a radio transmitter and is extracted from the serial on the Arduino console (updates in real-time with the physical plane). The symbol of the plane has dynamic turning. Depending on the bearing angle, the symbol rotates up to 360 degrees with multiples of 15 degrees to prevent image degradation. A meter animation at the bottom with dynamic colour changing (increases red value on the RGB scale depending on how full it's getting) has been built but needs to be implemented for values such as velocity.

## Plans
* Connect to radio transmitter with the plane
* Make landing and takeoff algo
* Turning Algorithm
* Optimal Path Algorithm
* Ascent/Descent Algorithm
* Acceleration/Deceleration Algorithm
         
## Creators

**Humza A Iqbal**  
email: humzaaiqbal67@gmail.com  
**Hamza Mehmood**  
email:  hamza88mehmood@hotmail.com  
**Akash Santhanakrishnan**  
email: akashkrish27@gmail.com  
**Chanuth Weeraratna**  
email: chanuthw55@gmail.com   

## Refrences

[Plane body](https://www.rcpano.net/2019/11/05/how-to-make-rc-model-airplane-fun-fly-style-diy-rc-airplane-with-brushless-motor/)


