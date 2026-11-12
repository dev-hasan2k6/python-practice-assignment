name=input("Customer Name: ")

pro_1=input("Product 1: ")
p1=float(input("Price: "))

pro_2=input("Product 2: ")
p2=float(input("Price: "))

pro_3=input("Product 3: ")
p3=float(input("Price: "))

Sub=float(p1+p2+p3)

if Sub >= 5000:
    Dis=(Sub*(20/100))
elif 3000<= Sub <=4999:
    Dis=(Sub*(10/100))
elif 1000<= Sub <= 2999:
    Dis=(Sub*(5/100))
else:
    Dis=(Sub*0)

Ft=(Sub-Dis)

print(f"""
Customer Name: {name}

\nProduct 1: {pro_1}
Price: {p1}

\nProduct 2: {pro_2}
Price: {p2}

\nProduct 3: {pro_3}
Price: {p3}

\nSubtotal: {Sub:.2f}
Discount: {Dis:.2f}
Final Total: {Ft:.2f}
""")





