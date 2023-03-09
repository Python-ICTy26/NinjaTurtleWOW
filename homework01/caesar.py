import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                code_i = ord(i) - ord("A")
                ciphertext += chr((code_i + shift) % 26 + ord("A"))
            else:
                code_i = ord(i) - ord("a")
                ciphertext += chr((code_i + shift) % 26 + ord("a"))
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if i.isupper():
                code_i = 25 - ord(i) + ord("A")
                plaintext += chr(25 - (code_i + shift) % 26 + ord("A"))
            else:
                code_i = 25 - ord(i) + ord("a")
                plaintext += chr(25 - (code_i + shift) % 26 + ord("a"))
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
