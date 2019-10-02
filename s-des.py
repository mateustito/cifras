def text_to_bin(plaintext): # converter String para Binario
    binario = ''
    for i in plaintext:
        binario += bin(ord(i))[2::] + ' '
    
    return binario

def bin_to_text(binario): # converter Binario para String
    binario = str(binario)
    caractere = ''
    string = ''
    tam = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tam:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''
        k += 1
    return string

def text_to_blocks(bintext):
    pass

def key_generation(key):
    pass

# mtb
def initial_permutation(block):
    pass

def inverse_permutation(block):
    pass

def expansion_permutation(block):
    pass

# apoio da função F (Feistel)
# block depois da expansao entra aqui
def exclusive_or(block, subkey): # XOR entre valores Binarios
    # cada 4 bits faz o xor com o 4 bits da chave da rodada
    result = int(block, 2) ^ int(subkey, 2)
    result = bin(result)
    return '{:0>4}'.format(result[2:])
    # depois daqui eh a parte da Substituição com as S-Boxes

def substitution(block):
    pass

def permutation(block):
    pass

# mtb
def function_k(block, key):
    pass

def switch_fuction(left_block, right_block):
    pass

def sdes_encryption(plaintext_block, key):
    pass

def sdes_decryption(ciphertext_block, key):
    pass
