cartorio = {}

e = 65537 # valor de "e" recomendado ao RSA
KEY_LENGTH = 1024 # tamanho da chave

def mdc(a, b):
    # Calcular o MDC entre dois números
    while b != 0:
        a, b = b, a % b
    return a

def euclides_ext(a, b):
    # Calcular Euclides Extendido entre dois números
    if a == 0:
        return (b, 0, 1)
    
    g, y, x = euclides_ext(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(b, n):
    # Inverso de um número na Aritmetica Modular
    g, x, _ = euclides_ext(b, n)
    if g == 1:
        return x % n

# Cifragem --> mensagem ^ e mod N
# N = p * q (p e q são dois números primos)
# Chave pública = (e, N)
def encryption(e, N, plain_text):
    # vai encriptando cada letra do plaintext
    cypher_text = [pow(ord(m), e, N) for m in plain_text]
    # retorna uma lista das letras encriptadas
    return cypher_text

# Decifragem --> mensagem ^ d mod N
# phi(N) = (p-1) * (q-1)
# e * d = 1 * (mod phi(N)) --> inverso multiplicativo
# Chave privada = (N, d)
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
    pass

def public_key():
    pass

def private_key():
    pass

if __name__ == "__main__":
    plain_text = "mateus tito eh orientando do professor candre batista de carvalho"
    
    n = 187 # soh pra teste, o N deve ser gerado
    
    print(encryption(e, n, plain_text))