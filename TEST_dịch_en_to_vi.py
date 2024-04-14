# ==========================Test dich English sang Việt ====================
# pip install googletrans==4.0.0-rc1 ( cần cài đặt thư viện trước khi chạy băg cmd )

from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='vi')
    return translation.text

# Đoạn văn bản bạn muốn dịch
english_text = """
My love is as a fever, longing still

For that which longer nurseth the disease;

Feeding on that which doth preserve the sill,

The uncertain sickly appetite to please.

"""

# Dịch đoạn văn bản
vietnamese_text = translate_text(english_text)
print(vietnamese_text)

