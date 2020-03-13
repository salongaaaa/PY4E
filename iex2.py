cnt = 0

while True:
    sval = input("enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue

    if cnt == 0:
        minval = fval
        maxval = fval
    elif fval < minval:
        minval = fval
    elif fval > maxval:
        maxval = fval

    cnt = cnt + 1

print("minimum value: ", minval, "maximum value: ", maxval)
