# Geração das chaves RSA
from parte1.keyGenerator import generate_rsa_keys
from parte2.assinRSA import sign_message, verify_file_signature
from parte3.chiper import rsa_encrypt_file, rsa_decrypt_file, read_file_as_bytes


def main():
    global signature
    print("Sistema de Criptografia RSA")

    # Geração das chaves RSA
    public_key, private_key = generate_rsa_keys(1024)
    print("Chaves RSA geradas com sucesso.")

    while True:
        print("\nOpções:")
        print("1. Cifrar um arquivo")
        print("2. Decifrar um arquivo")
        print("3. Assinar um arquivo")
        print("4. Verificar assinatura de um arquivo")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            input_file_path = input("Caminho do arquivo a ser cifrado: ")
            output_file_path = input("Caminho do arquivo cifrado: ")
            rsa_encrypt_file(public_key, input_file_path, output_file_path)
            print("Arquivo cifrado com sucesso.")

        elif escolha == '2':
            input_file_path = input("Caminho do arquivo cifrado: ")
            output_file_path = input("Caminho para salvar o arquivo decifrado: ")
            rsa_decrypt_file(private_key, input_file_path, output_file_path)
            print("Arquivo decifrado com sucesso.")
            with open(output_file_path, 'r', encoding='utf-8') as file:
                decrypted_content = file.read()
            print("Conteúdo Decifrado:", decrypted_content)

        elif escolha == '3':
            input_file_path = input("Caminho do arquivo a ser assinado: ")
            signature = sign_message(private_key, read_file_as_bytes(input_file_path))
            print("Assinatura:", signature)

        elif escolha == '4':
            input_file_path = input("Caminho do arquivo original: ")
            is_signature_valid = verify_file_signature(public_key, input_file_path, signature)
            print("Verificação da Assinatura:", is_signature_valid)

        elif escolha == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


