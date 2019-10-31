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

def prga(S, plaintext):
    i,j = 0,0
    ciphertext = []
    for char in plaintext:

        i = (i+1)%256
        j = (j+S[i]) %256
        S[i],S[j] = S[j],S[i]

        aux = format(ord(chr(S[(S[i]+S[j])%256] ^ ord(char))),'x')
        ciphertext.append(aux)
    
    return ciphertext


key = "candre"

S = ksa(key)
ciphertext = prga(S, input('\nDigite o que deseja cifrar: '))

print("\nTexto cifrado: " )

for x in ciphertext:
    print(x, end = ' ')

print("\n")