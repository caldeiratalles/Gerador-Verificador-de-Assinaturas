import hashlib
import base64

from parte3.chiper import read_file_as_bytes


# Função para calcular o hash SHA-3 de uma mensagem
def calculate_sha3_hash(message):
    sha3_hash = hashlib.sha3_256()
    # Verifica se a mensagem é uma string e codifica para bytes se necessário
    if isinstance(message, str):
        message = message.encode('utf-8')
    sha3_hash.update(message)
    return sha3_hash.digest()


# Função para assinar uma mensagem
def sign_message(private_key, message):
    _hash = calculate_sha3_hash(message)
    d, n = private_key
    signature = pow(int.from_bytes(_hash, byteorder='big'), d, n)
    return base64.b64encode(signature.to_bytes(
        (signature.bit_length() + 7) // 8, byteorder='big')
    ).decode()


def verify_file_signature(public_key, input_file_path, signature):
    message = read_file_as_bytes(input_file_path)
    return verify_signature(public_key, message, signature)


# Função para verificar uma assinatura
def verify_signature(public_key, message, signature):
    e, n = public_key
    signature = int.from_bytes(base64.b64decode(signature), byteorder='big')
    decrypted_hash = pow(signature, e, n)
    original_hash = calculate_sha3_hash(message)
    return original_hash == decrypted_hash.to_bytes(
        (decrypted_hash.bit_length() + 7) // 8, byteorder='big'
    )
