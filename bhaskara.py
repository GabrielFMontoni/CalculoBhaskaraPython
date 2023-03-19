#Criado por Gabriel Felipe Montoni
#https://github.com/GabrielFMontoni
#https://www.linkedin.com/in/gabriel-felipe-montoni/

a = int(input("Digite o número equivalente ao a "))
b = int(input("Digite o número equivalente ao b "))
c = int(input("Digite o número equivalente ao c "))
bhaskarap = ((-b)+((b**2-4*a*c)**0.5))/2*a
bhaskaran = ((-b)-((b**2-4*a*c)**0.5))/2*a
print(f"O valor de x1 é {bhaskarap:.1f} e o x2 {bhaskaran:.1f}")