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

def modinv(b, n):
    # Inverso de um número na Aritmetica Modular
    g, x, _ = euclides_ext(b, n)
    if g == 1:
        return x % n

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
def decryption(d, m, n):
    return (m ** d) % n

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
    pass

def public_key():
    pass

def private_key():
    pass

if __name__ == "__main__":
    plain_text = "mateus tito eh orientando do professor candre batista de carvalho"
    
    blocks = text_to_blocks(plain_text, DEFAULT_BLOCK_SIZE)
    
    print(text_to_blocks(plain_text, DEFAULT_BLOCK_SIZE))
    print(blocks_to_text(blocks, len(plain_text), DEFAULT_BLOCK_SIZE))