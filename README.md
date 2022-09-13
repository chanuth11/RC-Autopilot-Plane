# RC Autopilot Plane

Why we are doing this project: [Project Overview](https://docs.google.com/document/d/1GXb-hj0h31oRvuv6bn0ZbQ69HOYbUhehtujObRabfnY/edit?usp=sharing)

### Hardware

|                     | Transmitter Components | Receiver Components |
| ------------------- | ---------------------- | ------------------- |
| Soldered Components |  | <ul><li>nRF24L01 Breakout Adapter</li><li>Power MB V2 Voltage</li><li>Regulator/Power Supply</li><li>Arduino Nano iot 33</li><li>Servos x 4</li><li>Motor driver</li><li>PCB</li></ul> |
| Connected Components | <ul><li>Arduino UNO</li><li>nRF24L01 Breakout Adapter</li><li>nRF24L01 + PA transmitter</li></ul> | <ul><li>nRF24L01 + PA receiver to nRF24L01 Breakout Adapter</li><li>Connected 3.7 drone dc motors x 2 to motor driver</li><li>Connected 7.4V 5200mah LIPO battery to Power MB V2</li></ul> |

 **Receiver Schematic**
![receiver schematic](https://user-images.githubusercontent.com/57009205/115151764-533e3600-a03c-11eb-8dd1-f1ec7b6fffcc.png)

 ### Current Design
 
![PXL_20220701_225441883 MP](https://user-images.githubusercontent.com/57009205/189796200-9de04ee4-6d16-4adb-977a-7f1310741dd3.jpg)
![PXL_20220701_225522887 (1)](https://user-images.githubusercontent.com/57009205/189796354-98568f70-3896-477d-9f6b-9bb591d07503.jpg)
![PXL_20220701_225617443 (1)](https://user-images.githubusercontent.com/57009205/189796364-6f06a90c-a462-47ae-b9e2-c8428246ccfb.jpg)
![PXL_20220701_225544376](https://user-images.githubusercontent.com/57009205/189796367-afd2bce7-6475-4a72-abb7-942f10ed8fbd.jpg)
![PXL_20220701_225535863![PXL_20220701_225503098 (1)](https://user-images.githubusercontent.com/57009205/189796380-2ac5f50f-b9e7-469d-af1d-ed20905978f7.jpg)
](https://user-images.githubusercontent.com/57009205/189796373-c6020d33-431e-4b0d-8435-14c3c01bb45b.jpg)
![PXL_20220701_225503098 (1)](https://user-images.githubusercontent.com/57009205/189797735-d109453b-ba44-410f-817d-4daf81a0b999.jpg)

  **Link to test flights**
 https://photos.app.goo.gl/6WHYiJE59ZRLMAGVA
 
  **Older Videos**
 https://youtube.com/playlist?list=PLy_OHsmgOxpecJcippoSOJ2Jgk2Bfz1kq
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


