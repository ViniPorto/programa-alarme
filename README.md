# programa alarme
este é meu repositório git xD

Programa para aviso de coletas
@autor Vinícius Leinate Porto, estudante de Engenharia da Computação, UNOESC - Universidade do Oeste de Santa Catarina.
Com o intuito de melhorar a comunicação interna e diminuir os gastos com chamadas telefônicas no laboratório CEPAC,
o programa_alarme foi criado para fazer parte dos 2 arquivos que compõem o programa para aviso de coletas.
Este módulo é instalado na máquina que recebe o aviso, sendo assim, deve-se fazer os devidos ajustes para a correta
implementação e funcionamento. Primeiramente deve-se criar uma pasta compartilhada na rede, para que as duas máquinas
do processo façam acesso simultaneamente. Feito a criação da pasta compartilhada, deve-se criar 2 arquivos nesta pasta:
aviso.txt e ligado.txt, não importando o conteúdo dos mesmos. Nesta mesma pasta, deve ser acrescentado um arquivo .mp3
para funcionar de toque na chamada de aviso. Acrescentado os arquivos à pasta, agora deve-se copiar o path dos arquivos
e colar neste código nas linhas 44 (toque), 47 (aviso.txt) e 53 (aviso.txt). O aviso pode ser alterado mudando o que
está entre aspas na linha 37 (aviso) e 40 (nome da janela). Feita as alterações, com o uso da biblioteca pyinstaller,
deve-se rodar no terminarl o comando 'pyinstaller --noconsole yourprogram.py'. O arquivo .exe aparecerá na pasta dist
do windows pronto para rodar, recomenda-se colocar na pasta de inicialização para que sempre inicie com o computador.
Funcionamento:
O programa funciona em loop infinito, começando verificando se existe um arquivo 'aviso.txt' no path informado, este
arquivo serve como uma flag: sua existência na pasta indica que na outra máquina foi clicado na tela do programa (ao
clicar em 'avisar' é criado um arquivo 'aviso.txt'), informando que há coletas para fazer. Ao detectar a presença
deste arquivo no path, abre-se a uma GUI com um botão. Ao clicar no botão de 'ciente', o arquivo 'aviso.txt' é excluido
da pasta, a GUI fecha, a música para e o programa fica em loop aguardando a pasta 'aviso.txt' aparecer no path
novamente para dar o aviso. Ou seja, se não há uma pasta 'aviso.txt' no path informado o programa não faz nada.

Com o intuito de melhorar a comunicação interna e diminuir os gastos com chamadas telefônicas no laboratório CEPAC,
o programa_alarme2 foi criado para fazer parte dos 2 arquivos que compõem o programa para aviso de coletas.
Este módulo é instalado na máquina que faz o aviso, sendo assim, deve-se fazer os devidos ajustes para a correta
implementação e funcionamento. Primeiramente deve-se criar uma pasta compartilhada na rede, para que as duas máquinas
do processo façam acesso simultaneamente. Feito a criação da pasta compartilhada, deve-se criar 2 arquivos nesta pasta:
aviso.txt e ligado.txt, não importando o conteúdo dos mesmos. Nesta mesma pasta, deve ser acrescentado um arquivo .mp3
para funcionar de toque na chamada de aviso. Acrescentado os arquivos à pasta, agora deve-se copiar o path dos arquivos
e colar neste código nas linhas 46 (aviso.txt), 53 (aviso.txt) e 57 (ligado.txt). O aviso pode ser alterado mudando o
que está entre aspas na linha 35 (avisar) e 38 (nome da janela). Feita as alterações, usando aa biblioteca pyinstaller,
deve-se rodar no terminarl o comando 'pyinstaller --noconsole yourprogram.py'. O arquivo .exe aparecerá na pasta dist
do windows pronto para rodar, recomenda-se colocar na pasta de inicialização para que sempre inicie com o computador.
Funcionamento:
O programa funciona em loop infinito, começando verificando se existe um arquivo 'aviso.txt' no path informado, este
arquivo serve como uma flag: sua existência na pasta indica que na máquina foi clicado na tela do programa (ao
clicar em 'avisar' é criado um arquivo 'aviso.txt'), informando que há coletas para fazer. Se o programa detectar o
arquivo 'aviso.txt' no path não faz nada. Caso não encontre é sinal que ou o path informado está inacessível (computador
desligado) ou foi clicado no botão de 'ciente' na outra máquina e o arquivo 'aviso.txt' foi excluido. Para isso serve
o arquivo 'ligado.txt', porque ele fica sempre no path independente de o 'aviso.txt' se excluido ou não. Então após
não detectar a presença do 'aviso.txt' o programa verifica se detecta o 'ligado.txt' no path. Se detectar significa
que o outro computador está ligado e a pasta 'aviso.txt' foi excluida, assim, abre-se novamente a tela para fazer um
novo aviso, podendo ser usada novamente para posteriormente avisar de novas coletas. Caso não encontre significa que o
outro computador está desligado, neste caso o programa não faz nada e fica em fechado em loop até detectar esta pasta.
