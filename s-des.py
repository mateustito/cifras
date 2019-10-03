
def text_to_bin(plaintext):
	#retorna uma lista de bits formada por blocos de 8 bits
    return [bin(ord(x))[2:].zfill(8) for x in plaintext]

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
    op_data  = (block << 3) & int('10000000', 2)  # 4
    op_data |= (block >> 1) & int('01000000', 2)  # 1
    op_data |= (block )     & int('00100000', 2)  # 3
    op_data |= (block << 1) & int('00010000', 2)  # 5
    op_data |= (block << 2) & int('00001000', 2)  # 7
    op_data |= (block >> 4) & int('00000100', 2)  # 2
    op_data |= (block << 1) & int('00000010', 2)  # 8
    op_data |= (block >> 2) & int('00000001', 2)  # 6
    return op_data;

def expansion_permutation(block):
    pass

def exclusive_or(block, subkey):
    pass

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
    pass

def function_k(block, key):
    pass

def switch_fuction(left_block, right_block):
    block = right_block + left_block
    return block

def sdes_encryption(plaintext_block, key):
    pass

def sdes_decryption(ciphertext_block, key):
    pass

if __name__ == "__main__":
    print(key_generation('1010000010'))
