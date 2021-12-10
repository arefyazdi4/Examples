import pygame  # used to create video games
import tkinter as tkr  # used to develop GUI
from tkinter.filedialog import askdirectory  # it permit to select dir
import os  # it permits to interact with the operating system


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


if __name__ == '__main__':
    music_player = tkr.Tk()
    music_player.title('LifeInMusic')
    music_player.geometry('450x350')

    directory = askdirectory()
    os.chdir(directory)  # it permits to change the current dir
    song_list = os.listdir()  # it returns the list of files song

    play_list = tkr.Listbox(music_player, font='Helvetica12bold',
                            bg='yellow',
                            selectmode=tkr.SINGLE)
    for item in song_list:
        pos = 0
        play_list.insert(pos, item)
        pos += 1

    pygame.init()
    pygame.mixer.init()

    var = tkr.StringVar()
    song_title = tkr.Label(music_player, font='Helvetica12bold', textvariable=var)

    Button1 = tkr.Button(music_player, width=5, height=3, font='Helvetica12bold', text ='PLAY', command = play)
    Button2 = tkr.Button(music_player, width=5, height=3, font='Helvetica12bold', text ='STOP', command = stop, )
    Button3 = tkr.Button(music_player, width=5, height=3, font='Helvetica12bold', text ='PAUSE', command = pause)
    Button4 = tkr.Button(music_player, width=5, height=3, font='Helvetica12bold', text ='UNPAUSE', command = unpause)

    song_title.pack()
    Button1.pack(fill='x')
    Button2.pack(fill='x')
    Button3.pack(fill='x')
    Button4.pack(fill='x')
    play_list.pack(fill='both', expand ='yes')

    music_player.mainloop()
