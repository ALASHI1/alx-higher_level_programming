#!/usr/bin/python3

def uppercase(str):
    alha = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 
            'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 
            'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N',
            'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 
            't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 
            'y':'Y', 'z':'Z'}
    
    for i in str:
        if i in alha:
            print('{}'.format(alha[i]), end="")
        else:
            print(i, end="")
