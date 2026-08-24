while True:
    print("Welcome to Ohm's law calculator")
    print("1. Calculate Current")
    print("2. Calculate Resistance")
    print("3. Calculate Voltage")
    print("4. Calculate Power")
    choice= int(input("Choose an action from 1 to 5:"))
    if choice < 1 or choice > 5:
        print("Invalid input. Enter a value between 1 and 5")
    if choice== 1:
        v= float(input("Enter Voltage:"))
        r= float(input("Enter Resistance:"))
        a=v/r
        print("The value of Current is:",a,"A")
    elif choice == 2:
        cu=float(input("Enter Current:"))
        vo= float(input("Enter Voltage:"))
        b=vo/cu
        print("The value of resistance is:", b,"ohm")
    elif choice== 3:
        i= float(input("Enter Current:"))
        re= float(input("Enter Resistance:"))
        vl= i*re
        print("The value of Voltage is:",vl,"V")
    elif choice == 4:
        print("what are the values do you have?")
        print("Voltage + current")
        print("Voltage + Resistance")
        print("Current + Resistance")
        l= int(input("Enter a value from 1 to 3"))
        if l== 1:
            vol= float(input("Enter Voltage:"))
            cur= float(input("Enter Current:"))
            p= vol*cur
            print("The value of power is:",p,"W")
        elif l==2:
            curr= float(input("Enter Current:"))
            resi= float(input("Enter Resistnace:"))
            pow= curr*curr*resi
            print("The value of power is:",pow,"W")
        elif l==3:
            volt= float(input("Enter Voltage:"))
            resis= float(input("Enter resistance:"))
            power=(volt*volt)/resis
            print("The value of power is:",power,"W")
        else:
            print("Invalid input")
    again = input("Do you want another calculation? (y/n): ")

    if again.lower() == "n":
        print("Exiting calculator, Bye!!")
        break

