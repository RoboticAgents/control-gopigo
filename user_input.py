import pygame

gpg = easy.EasyGoPiGo3()

pygame.mixer.init()
i = 0

def command(inputs):
    global i
    if inputs == 'w':
        gpg.forward()

    if inputs == 's':
        gpg.backward()

    if inputs == 'a':
        gpg.left()

    if inputs == 'd':
        gpg.right()
    
    if inputs == 'q':
    
        i += 50
        gpg.set_motor_dps(gpg.MOTOR_RIGHT, i)
        
        gpg.set_motor_dps(gpg.MOTOR_LEFT, i)

    if inputs == 'e':
        
        i -= 50
        gpg.set_motor_dps(gpg.MOTOR_RIGHT, i)
        
        gpg.set_motor_dps(gpg.MOTOR_LEFT, i)

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
            
    if inputs == 'f':
        gpg.stop()
    if inputs == 'v':
        pygame.mixer.music.pause()
    if inputs == 'p':
        pygame.quit()

def main():
    # TODO make GUI here 
    print("HELLO WORLD")
    mylist = []
    while True:

        inputs = input("enter command: ")
        #     print("this is your input:", inputs)

        mylist.append(inputs)
        command(mylist[0])
        # print(mylist)
        mylist.clear()
    
main()