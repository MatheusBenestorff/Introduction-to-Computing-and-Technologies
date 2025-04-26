anoNascimento =int(input("Digite o seu ano de nascimento: "))

idade =2025- anoNascimento

print(f"Ano de nascimento: {anoNascimento}")
print(f"Idade: {idade} anos")

if idade ==18:
    print("Situação: Já deve se alistar ao serviço militar.")
elif idade >18:
    print(f"Situação: Já passou o prazo do alistamento. Está {idade -18} anos atrasado.")
else:
    print(f"Situação: Ainda não precisa se alistar. Faltam {18- idade} anos para o alistamento militar.")    