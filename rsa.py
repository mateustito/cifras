import random #utilizado para geração de numeros randômicos

## Chave Publica
n = 0
e = 65537 #Para o sistema ficar protegido de alguns tipos de ataque sugere-se este valor = 2^16+1

def encryption(e, m, n):
    return (m ** e) % n

def decryption(d, m, n):
    return (m ** d) % n

def text_to_blocks():
    pass

def blocks_to_text():
    pass

def encrypt_blocks():
    pass

def decrypt_blocks():
    pass

def random_number():
    n = random.randint(0, pow(10, 100))
    if n % 2 == 0:
        n = n + 1
    while not is_probable_prime(n):
        n += 2
    if n == 1:
        n = n + 1
    return (n)

def inv_mult(a, p):
    x = 1
    for x in range(1, p+1):
        if ((a*x)%p) == 1:
            return x

def keys():
    p = random_number()
    q = random_number()
    while p == q:
        q = random_number() 
    n = p*q
    d = inv_mult(e, ((p-1) * (q-1)))
    return (d, n)

def is_probable_prime(n,k=40):
	#Teste de primalidade Miller-Rabin 
	# k = 40 numero recomendado de rounds de teste
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    d , n = keys()
    m = "Hello, world!"
    
    c = encryption(e, m, n) 
    p = decryption(d, c, n)
    answer = input("Deseja gerar os valores de (e,d,n) automaticamente? S- Sim <Outro>- Não")
    if answer != 'S':
        e = int(input("Digite o valor para e"))
        d = int(input("Digite o valor de d:"))
        n = int(input("Digite o valor de n:"))
    m = input("Digite a mensagem a ser encriptada: ")
    c = encryption(e, m, n) 
    print("Texto claro: {0}\nChave Pública: ({1}, {2})\nTexto cifrado obtido: {5}\n".format(m,e,n,c))
    answer = input("Deseja obter o texto claro a partir do texto cifrado obtido? S- Sim <Outro>- Não")
    if answer != 'S':
        c = input("Digite o texto cifrado desejado:")
    print("Texto cifrado: {0}\nChave Privada: ({3}, {4})\nTexto claro obtido: {5}\n".format(c,d,n,m))
    

