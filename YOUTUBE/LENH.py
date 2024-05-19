
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
root.title("Tạo Subtitle Youtube")
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
# ---------------------------------------------------------------------------------------------------------------------------
# import subprocess
# import tkinter as tk
# from datetime import datetime

# def download_and_process():
#     youtube_link = entry_link.get()

#     # Lệnh để tải video từ YouTube
#     download_command = ["python", "autocap.py", "youtube-g", youtube_link]
#     subprocess.run(download_command)

#     # Lệnh ffmpeg để thêm phụ đề và xuất video
#     ffmpeg_command = [
#         "ffmpeg", "-y",
#         "-i", "yt.mp4",
#         "-i", "temp.mp3",
#         "-filter_complex", "subtitles=output.srt:force_style='Name=Default,Fontname=Cambria Bold,Fontsize=20,PrimaryColour=&H05C8F7&,SecondaryColour=&h0000FF,BackColour=&H0,BorderStyle=3,Shadow=0',setsar=1",
#         "-map", "1:a:0",
#         "-vcodec", "libx264",
#         "-pix_fmt", "yuv420p",
#         "-r", "25",
#         "-g", "160",
#         "-b:v", "4000k",
#         "-profile:v", "main",
#         "-level", "3.1",
#         "-acodec", "libmp3lame",
#         "-b:a", "128k",
#         "-ar", "44100",
#         "-preset", "superfast",
#         "outvideo.mp4"
#     ]

#     # Thực thi lệnh ffmpeg
#     subprocess.run(ffmpeg_command)

#     # Hiển thị thời gian thực thi
#     end_time = datetime.now()
#     execution_time = end_time - start_time
#     label_time.config(text=f"Thời gian thực thi: {execution_time}")

# def open_video():
#     # Mở video sau khi hoàn thành
#     subprocess.run(["outvideo.mp4"], shell=True)

# # Tạo cửa sổ giao diện
# root = tk.Tk()
# root.title("Ứng dụng tạo phụ đề")

# # Khởi tạo các widget
# label_link = tk.Label(root, text="Link YouTube:")
# entry_link = tk.Entry(root, width=50)
# button_download = tk.Button(root, text="Tải và xử lý", command=download_and_process)
# label_time = tk.Label(root, text="")
# button_open_video = tk.Button(root, text="Mở video", command=open_video)

# # Định vị các widget trên cửa sổ giao diện
# label_link.grid(row=0, column=0, padx=10, pady=5, sticky="e")
# entry_link.grid(row=0, column=1, padx=10, pady=5)
# button_download.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
# label_time.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
# button_open_video.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# # Bắt đầu thời gian khi chương trình được khởi chạy
# start_time = datetime.now()

# # Chạy vòng lặp giao diện chính
# root.mainloop()

