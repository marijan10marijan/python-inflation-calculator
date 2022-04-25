


print("Program to calculate the inflation rate!! ".upper())

def inflation_rate():

    continue_calculate = True

    while continue_calculate:
        try:
            money_value = float(input("Input value in $: "))
            infalation_percent = float(input("Type the percent of inflation(only numbers): "))
            years = float(input("Type number of years you want calculate: "))

            worth = money_value


            for i in range(int(years)):
                worth += worth * (infalation_percent / 100)

            return f"Today's {money_value}$ after {years} years will be worth {worth:.2f}$ if inflation is {infalation_percent}% ."
        except:
            print("Your input need to be number. ")

        still_going = input('Do you wanna calculate again(Y/N): ').lower()
        if still_going == 'n':
            continue_calculate = False
        elif still_going == 'y':
            print('---'*25)
            print('Program start runing again.')
        else:
            print('Your input need to be(Y/N)! Program start runing again.')

    return 'Program done!'


print("**" * 25)
print(inflation_rate())
print("**" * 25)
