def text_to_bin(plaintext):
    pass

def text_to_blocks(bintext):
    pass

def key_generation(key):
    """
    Retorna as sub-chaves usadas nas rodadas do
    DES Simplificado
    :param key: bin() ou str()
                Chave de 10 bits
    :return subkeys: list()
                Lista com as sub-chaves
    """
    subkeys = list()
    p10 = [3,5,2,7,4,10,1,9,8,6]
    p8 = [6,3,7,4,8,5,10,9]
    output_p10 = list()
    #P10
    for index in p10:
        output_p10.append(key[index-1])
    
    #Circular left shift
    left = output_p10[0:5]
    left_key = ""
    for i in range(5):
        left_key += left[(i+1)%5]

    right = output_p10[5:10]
    right_key = ""
    for i in range(5):
        right_key += right[(i+1)%5]

    output = left_key + right_key

    #P8
    subkey = ""
    for index in p8:
        subkey += output[index-1]
    subkeys.append(subkey) #k1
    
    #Circurlar left shift
    left = left_key
    left_key = ""
    for i in range(5):
        left_key += left[(i+2)%5]

    right = right_key
    right_key = ""
    for i in range(5):
        right_key += right[(i+2)%5]
    output = left_key + right_key

    #P8
    subkey = ""
    for index in p8:
        subkey += output[index-1]
    subkeys.append(subkey) #k2

    return subkeys

def initial_permutation(block):
    pass

def inverse_permutation(block):
    pass

def expansion_permutation(block):
    """
    Realiza uma expansão e ao mesmo tempo uma permutação
    no block de entrada

    :param block: bin()
                  Número binário de 4 bits
    
    :return ep: bin()
                Resultado de expansão e permutação no bloco de entrada
    """
    
    exp_per = [4, 1, 2, 3, 2, 3, 4, 1]
    ep = ''
    for index in exp_per:
        ep += block[index]
    
    return ep

def exclusive_or(block, subkey):
    pass

def substitution(block):
    pass

def permutation(block):
    """
    Realiza uma permutação nos bits de entrada

    :param block: bin()
                  Número binário de 4 bits

    :return p: bin()
               Número binário de 4 bits de entrada permutado
    """
    per = [2, 4, 3, 1]
    p = ''
    for index in per:
        p += block[index]
    
    return p

def function_k(block, key):
    pass

def switch_fuction(left_block, right_block):
    pass

def sdes_encryption(plaintext_block, key):
    """
    Implementa o algoritmo de encriptação do DES Simplificado

    :param plaintext_block: bin()
                            Bloco do plaintext de 8 bits
    :param key: bin()
                Número binário de 10 bits
    :return ciphertext_block: bin()
                              Bloco do plaintext de entrada criptografado.
    """
    subkeys = key_generation(key)
    b_per = initial_permutation(plaintext_block)
    saida = function_k(b_per, subkeys[0])
    s_switch = switch_fuction(saida[0], saida[1])
    saida = function_k(saida, subkeys[1])
    ciphertext_block = inverse_permutation(saida)

    return ciphertext_block



def sdes_decryption(ciphertext_block, key):
    pass

if __name__ == "__main__":
    print(key_generation('1010000010'))
