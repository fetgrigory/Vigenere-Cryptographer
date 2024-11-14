from tkinter import Tk, Label, Entry, Button, Menu, END
from tkinter import messagebox as mb


class VigenereCipher:
    """AI is creating summary for
    """
    def __init__(self, key):
        # Initialize the Vigenere Cipher with a given key
        self.key = key

    def encrypt(self, text):
        """AI is creating summary for encrypt

        Args:
            text ([type]): [description]

        Returns:
            [type]: [description]
        """
        # Encrypts the input text using the Vigenere cipher
        result = ""
        # The length of the cipher key
        key_length = len(self.key)
        for i, char in enumerate(text):
            # Process only alphabetic characters
            if char.isalpha():
                # Calculate the shift based on the corresponding key character
                shift = ord(self.key[i % key_length].lower()) - ord('а')
                if char.islower():
                    # Encrypt lowercase letters
                    new_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
                else:
                    # Encrypt uppercase letters
                    new_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
                result += new_char
            else:
                result += char
        return result

    def decrypt(self, text):
        """AI is creating summary for decrypt

        Args:
            text ([type]): [description]

        Returns:
            [type]: [description]
        """
        # Decrypts the input text using the Vigenère cipher
        result = ""
        # The length of the cipher key
        key_length = len(self.key)
        for i, char in enumerate(text):
            # Process only alphabetic characters
            if char.isalpha():
                # Calculate the shift based on the corresponding key character
                shift = ord(self.key[i % key_length].lower()) - ord('а')
                if char.islower():
                    # Decrypt lowercase letters
                    new_char = chr((ord(char) - ord('а') - shift) % 32 + ord('а'))
                else:
                    # Decrypt uppercase letters
                    new_char = chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
                result += new_char
            else:
                result += char
        return result


class AppGUI:
    """AI is creating summary for
    """
    def __init__(self, root):
        # Initialize the GUI components
        self.root = root
        self.text_entry = None
        self.shift_entry = None
        self.result_entry = None
        self.setup_gui()

    def setup_gui(self):
        """AI is creating summary for setup_gui
        """
        # Configure the main GUI window
        self.root.title("Шифр Виженера")
        self.root.geometry("600x500")
        self.root["bg"] = "#008000"

        text_label = Label(
            self.root, text="Введите текст:",
            font="Arial 14 italic",
            bg="#008000",
            fg="black"
        )
        text_label.pack(pady=10)
        self.text_entry = Entry(self.root, font="Arial 14", width=40)
        self.text_entry.pack(pady=10)
        shift_label = Label(
            self.root,
            text="Введите ключ шифрования:",
            font="Arial 14 italic",
            bg="#008000",
            fg="black",
        )
        shift_label.pack(pady=10)

        # Create an entry widget to accept key input
        self.shift_entry = Entry(self.root, font="Arial 14", width=40)
        self.shift_entry.pack(pady=10)

        # Create a button to trigger encryption
        encrypt_button = Button(
            self.root,
            text="Зашифровать текст",
            bg="#DAA520",
            font="Arial 14",
            command=self.vigenere_encrypt_text,
        )
        encrypt_button.pack(pady=10) 

        # Create a button to trigger decryption
        decrypt_button = Button(
            self.root,
            text="Расшифровать текст",
            bg="#DAA520",
            font="Arial 14",
            command=self.vigenere_decrypt_text,
        )
        decrypt_button.pack(pady=10)

        result_label = Label(
            self.root,
            text="Результат:",
            font="Arial 14 italic",
            bg="#008000",
            fg="black"
        )
        result_label.pack(pady=10)

        # Create an entry widget to display the encryption/decryption result
        self.result_entry = Entry(self.root, font="Arial 14", width=40)
        self.result_entry.pack(pady=10)

        self.setup_menu()

    def setup_menu(self):
        """AI is creating summary for setup_menu
        """
        # Configure the menu for the application window
        main_menu = Menu(self.root)
        about_menu = Menu(main_menu, tearoff=0)
        about_menu.add_command(label="О программе", command=self.show_info)
        main_menu.add_cascade(label="Справка", menu=about_menu)
        self.root.config(menu=main_menu)

    def show_info(self):
        """AI is creating summary for show_info
        """
        mb.showinfo("О программе", "Феткулин Григорий - Шифр Виженера, 2023")


class VigenereApp(AppGUI, VigenereCipher):
    """AI is creating summary for VigenereApp

    Args:
        AppGUI ([type]): [description]
        VigenereCipher ([type]): [description]
    """
    # Combine GUI and Cipher functionalities in a single application
    def __init__(self, root):
        AppGUI.__init__(self, root)
        VigenereCipher.__init__(self, key="")

    def vigenere_encrypt_text(self):
        """AI is creating summary for vigenere_encrypt_text
        """
        # Encrypt the text entered in the GUI
        text = self.text_entry.get()
        self.key = self.shift_entry.get()

        if not text or not self.key:
            # Show error if text or key is not provided
            mb.showerror("Ошибка", "Введите текст и ключ шифрования")
            return
        # Encrypt the text
        result = self.encrypt(text)
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, result)

    def vigenere_decrypt_text(self):
        """AI is creating summary for vigenere_decrypt_text
        """
        # Decrypt the text entered in the GUI
        text = self.text_entry.get()
        self.key = self.shift_entry.get()

        if not text or not self.key:
            # Show error if text or key is not provided
            mb.showerror("Ошибка", "Введите текст и ключ шифрования")
            return
            # Decrypt the text
        result = self.decrypt(text)
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, result)


if __name__ == "__main__":
    root = Tk()
    app = VigenereApp(root)
    root.mainloop()
