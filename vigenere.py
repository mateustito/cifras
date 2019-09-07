'''
--- Cifra de Vigenère ---

*Definição:
Usa-se uma tabela de alfabetos, sendo o alfabeto escrito 26 vezes em diferentes linhas,
cada um deslocado ciclicamente do anterior por uma posição.
Usa-se uma palavra-chave, e cada letra dela é a linha a ser usada da tabela, tanto pra cifrar ou decifrar.

*Ex.:
- texto claro (organizado): ATACARBASESUL
- chave utilizada: LIMAOLIMAOLIM (do mesmo tamanho do texto claro)
- cifragem: L (key) = linha 12, A (texto claro) = coluna 1 --> saída letra L
- decifragem (inverso): L (key) = linha 12, L (texto cifrado) = coluna 1 --> saída A

.. Matematicamente:
Letras A-Z sendo inteiros (0 a 25)

Texto_Cifrado = Texto_Claro + Chave (mod 26)
Texto_Claro = Texto_Cifrado - Chave + 26 (mod 26)

'''

class Cifra(object):

    texto = input('\nMensagem: ')
    chave = input('\nChave: ')

    def format_str(self, texto):

        return texto.replace(' ', '').upper() # junta tudo e bota caixa alta

    def desloca_alfabeto(self, alfabeto, desloca):

        return alfabeto[desloca:] + alfabeto[:desloca] # montagem da tabela do alfabeto com o deslocamento


class Vigenere(Cifra):

    def __init__(self):
        self.letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def testa_chave(self, chave, texto): # colocar o tamanho da chave no mesmo tamanho do texto

        if len(chave) < len(texto): # Ex.: ATACARBASESUL (13) > LIMAO (5) 
            nova_chave = chave * int((len(texto) / len(chave))) # int 13/5 = 2 --> LIMAO * 2 = LIMAOLIMAO (10)
            if len(nova_chave) < len(texto):
                nova_chave += chave[:(len(texto)-len(nova_chave))] # LIMAOLIMAO (10) + LIM (3) = LIMAOLIMAOLIM
            
            return nova_chave.upper()
        
        return chave.upper()
