
import random #utilizado para geração de numeros randômicos

cartorio = {}
def encryption(e, m, n):
    return (m ** e) % n

def decryption(d, m, n):
    return (m ** d) % n

def text_to_blocks():
    pass

def blocks_to_text():
    pass

def encrypt_blocks():
    pass

def decrypt_blocks():
    pass

def random_number(bits):
    n = random.randint(0, pow(2, bits))
    if n % 2 == 0:
        n = n + 1
    while not is_prime(n):
        n += 2
    if n == 1:
        n=n+1
    return (n)

def is_prime(a):
    return all(a % i for i in range(2, a))

def public_key(bits):
    p = random_number(bits)
    q = random_number(bits)
    while p == q:
        q = random_number(bits)
    n = p*q
    return (n, p, q)
    

def private_key():
    pass

if __name__ == "__main__":
    bits = 4 # número de bits da chave
    n, p, q = public_key(bits) #gera a chave pública
    

