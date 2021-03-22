"""
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
"""
import PySimpleGUI as sg
import os
from time import sleep
from pygame import mixer

sg.change_look_and_feel('LightGreen3')


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Button("Ciente", size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window("Aviso de coleta").layout(layout)

    def iniciar(self):
        mixer.init()
        mixer.music.load('kiratheme.mp3')  # Toque .mp3
        mixer.music.play()
        self.janela.Read()
        os.remove('Z:\\aviso.txt')  # Path para o arquivo aviso.txt
        self.janela.close()


while True:
    try:
        arquivo = open('Z:\\aviso.txt', 'r', encoding='UTF-8')  # Path para o arquivo aviso.txt
        arquivo.close()
    except FileNotFoundError:
        pass
    else:
        tela = TelaPython()
        tela.iniciar()
        mixer.quit()
    finally:
        sleep(5)
