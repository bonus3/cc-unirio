#programa que recebe nome de um aluno e suas quatro notas e calcula a média

#Receber o nome do aluno
nome_aluno = input("Escreva o nome do aluno: ")

#A varipavel "soma_notas" armazenará a soma das notas informadas
#inicializamos com o valor zero e somaremos cada nota informada
soma_notas = 0

#"for" é uma estrutura de repetição quando sabemos a quantidade de vezes que o trecho de código irá repetir
#No caso, iremos pegar as quatro notas dos alunos, então o trecho de código vai repetir quatro vezes
#A função range() é nativa do python que retorna uma lista de números. A forma com que estamos a usando, retornará uma lista de 1 até 4
for x in range(1, 5):
    nota_digitada = float(input("Informe a nota " + str(x) + " de " + nome_aluno + ": "))
    soma_notas = soma_notas + nota_digitada #Adiciona o valor da nota digitada ao valor que estiver em "soma_notas"

#cálculo da média: soma das notas dividido pelo número de notas
media = soma_notas / 4

#A variável "status_aluno" receberá o valor "aprovado" se a média for maior que 5. Caso contrário, receberá o valor "reprovado"
if (media > 5) :
    status_aluno = "aprovado"
else :
    status_aluno = "reprovado"
    
#A mesma atribuição condicional de valor pra variável 'status_aluno' poderia ser feita de outra forma mais simplificada:
status_aluno = "aprovado" if media > 5 else "reprovado" #Essa linha tem o mesmo resultado do if else anterior

print("O(A) aluno(a) " + nome_aluno + " tem média " + str(media) + " e está " + status_aluno)
print("Obrigado!")