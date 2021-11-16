def setlevel(age):
    if age >= 1 and age <= 5:
        print('O aluno {} tem {} anos e está na Educação Infantil'.format(name, age))
    elif age >= 6 and age <= 10:
        print('O aluno {} tem {} anos e está no Ensino Fundamental I'.format(name, age))
    elif age >= 11 and age <= 14:
        print('O aluno {} tem {} anos e está no Ensino Fundamental II'.format(name, age))
    elif age >= 15:
        print('O aluno {} tem {} anos e está no Ensino Médio'.format(name, age))



#Programa Principal
while True:
    name = input('Nome aluno: ')
    age = int(input('Idade: '))

    setlevel(age) # Função para cálculo do nível escolar através de uma estrutura condicional
    answer = int(input('Deseja continuar? (0 - Não / 1 - Sim): '))
    if answer == 0:
        print('Encerrando programa...')
        break
    elif answer == 1:
        continue
    else:
        print('Opção inválida. Tente novamente!')