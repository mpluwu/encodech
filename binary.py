action = input("If you want to decode, enter 'd'. If you want to encode, enter 'e': ")

if action == 'd':
    binary_string = input("Enter the binary string to decode: ")
    decoded_string = ''.join([chr(int(b, 2)) for b in binary_string.split()])
    print("Decoded string:", decoded_string)
elif action == 'e':
    text = input("Enter the text to encode: ")
    binary_string = ' '.join(format(ord(c), '08b') for c in text)
    print("Encoded binary string:", binary_string)
else:
    print("Invalid action. Please enter 'd' or 'e'.")