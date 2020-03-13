try:
    hours = float(input ("enter hours: "))
    rate = float(input ("enter rate: "))
except:
    print("error, please enter numeric input.")
    quit()

if hours > 40:
    pay = ((hours - 40)*(rate * 1.5))+(40*rate)
    print("pay: ", pay)
else:
    pay = hours * rate
    print("pay: ", pay)
