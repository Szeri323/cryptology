from alphabet import alphabet
from fields import is_number_reversable
import math



def encription(alphabet, Z, K, plain_text):
    cipher_text = ""
    for letter in plain_text:
        pt_index = alphabet.index(letter)
        ct_index = (K[0] * pt_index + K[1]) % Z 
        cipher_text += alphabet[ct_index]
    return cipher_text

def multiplicative_inverse(number):
    
    return True

def eea(K):
    print(K[0])
    print(math.pow(K[0], -1))
    return math.pow(K[0], -1) % 26

def decription(alphabet, Z, K, cipher_text):
    plain_text = ""
    K_prime = eea(K)
    print(f"k': {K_prime}")
    for letter in cipher_text:
        ct_index = alphabet.index(letter)
        pt_index = (K[0] * ct_index + K[1]) % Z 
        plain_text += alphabet[pt_index]
    return plain_text

def main():
    Z = len(alphabet)
    a = int(input())
    b = int(input())
    check = is_number_reversable(a, Z)
    if check == False:
        print("a doesn't have multiplicative inverse")
        return
    K = [a, b]
    plain_text = "KRYPTOGRAFIA"
    cipher_text = encription(alphabet, Z, K, plain_text)
    print(cipher_text)
    plain_text2 = decription(alphabet, Z, K, cipher_text)
    print(plain_text2)
    
if __name__ == "__main__":
    main()