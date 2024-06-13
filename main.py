
import os
from datetime import date

def exibir_data():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    
    print(f'\nBrasília {dia} de {meses[mes -1]} de {ano}.\n')
    
#Funções
def medias(notas):
    return sum(notas) / len(notas)
	
def aprovacao(media):
	if media >= 7:
		return 'Aprovado'
	else:
		return 'Reprovado'

#Inicio do programa
if __name__ == '__main__':
    
    alunos = []

for i in range(2):
    exibir_data()
    nome = input('Informe o nome do aluno: ')
    
    notas = []
	
    for n in range(5):
        nota = int(input(f'Digite a nota {n+1} do aluno {nome}: '))
        
        notas.append(nota)

    os.system('cls')

    media = medias(notas)
    resultado = aprovacao(media)
    
    alunos.append({'nome': nome, 'notas': notas, 'media': media, 'resultado': resultado})

# Resultados
for aluno in alunos:
    print(f'Aluno: {aluno['nome']}')
    print(f'Notas: {aluno['notas']}')
    print(f'Média: {aluno['media']}')
    print(f'Resultado: {aluno['resultado']}')
    print(f'{'-'*25}')