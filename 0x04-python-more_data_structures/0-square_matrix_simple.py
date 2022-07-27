#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mutiples = []
    new_matrix = map(lambda x: map(lambda y: y ** 2, x), matrix)
    omo = list(new_matrix)
    for i in omo:
        oya = list(i)
        mutiples.append(oya)
    return mutiples
