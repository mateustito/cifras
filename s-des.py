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

# permutação inicial para rodar o algoritmo
# IP: 2 6 3 1 4 8 5 7 (8 bits)
# 2 bit do block na posição 1 ... 6 bit block na posição 2 ...
def initial_permutation(block):
    key = [2, 6 ,3, 1, 4, 8, 5, 7]
    output = ""
    for i in key:
        output += block[i-1]
    return output

# IP-1 Reverse: 4 1 3 5 7 2 8 6
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
    '''new_block = permutation(substitution(exclusive_or(expansion_permutation(block), key)))
    return new_block'''
    pass

def switch_fuction(left_block, right_block):
    pass

def sdes_encryption(plaintext_block, key):
    pass

def sdes_decryption(ciphertext_block, key):
    '''
    Implementação da decriptação do DES-Simplificado
    '''
    subkeys = key_generation(key) # gera as mesmas chaves da Encryption
    b_per = initial_permutation(ciphertext_block) # IP
    saida = function_k(b_per, subkeys[1]) # vai usar a chave 2
    s_switch = switch_fuction(saida[0], saida[1]) # troca ordem dos blocos
    saida = function_k(s_switch, subkeys[0])
    plaintext_block = inverse_permutation(saida) # IP^-1
    
    return plaintext_block
