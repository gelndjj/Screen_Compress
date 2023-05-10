import tkinter as tk
from tkinter import filedialog
import subprocess, os, time
import customtkinter as ck
from PIL import ImageTk, Image

def select_file():
    file_paths = filedialog.askopenfilenames()
    input_entry.delete(0, tk.END)
    for file_path in file_paths:
        input_entry.insert(tk.END, file_path + "\n")

    if input_entry.get():
        compress_2k_button.configure(state=tk.NORMAL)
        compress_1080p_button.configure(state=tk.NORMAL)
        compress_720p_button.configure(state=tk.NORMAL)
        compress_480p_button.configure(state=tk.NORMAL)
        compress_h265_button.configure(state=tk.NORMAL)
    else:
        compress_2k_button.configure(state=tk.DISABLED)
        compress_1080p_button.configure(state=tk.DISABLED)
        compress_720p_button.configure(state=tk.DISABLED)
        compress_480p_button.configure(state=tk.DISABLED)
        compress_h265_button.configure(state=tk.DISABLED)
def quit():
    root.destroy()

def compress_video_2K():
    input_files = input_entry.get().split("\n")[:-1]
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_2K.mp4"
        start_time = time.time()
        command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-c:a', 'copy', '-filter:v', 'scale=w=2560:h=1440:force_original_aspect_ratio=decrease,pad=2560:1440:(ow-iw)/2:(oh-ih)/2', output_file]
        subprocess.run(command)
        end_time = time.time()
        time_taken = end_time - start_time
        success_label.configure(text="Compression 2K complete!\nTime taken: {:.2f} seconds".format(time_taken))

def compress_1080p():
    input_files = input_entry.get().split("\n")[:-1]
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_1080.mp4"
        start_time = time.time()
        command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-c:a', 'copy', '-vf',
                   'scale=w=1920:h=1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2',
                   output_file]
        subprocess.run(command)
        end_time = time.time()
        time_taken = end_time - start_time
        success_label.configure(text="Compression 1080 complete!\nTime taken: {:.2f} seconds".format(time_taken))

def compress_720p():
    input_files = input_entry.get().split("\n")[:-1]
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_720.mp4"
        start_time = time.time()
        command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '23', '-preset', 'slow', '-c:a', 'copy', '-filter:v', 'scale=w=1280:h=720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2', output_file]
        subprocess.run(command)
        end_time = time.time()
        time_taken = end_time - start_time
        success_label.configure(text="Compression 720 complete!\nTime taken: {:.2f} seconds".format(time_taken))

def compress_480p():
    input_files = input_entry.get().split("\n")[:-1]
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_480.mp4"
        start_time = time.time()
        command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '25', '-preset', 'slow', '-c:a', 'copy', '-filter:v', 'scale=w=854:h=480:force_original_aspect_ratio=decrease,pad=854:480:(ow-iw)/2:(oh-ih)/2', output_file]
        subprocess.run(command)
        end_time = time.time()
        time_taken = end_time - start_time
        success_label.configure(text="Compression 480 complete!\nTime taken: {:.2f} seconds".format(time_taken))

def compress_h265():
    input_files = input_entry.get().split("\n")[:-1]
    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_h265.mp4"
        start_time = time.time()
        command = ['ffmpeg', '-i', input_file, '-c:v', 'libx265', '-crf', '28', '-preset', 'medium', '-c:a', 'copy', output_file]
        subprocess.run(command)
        end_time = time.time()
        time_taken = end_time - start_time
        success_label.configure(text="Compression h265 complete!\nTime taken: {:.2f} seconds".format(time_taken))

# Create the GUI
root = tk.Tk()
root.geometry("720x150")
root.title("Screen Record Compressor")

frame = tk.Frame(root, width=720, height=150, borderwidth=0, highlightthickness=0)
frame.pack()
image = Image.open("img_soft/main_win.png")
img = ImageTk.PhotoImage(image)

canvas = tk.Canvas(frame, width=720, height=150, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=img)

input_label = ck.CTkLabel(frame, text="Input File", fg_color="#66fe8d", text_color="black")
input_label.place(x=60, y=52)

input_entry = ck.CTkEntry(frame, width=240, corner_radius=0, fg_color="white", text_color="black", border_color="black", border_width=3)
input_entry.place(x=180, y=52)

input_button = ck.CTkButton(frame, text="Select File", width=70, bg_color="#66fe8d", border_width=3, border_color="black", command=select_file)
input_button.place(x=445, y=52)

quit_button = ck.CTkButton(frame, text="Quit", width=70, bg_color="#66fe8d", border_width=3, border_color="black", command=quit)
quit_button.place(x=570, y=52)

compress_2k_button = ck.CTkButton(frame, text="2K", width=70, bg_color="#a67614", border_width=3, border_color="black", state=tk.DISABLED, command=compress_video_2K)
compress_2k_button.place(x=60, y=110)

compress_1080p_button = ck.CTkButton(frame, text="1080", width=70, bg_color="#a67614", border_width=3, border_color="black", state=tk.DISABLED, command=compress_1080p)
compress_1080p_button.place(x=140, y=110)

compress_720p_button = ck.CTkButton(frame, text="720", width=70, bg_color="#a67614", border_width=3, border_color="black", state=tk.DISABLED, command=compress_720p)
compress_720p_button.place(x=222, y=110)

compress_480p_button = ck.CTkButton(frame, text="480", width=70, bg_color="#a67614", border_width=3, border_color="black", state=tk.DISABLED, command=compress_480p)
compress_480p_button.place(x=303, y=110)

compress_h265_button = ck.CTkButton(frame, text="H.265", width=70, bg_color="#a67614", border_width=3, border_color="black", state=tk.DISABLED, command=compress_h265)
compress_h265_button.place(x=385, y=110)

success_label = ck.CTkLabel(frame, bg_color="#814f00", text="", text_color="black")
success_label.place(x=507, y=110)

root.mainloop()
