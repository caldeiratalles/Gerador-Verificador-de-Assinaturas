# Geração das chaves RSA
from parte1.keyGenerator import generate_rsa_keys
from parte2.assinRSA import sign_message, verify_file_signature
from parte3.chiper import rsa_encrypt_file, rsa_decrypt_file, read_file_as_bytes

# Geração das chaves RSA
public_key, private_key = generate_rsa_keys(1024)

# Caminho para o arquivo a ser cifrado e assinado
input_file_path = 'teste.txt'

# Cifra o conteúdo do arquivo
encrypted_file_path = 'c.txt'
rsa_encrypt_file(public_key, input_file_path, encrypted_file_path)

# Decifra o conteúdo do arquivo cifrado
decrypted_file_path = 'd.txt'
rsa_decrypt_file(private_key, encrypted_file_path, decrypted_file_path)

with open(decrypted_file_path, 'r', encoding='utf-8') as file:
    decrypted_content = file.read()
print("Conteúdo Decifrado:", decrypted_content)


# Assina o conteúdo do arquivo original
signature = sign_message(private_key, read_file_as_bytes(input_file_path))
print("Assinatura:", signature)

# Verifica a assinatura do arquivo
is_signature_valid = verify_file_signature(public_key, input_file_path, signature)
print("Verificação da Assinatura:", is_signature_valid)

