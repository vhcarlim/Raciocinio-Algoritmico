# Atividade dos Triângulos
# Peça os três lados de uma figura. Primeiro, verifique se esses valores podem formar um triângulo.
# Lembre-se: a soma de dois lados deve ser sempre maior que o terceiro.
# Se for possível formar um triângulo, classifique-o: Equilátero: todos os lados têm o mesmo tamanho. Isósceles: dois lados têm o mesmo tamanho. Escaleno: todos os lados são diferentes.
# Além disso, verifique se o triângulo é retângulo: Um triângulo é retângulo quando o quadrado do maior lado é igual à soma dos quadrados dos outros dois lados. Caso os valores não formem um triângulo, informe isso ao usuário.

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    lados = sorted([lado1, lado2, lado3])
    if lados[2]**2 == lados[0]**2 + lados[1]**2:
        print(f"O triângulo é {tipo} e retângulo.")
    else:
        print(f"O triângulo é {tipo} e não é retângulo.")
