import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import tkinter as tk
from tkinter import ttk
from tkinter import *

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        # Đảm bảo đầu vào là một chuỗi
        if isinstance(text, str) and text.strip():
            translation = translator.translate(text, src=src_lang, dest=dest_lang)
            return translation.text
        else:
            return ''
    except Exception as e:
        print(f"Translation error: {e}")
        return ''

# Cào dữ liệu từ web
def scrape_webpage():
    url = src_text.get("1.0", tk.END).strip()
    src_lang = languages[src_lang_combobox.get()]
    dest_lang = languages[tgt_lang_combobox.get()]
    
    # Gửi yêu cầu GET tới url
    response = requests.get(url)
    
    # Kiểm tra xem thành công không
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất thông tin cần từ HTML
        paragraphs = soup.find_all(['p', 'b', 'i', 'strong', 'emp', 'font', 'ul', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        translated_paragraphs = []

        for p in paragraphs:
            paragraph_text = p.get_text().strip()
            if paragraph_text:
                translated_text = translate_text(paragraph_text, src_lang, dest_lang)
                if translated_text:
                    translated_paragraphs.append(translated_text)

        text = '\n'.join(translated_paragraphs)
        tgt_text.delete("1.0", tk.END)
        tgt_text.insert(tk.END, text)
        return text

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

# Hàm để xóa văn bản trong ô nguồn và ô đích
def clear_text():
    src_text.delete("1.0", tk.END)
    tgt_text.delete("1.0", tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Dịch Thuật")

# Thiết lập icon cho cửa sổ
image_icon = PhotoImage(file = "WEB_/icon.png")
root.iconphoto(False, image_icon)

# Tạo các khung cho giao diện
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Nhãn và khung nhập văn bản nguồn
ttk.Label(frame, text="Văn bản nguồn :").grid(row=0, column=0, sticky=tk.W)
src_text = tk.Text(frame, width=50, height=10)
src_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Nhãn và khung nhập văn bản đích
ttk.Label(frame, text="Văn bản dịch :").grid(row=2, column=0, sticky=tk.W)
tgt_text = tk.Text(frame, width=50, height=10)
tgt_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Danh sách các ngôn ngữ
languages = {
    'Tiếng Anh': 'en',
    'Tiếng Việt': 'vi',
    'Tiếng Pháp': 'fr',
    'Tiếng Đức': 'de',
    'Tiếng Tây Ban Nha': 'es',
    'Tiếng Trung': 'zh-cn',
    'Tiếng Nhật': 'ja',
    'Tiếng Hàn': 'ko',
}

# Nhãn và combobox chọn ngôn ngữ nguồn
src_lang_combobox = ttk.Combobox(frame, values=list(languages.keys()), state='readonly')
src_lang_combobox.grid(row=0, column=1, sticky=tk.W)
src_lang_combobox.set('Tiếng Anh')

# Nhãn và combobox chọn ngôn ngữ đích
tgt_lang_combobox = ttk.Combobox(frame, values=list(languages.keys()), state='readonly')
tgt_lang_combobox.grid(row=2, column=1, sticky=tk.W)
tgt_lang_combobox.set('Tiếng Việt')

# Nút dịch
translate_button = ttk.Button(frame, text="Dịch", command=scrape_webpage)
translate_button.grid(row=2, column=0, columnspan=2, sticky=tk.E)

# Nút xóa
clear_button = ttk.Button(frame, text="Xóa", command=clear_text)
clear_button.grid(row=0, column=0, columnspan=2, sticky=tk.E)

# Chạy vòng lặp chính của giao diện
root.mainloop()