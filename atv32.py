def verificar_paridade(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

# Solicitar ao usuário um número
numero_informado = int(input("Digite um número: "))
resultado = verificar_paridade(numero_informado)

# Exibir o resultado
print(resultado)
