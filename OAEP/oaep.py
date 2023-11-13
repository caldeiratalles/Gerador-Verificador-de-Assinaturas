import os
import hashlib


# Função de padding OAEP
def oaep_pad(message, keysize, hash_algo=hashlib.sha256):
    hash_len = hash_algo().digest_size
    k = keysize // 8
    m_len = len(message)

    # Verifica se a mensagem é muito longa
    if m_len > k - 2 * hash_len - 2:
        raise ValueError("Mensagem muito longa")

    # Gera um padding aleatório
    padding = os.urandom(hash_len)
    pad_len = k - m_len - 2 * hash_len - 2

    # Cria o padding de acordo com o OAEP
    padded_message = b'\x00' + padding + b'\x00' * (pad_len + 1) + message
    return padded_message


def oaep_unpad(padded_message, keysize):
    k = keysize // 8

    delimiter_index = padded_message.rfind(b'\x00')

    if delimiter_index == -1:
        raise ValueError("Decodificação falhou")

    padding_start = 1

    # # Verifica se o tamanho da mensagem é apropriado
    if len(padded_message[padding_start:delimiter_index]) > k:
        raise ValueError("Tamanho de mensagem inválido")

    # Retorna a mensagem original removendo o padding
    return padded_message[delimiter_index + 1:]
