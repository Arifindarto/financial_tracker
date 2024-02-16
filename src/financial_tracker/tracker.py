def tracker():
    print("Simple Financial Tracker")

    income_list=[]
    expense_list=[]

    print("0. Quit")
    print("1. Add income")
    print("2. Add expense")
    print("3. list income")
    print("4. list expense")
    print("5. balance")
    print("================================")

    while True:
        option = int(input("Choose an option:"))
        
        if option == 1:
            income = int(input("Add income:"))
            income_list.append(income)
            print("================================")
        
        if option == 2:
            expense = int(input("Add expense:"))
            expense_list.append(expense)
            print("================================")
        if option == 3:
            print(income_list)
            print("================================")
        if option == 4:
            print(expense_list)
            print("================================")
        if option == 5:
            print(sum(income_list)-sum(expense_list))
            print("================================")
        if option == 0:
            print("Bye-bye")
            break
        
