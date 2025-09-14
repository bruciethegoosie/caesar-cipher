import tkinter as tk
from tkinter import messagebox




def encrypt(plaintext: str, key: int) -> str:
    key %= 26
    for ch in plaintext:
        
    ciphertext = plaintext + key


#def decrypt(ciphertext, key):
    #plaintext = ciphertext - key

input_key = int(input("Enter a key (0-25): "))
user_input = str(input("Enter a message to encrypt: ")).strip()
encrypt(user_input, input_key)