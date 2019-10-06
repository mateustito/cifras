
# def text_to_bin(plaintext): # converter String para Binario
#     binario = ''
#     for i in plaintext:
#         binario += bin(ord(i))[2::] + ' '
    
#     return binario

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
  
def text_to_blocks(plaintext):
 	#retorna uma lista de bits formada por blocos de 8 bits
    return [bin(ord(x))[2:].zfill(8) for x in plaintext]

def bin_to_blocks(ciphertext):
    return [ciphertext[i:8+i] for i in range(0, len(ciphertext), 8)]

def key_generation(key):
    """
    Retorna as sub-chaves usadas nas rodadas do
    DES Simplificado
    :param key: bin()
                Chave de 10 bits
    :return subkeys: list()
                Lista com as sub-chaves
    """
    subkeys = list()
    key = key[2:].zfill(10)
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
    return split_list(output)

# IP-1 Reverse: 4 1 3 5 7 2 8 6
def inverse_permutation(block):
    iip = [4, 1, 3, 5, 7, 2, 8, 6]
    output = ''
    for index in iip:
        output += block[index - 1]
    return split_list(output)

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
        ep += block[index - 1]
    
    return ep

# apoio da função F (Feistel)
# block depois da expansao entra aqui
def exclusive_or(block, subkey): # XOR entre valores Binarios
    # cada 4 bits faz o xor com o 4 bits da chave da rodada
    result = int(block, 2) ^ int(subkey, 2)
    result = bin(result)
    return '{0}'.format(result[2:].zfill(8))
    # depois daqui eh a parte da Substituição com as S-Boxes

def exclusive_or2(block1, block2):
    result = int(block1, 2) ^ int(block2, 2)
    result = bin(result)
    return '{0}'.format(result[2:].zfill(4))

def split_list(a_list):
    half = ((len(a_list))//2)
    return a_list[:half], a_list[half:]

def substitution(block):
    sbox0 = [['1','0','3','2'],
       		['3','2','1','0'],
       		['0','2','1','3'],
       		['3','1','3','2']]

    sbox1 = [['0','1','2','3'],
       		['2','0','1','3'],
       		['3','0','1','0'],
       		['2','1','0','3']]
       		
    head, tail = split_list(block)
    #binario pra inteiro
    h_row = int(head[0] + head[3], 2)
    h_column = int(head[1] + head[2], 2)
    t_row = int(tail[0] + tail[3], 2)
    t_column = int(tail[1] + tail[2], 2)

    #sboxs
    h_value = sbox0[h_row][h_column]
    t_value = sbox1[t_row][t_column]

    #inteiro para binario
    str1 = "{0:b}".format(int(h_value))
    str2 = "{0:b}".format(int(t_value))

    if str1 == "1" or str1 == "0":
        str1 = "0" + str1

    if str2 == "1" or str2 == "0":
        str2 = "0" + str2

    final = str1 + str2
    return final

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
        p += block[index - 1]
    
    return p

# mtb
def function_k(block, key):
    new_block = exclusive_or2( block[0], permutation(substitution(exclusive_or(expansion_permutation(block[1]), key))))
    return new_block, block[1]

def switch_fuction(left_block, right_block):
    return right_block, left_block

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
    block_per = initial_permutation(plaintext_block)
    output = function_k(block_per, subkeys[0])
    output_switch = switch_fuction(output[0], output[1])
    output_aux = function_k(output_switch, subkeys[1])
    output = output_aux[0] + output_aux[1]
    ciphertext_block = inverse_permutation(output)

    return ciphertext_block[0] + ciphertext_block[1]



def sdes_decryption(ciphertext_block, key):
    '''
    Implementação da decriptação do DES-Simplificado
    '''
    subkeys = key_generation(key)
    block_per = initial_permutation(ciphertext_block)
    output = function_k(block_per, subkeys[1])
    output_switch = switch_fuction(output[0], output[1])
    output_aux = function_k(output_switch, subkeys[0])
    output = output_aux[0] + output_aux[1]
    plaintext_block = inverse_permutation(output)

    return plaintext_block[0] + plaintext_block[1]

if __name__ == "__main__":
    plaintext = "Olá, prof. André!"
    key = bin(5)
    print("Remetente-Plaintext: ", plaintext)
    print("Key: ", key)
    blocks = text_to_blocks(plaintext)
    print("Plaintext Blocks: ", blocks)
    ciphertext = ''
    for block in blocks:
        ciphertext += sdes_encryption(block, key)
    print(ciphertext)

    blocks = bin_to_blocks(ciphertext)
    print("Ciphertext Blocks: ", blocks)
    plaintext = ''
    for block in blocks:
        plaintext += bin_to_text(sdes_decryption(block, key))
    print("Destinatário-Plaintext: ", plaintext)
