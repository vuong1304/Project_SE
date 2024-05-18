
import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import os

def run_autocap():
    # Lấy link YouTube từ input_entry
    youtube_link = input_entry.get()
    #  https://www.youtube.com/shorts/stUofW3whpE
    # Kiểm tra xem link có hợp lệ không
    if not youtube_link.startswith("https://www.youtube.com"):
        messagebox.showerror("Error", "Invalid YouTube link")
        return
    
    

    # Thực hiện thời gian bắt đầu
    start_time = time.time()

    # Thực thi lệnh python autocap.py youtube-g <youtube_link>
    subprocess.run(["python", "autocap.py", "youtube-g", youtube_link])

    # Thực hiện lệnh ffmpeg để thêm phụ đề vào video
    ffmpeg_command = [
        "ffmpeg", "-y",
        "-i", "yt.mp4",
        "-i", "temp.mp3",
        "-filter_complex", "subtitles=output.srt:force_style='Name=Default,Fontname=Cambria Bold,Fontsize=20,PrimaryColour=&H05C8F7&,SecondaryColour=&h0000FF,BackColour=&H0,BorderStyle=3,Shadow=0',setsar=1",
        "-map", "1:a:0",
        "-vcodec", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "25",
        "-g", "160",
        "-b:v", "4000k",
        "-profile:v", "main",
        "-level", "3.1",
        "-acodec", "libmp3lame",
        "-b:a", "128k",
        "-ar", "44100",
        "-preset", "superfast",
        "outvideo.mp4"
    ]
    subprocess.run(ffmpeg_command)
    
    # Tính thời gian chạy
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    time_label.config(text=f"Elapsed Time: {elapsed_time_str}")

    messagebox.showinfo("Success", "Video with subtitles created successfully!")
    
    # Mở file outvideo.mp4 sau khi chạy xong
    os.system("outvideo.mp4")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Ứng dụng Dịch thuật")
# Thiết lập icon cho cửa sổ
root.iconbitmap("icon.ico")

# Tạo label và entry cho link YouTube
youtube_label = tk.Label(root, text="Enter YouTube link:")
youtube_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()

# Tạo nút để chạy chương trình
run_button = tk.Button(root, text="Run", command=run_autocap)
run_button.pack()

# Label để hiển thị thời gian chạy
time_label = tk.Label(root, text="")
time_label.pack()

# Chạy vòng lặp chính của giao diện
root.mainloop()
