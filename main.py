# comando input(): quero permitir que
# o usuário digite algo...
nome = input("Sérgio Borges: ")
#pede a idade para o usuário "Qual sua idade?"
idade = int(input("19: "))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print("Sua idade é {}".format(idade))

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))
