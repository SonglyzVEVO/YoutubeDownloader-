from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import YT 
import tkinter.messagebox as tk1
import tkinter.messagebox as tk1
import webbrowser
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\narae\OneDrive\Desktop\YoutubeDownloader\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def know_more_clicked(event):
    instructions = ("https://github.com/SonglyzVEVO?tab=repositories")
    webbrowser.open_new_tab(instructions)


def btn_clicked_dowload_Audio():
    # 1.0, "end-1c"
    URL = entry_1.get("1.0","end")
    print(f"Get URL : {URL}")
    entry_1.delete("1.0","end")
    YT.getAudio(URL)
    

def btn_clicked_dowload_Video():
    # 1.0, "end-1c"
    URL = entry_1.get("1.0","end")
    print(f"Get URL : {URL}")
    entry_1.delete("1.0","end")
    YT.getVideo(URL)
    
    
window = Tk()
window.title("Youtube Downloader by Songlyz")

window.geometry("600x250")
window.configure(bg = "#F5F5F5")


canvas = Canvas(
    window,
    bg = "#F5F5F5",
    height = 250,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# Audio dowload
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: btn_clicked_dowload_Audio(),
    relief="flat"
)
button_1.place(
    x=473.0,
    y=133.0,
    width=80.0,
    height=40.0
)

# Audio dowload
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: btn_clicked_dowload_Video(),
    relief="flat"
)
button_2.place(
    x=387.0,
    y=133.0,
    width=80.0,
    height=40.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

entry_bg_1 = canvas.create_image(
    248.0,
    153.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=133.0,
    y=133.0,
    width=230.0,
    height=38.0
)

canvas.create_text(
    35.0,
    133.0,
    anchor="nw",
    text="URL",
    fill="#000000",
    font=("UbuntuMono Regular", 40 * -1)
)

canvas.create_text(
    129.0,
    27.0,
    anchor="nw",
    text="Youtube Download",
    fill="#000000",
    font=("UbuntuMono Regular", 40 * -1)
)

canvas.create_text(
    128.0,
    84.0,
    anchor="nw",
    text="Paste URL and Click red button",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

know_more = tk.Label(
    text="Click here for more detail",
    bg="#3A7FF6", fg="white", cursor="hand2")
know_more.place(x=225, y=200)
know_more.bind('<Button-1>', know_more_clicked)

window.resizable(False, False)
window.mainloop()
