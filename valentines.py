import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence  # Import Pillow for GIF handling

def ask_valentine():
    # List of messages to display when "No" is pressed
    no_messages = [
        "HEY! WRONG BUTTON",
        ":( Try the button to the left...",
        "Meanie ",
        "PLEASEEEEEEE",
        "PRETTYYYY PLEASEESEESEESE",
        "STOPPPPPPPPPP",
        "You're breaking my heart ;("
    ]
    message_index = 0  # Index to keep track of the current message

    def on_yes():
        messagebox.showinfo("YAY!", "I LOVE YOUUUU!!!!")
        root.destroy()  # Close the window

    def on_no():
        nonlocal message_index
        # Display the current message
        messagebox.showinfo(":(", no_messages[message_index])
        # Increment the message index, and loop back to the start if necessary
        message_index = (message_index + 1) % len(no_messages)

    # Function to update the GIF frames
    def update_gif(frame):
        frame = next(frames)  # Get the next frame
        gif_label.configure(image=frame)
        root.after(100, update_gif, frame)  # Schedule the next update (100ms delay)

    # Create the main window
    root = tk.Tk()
    root.title("Valentine's Question")
    root.geometry("800x800")  # Set window size

    # Load the animated GIF
    try:
        gif = Image.open(r'D:\Valentine\gif-valentine.gif')  # Replace with your GIF file path
        frames = iter(ImageSequence.Iterator(gif))  # Extract frames
        first_frame = next(frames)  # Get the first frame
        photo = ImageTk.PhotoImage(first_frame)

        # Add the GIF to a label
        gif_label = tk.Label(root, image=photo)
        gif_label.image = photo  # Keep a reference to avoid garbage collection
        gif_label.pack(pady=10)

        # Start the animation
        root.after(100, update_gif, first_frame)  # Start updating frames
    except FileNotFoundError:
        # If the GIF is not found, display a placeholder text
        error_label = tk.Label(root, text="GIF not found!", font=("Arial", 12), fg="red")
        error_label.pack(pady=10)

    # Add a label with the question
    label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 16), fg="red")
    label.pack(pady=10)

    # Add a "Yes" button
    yes_button = tk.Button(root, text="Yes", font=("Arial", 12), bg="pink", fg="white", command=on_yes)
    yes_button.pack(side=tk.LEFT, padx=80)

    # Add a "No" button
    no_button = tk.Button(root, text="No", font=("Arial", 12), bg="lightgray", fg="black", command=on_no)
    no_button.pack(side=tk.RIGHT, padx=80)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    ask_valentine()