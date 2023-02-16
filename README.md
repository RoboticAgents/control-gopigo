# GoPiGo Controller

## Project Summary

For our completed project, we created a program for GOPIGO that would allow people to control the GOPIGO Robot using their keyboard. By entering a key the robot will take that action until a new command is entered, with music being the only exception. Using `Q`, the controller can increase the speed of the motors. While `E` does the opposite and decreases the speed. `W` has it drive forward, and `S` tells it to go backwards. A tells it to turn left. `D` tells it to turn right. `F` stops it from moving. `Z`, `X`, and `C` tell it to play different music files using the pygame module. V pauses the music. P stops the music player by quiting the pygame module. We designed this because we wanted to make it easier and more fun to use the GOPIGO robot. This program can be used by anyone without much background knowledge required at all.

This is the output:

```bash
    🤖 Welcome to GOPIGO Controller!
    Using this program you can control your GOPIGO Robot using your computer keyboard! ⌨️
    These are your controls:
    Q   W   E       P
    A   S   D   F
    Z   X   C   V

    Q = Increase Speed ⏩
    W = Drive Forward ⬆️
    E = Decrease Speed ⏪

    A = Turn Left ⬅️
    S = Drive Backwards ⬇️
    D = Turn Right ➡️
    F = Stop Moving ⏹️

    Z = Play Song 1 🎵
    X = Play Song 2 🎵
    C = Play Song 3 🎵
    V = Pause Music ⏸️

    P = Stop Music Player ⏹️

    📨 Enter your commands below:
```

## Project Implementation Details

Step One: You have to connect to a GOPIGO robot that comes with the pygame module if you want to use the music feature if not, then all you need to do is run the code in the Jupyter notebook.

That's the only step needed to use our program, our GOPIGO robot already had pygame, so we did not have to manually install it. To create the program we just used our already known knowledge of while loops and if statements to code our implementation. Besides that we referenced old projects to get the commands for GOPIGO. Makell already knew a bit about pygame, so he was able to implement that in pretty easily.

## Experimental Results

Experiment One: We commanded it while playing wii music. It was able to run fine while playing the music, even when we inputted new commands it didn't interfere with the music command. At first we thought that we may have had to make a separate list just to store the music inputs, but we didn't.

Experiment Two: We commanded it while playing wii music, then switched between the other two tracks. The music commands and movement commands didn't interfere with each other and worked independently. We were able to change tracks smoothly with no interruption to the robots movements.

Experiment Three: We command it after we quit out of the pygame module, although it was able to move fine, it would error if we tried to input any music commands quitting the program.

## Ethical Implications

1. Who would typically make the technology of the similar type as your project? Why?

Developers interested in making robots easier to use and interact with. As interfaces like the one we made are an easier way for those who don't know code to enjoy and develop interest in robots.

1. Who are the intended users of this robotic application? How does this technology benefit them?

People new to interacting with GOPIGO, and experienced users who want to use GOPIGO for other tasks without having to code themselves.

1. Who is not supposed to use this technology? Why?

You may want to supervise children and neurodivergent people for their safety as it could become a hazard or disturbence.

1. How can the type of robotic application implemented in your project cause harm?

It could causes people to trip if not used carefully.

1. What solutions can be developed to avoid the harm caused by this type of technology or to fix the harm?

A proximity or distance sensor that can detect when it's about to collide with something and command it to stop to minimize the damage it can cause to others.
