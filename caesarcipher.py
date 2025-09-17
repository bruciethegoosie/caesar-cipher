import tkinter as tk
from tkinter import messagebox

#Function for shifting char when provided a key to shift by
def shift_char(ch: str, key: int)-> str:
    if ch.isupper():
        base = ord('A')
        return chr((ord(ch) - base + key) % 26 + base)
    elif ch.islower():
        base = ord('a')
        return chr((ord(ch) - base + key) % 26 + base)
    else:
        return ch

"""The function takes in a string as an argument and loops over each character 
to pass to the shift functio and return the characters back as a list."""
def encrypt(plaintext: str, key: int) -> str:
    enc_message = []
    for ch in plaintext:
        enc_message.append(shift_char(ch, key))
    return "".join(enc_message)

"""This function decrypts the message when provided a ciphertext and key by subtracting
the key to return the message to the original state."""
def decrypt(ciphertext: str, key: int) -> str:
    dec_message = []
    for ch in ciphertext:
        dec_message.append(shift_char(ch, -key))  # negative shift
    return "".join(dec_message)


print(encrypt('xyz', 1))
print(decrypt('bcd', 1))

"""# Main window
root = tk.Tk()
root.title("Caesar Cipher")

# Step 1: Key input
key_label = tk.Label(root, text="Enter a key (0-25):")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

key_button = tk.Button(root, text="Submit Key", command=check_key)
key_button.pack(pady=10)

root.mainloop()"""

