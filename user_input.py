import easygopigo3 as easy
import time
import pygame

my_gopigo = easy.EasyGoPiGo3()


def main():
    inputs = input("enter input here: ")
    print("this is your input: ", inputs)
    while True:
        if inputs == 'w':
            # gpg.drive_inches(5)
            print("going forward")
        
        if inputs == 's':
        
            print("going backward")
        
        if inputs == 'q':
        
            print("turn left slightly")
    
        if inputs == 'e':
            print("turn right slightly")
    
        if inputs == 'a':
            print("turn left 90 degree")
    
        if inputs == 'd':
            print("turn right 90 degree")
    
        if inputs == 'z':
            print("turn left x degree")
    
        if inputs == 'c':
            print("turn right x degree")
        
        if inputs == 'p': # working 
            print("exit code")
        return False
main()