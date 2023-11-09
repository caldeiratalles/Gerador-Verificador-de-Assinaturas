# Gerador-Verificador-de-Assinaturas
Talles Marcelo 20/0060295
Para usar a interface interativa que discutimos, siga esta sequência de inputs:
# ATENÇÃO: TAMANHO MÁXIMA DE INFORMAÇÃO ATÉ 100 CARACTERES CONTANDO OS ESPAÇOS
# Cálculo Aproximado do Tamanho Máximo da Mensagem
Para texto ASCII (onde cada caractere é representado por 1 byte), o tamanho máximo seria um pouco menos de 128 caracteres para uma chave de 1024 bits.
Para UTF-8, o tamanho máximo pode ser significativamente menor, pois caracteres especiais ou acentuados podem usar mais de um byte cada.
# Recomendação Prática
Para uma chave de 1024 bits, um tamanho seguro para a mensagem seria cerca de 100 caracteres ASCII ou menos para garantir que a conversão em número não exceda o tamanho do módulo n.
Se a mensagem contiver caracteres acentuados ou especiais, o número seguro de caracteres deve ser reduzido ainda mais.
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
   - Forneça a assinatura que você recebeu ao assinar o arquivo na etapa 3.

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
   - Assinatura para verificação: (Use a assinatura que você obteve na etapa 3)

5. **Sair**:
   - Opção: `5`
