from alphabet import alphabet

def encription(alphabet, Z, K, plain_text):
    cipher_text = ""
    for letter in plain_text:
        pt_index = alphabet.index(letter)
        ct_index = (pt_index + K) % Z 
        cipher_text += alphabet[ct_index]
    return cipher_text
def decription(alphabet, Z, K, cipher_text):
    plain_text = ""
    for letter in cipher_text:
        ct_index = alphabet.index(letter)
        pt_index = (ct_index - K) % Z 
        plain_text += alphabet[pt_index]
    return plain_text


def main():
    Z = len(alphabet)
    K = 10
    plain_text = "LOVE"
    cipher_text = encription(alphabet, Z, K, plain_text)
    print(cipher_text)
    plain_text2 = decription(alphabet, Z, K, cipher_text)
    print(plain_text2)
    
if __name__ == "__main__":
    main()