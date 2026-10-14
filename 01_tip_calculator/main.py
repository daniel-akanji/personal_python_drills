def tip_calculator():
    global ammount
    global tip_percentage
    global people

    ammount = input("Enter bill amount: ").strip()
    tip_percentage = input("Enter tip percentage: ").strip()
    people = input("Number of people: ").strip()
    
    def validate_input():
        global ammount
        global tip_percentage
        global people
        try:
            ammount = float(ammount)
            tip_percentage = float(tip_percentage)
            people = int(people)
        except:
            print("Invalid input")
            tip_calculator()
    validate_input()

    if ammount < 0 or tip_percentage < 0 or people <= 0:
        print("invlaid input")
        tip_calculator()

    total_tip = (tip_percentage/100) * ammount
    total_amount = ammount + total_tip
    each_share = round(total_amount / people, 2)


    return f"DONE!\n\nTotal tip: {total_tip}\nEach person's share: {each_share}"

print(tip_calculator())