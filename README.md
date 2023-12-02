
# Gerador-Verificador-de-Assinaturas
Talles Marcelo 20/0060295
OBS: Olhar os comentários ao final do README
Para usar a interface interativa que discutimos, siga esta sequência de inputs:

# Cálculo Aproximado do Tamanho Máximo da Mensagem
Para texto ASCII (onde cada caractere é representado por 1 byte), o tamanho máximo ideal seria um pouco menos de 189 caracteres para uma chave de 2048 bits.
Tamanho Máximo da Mensagem = (Tamanho da chave RSA/8) - 2 x Tamanho do Hash - 2
Valor Máximo ideal(Valor máximo real 189): 180 caracteres com a proporção de caracteres especiais
Mensagem com o Máximo de caractere especial possível -> Mensagem especial: ão, é, ê, í, ó! Celebrando a vida, a arte e a alegria com paixão, cor e vibração. A cada passo, um novo êxtase.
Mensagem com espaço,virgula e ponto -> Esta jornada da vida nos leva por caminhos repletos de aprendizado, desafios e oportunidades. Cada experiencia nos molda e fortalece, abrindo caminhos para novos horizontes e descobertas r

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
### Comentários
Foi executado alguns testes(aleatórios) para tentar compreender quais seriam mais ou menos o valor aproximado de caracteres que devemos tirar para conseguir codificar/decodificar as mensagens sem problemas mesmo com acentos

Mensagem utilizada:
Fé e esperança são as lanternas eternas que iluminam o caminho de minha alma, guiando-me através das sombras da incerteza e da dúvida. Em cada passo dessa jornada, percebo que a fé não

Valor: 189

Valor calculado por causa dos caracteres: 191

Equivalência para calculo aproximado: 1 carateres especial -> Perdemos mais ou menos 2 caracteres de mensagem, para testes sem erro considere 1 para 3.

Foi analisado que para cada caractere "á é í ó ú â ê ô ã õ ç" o peso é 2

Valor Máximo ideal(Máximo real é 189): 180 caracteres com a proporção de caracteres especiais
