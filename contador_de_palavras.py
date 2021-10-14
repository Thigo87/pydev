txt = str(input(''' Digite o seu texto: 
'''))

words = list(txt.split())

letters = list(txt)

wCounter = len(words)

lCounter = len(letters)


print(f'O seu texto tem {wCounter} palavras.')
print('O seu texto tem', lCounter,'letras.')