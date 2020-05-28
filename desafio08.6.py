#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
import pygame
pygame.mixer.init() #iniciar o mixer do Pygame
pygame.init() #iniciar o Pygame
pygame.mixer.music.load('ex01.mp3') #carregar o arquivo mp3, que já deve estar salvo dentro do projeto
pygame.mixer.music.play() #executar o player
pygame.event.wait() #esperar a música acabar para parar de executar






