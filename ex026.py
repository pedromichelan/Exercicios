a = str(input('Digite uma frase:')).strip()
a1 = a.lower()
print('A letra A aparece {} vezes na frase.'.format(a1.count('a')))
print('A primeira letra A apareceu na posição {}'.format(a1.find('a')+1))
print('A última letra A apareceu na posição {}'.format(a1.rfind('a')+1))