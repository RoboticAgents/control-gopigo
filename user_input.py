import easygopigo3 as easy
# import time
import pygame

gpg = easy.EasyGoPiGo3()

pygame.mixer.init()


def command(inputs):
    if inputs == 'w':
        gpg.forward()

    if inputs == 's':
        gpg.backward()

    if inputs == 'a':
        gpg.left()

    if inputs == 'd':
        gpg.right()

#     if inputs == 'q':
#         print("increasing speed")

#     if inputs == 'e':
#         print("decreasing speed")

    if inputs == 'z':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        pygame.mixer.music.load("Happy.mp3")
        pygame.mixer.music.play()
        print("playing music 1 here")

    if inputs == 'x':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        pygame.mixer.music.load("Wii_Music.mp3")
        pygame.mixer.music.play()
        print("playing music 2 here")

    if inputs == 'c':
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        pygame.mixer.music.load("No_Role_Modelz.mp3")
        pygame.mixer.music.play()
        print("playing music 3 here")

    if inputs == 'p':
        gpg.stop()

def main():

    mylist = []

    while True:

        inputs = input("Enter command here: ")
        #     print("this is your input:", inputs)

        mylist.append(inputs)
        command(mylist[0])
        # print(mylist)
        mylist.clear()
    
main()