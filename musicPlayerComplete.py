from pygame import mixer
from random import shuffle
from tkinter import Tk, Button, Label
from tkinter.filedialog import askdirectory  # it permit to select dir
import os  # it permits to interact with the operating system

# Initialize the window and the mixer
window = Tk()
mixer.init()

# get list of files
# directory = askdirectory()
# os.chdir(directory)  # it permits to change the current dir
playlist = os.listdir('./Music')  # it returns the list of files song
active_playlist = playlist
shuffled_playlist = []

# Get number of files
file_range = len(playlist) - 1

# Settings variables used to control play logic
music_option = True
shuffle_music = False
indexed_track = 0
display_track = indexed_track + 1
is_stopped = True
is_paused = False
is_started = False
repeat_track = False
repeat_all = False


# Shuffle music logic
def shuffle_playlist():
    global shuffle_music, playlist, is_started, shuffled_playlist, indexed_track, is_stopped, active_playlist
    indexed_track = 0
    if shuffle_music:
        shuffle_music = False
        active_playlist = playlist
    else:
        shuffle_music = True
        shuffle(playlist)
        shuffled_playlist = playlist
        playlist = os.listdir('./Music')
    update_display()


# Repeat one or all logic
def repeat_loop():
    global repeat_all, repeat_track
    if not repeat_track and not repeat_all:
        repeat_track = True
        repeat_button.config(text="🔂")
    elif repeat_track:
        repeat_track = False
        repeat_all = True
        repeat_button.config(text="🔁")
    elif repeat_all:
        repeat_all = False
        repeat_button.config(text="🔄")


# Updates the display values of the current track number and name
def update_display():
    global display_track
    display_track = playlist.index(active_playlist.__getitem__(indexed_track)) + 1
    track_num_display.config(text=f"Track: {display_track}")
    track_name_display.config(text=f"Now Playing:\n{active_playlist.__getitem__(indexed_track)}")


# Logic to run music
def start_music():
    global indexed_track, is_started, is_stopped, active_playlist

    # Determine if random or normal play
    if shuffle_music:
        active_playlist = shuffled_playlist
    else:
        active_playlist = playlist

    # If music is not already playing, it has not been stopped or paused then grabs next song in queue
    while not mixer.music.get_busy() and not is_stopped and not is_paused and not is_started:
        mixer.music.load(f"./Music/{active_playlist.__getitem__(indexed_track)}")
        mixer.music.play()
        is_started = True
    # While music is playing check every 100 milliseconds if music track has finished playing and re-trigger music.
    if mixer.music.get_busy():
        window.after(100, start_music)
    else:
        # Repeat logic
        if not is_stopped and not is_paused:
            # If not repeating then at last track trigger stop
            if not repeat_all and not repeat_track and indexed_track == file_range:
                stop_music()

            # Repeat one logic reduce index call by 1 prior to adding 1 so always stay on same track
            elif repeat_track:
                indexed_track -= 1

            # Else it is repeating all
            indexed_track += 1
            is_started = False

            # Checks to make sure track is not skipped past last song or into negative.
            if indexed_track < 0 or indexed_track > file_range:
                indexed_track = 0

            # Update the display with current track info
            update_display()

            # Repeat music
            start_music()


# Gets the current status of the music player
def music_status():
    music_yes = mixer.music.get_busy()
    return music_yes


# Stop the music from playing. If already stopped then it resets repeat status and the playlist
def stop_music():
    global is_stopped, is_started, indexed_track, repeat_all, repeat_track
    if is_stopped:
        indexed_track = 0
        repeat_all = False
        repeat_track = False
        update_display()
    mixer.music.stop()
    is_stopped = True
    is_started = False
    start_music()


# Skip to next track
def next_track():
    global indexed_track, is_started
    # If music is playing stop it and move it to the next track and start again
    music_playing = music_status()
    if music_playing:
        mixer.music.stop()
        if indexed_track == file_range:
            indexed_track = 0
            is_started = False
        start_music()

    # If music is not playing move to next track and if on last track move to first
    else:
        if indexed_track != file_range:
            indexed_track += 1
        else:
            indexed_track = 0
    update_display()


# Skip to last track
def prev_track():
    global indexed_track, is_started
    # If music is playing stop it move to prior track or if on first track move to last track.
    music_playing = music_status()
    if music_playing:
        if display_track == 1:
            indexed_track = file_range
            is_started = False
        else:
            indexed_track -= 2
        mixer.music.stop()
        start_music()

    # If music is not playing skip back one, if on first track move to last track
    else:
        if indexed_track != 0:
            indexed_track -= 1
        else:
            indexed_track = file_range
    update_display()


# Play or pause logic
def play_track():
    global is_paused, is_stopped
    music_playing = music_status()
    # If music is playing then pause it and mark the paused flag as True
    if music_playing:
        is_paused = True
        mixer.music.pause()

    # Else it was paused so unpause and mark paused flag as False
    else:
        is_paused = False
        mixer.music.unpause()

    # Mark stopped as False and start music
    is_stopped = False
    start_music()


if __name__ == '__main__':
    # Control buttons
    previous_button = Button(text="⏮", font=("", 12, ""), command=prev_track)
    previous_button.grid(row=2, column=0)
    stop_button = Button(text="⏹", font=("", 12, ""), command=stop_music)
    stop_button.grid(row=2, column=1)
    start_button = Button(text="⏯", font=("", 12, ""), command=play_track)
    start_button.grid(row=2, column=2)
    next_button = Button(text="⏭", font=("", 12, ""), command=next_track)
    next_button.grid(row=2, column=3)
    repeat_button = Button(text="🔄", font=("", 16, ""), command=repeat_loop)
    repeat_button.grid(row=3, column=2)
    shuffle_button = Button(text="🔀", command=shuffle_playlist)
    shuffle_button.grid(row=3, column=1)

    # Displayed information
    track_num_display = Label(text=f"Track: {display_track}")
    track_name_display = Label(text=f"Now Playing:\n{active_playlist.__getitem__(indexed_track)}")
    track_num_display.grid(row=0, column=1, columnspan=2)
    track_name_display.grid(row=1, column=0, columnspan=4)

    # Loop main window
    window.mainloop()
