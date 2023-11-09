def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


def write_bytes_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)


def rsa_encrypt_file(public_key, input_file_path, output_file_path):
    message = read_file_as_bytes(input_file_path)
    encrypted_message = rsa_encrypt(public_key, message)
    write_bytes_to_file(output_file_path, encrypted_message)


def rsa_decrypt_file(private_key, input_file_path, output_file_path):
    ciphertext = read_file_as_bytes(input_file_path)
    decrypted_message = rsa_decrypt(private_key, ciphertext)
    write_bytes_to_file(output_file_path, decrypted_message)


# Função para cifrar uma mensagem com RSA
def rsa_encrypt(public_key, message):
    e, n = public_key
    message_as_int = int.from_bytes(message, byteorder='big')
    ciphertext = pow(message_as_int, e, n)
    return ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')


# Função para decifrar uma mensagem com RSA
def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    ciphertext_as_int = int.from_bytes(ciphertext, byteorder='big')
    decrypted_int = pow(ciphertext_as_int, d, n)
    return decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
