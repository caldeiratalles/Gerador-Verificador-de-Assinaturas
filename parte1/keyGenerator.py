import random


# Função Auxiliar: Teste de Primalidade (Teste de Miller-Rabin simplificado)
def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Escreva o número n-1 como 2 elevado a r * d
    # com d sendo ímpar, isso é feito subtraindo 1 de n e dividindo por 2 repetidamente.
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Teste de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


# Função para gerar um número primo grande
def generate_large_prime(keysize=2048):
    while True:
        prime_candidate = random.getrandbits(keysize)
        if is_prime(prime_candidate):
            return prime_candidate


# Geração das chaves RSA
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def xgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = xgcd(b % a, a)
        return g, x - (b // a) * y, y


# Função para encontrar o inverso multiplicativo
def modinv(a, m):
    g, x, _ = xgcd(a, m)
    if g != 1:
        raise Exception("Inverso multiplicativo não existe")
    return x % m


# Geração das chaves RSA
def generate_rsa_keys(keysize):
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Exponente público comum
    d = modinv(e, phi)  # Inverso multiplicativo de e modulo phi

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key
