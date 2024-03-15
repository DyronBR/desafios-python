import pygame

# Iniciando o pygame
pygame.init()

# Comando para abrir o mp3, que deve estar dentro da pasta do projeto
pygame.mixer.music.load('desafio21.mp3')

# Comando para reproduzir a música importada
pygame.mixer.music.play()

# Precisa dar um input para reproduzir
input()

# Esse comando serve para que o programa espere a música ser reproduzida
pygame.event.wait()

