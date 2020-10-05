nome = str(input("Digite o nome do aluno:"))
nota1 = int(input("Digite a primeira nota do aluno:"))
nota2 = int(input("Digite a segunda nota do aluno:"))
media = (nota1 + nota2) / 2
print ("Média do aluno é:", media)
if media < 7:
    print("Aluno Reprovado.")

else:
    print ("Aluno Aprovado.")