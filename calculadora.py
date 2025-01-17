#calculadora ;-;
#acho que consigo fazer
#lesgoo

print("calculadora")
print("use + para adiçao, - para subtraçao, * para multiplicaçao e / para divisao")
numero1 = int(input("digite seu primeiro numero"))
operaçao = input("digite qual operaçao voce quer fazer")
numero2 = int(input("digite seu segundo numero"))



#adiçao
if operaçao == "+":
    print(numero1 + numero2)
#subtraçao
elif operaçao == "-":
    print(numero1 - numero2)
#multiplicaçao
elif operaçao == "*":
    print(numero1 * numero2)
#divisao
elif operaçao == "/":
    print(numero1 / numero2)

