#Faça um programa em python qe abra e reproduza o audio de um arquivo mp3
import pygame

pygame.mixer.init()
pygame.mixer.music.load("seu_arquivo.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue