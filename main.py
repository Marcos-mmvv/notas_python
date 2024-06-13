
import os
from datetime import date

#Data
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

#Laço 1
for i in range(30):
    exibir_data()
    print(f'{'-'*30} BOLETIM MENSAL PYTHON SCHOOL {'-'*30}\n')
    nome = input('Informe o nome do aluno(a): ')
    
    notas = []
	#Laço 2
    for n in range(5):
        nota = int(input(f'Digite a nota {n+1} do aluno(a) {nome}: '))
        notas.append(nota)

    os.system('cls')

    #Funções
    media = medias(notas)
    resultado = aprovacao(media)

    # Lista final
    alunos.append({'nome': nome, 'notas': notas, 'media': media, 'resultado': resultado})

# Resultados
for aluno in alunos:
    print(f'Aluno(a): {aluno['nome']}')
    print(f'Notas: {aluno['notas']}')
    print(f'Média: {aluno['media']}')
    print(f'Resultado: {aluno['resultado']}')
    print(f'{'-'*25}')