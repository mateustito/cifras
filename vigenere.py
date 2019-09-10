'''
--- Cifra de Vigenère ---

*Definição:
Usa-se uma tabela de alfabetos, sendo o alfabeto escrito 26 vezes em diferentes linhas,
cada um deslocado ciclicamente do anterior por uma posição.
Usa-se uma palavra-chave, e cada letra dela é a linha a ser usada da tabela, tanto pra cifrar ou decifrar.

*Ex.:
- texto claro (organizado): ATACARBASESUL
- palavra-chave: LIMAO (a chave é derivada dessa palavra, melhor dizendo, é uma concatenação dessa palavra)
- cifragem: L (key) = linha 12, A (texto claro) = coluna 1 --> saída letra L
- decifragem (inverso): L (key) = linha 12, L (texto cifrado) = coluna 1 --> saída A

.. Matematicamente:
Letras A-Z sendo inteiros (0 a 25)

Texto_Cifrado = Texto_Claro + Chave (mod 26)
Texto_Claro = Texto_Cifrado - Chave + 26 (mod 26)

'''

class Cifra(object):

    def desloca_alfabeto(self, alfabeto, desloca):

        return alfabeto[desloca:] + alfabeto[:desloca] # montagem da tabela do alfabeto com o deslocamento


class Vigenere(Cifra):

    def __init__(self):
        self.letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def testa_chave(self, chave, texto): # colocar o tamanho da chave no mesmo tamanho do texto
        j = 0
        key = ""
        for i in range(len(texto)):
            if texto[i] != ' ':
                key += chave[j]
                j = (j+1) % len(chave)
            else:
                key += ' '
        """
        if len(chave) < len(texto): # Ex.: ATACARBASESUL (13) > LIMAO (5) 
            nova_chave = chave * int((len(texto) / len(chave))) # int 13/5 = 2 --> LIMAO * 2 = LIMAOLIMAO (10)
            if len(nova_chave) < len(texto):
                nova_chave += chave[:(len(texto)-len(nova_chave))] # LIMAOLIMAO (10) + LIM (3) = LIMAOLIMAOLIM
            
            return nova_chave.upper()
        """
        return key.upper()
    
    def decifragem(self, key, cipher):
        """
        Decifra o criptograma usando a chave

        :param key: str representando a chave 
        :param cipher: str representando o criptograma

        :return plaintext: str com a mensagem descriptografada
        """

        alphabet = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8, 'J':9, 'K':10,'L':11,'M':12, 'N':13, 'O':14,'P':15, 'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
        _alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
        plaintext = ""
        for index in range(len(cipher)):
            if (key[index] == ' ') and (cipher[index] == ' '):
                plaintext += ' '
            else:
                key_index = alphabet[key[index]]
                cipher_index = alphabet[cipher[index]]
                new_index = (abs(26 - key_index) + cipher_index) % 26
                plaintext += _alphabet[new_index]
        return plaintext

if __name__ == "__main__":
    v = Vigenere()
    plaintext = "a seguranca de um sistema criptografico reside na chave"
    cipher = "I EIOGVIZGI PI CY WQEXMYE KDMXFSODENUGW DIAUHM ZE KTEDQ"
    keyword = "IME"
    key = v.testa_chave(keyword, plaintext)
    print("Plaintext: {0}\nKey: {1}\nCipher: {2}".format(plaintext, key, cipher))
    print(v.decifragem(key, cipher))