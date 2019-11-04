import random #utilizado para geração de numeros randômicos

## Chave Publica
n = 0
e = 65537 #Para o sistema ficar protegido de alguns tipos de ataque sugere-se este valor = 2^16+1

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

def random_number():
    n = random.randint(0, pow(10, 100))
    if n % 2 == 0:
        n = n + 1
    while not is_prime(n):
        n += 2
    if n == 1:
        n = n + 1
    return (n)

def is_prime(a):
    return all(a % i for i in range(2, a))

def public_key():
    p = random_number()
    q = random_number()
    while p == q:
        q = random_number()
    _n = p*q
    return _n
    

def private_key():
    pass

if __name__ == "__main__":
    n = public_key() #gera a chave pública
    

