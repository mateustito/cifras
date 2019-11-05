# Implementação do algoritmo criptográfico RC4 - crifra de fluxo

# chave de 1 a 256 bytes
# período da cifra maior que 10^100
# geradores KSA e PRGA
# manipulação de um vetor S de 256 bytes, com permutações de 8 bits possíveis

def ksa(key):
    S = [x for x in range(256)]
    j = 0
    key = [ord(x) for x in key]
    for i in range(256):
        j = (j+S[i] + int(key[i % len(key)]))%256
        S[i],S[j] = S[j],S[i]
    
    return S

def prga(S, inputtext):
    i,j = 0,0
    outputtext = ''
    for char in inputtext:

        i = (i+1)%256
        j = (j+S[i]) %256
        S[i],S[j] = S[j],S[i]
        outputtext += chr(S[(S[i]+S[j])%256] ^ ord(char))
    
    return outputtext


plaintext = input('\nDigite o que deseja cifrar: ')
key = input('Key: ')
S = ksa(key)
ciphertext= prga(S, plaintext)
print("\nPlaintext: {0}\nKey: {1}\nCiphertext obtido: {2}\n".format(plaintext, key, ciphertext))



c = input("Deseja decifrar outro texto que não seja o 'Ciperhtext obtido'? S - Sim | <Outro>- Não \n")
if c == 'S':
    ciphertext = input('\nDigite o que deseja decifrar: ')
    key = input("Key: ")

S = ksa(key)
plaintext = prga(S, ciphertext)

print("\nCiphertext: {0}\nKey: {1}\nPlaintext obtido: {2}\n".format(ciphertext, key, plaintext))
