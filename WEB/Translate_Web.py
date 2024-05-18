import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import tkinter as tk
from tkinter import ttk
from tkinter import *

def translate_text(english_text):
    translator = Translator()
    try:
        # Ensure input is a string
        if isinstance(english_text, str) and english_text.strip():
            translation = translator.translate(english_text, src='en', dest='vi')
            return translation.text
        else:
            return ''
    except Exception as e:
        print(f"Translation error: {e}")
        return ''

def scrape_webpage():
    url = src_text.get("1.0", tk.END).strip()
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        translated_paragraphs = []

        for p in paragraphs:
            paragraph_text = p.get_text().strip()
            if paragraph_text:
                translated_text = translate_text(paragraph_text)
                if translated_text:
                    translated_paragraphs.append(translated_text + '\n\n')  # Thêm ký tự xuống dòng vào cuối mỗi đoạn dịch

        text = '\n'.join(translated_paragraphs)
        tgt_text.delete("1.0", tk.END)
        tgt_text.insert(tk.END, text)
        return text
    else:
        print("Không thể lấy nội dung trang web. Mã trạng thái:", response.status_code)
        return None


# Hàm để xóa văn bản trong ô nguồn và ô đích
def clear_text():
    src_text.delete("1.0", tk.END)
    tgt_text.delete("1.0", tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Dịch thuật Website English")

# Thiết lập icon cho cửa sổ
# image_icon = PhotoImage(file = "icon.png")
# root.iconphoto(False, image_icon)
root.iconbitmap("icon.ico")  

# Tạo các khung cho giao diện
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Nhãn và khung nhập văn bản nguồn
ttk.Label(frame, text="Web English :").grid(row=0, column=0, sticky=tk.W)
src_text = tk.Text(frame, width=50, height=10)
src_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Nhãn và khung nhập văn bản đích
ttk.Label(frame, text="Văn bản dịch :").grid(row=2, column=0, sticky=tk.W)
tgt_text = tk.Text(frame, width=50, height=10)
tgt_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Danh sách các ngôn ngữ
# languages = {
#     'Tiếng Anh': 'en',
#     'Tiếng Việt': 'vi',
#     'Tiếng Pháp': 'fr',
#     'Tiếng Đức': 'de',
#     'Tiếng Tây Ban Nha': 'es',
#     'Tiếng Trung': 'zh-cn',
#     'Tiếng Nhật': 'ja',
#     'Tiếng Hàn': 'ko',
# }

# Nhãn và combobox chọn ngôn ngữ nguồn
# src_lang_combobox = ttk.Combobox(frame, values=list(languages.keys()), state='readonly')
# src_lang_combobox.grid(row=0, column=1, sticky=tk.W)
# src_lang_combobox.set('Tiếng Anh')

# Nhãn và combobox chọn ngôn ngữ đích
# tgt_lang_combobox = ttk.Combobox(frame, values=list(languages.keys()), state='readonly')
# tgt_lang_combobox.grid(row=2, column=1, sticky=tk.W)
# tgt_lang_combobox.set('Tiếng Việt')

# Nút dịch
translate_button = ttk.Button(frame, text="Run", command=scrape_webpage)
translate_button.grid(row=2, column=0, columnspan=2, sticky=tk.E)

# Nút xóa
clear_button = ttk.Button(frame, text="Xóa", command=clear_text)
clear_button.grid(row=0, column=0, columnspan=2, sticky=tk.E)

# Chạy vòng lặp chính của giao diện
root.mainloop()