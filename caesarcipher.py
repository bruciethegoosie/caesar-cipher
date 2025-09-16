import tkinter as tk
from tkinter import messagebox



"""The function takes in a string as an argument and loops over each character 
to shift it by the key and return the characters back as a list.
"""
def encrypt(plaintext: str, key: int) -> list:
    key %= 26
    enc_message = []
    for ch in plaintext:
        enc_message.append(chr(ord(ch) + key))
    print(enc_message)
    
    return enc_message

"""This function decrypts the message when provided a ciphertext and key by subtracting
the key to return the message to the original state"""
def decrypt(ciphertext: str, key: int)-> str: 
    dec_message = []
    for ch in ciphertext:
        dec_message.append(chr(ord(ch) - key))
    print(dec_message)
    
    return dec_message
    

input_key = int(input("Enter a key (0-25): "))
user_input = str(input("Enter a message to encrypt: ")).strip()
encrypt(user_input, input_key)