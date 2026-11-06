#pedir datos 
nota1= input('decime una nota: ')
primer_nota = int(nota1)

nota2 = input('decime la otra nota: ')
segunda_nota = int(nota2)

nota3 = input('decime la ultima nota: ')
tercera_nota = int(nota3)

sum_notas = primer_nota + segunda_nota + tercera_nota
promedio_notas = (sum_notas / 3)
print(f'promedio: {promedio_notas} ') 
print('...............')

porcentaje = primer_nota * 100 // 10
print(f'{porcentaje}%')

if primer_nota > 6:
    print('promociona la materia ')
elif primer_nota > 4 < 6 :
    print('aprobado')
else: 
    print('Desaprobado')

print('................')

porcentaje2 = segunda_nota * 100 // 10
print(f'{porcentaje2:}%')

if segunda_nota > 6:
    print('promociona la materia ')
elif segunda_nota > 4 < 6:
    print('aprobado')
else: 
    print('Desaprobado')

print('................')

porcentaje3 = tercera_nota * 100 // 10
print(f'{porcentaje3}%')

if tercera_nota > 6:
    print('promociona la materia ')
elif segunda_nota > 4 < 6:
    print('aprobado')
else: 
    print('Desaprobado')