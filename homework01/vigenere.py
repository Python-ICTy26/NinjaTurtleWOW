def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        symbol = plaintext[i]
        if symbol.isalpha():
            if symbol.isupper():
                shift = ord(keyword[i % len(keyword)]) - ord("A")
                code_of_symbol = ord(symbol) - ord("A")
                ciphertext += chr((code_of_symbol + shift) % 26 + ord("A"))
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
                code_of_symbol = ord(symbol) - ord("a")
                ciphertext += chr((code_of_symbol + shift) % 26 + ord("a"))
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        symbol = ciphertext[i]
        if symbol.isalpha():
            if symbol.isupper():
                shift = ord(keyword[i % len(keyword)]) - ord("A")
                code_of_symbol = 25 - ord(symbol) + ord("A")
                plaintext += chr(25 - (code_of_symbol + shift) % 26 + ord("A"))
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
                code_of_symbol = 25 - ord(symbol) + ord("a")
                plaintext += chr(25 - (code_of_symbol + shift) % 26 + ord("a"))
        else:
            plaintext += symbol
    return plaintext
