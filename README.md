# RC Autopilot Plane

Why we are doing this project: [Project Overview](https://docs.google.com/document/d/1GXb-hj0h31oRvuv6bn0ZbQ69HOYbUhehtujObRabfnY/edit?usp=sharing)

## Current Progress

### Hardware

*write here 
add images/videos*

### Software

![plane](https://user-images.githubusercontent.com/57009205/105204286-04066900-5b12-11eb-8547-1b9bb6df8277.PNG)

The desktop application designed in PyGame functions as a visualizer to plot the position of the plane relative to the position of the destination -> marked as an x a the origin. The scale is 250 m in each direction from the origin. Multiple stats are displayed on the application. Currently, the stats that are working are Time Elapsed and Bearing Angle. The other stats need functions to be calculated. The position of the plane updates every time a signal is received through a radio transmitter and is extracted from the serial on the Arduino console (updates in real-time with the physical plane). The symbol of the plane has dynamic turning. Depending on the bearing angle, the symbol rotates up to 360 degrees with multiples of 15 degrees to prevent image degradation. A meter animation at the bottom with dynamic colour changing (increases red value on the RGB scale depending on how full it's getting) has been built but needs to be implemented for values such as velocity.

## Plans
* Connect to radio transmitter with the plane
* Make landing and takeoff algo
* Turning Algorithm
* Optimal Path Algorithm
* Ascent/Descent Algorithm
* Acceleration/Deceleration Algorithm
         
## Creators

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Refrences

*write here*

