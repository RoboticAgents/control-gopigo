# Report by Add Team Member Names

## Project Summary

For our completed project, we created a program for GOPIGO that would allow people to control the GOPIGO Robot using their keyboard. By entering a key the robot will do that action until a new command is entered, with music being the only excetion. Using Q, the controller can increase the speed of the motors. While E does the opposite and decreases the speed. W has it drive forward, and S tells it to go backwards. A tells it to turn left. D tells it to turn right. F stos it from moving. Z, X, and C tell it to play different music files using the pygame module. V pauses the music. P stops the music player by quiting the pygame module. We designed this because we wanted to make it easier and more fun to use the GOPIGO robot. Also we exerienced difficulties with the EvoArm. This program can be used by anyone without much background knowledge required at all. 

## Project Implementation Details

Step One: You have to connect to a GOPIGO robot that comes with the pygame module if you want to use the music feature if not, then all you need to do is run the code in the notebook.  

That's the only step needed to use our program, our GOPIGO robot already had pygame, so we didn't have to manually install it. To create the program we just used our already known knowledge of while loops and if statements to code our implementation. Besides that we referenced old projects to get the commands for GOPIGO. Makell already knew a bit about pygame, so he was able to implement that in pretty easily.

## Experimental Results

Experiment One: We commanded it while playing wii music. It was able to run fine while playing the music, even when we inputted new commands it didn't interfere with the music command.

Experiment Two: We commanded it while playing wii music, then switched between the other two tracks. The music commands and movement commands didn't infere with each other and worked independently. We were able to change tracks smoothly with no interuption to the robots movements.

Experiment Three: We command it after we quit out of the pygame module, although it was able to move fine, it would error if we tried to input any music commands quitting the program.

## Ethical Implications

Based on your experiences with the project and from our discussions in class, please provide answers for the following questions as related to the project you chose to implement:

1. Who would typically make the technology of the similar type as your project? Why?

Developers interested in making robots easier to use and interact with. As interfaces like the one we made are an easier way for those who don't know code to enjoy and develop interest in robots. 

1. Who are the intended users of this robotic application? How does this technology benefit them?

People new to interacting with GOPIGO, and experienced users who want to use GOPIGO for other tasks without having to code themselves.

1. Who is not supposed to use this technology? Why?

Anyone can honestly, you may want to supervise children and neurodivergent people for their safety as it could become a hazard or disturbence. 

1. How can the type of robotic application implemented in your project cause harm?

It could causes people to trip if not used carefully.

1. What solutions can be developed to avoid the harm caused by this type of technology or to fix the harm?

A proximity or distance sensor that can detect when it's about to collide with something and command it to stop to minimize the damage it can cause to others.

## Team Working Strategy

As a team we created this program. Gary was responsible for the GOPIGO portion of the project. While Makell was in charge of implementing pygame and designing the code output. We took turns with the writing portions, but discussed everything together. Outside of class we spent time together in ALIC working out our bugs and coming up with solutions.

## Challenges and Learning Experiences

Our only challenge when working on this project was that we were limited in our options due to it being difficult to install dependencies in the jupyter notebook as it wasn't connected to wifi. Also since we were in a notebook some features of pygame that I wanted to use weren't implementable. We did learn that their are many ways to complete a task outside of relying on dependencies. Although they make things easier and cleaner there are still methods to do things without them. It just takes more code.
