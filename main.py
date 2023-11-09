# # Geração das chaves RSA
# from parte1.keyGenerator import generate_rsa_keys
# from parte2.assinRSA import sign_message, verify_file_signature
# from parte3.chiper import rsa_encrypt_file, rsa_decrypt_file, read_file_as_bytes
#
# # Geração das chaves RSA
# public_key, private_key = generate_rsa_keys(1024)
#
# # Caminho para o arquivo a ser cifrado e assinado
# input_file_path = 'teste.txt'
#
# # Cifra o conteúdo do arquivo
# encrypted_file_path = 'c.txt'
# rsa_encrypt_file(public_key, input_file_path, encrypted_file_path)
#
# # Decifra o conteúdo do arquivo cifrado
# decrypted_file_path = 'd.txt'
# rsa_decrypt_file(private_key, encrypted_file_path, decrypted_file_path)
#
# with open(decrypted_file_path, 'r', encoding='utf-8') as file:
#     decrypted_content = file.read()
# print("Conteúdo Decifrado:", decrypted_content)
#
#
# # Assina o conteúdo do arquivo original
# signature = sign_message(private_key, read_file_as_bytes(input_file_path))
# print("Assinatura:", signature)
#
# # Verifica a assinatura do arquivo
# is_signature_valid = verify_file_signature(public_key, input_file_path, signature)
# print("Verificação da Assinatura:", is_signature_valid)

import hashlib
import base64
import random
import re  # Importe diretamente a biblioteca re

import unicodedata


# Função Auxiliar: Teste de Primalidade (Teste de Miller-Rabin simplificado)
def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Escreva o número n-1 como 2^r * d
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
def generate_large_prime(keysize=1024):
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
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('Inverso multiplicativo não existe')
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


# Função para calcular o hash SHA-3 de uma mensagem
def calculate_sha3_hash(message):
    sha3_hash = hashlib.sha3_256()
    sha3_hash.update(message.encode('utf-8'))
    return sha3_hash.digest()


# Função para assinar uma mensagem
def sign_message(private_key, message):
    hash = calculate_sha3_hash(message)
    # Cifrar o hash usando a chave privada RSA
    d, n = private_key
    # RSA Encryption/Decryption é normalmente pow(message, key_part, n)
    signature = pow(int.from_bytes(hash, byteorder='big'), d, n)
    # Converta o resultado para BASE64 e retorne
    return base64.b64encode(signature.to_bytes((signature.bit_length() + 7) // 8, byteorder='big')).decode()


# Função para verificar uma assinatura
def verify_signature(public_key, message, signature):
    # Decifre a assinatura usando a chave pública
    e, n = public_key
    signature = int.from_bytes(base64.b64decode(signature), byteorder='big')
    decrypted_hash = pow(signature, e, n)
    # Calcule o hash da mensagem original
    original_hash = calculate_sha3_hash(message)
    # Compare os dois hashes e retorne True se forem iguais, caso contrário, False
    return original_hash == decrypted_hash.to_bytes((decrypted_hash.bit_length() + 7) // 8, byteorder='big')


def rsa_encrypt(public_key, message):
    e, n = public_key
    # Converte a mensagem em um número (codificação para bytes e depois para um inteiro)
    message_as_int = int.from_bytes(message.encode('utf-8'), byteorder='big')
    # Cifra o número usando a chave pública (exponenciação modular)
    ciphertext = pow(message_as_int, e, n)
    # Converte o texto cifrado de volta para bytes
    return ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')


def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    # Converte o texto cifrado para um número
    ciphertext_as_int = int.from_bytes(ciphertext, byteorder='big')
    # Decifra o número usando a chave privada (exponenciação modular)
    decrypted_int = pow(ciphertext_as_int, d, n)
    # Converte o número de volta para texto (decodificação de bytes para string)
    return decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')


public_key, private_key = generate_rsa_keys(1024)

# Mensagem a ser cifrada e assinada
original_message = ("O SENHOR é o meu pastor, nada me faltará.Deitar-me faz em verdes pastos, guia-me mansamente a ")


# def remove_accents_and_spaces(text):
#     # Normaliza o texto para decompor os acentos
#     normalized_text = unicodedata.normalize('NFKD', text)
#     # Mantém apenas caracteres alfanuméricos (remove acentos e espaços)
#     only_alpha_numeric = ''.join([c for c in normalized_text if not unicodedata.combining(c)])
#     # Remove caracteres especiais e espaços
#     cleaned_text = re.sub(r'\W+', '', only_alpha_numeric)
#     return cleaned_text


# original_message = remove_accents_and_spaces(original_message)
print(original_message)
# Cifração da mensagem
encrypted_message = rsa_encrypt(public_key, original_message)
print("Mensagem Cifrada:", encrypted_message)

# Decifração da mensagem
decrypted_message = rsa_decrypt(private_key, encrypted_message)
print("Mensagem Decifrada:", decrypted_message)

# Assinatura da mensagem
signature = sign_message(private_key, original_message)
print("Assinatura:", signature)

# Verificação da assinatura
is_signature_valid = verify_signature(public_key, original_message, signature)
print("Verificação da Assinatura:", is_signature_valid)
