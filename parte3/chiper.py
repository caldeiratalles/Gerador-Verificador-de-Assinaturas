from OAEP.oaep import oaep_pad, oaep_unpad


def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


def write_bytes_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)


def rsa_encrypt_file(public_key, input_file_path, output_file_path):
    message = read_file_as_bytes(input_file_path)
    encrypted_message = rsa_encrypt_with_oaep(public_key, message)
    write_bytes_to_file(output_file_path, encrypted_message)


def rsa_decrypt_file(private_key, input_file_path, output_file_path):
    ciphertext = read_file_as_bytes(input_file_path)
    decrypted_message = rsa_decrypt_with_oaep(private_key, ciphertext)
    write_bytes_to_file(output_file_path, decrypted_message)


# Função para cifrar uma mensagem com RSA
# def rsa_encrypt(public_key, message):
#     e, n = public_key
#     message_as_int = int.from_bytes(message, byteorder='big')
#     ciphertext = pow(message_as_int, e, n)
#     return ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')


# Função para cifrar com OAEP
#Big-endian (byteorder='big'):
# Os bytes mais significativos são armazenados em endereços de memória menores.
# Por exemplo, o número 0x1234 seria armazenado como 12 34 em big-endian.
def rsa_encrypt_with_oaep(public_key, message):
    e, n = public_key
    padded_message = oaep_pad(message, len(bin(n)) - 2)
    message_as_int = int.from_bytes(padded_message, byteorder='big')
    ciphertext = pow(message_as_int, e, n)
    return ciphertext.to_bytes(
        (ciphertext.bit_length() + 7) // 8, byteorder='big'
    )


# Função para decifrar com OAEP
def rsa_decrypt_with_oaep(private_key, ciphertext):
    d, n = private_key
    ciphertext_as_int = int.from_bytes(ciphertext, byteorder='big')
    decrypted_int = pow(ciphertext_as_int, d, n)
    decrypted_message = decrypted_int.to_bytes(
        (decrypted_int.bit_length() + 7) // 8, byteorder='big'
    )
    unpadded_message = oaep_unpad(decrypted_message, len(bin(n)) - 2)
    return unpadded_message

# # Função para decifrar uma mensagem com RSA
# def rsa_decrypt(private_key, ciphertext):
#     d, n = private_key
#     ciphertext_as_int = int.from_bytes(ciphertext, byteorder='big')
#     decrypted_int = pow(ciphertext_as_int, d, n)
#     return decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
