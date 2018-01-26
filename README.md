# Data Science do Zero

Este repositório contém meus estudos dos exemplos do livro **Data Science do Zero** da editora **Alta Books**. Todos os exemplos são construídos utilizando python 3, e com correções para as atualizações do matplot ou erros encontrados durante o estudo do livro.

Para executar os exemplos basta em um Terminal, Prompt de Comando ou _PowerShell_ escrever o comando:

**Unix/Linux/MacOS**
```Shell
$ python3 arquivo_exemplo.py
```

ou

**Windows**
```posh
PS > python3.exe arquivo_exemplo.py
```

Onde `arquivo_exemplo` deve ser trocado pelo nome do exemplo a ser executado.

## Requerimentos

Para executar estes exemplos é necessário antes instalar as seguintes bibliotecas do python3:

- matplotlib

É possível instalar estas bibliotecas utilizando o `pip` ou `conda` caso tenha a distribuição **Anaconda** instalado. Um exemplo pode ser visto a seguir:

**Unix/Linux/MacOS**
```Shell
$ pip3 install matplotlib
```

ou

```Shell
$ conda install matplotlib
```

Também é possível utilizar o arquivo `requirments.txt` para instalar qualquer requerimento necessário, cada pasta do capítulo que necessite de um requerimento conterá este arquivo, basta executar o comando para instalar os requerimentos:

```Shell
$ pip install -r requeriments.txt
```

No Linux é provável que seja necessário utilizar o comando sudo caso não esteja utilizando um ambiente virtual. Em caso de estar utilizando um ambiente virtual configurado para python 3, pode-se utilizar o comando `pip` direto ao invés de `pip3`, este último é usado em sistemas que possui as duas versões do python instalados.

No Linux é provável que seja ainda necessário instalar a biblioteca `tk` para python 3.

**Ubuntu**
```Shell
$ sudo apt install python3-tk
```

**Fedora**
```Shell
$ sudo dnf install python3-tk
```

Em outras distribuição procure por este nome de pacote que deve ser encontrado.

Para instalar as bibliotecas necessárias no Windows, pode-se usar o mesmo comando, caso tenha apenas o python 3 instalado utilize apenas `pip` ao invés de `pip3`, o mesmo caso esteja utilizando um ambiente virtual python. No caso do **Anaconda** o comando não se altera e pode ser digitado tanto no ambiente padrão como em um ambiente virtual criado pelo _conda_.

## Instalação Python 3

Caso seu sistema operacional não possua o python 3, é possível instalar baixando os instalador, pacote de distribuição ou código fonte para se compilar do [site oficial do Python](https://www.python.org), lembre-se de pegar a versão para python 3 respectiva a arquitetura do seu sistema operaciona, que pode ser X86, X64 entre outras.

A instalação do Windows é simples, pois a equipe do python provem um instalador para o sistema da Microsoft. É aconselhado que se inclua na hora da instalação a opção por permitir adicionar o python ao _path_ do sistema operacional, assim basta digitar o nome `python` ou `python.exe` em qualquer lugar no Prompt ou PowerShell que ele reconhecerá o programa.

A maioria das distribuições Linux/U