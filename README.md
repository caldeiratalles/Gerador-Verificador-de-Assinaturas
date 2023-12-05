
# Gerador-Verificador-de-Assinaturas
Talles Marcelo 20/0060295
OBS: Olhar os comentários ao final do README
Para usar a interface interativa que discutimos, siga esta sequência de inputs:
### Para a assinatura
Para a analise da assinatura podemos usar qualquer tamanho de mensagem.

### Cálculo Aproximado do Tamanho Máximo da Mensagem
Para texto ASCII (onde cada caractere é representado por 1 byte), o tamanho máximo ideal seria um pouco menos de 189 caracteres para uma chave de 1048 bits.

Tamanho Máximo da Mensagem = (Tamanho da chave RSA/8) - 2 x Tamanho do Hash - 2

Valor Máximo ideal(Valor máximo real 189): 180 caracteres com a proporção de caracteres especiais

Mensagem com o Máximo de caractere especial possível -> Mensagem especial: ão, é, ê, í, ó! Celebrando a vida, a arte e a alegria com paixão, cor e vibração. A cada passo, um novo êxtase.

Mensagem com espaço,virgula e ponto -> Esta jornada da vida nos leva por caminhos repletos de aprendizado, desafios e oportunidades. Cada experiencia nos molda e fortalece, abrindo caminhos para novos horizontes e descobertas r

### Fluxo de Utilização
O sistema apresenta duas sequências principais de uso:

### Sequência de Uso para Assinatura de Arquivos
Para cifrar, assinar e verificar a assinatura de um arquivo, siga estes passos:

## Cifrar o Arquivo (Opção 3):

Caminho do Arquivo a ser Cifrado: Especifique o caminho do arquivo que deseja cifrar.
Caminho para Salvar o Arquivo Cifrado: Forneça o caminho onde o arquivo cifrado será salvo.
Observação: Esta opção é adequada para arquivos de qualquer tamanho.
## Assinar o Arquivo (Opção 4):

Caminho do Arquivo a ser Assinado: Indique o caminho do arquivo que você deseja assinar.
Uma assinatura digital será gerada e exibida.
## Verificar Assinatura (Opção 5):

Caminho do Arquivo Original: Forneça o caminho do arquivo original para verificar a assinatura.
O sistema verificará a validade da assinatura digital.
## Sair (Opção 6)

### Sequência de Uso para Manipulação de Mensagens
Para cifrar, decifrar, assinar e verificar a assinatura de um arquivo, proceda da seguinte forma:

## Cifrar o Arquivo (Opção 1):

Caminho do Arquivo a ser Cifrado: Indique o caminho do arquivo a ser cifrado.
Caminho para Salvar o Arquivo Cifrado: Especifique onde o arquivo cifrado será armazenado.
Observação: Use esta opção para arquivos com até 180 caracteres.
## Decifrar o Arquivo (Opção 2):

Caminho do Arquivo Cifrado: Forneça o caminho do arquivo cifrado.
Caminho para Salvar o Arquivo Decifrado: Indique onde deseja salvar o arquivo decifrado.
## Assinar o Arquivo (Opção 4):

Caminho do Arquivo a ser Assinado: Especifique o caminho do arquivo que será assinado.
Uma assinatura digital será gerada e exibida.
## Verificar Assinatura (Opção 5):

Caminho do Arquivo Original: Forneça o caminho do arquivo original para verificar a assinatura.
O sistema irá confirmar a validade da assinatura digital.
## Sair (Opção 6)

### Indicação(Apenas dica): Para não ter confusão entre arquivos utilize;

teste.txt como arquivo original

c.txt arquivo cifrado

d.txt arquivo decifrado


### Comentários
Foi executado alguns testes(aleatórios) para tentar compreender quais seriam mais ou menos o valor aproximado de caracteres que devemos tirar para conseguir codificar/decodificar as mensagens sem problemas mesmo com acentos

Mensagem utilizada:
Fé e esperança são as lanternas eternas que iluminam o caminho de minha alma, guiando-me através das sombras da incerteza e da dúvida. Em cada passo dessa jornada, percebo que a fé não

Valor: 189

Valor calculado por causa dos caracteres: 191

Equivalência para calculo aproximado: 1 carateres especial -> Perdemos mais ou menos 2 caracteres de mensagem, para testes sem erro considere 1 para 3.

Foi analisado que para cada caractere "á é í ó ú â ê ô ã õ ç" o peso é 2

Valor Máximo ideal(Máximo real é 189): 180 caracteres com a proporção de caracteres especiais
