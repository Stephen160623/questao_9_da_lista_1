print("Programa para resolver ax^2 + bx + c = y")

# Atribuição de variáveis

# Entrada de dados

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
y = float(input("y: "))

# Processamento de dados

c2 = c-y

x1 = (-b+((b**2)-4*a*c2)**0.5)/(2*a)
x2 = (-b-((b**2)-4*a*c2)**0.5)/(2*a)

# Saída de dados

print(str(x1)+" e "+str(x2))
