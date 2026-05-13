from tkinter import *

# Main window
root = Tk()
root.geometry("700x220")
root.title("Sangeet")
root.resizable(0, 0)

# Frames
song_frame = LabelFrame(
    root, text="Current Song", bg="MediumPurple1", width=400, height=80
)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(
    root, text="Control Buttons", bg="purple3", width=400, height=120
)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text="Playlist", bg="purple4")
listbox_frame.place(x=400, y=0, height=200, width=300)

# Variables
current_song = StringVar(root, value="Not selected")
song_status = StringVar(root, value="Not Available")

# Labels
Label(
    song_frame,
    text="CURRENTLY PLAYING:",
    bg="snow3",
    font=("Times", 10, "bold"),
).place(x=5, y=20)

song_lbl = Label(
    song_frame,
    textvariable=current_song,
    bg="snow3",
    font=("Times", 12),
    width=25,
)
song_lbl.place(x=150, y=20)