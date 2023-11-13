
# Gerador-Verificador-de-Assinaturas
Talles Marcelo 20/0060295
Para usar a interface interativa que discutimos, siga esta sequência de inputs:

# Cálculo Aproximado do Tamanho Máximo da Mensagem
Para texto ASCII (onde cada caractere é representado por 1 byte), o tamanho máximo seria um pouco menos de 62 caracteres para uma chave de 1024 bits.
Tamanho Máximo da Mensagem = (Tamanho da chave RSA/8) - 2 x Tamanho do Hash - 2
Por exemplo, para uma chave RSA de 1024 bits (128 bytes) e usando SHA-256 para o OAEP (que tem um tamanho de hash de 32 bytes), o tamanho máximo da mensagem seria:
128−2×32−2=62 bytes


Indicação(Apenas dica): Para não ter confusão entre arquivos utilize;
teste.txt como arquivo original
c.txt arquivo cifrado
d.txt arquivo decifrado
1. **Cifrar um Arquivo**:
   - Escolha a opção `1`.
   - Forneça o caminho do arquivo que você deseja cifrar (por exemplo, `"caminho/para/seu/arquivo.txt"`).
   - Forneça o caminho onde o arquivo cifrado será salvo (por exemplo, `"caminho/para/arquivo_cifrado.txt"`).

2. **Decifrar um Arquivo**:
   - Escolha a opção `2`.
   - Forneça o caminho do arquivo cifrado (que você cifrou na etapa anterior).
   - Forneça o caminho onde o arquivo decifrado será salvo.

3. **Assinar um Arquivo**:
   - Escolha a opção `3`.
   - Forneça o caminho do arquivo que você deseja assinar (pode ser o arquivo original ou qualquer outro arquivo).

4. **Verificar a Assinatura de um Arquivo**:
   - Escolha a opção `4`.
   - Forneça o caminho do arquivo original que foi assinado.
   - Pode validar que na main nós criamos uma variavel global para não ocorrer problemas de copia e cola

5. **Sair do Programa**:
   - Escolha a opção `5` para sair do programa.

### Exemplo de Sequência de Uso

Suponha que você queira cifrar, decifrar, assinar e verificar a assinatura de um arquivo chamado `"meu_documento.txt"`. Aqui está um exemplo de como você poderia proceder:

1. **Cifrar**:
   - Opção: `1`
   - Caminho do arquivo a ser cifrado: `"meu_documento.txt"`
   - Caminho do arquivo cifrado: `"meu_documento_cifrado.txt"`

2. **Decifrar**:
   - Opção: `2`
   - Caminho do arquivo cifrado: `"meu_documento_cifrado.txt"`
   - Caminho para salvar o arquivo decifrado: `"meu_documento_decifrado.txt"`

3. **Assinar**:
   - Opção: `3`
   - Caminho do arquivo a ser assinado: `"meu_documento.txt"`
   - (Você receberá uma assinatura como output)

4. **Verificar Assinatura**:
   - Opção: `4`
   - Caminho do arquivo original: `"meu_documento.txt"`

5. **Sair**:
   - Opção: `5`
