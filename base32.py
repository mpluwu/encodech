import base64

action = input("If you want to decode, enter 'd'. If you want to encode, enter 'e': ")

if action == 'd':
    base32_string = input("Enter the Base32 string to decode: ")
    decoded_bytes = base64.b32decode(base32_string)
    print("Decoded string:", decoded_bytes.decode())
elif action == 'e':
    text = input("Enter the text to encode: ")
    encoded_bytes = base64.b32encode(text.encode())
    print("Encoded Base32 string:", encoded_bytes.decode())
else:
    print("Invalid action. Please enter 'd' or 'e'.")
