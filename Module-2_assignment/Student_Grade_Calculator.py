name=input("Student Name: ")

Sub_1=float(input("Enter Subject-1 marks: "))
Sub_2=float(input("Enter Subject-2 marks: "))
Sub_3=float(input("Enter Subject-3 marks: "))

Tm= Sub_1+Sub_2+Sub_3

Av= Tm/3

if (Sub_1<0 or Sub_1>100) or (Sub_2<0 or Sub_2>100) or (Sub_3<0 or Sub_3>100):
    print("Invalid Marks.")
else:    

    if Av >= 80:
        grade="A+"
    elif Av >= 70:
        grade="A"
    elif Av >= 60:
        grade="B"
    elif Av >= 50:
        grade="C"
    else:
        grade="F"

    print(f"""Student Name: {name}

Total Marks: {Tm:.2f}

Average: {Av:.2f}

Grade: {grade}""") 
