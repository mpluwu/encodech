action = input("If you want to decode, enter 'd'. If you want to encode, enter 'e': ")

if action == 'd':
    ascii_string = input("Enter the ASCII string to decode: ")
    decoded_string = ''.join([chr(int(c)) for c in ascii_string.split()])
    print("Decoded string:", decoded_string)
elif action == 'e':
    text = input("Enter the text to encode: ")
    ascii_string = ' '.join(str(ord(c)) for c in text)
    print("Encoded ASCII string:", ascii_string)
else:
    print("Invalid action. Please enter 'd' or 'e'.")
