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
    for j in range(len(plaintext)):
        i = plaintext[j]
        if i.isalpha():
            if i.isupper():
                ciphertext += chr((ord(i) + ord(keyword[j % len(keyword)]) - 130) % 26 + 65)
            else:
                ciphertext += chr((ord(i) + ord(keyword[j % len(keyword)]) - 194) % 26 + 97)
        else:
            ciphertext += i
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
    for j in range(len(ciphertext)):
        i = ciphertext[j]
        if i.isalpha():
            if i.isupper():
                plaintext += chr((ord(i) - ord(keyword[j % len(keyword)])) % 26 + 65)
            else:
                plaintext += chr((ord(i) - ord(keyword[j % len(keyword)])) % 26 + 97)
        else:
            plaintext += i
    return plaintext
