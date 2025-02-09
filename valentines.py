import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

def ask_valentine():
    no_messages = [
        "HEY! WRONG BUTTON",
        ":( Try the button to the left...",
        "Meanie ",
        "PLEASEEEEEEE",
        "PRETTYYYY PLEASEESEESEESE",
        "STOPPPPPPPPPP",
        "You're breaking my heart ;("
    ]
    message_index = 0  

    def on_yes():
        messagebox.showinfo("💖 YAYYYYY!!!! 💖", 
        "Happy Valentine's Day Baby! 💕\n\n"
        "You make me so happy, and I am very happy that we will have spent two Valentine's Days together.\n\n"
        "You asked me why I love you, here's why:\n\n"
        "1) You are so friendly to everyone you meet, and it lights up the whole room. Your energy is addictive.\n"
        "2) I like how I can be myself around you, and you can be yourself around me. I've never felt like I had to be someone else when I'm with you.\n"
        "3) You are so empathetic, and it makes me feel secure in our future if we are lucky enough to become parents.\n"
        "4) You took interest in one of my hobbies and even started playing Clash Royale with me hehe. 😊\n\n"
        "This is just **1%** of the reasons why I love you. Please never think that I don't love you or that I'm getting 'tired' of you—that's ridiculous!\n\n"
        "I love you so much!!! 💖\n"
        "I really hope that I get to see you in a wedding dress, and I'm the groom. 😍\n\n"
        "I love you, Jessie. Happy Valentine's Day! ❤️")
        root.destroy()

    def on_no():
        nonlocal message_index
        messagebox.showinfo(":(", no_messages[message_index])
        message_index = (message_index + 1) % len(no_messages)

    # Create the main window
    root = tk.Tk()
    root.title("Valentine's Question")
    root.geometry("800x800")

    try:
        gif = Image.open(r'D:\Valentine\gif-valentine.gif')  # Replace with your GIF file path
        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]  # Load all frames
        frame_count = len(frames)
        frame_index = 0  # Track the current frame

        gif_label = tk.Label(root, image=frames[frame_index])
        gif_label.pack(pady=10)

        def update_gif():
            nonlocal frame_index
            frame_index = (frame_index + 1) % frame_count  # Loop through frames
            gif_label.config(image=frames[frame_index])
            gif_label.image = frames[frame_index]  # Prevent garbage collection
            root.after(100, update_gif)  # Schedule next frame

        root.after(0, update_gif)  # Start animation

    except FileNotFoundError:
        error_label = tk.Label(root, text="GIF not found!", font=("Arial", 12), fg="red")
        error_label.pack(pady=10)

    label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 16), fg="red")
    label.pack(pady=10)

    yes_button = tk.Button(root, text="Yes", font=("Arial", 12), bg="pink", fg="white", command=on_yes)
    yes_button.pack(side=tk.LEFT, padx=80)

    no_button = tk.Button(root, text="No", font=("Arial", 12), bg="lightgray", fg="black", command=on_no)
    no_button.pack(side=tk.RIGHT, padx=80)

    root.mainloop()

if __name__ == "__main__":
    ask_valentine()
