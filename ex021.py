#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
# Esse eu não consegui fazer, então assisti a aula e fiz junto com o guanabara.

#pip install pygame

import pygame
def reproduzir_mp3(caminho_do_arquivo):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load('audio021.mp3')
        pygame.mixer.music.play()

        # Aguarda até que a música termine de tocar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Erro ao reproduzir o arquivo MP3: {e}")

    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    caminho_do_arquivo = "audio021.mp3"  # Substitua pelo caminho do seu arquivo MP3
    reproduzir_mp3(caminho_do_arquivo)
