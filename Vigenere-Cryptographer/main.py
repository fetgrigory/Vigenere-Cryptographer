"""
This module make

Author: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/04/17
Ending 2022/04/17

"""

from tkinter import Tk, Label, Entry, Button, Menu, LEFT, W, END
from tkinter import messagebox as mb


def vigenere_encrypt_text():
    """AI is creating summary for vigenere_encrypt_text
    """

    #  Get the text and the encryption key
    text = text_entry.get()
    key = shift_entry.get()

    # Check that the text and key are not empty
    if not text or not key:
        mb.showerror("Ошибка", "Введите текст и ключ шифрования")
        return

    # We give the text and the key to the upper case
    text = text.upper()
    key = key.upper()

    # Encrypt the text
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            case = char.isupper()
            char_code = ord(char) - ord("А")
            key_code = ord(key[i % len(key)]) - ord("А")
            # 32 letters in the Russian alphabet
            new_code = (char_code + key_code) % 32
            new_char = chr(new_code + ord("А"))
            if not case:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char

    # Output the result
    result_entry.delete(0, END)
    result_entry.insert(0, result)


def vigenere_decrypt_text():
    """AI is creating summary for vigenere_decrypt_text
    """

    #  Get the text and the encryption key
    text = text_entry.get()
    key = shift_entry.get()

    # Check that the text and key are not empty
    if not text or not key:
        mb.showerror("Ошибка", "Введите текст и ключ шифрования")
        return

    # Give the text and the key to the upper case
    text = text.upper()
    key = key.upper()

    # Decoding the text
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            case = str.isupper(char)
            char_code = ord(char) - ord("А")
            key_code = ord(key[i % len(key)]) - ord("А")
            # 32 letters in the Russian alphabet
            new_code = (char_code - key_code) % 32
            new_char = chr(new_code + ord("А"))
            if not case:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char

    # Output the result
    result_entry.delete(0, END)
    result_entry.insert(0, result)


# Creating a graphical interface
root = Tk()
root.title("Шифр Виженера")
root.geometry("600x500")
root["bg"] = "#008000"

# Creating elements for entering text and a key
text_label = Label(
    root, text="Введите текст:",
    font="Arial 14 italic",
    bg="#008000",
    fg="white"
)
text_label.pack(pady=10)
text_label.config(
    font="Arial 14",
    fg="black",
    bg="#008000",
    width=40,
    height=1,
    anchor=W,
    wraplength=500,
    justify=LEFT,
    padx=10,
    pady=10,
)

text_entry = Entry(root, font="Arial 14", width=40)
text_entry.pack(pady=10)

shift_label = Label(
    root,
    text="Введите ключ шифрования:",
    font="Arial 14 italic",
    bg="#008000",
    fg="white",
)
shift_label.pack(pady=10)
shift_label.config(
    font="Arial 14",
    fg="black",
    bg="#008000",
    width=40,
    height=1,
    anchor=W,
    wraplength=500,
    justify=LEFT,
    padx=10,
    pady=10,
)

shift_entry = Entry(root, font="Arial 14", width=40)
shift_entry.pack(pady=10)

# Creating buttons for encrypting and decrypting text
encrypt_button = Button(
    root,
    text="Зашифровать текст",
    bg="#DAA520",
    font="Arial 14",
    command=vigenere_encrypt_text,
)
encrypt_button.pack(pady=10)

decrypt_button = Button(
    root,
    text="Расшифровать текст",
    bg="#DAA520",
    font="Arial 14",
    command=vigenere_decrypt_text,
)
decrypt_button.pack(pady=10)

# Creating a widget to display the result
result_label = Label(
    root, text="Результат:", font="Arial 14 italic", bg="#008000", fg="white"
)
result_label.pack(pady=10)
result_label.config(
    font="Arial 14",
    fg="black",
    bg="#008000",
    width=40,
    height=1,
    anchor=W,
    wraplength=500,
    justify=LEFT,
    padx=10,
    pady=10,
)

result_entry = Entry(root, font="Arial 14", width=40)
result_entry.pack(pady=10)


# Adding the Help menu and the About sub-menu to the main menu
def show_info():
    """AI is creating summary for show_info
    """
    mb.showinfo("О программе", "Феткулин Григорий - Шифр Виженера, 2023")


main_menu = Menu()
file_menu = Menu()
about_menu = Menu()
about_menu.add_command(label="О программе", command=show_info)
main_menu.add_cascade(label="Справка", menu=about_menu)
root.config(menu=main_menu)

# Starting the event processing cycle
root.mainloop()
