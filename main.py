from tkinter import Tk, Label, Entry, Button, Menu, LEFT, W, END
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
        # Encrypts the input text using the Vigenère cipher
        result = ""
        key_length = len(self.key)  # The length of the cipher key
        for i, char in enumerate(text):
            if char.isalpha():  # Process only alphabetic characters
                # Calculate the shift based on the corresponding key character
                shift = ord(self.key[i % key_length].lower()) - ord('а')
                if char.islower():
                    # Encrypt lowercase letters
                    new_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
                else:
                    # Encrypt uppercase letters
                    new_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
                result += new_char  # Append encrypted character to the result
            else:
                result += char  # Append non-alphabetic characters unchanged
        return result  # Return the encrypted text

    def decrypt(self, text):
        """AI is creating summary for decrypt

        Args:
            text ([type]): [description]

        Returns:
            [type]: [description]
        """
        # Decrypts the input text using the Vigenère cipher
        result = ""
        key_length = len(self.key)  # The length of the cipher key
        for i, char in enumerate(text):
            if char.isalpha():  # Process only alphabetic characters
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
    def __init__(self, root):
        # Initialize the GUI components
        self.root = root
        self.text_entry = None
        self.shift_entry = None
        self.result_entry = None
        self.setup_gui()  # Set up the user interface

    def setup_gui(self):
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

        # Add a label for showing the result
        result_label = Label(
            self.root,
            text="Результат:",
            font="Arial 14 italic",
            bg="#008000",
            fg="black"
        )
        result_label.pack(pady=10)  # Add padding around the label

        # Create an entry widget to display the encryption/decryption result
        self.result_entry = Entry(self.root, font="Arial 14", width=40)
        self.result_entry.pack(pady=10)

        self.setup_menu()  # Set up the application menu

    def setup_menu(self):
        # Configure the menu for the application window
        main_menu = Menu(self.root)
        about_menu = Menu(main_menu, tearoff=0)
        about_menu.add_command(label="О программе", command=self.show_info)
        main_menu.add_cascade(label="Справка", menu=about_menu)
        self.root.config(menu=main_menu)

    def show_info(self):
        mb.showinfo("О программе", "Феткулин Григорий - Шифр Виженера, 2023")


class VigenereApp(AppGUI, VigenereCipher):
    # Combine GUI and Cipher functionalities in a single application
    def __init__(self, root):
        AppGUI.__init__(self, root)  # Initialize the GUI part
        VigenereCipher.__init__(self, key="")  # Initialize the cipher with an empty key

    def vigenere_encrypt_text(self):
        # Encrypt the text entered in the GUI
        text = self.text_entry.get()  # Get the input text
        self.key = self.shift_entry.get()  # Get the cipher key

        if not text or not self.key:
            # Show error if text or key is not provided
            mb.showerror("Ошибка", "Введите текст и ключ шифрования")
            return

        result = self.encrypt(text)  # Encrypt the text
        self.result_entry.delete(0, END)  # Clear the result entry field
        self.result_entry.insert(0, result)  # Insert the encrypted result

    def vigenere_decrypt_text(self):
        # Decrypt the text entered in the GUI
        text = self.text_entry.get() 
        self.key = self.shift_entry.get()

        if not text or not self.key:
            # Show error if text or key is not provided
            mb.showerror("Ошибка", "Введите текст и ключ шифрования")
            return

        result = self.decrypt(text)  # Decrypt the text
        self.result_entry.delete(0, END)  # Clear the result entry field
        self.result_entry.insert(0, result)  # Insert the decrypted result


if __name__ == "__main__":
    root = Tk()
    app = VigenereApp(root)
    root.mainloop()