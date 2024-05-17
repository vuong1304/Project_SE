import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Hàm để dịch văn bản
def translate_text():
    src_lang = languages[src_lang_combobox.get()]
    tgt_lang = languages[tgt_lang_combobox.get()]
    text = src_text.get("1.0", tk.END).strip()
    
    if text:
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=tgt_lang)
        tgt_text.delete("1.0", tk.END)
        tgt_text.insert(tk.END, translated.text)

# Hàm để xóa văn bản trong ô nguồn và ô đích
def clear_text():
    src_text.delete("1.0", tk.END)
    tgt_text.delete("1.0", tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Dịch thuật")

# Thiết lập icon cho cửa sổ
root.iconbitmap("icon.ico")  # Thay đổi đường dẫn đến tệp icon của bạn

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
translate_button = ttk.Button(frame, text="Dịch", command=translate_text)
translate_button.grid(row=2, column=0, columnspan=2, sticky=tk.E)

# Nút xóa
clear_button = ttk.Button(frame, text="Xóa", command=clear_text)
clear_button.grid(row=0, column=0, columnspan=2, sticky=tk.E)

# Chạy vòng lặp chính của giao diện
root.mainloop()