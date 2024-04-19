#programa que recebe nome de um aluno e suas quatro notas e calcula a média

#Receber o nome do aluno
nome_aluno = input("Escreva o nome do aluno: ")

#receber as notas do aluno
nota_1 = float(input("Informe a nota 1: "))
nota_2 = float(input("Informe a nota 2: "))
nota_3 = float(input("Informe a nota 3: "))
nota_4 = float(input("Informe a nota 4: "))
#a função float() recebe um valor como parâmetro e retorna esse valor convertido para o tipo float
#no caso, estamos passando como parâmetro o que o usuário informar

#cálculo da média: soma das notas dividido pelo número de notas
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

#A variável "status_aluno" receberá o valor "aprovado" se a média for maior que 5. Caso contrário, receberá o valor "reprovado"
if (media > 5) :
    status_aluno = "aprovado"
else :
    status_aluno = "reprovado"

print("O(A) aluno(a) " + nome_aluno + " tem média " + str(media) + " e está " + status_aluno)
#a função str() é para converter o valor numérico para string e, somente assim, conseguirmos concatenar

print("Obrigado!")