#Simple automated FV calculation;

print('How many years you will be saving?')
years = int(input('Enter years: '))

print('How much money is currently n your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan on investing monthly?')
monthly_invest = float(input('Enter amount: '))

print('What do you estimate will be the yearly interest of this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1: '))

print(' ')

monthly_invest = monthly_invest *12
final_amount = 0

for i in range (0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

print ('This is how much you would have in your account after {} years: '.format(years) + str(final_amount))