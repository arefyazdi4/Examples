import pygame  # used to create video games
import os  # it permits to interact with the operating system


class MusicPlayer:
    pygame.mixer.init()

    def __init__(self):
        pass

    @staticmethod
    def play(music_name: str):
        pygame.mixer.music.load(music_name)
        pygame.mixer.music.play()

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()


if __name__ == '__main__':
    while True:
        mode = input("enter mode: \n")
        if mode == 'p':
            MusicPlayer().play('Alicia.mp3')
        elif mode == 's':
            MusicPlayer().pause()
        elif mode == 'u':
            MusicPlayer.unpause()
        elif mode == 'n':
            MusicPlayer.stop()
        else:
            break

