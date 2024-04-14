# ==========================Test dich English sang Việt ====================
# pip install googletrans==4.0.0-rc1 ( cần cài đặt thư viện trước khi chạy băg cmd )

# from googletrans import Translator

# def translate_text(text):
#     translator = Translator()
#     translation = translator.translate(text, src='en', dest='vi')
#     return translation.text

# # Đoạn văn bản bạn muốn dịch
# english_text = """
# My love is as a fever, longing still

# For that which longer nurseth the disease;

# Feeding on that which doth preserve the sill,

# The uncertain sickly appetite to please.

# """

# # Dịch đoạn văn bản
# vietnamese_text = translate_text(english_text)
# print(vietnamese_text)
#=======================================================================================
import tkinter as tk
from googletrans import Translator

def translate_text():
    

    english_text = text_entry.get("1.0",'end-1c')
    translator = Translator()
    translation = translator.translate(english_text, src='en', dest='vi')
    vietnamese_output.delete("1.0", tk.END)
    vietnamese_output.insert("1.0", translation.text)

def clear_text():
    text_entry.delete("1.0", tk.END)
    vietnamese_output.delete("1.0", tk.END)

# Tạo cửa sổ
root = tk.Tk()
root.title("English to Vietnamese Translator")

# Tạo các thành phần giao diện
text_entry_label = tk.Label(root, text="Nhập văn bản tiếng Anh:")
text_entry_label.grid(row=0, column=0, padx=10, pady=10)

text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=1, column=0, padx=10, pady=10)

translate_button = tk.Button(root, text="Chuyển đổi", command=translate_text)
translate_button.grid(row=2, column=0, padx=10, pady=5)

clear_button = tk.Button(root, text="Xóa tất cả", command=clear_text)
clear_button.grid(row=3, column=0, padx=10, pady=5)

vietnamese_output_label = tk.Label(root, text="Văn bản tiếng Việt:")
vietnamese_output_label.grid(row=4, column=0, padx=10, pady=10)

vietnamese_output = tk.Text(root, height=10, width=50)
vietnamese_output.grid(row=5, column=0, padx=10, pady=10)

# Chạy ứng dụng
root.mainloop()
#================================================================================================================

