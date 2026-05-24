setting = int(input("Type 1 for CAD to mani kala, type 2 for mani kala to CAD. "))

if setting == 1:
    num = float(input("Type amount of CAD: "))
    
    print(f"{num} CAD is {round(num / 0.125) // 20} kala suli and {round(num / 0.125) % 20} kala lili")

if setting == 2:
    num1 = int(input("Type amount of kala suli: "))
    num2 = int(input("Type amount of kala lili: "))
    
    print(f"{num1} kala suli and {num2} kala lili is {round((num1 + num2/20) * 2.5, 2):.2f}$ CAD")

input()