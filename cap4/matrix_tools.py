"""Ferramenta de simulação de matriz para listas em python.

Esta ferramenta é uma implementação do capítulo 4, do livro Data Science do Zero
em python 3 para meus estudos. O nome de algumas funções foi renomeado para 
simplificar.

Lembrando que não deve ser utilizado para fins produtivos, pois utiliza listas
do python que não são as melhores alternativas em performance. O melhor seria 
utilizar numpy para trabalhar com vetores.

Exemplo:
    ...
"""
from typing import Callable, List, NewType

Array = NewType('Array', List[int])
Matrix = NewType('Matrix', Array)   # cria um novo tipo como lista-de-listas do
                                    # tipo `int`.

def matrix_shape(A: Matrix) -> (int, int):
    """Retorna a forma da matriz no estilo número de linha X número de coluna.

    A partir de uma lista-de-listas que representa uma matriz, retorna seu 
    número de linhas e colunas.
    
    Args:
        A (Matrix): Lista-de-listas que representa a matriz.
    Return:
        int: Número de linhas da matriz.
        int: Número de colunas da matriz.
    """
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_rows, num_cols

def matrix_get_row(A: Matrix, i: int) -> List[int]:
    """Retorna a i-ésima linha da matriz.

    Atravéz de um número de linha retorna a lista que representa aquela linha na
    matriz.
    
    Args:
        A (Matrix): Lista-de-listas que representa a matriz.
        i (int): Número i-ésima linha da matriz.
    Return:
        List[int]: Lista que representa a i-ésima linha
    """
    return A[i]

def matrix_get_col(A: Matrix, j: int) -> List[int]:
    """Retorna a j-ésima coluna da matriz.

    Atravéz de um número de coluna retorn a lista que representa aquela coluna 
    da matriz.
    
    Args:
        A (Matrix): Lista-de-listas que representa a matriz.
        j (int): Número da j-ésima coluna da matriz.
    Return:
        List[int]: Lista que representa a j-ésima coluna.
    """
    return [A_i[j] for A_i in A]

def matrix_make(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], int]=None) -> Matrix:

    return [[entry_fn(i, j) if entry_fn else None
            for j in range(num_cols)]
                for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0