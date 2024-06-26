import tkinter as tk
import subprocess
import os


def run_trans():
    # Đường dẫn tới file Trans.py trong thư mục translator
    # trans_path = os.path.join("translator", "Trans.py")
    # subprocess.run(["python", trans_path])

    project_se_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Đường dẫn đến thư mục translator trong Project_SE
    translator_path = os.path.join(project_se_path, "translator")

    # Đường dẫn đến file Trans.py trong thư mục translator
    trans_path = os.path.join(translator_path, "Trans.py")
    subprocess.Popen(["python", trans_path])


def run_lenh():
    # Đường dẫn tới file LENH.py trong thư mục YOUTUBE
    # lenh_path = os.path.join("YOUTUBE", "LENH.py")
    lenh_path = os.path.join("LENH.py")
    subprocess.run(["python", lenh_path])

def run_web():
    # web_path = os.path.join("WEB", "Translate_Web.py")
    # subprocess.run(["python", web_path])

    project_se_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Đường dẫn đến thư mục translator trong Project_SE
    translator_path = os.path.join(project_se_path, "WEB_")

    # Đường dẫn đến file Trans.py trong thư mục translator
    trans_path = os.path.join(translator_path, "Translate_Web.py")
    subprocess.Popen(["python", trans_path])


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng Dụng Dịch Thuật")
root.iconbitmap("icon.ico") 
# Thiết lập kích thước của cửa sổ chính
root.geometry("300x300")

# Tạo nhãn tiêu đề
title_label = tk.Label(root, text="Translator Options", font=("Arial", 16))
title_label.pack(pady=20)

# Tạo nút cho lựa chọn 1: Dịch một đoạn văn
trans_button = tk.Button(root, text="Dịch một đoạn văn", command=run_trans, width=20, height=2)
trans_button.pack(pady=10)

# Tạo nút cho lựa chọn 2: Dịch youtube
lenh_button = tk.Button(root, text="Dịch youtube", command=run_lenh, width=20, height=2)
lenh_button.pack(pady=10)

#Nút 3

lenh_button = tk.Button(root, text="Dịch website", command=run_web, width=20, height=2)
lenh_button.pack(pady=10)

# Chạy vòng lặp chính của giao diện
root.mainloop()

