Student_Name=(input("Enter student name: "))

Math=float(input("\n\nEnter Math marks: "))
English=float(input("\nEnter English marks: "))
Python=float(input("\nEnter Python marks: "))
if (Math<0 or Math>100) or (English<0 or English>100) or (Python<0 or Python>100):
    print("\nInvaild Marks.")
else:
    Average_Marks=((Math + English + Python) / 3)
    print(f"\n\nStudent Name: {Student_Name} ")
    print(f"\nAverage Marks: {Average_Marks:.2f}")

    if Average_Marks >=80 and Average_Marks <=100:
        print("\nFinal Grade: A+")
    elif Average_Marks >=70 and Average_Marks <=79:
        print("\nFinal Grade: A")
    elif Average_Marks >=60 and Average_Marks <=69:
        print("\nFinal Grade: A-")
    elif Average_Marks >=50 and Average_Marks <=59:
        print("\nFinal Grade: B")
    elif Average_Marks >=40 and Average_Marks <=49:
        print("\nFinal Grade: C")
    else:
        print("\nFinal Grade: F")