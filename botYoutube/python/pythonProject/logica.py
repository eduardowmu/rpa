numero = 10
texto = "Ola"
verdade = True

print(numero, texto, verdade)
print('Numero: ' + str(numero), f'Texto: {texto}', f"Verdade: {str(verdade)}")
print(type(numero), type(texto), type(verdade))

if texto != 'Hello':
    print(verdade)
else:
    texto = 'Hello'
    print(texto)

#listas
funcionarios = ['Eduardo', 'Camila', 'Rodolfo']
for f in funcionarios:
    print(f)

#printa somente o primeiro caractere de cada nome
for f in funcionarios:
    print(f[0])

#printa somente o ultimo caractere de cada nome
for f in funcionarios:
    print(f[-1])

#printa todos os nomes porém exceto a ultima letra de cada
for f in funcionarios:
    print(f[:-1])