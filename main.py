import tkinter as tk
import subprocess
import os

def run_trans():
    # Đường dẫn tới file Trans.py trong thư mục translator
    trans_path = os.path.join("translator", "Trans.py")
    subprocess.run(["python", trans_path])

def run_lenh():
    # Đường dẫn tới file LENH.py trong thư mục YOUTUBE
    lenh_path = os.path.join("YOUTUBE", "LENH.py")
    subprocess.run(["python", lenh_path])

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Translator GUI")

# Thiết lập kích thước của cửa sổ chính
root.geometry("300x200")

# Tạo nhãn tiêu đề
title_label = tk.Label(root, text="Translator Options", font=("Arial", 16))
title_label.pack(pady=20)

# Tạo nút cho lựa chọn 1: Dịch một đoạn văn
trans_button = tk.Button(root, text="Dịch một đoạn văn", command=run_trans, width=20, height=2)
trans_button.pack(pady=10)

# Tạo nút cho lựa chọn 2: Dịch youtube
lenh_button = tk.Button(root, text="Dịch youtube", command=run_lenh, width=20, height=2)
lenh_button.pack(pady=10)

# Chạy vòng lặp chính của giao diện
root.mainloop()
