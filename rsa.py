import random

cartorio = {}

e = 65537 # valor de "e" recomendado ao RSA
KEY_LENGTH = 1024 # tamanho da chave
DEFAULT_BLOCK_SIZE = 128 # tamanho do bloco em bytes

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

# Cifragem --> mensagem ^ e mod N
# N = p * q (p e q são dois números primos)
# Chave pública = (e, N)
def encryption(plaintext, e, N, blockSize = DEFAULT_BLOCK_SIZE):
    # converter a mensagem em blocos
    encryptedBlocks = []

    # aplica block^e mod N em todos os blocos
    for block in text_to_blocks(plaintext, blockSize):
        encryptedBlocks.append(pow(block,e,N))

    return encryptedBlocks

# Decifragem --> mensagem ^ d mod N
# phi(N) = (p-1) * (q-1)
# e * d = 1 * (mod phi(N)) --> inverso multiplicativo
# Chave privada = (N, d)
#def decryption(d, m, n):
    #return (m ** d) % n

# usado na criptografia, onde cada bloco sera aplicado a encript
def text_to_blocks(plaintext, blockSize = DEFAULT_BLOCK_SIZE):
    messageBytes = plaintext.encode('ascii')
    
    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range (blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i]*(256 ** (i % blockSize))
        blockInts.append(blockInt)
    
    return blockInts

# usado na Descriptografia
def blocks_to_text(blocks, msgLenght, blockSize = DEFAULT_BLOCK_SIZE):
    message = []
    for block in blocks:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < msgLenght:
                # reverter de Ascii
                asciiNumber = block // (256 ** i)
                block = block % (256 ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
        
    return ''.join(message)

def encrypt_blocks():
    pass

def decrypt_blocks():
    pass

def random_number():
    n = random.randint(0, pow(10, 100))
    if n % 2 == 0:
        n = n + 1
    while not is_probable_prime(n):
        n += 2
    if n == 1:
        n = n + 1
    
    return (n)

def inv_mult(a, p):
    x = 1
    for x in range(1, p+1):
        if ((a*x)%p) == 1:
            return x

def keys():
    p = random_number()
    q = random_number()
    while p == q:
        q = random_number() 
    n = p*q
    d = inv_mult(e, ((p-1) * (q-1)))
    return (d, n)

def is_probable_prime(n,k=40):
	#Teste de primalidade Miller-Rabin 
	# k = 40 numero recomendado de rounds de teste
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    d , n = keys()
    answer = input("Deseja gerar os valores de (e,d,n) automaticamente? S- Sim <Outro>- Não")
    if answer != 'S':
        e = int(input("Digite o valor para e"))
        d = int(input("Digite o valor de d:"))
        n = int(input("Digite o valor de n:"))
    m = input("Digite a mensagem a ser encriptada: ")
    c = encryption(e, m, n) 
    print("Texto claro: {0}\nChave Pública: ({1}, {2})\nTexto cifrado obtido: {5}\n".format(m,e,n,c))
    answer = input("Deseja obter o texto claro a partir do texto cifrado obtido? S- Sim <Outro>- Não")
    if answer != 'S':
        c = input("Digite o texto cifrado desejado:")
    print("Texto cifrado: {0}\nChave Privada: ({3}, {4})\nTexto claro obtido: {5}\n".format(c,d,n,m))
