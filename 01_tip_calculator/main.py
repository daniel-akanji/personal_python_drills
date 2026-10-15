def calculate_tip(amount, tip_percentage, people):    
    tip = (tip_percentage/100) * amount
    total = amount + tip
    each_share = round(total / people, 2)

    return round(tip, 2), round(total, 2), round(each_share, 2)
     

def validate_input(prompt, cast=float, minimum = 0):
    while True:
        try:
            value = cast(input(prompt.strip()))
        except ValueError or TypeError:
            print("Please enter a valid number")
            continue
        if value < minimum:
            print(f"Value must be at least {minimum}")
            continue
        return value       
 
def main():
    ammount = validate_input("Enter Bill amount: ") 
    tip_percentage = validate_input("Enter tip percentage: ")
    people = validate_input("Number of people: ", cast = int, minimum=1)

    tip, total, each_share = calculate_tip(ammount, tip_percentage, people)

    return f"DONE!\n\nTotal amount: {total}\nTotal tip: {tip}\nEach person's share: {each_share}"

print(main())