import tkinter as tk
from tkinter import messagebox

# Function to check if the key is valid
def check_key():
    try:
        key = int(key_entry.get())
        if key >= 0 and key <= 25:
            messagebox.showinfo("Valid Key", f"Key {key} is valid.")

            # Hide key input widgets after valid key entry
            key_label.pack_forget()
            key_entry.pack_forget()
            key_button.pack_forget()

            """# Show message input widgets
            msg_label.pack(pady=7)
            msg_entry.pack()
            msg_button = tk.Button(window, text="Encrypt/Decrypt", command=encrypt)
            msg_button.pack(pady=7)"""

        else:
            messagebox.showerror("Invalid Key", "Key must be between 0 and 25.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# (Caesar Cipher logic)
def shift_char(ch: str, key: int)-> str:
    if ch.isupper():
        base = ord('A')
        return chr((ord(ch) - base + key) % 26 + base)
    elif ch.islower():
        base = ord('a')
        return chr((ord(ch) - base + key) % 26 + base)
    else:
        return ch

# Encryption function that shifts each char by the key provided
def encrypt(plaintext: str, key: int) -> str:
    enc_message = []
    for ch in plaintext:
        enc_message.append(shift_char(ch, key))
    return "".join(enc_message)

# Decryption function that shifts each char back by the key provided
def decrypt(ciphertext: str, key: int) -> str:
    dec_message = []
    for ch in ciphertext:
        dec_message.append(shift_char(ch, -key))  # negative shift
    return "".join(dec_message)


print("Encrypted Message:", encrypt('Pizza is good', 1))
print("Decrypted Message:", decrypt('Qjaab jt hppe', 1))

# Main window
window = tk.Tk()
window.title("Caesar Cipher Input Box")
window.geometry("300x300")
window.config(background="#0b0312")

# Key input and button
key_label = tk.Label(window, text="Enter a key (0-25):")
key_label.pack(pady=7)
key_entry = tk.Entry(window)
key_entry.pack()
key_button = tk.Button(window, text="Submit Key", command=check_key)
key_button.pack(pady=7)

# Enter a message to encrypt/decrypt
msg_label = tk.Label(window, text="Enter a message to Encrypt:", bg="#0b0312", fg="white")
msg_entry = tk.Entry(window, width=40)

window.mainloop()

