def gpa_calc():
    n = int(input("Enter the number of subjects: "))
    total = 0
    chr = 0
    for i in range(n):
        gp = float(input(f"Enter the GPA of subject {i+1}: "))
        ch = int(input(f"Enter the credit hours of subject {i+1}: "))
        total += gp * ch
        chr += ch
    return total/chr
def cgpa_calc():
    n = int(input("Enter the number of semesters: "))
    total = 0
    total_ch = 0
    for i in range(n):
        ch = int(input(f"Enter the total credit hours of semester {i+1}: "))
        cgpa = float(input(f"Enter the CGPA of semester {i+1}: "))
        total += cgpa * ch
        total_ch += ch
    return total/total_ch
while True:
    n = input("Enter \n1 for GPA calculation\n2 for CGPA calculation\n3 to exit\n>")
    if n == '1':
        print("Your GPA is :",gpa_calc())
    elif n == '2':
        print("Your CGPA is :",cgpa_calc())
    elif n == '3':
        break
    else:
        print("Invalid input! Please")
