import easygopigo3 as easy
import time
import pygame
import sys

my_gopigo = easy.EasyGoPiGo3()

pygame.init()
pygame.display.set_mode((1200,800))

def main():
    while True:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            # gpg.drive_inches(5)
            print("going forward")
          if event.key == pygame.K_s:
            print("going backward")
          if event.key == pygame.K_q:
            print("turn left slightly")
          if event.key == pygame.K_e:
            print("turn right slightly")
          if event.key == pygame.K_a:
            print("turn left 90 degree")
          if event.key == pygame.K_d:
            print("turn right 90 degree")
          if event.key == pygame.K_z:
            print("turn left x degree")
          if event.key == pygame.K_c:
            print("turn right x degree")
          if event.key == pygame.K_p: # working 
            pygame.quit()
            print("exit code")
            return False
        pygame.display.update()
main()
