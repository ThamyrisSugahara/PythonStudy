import pygame

pygame.mixer.init()
pygame.mixer.music.load('Ghost.mp3')  # A música deve estar no mesmo diretório
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

pygame.quit()
