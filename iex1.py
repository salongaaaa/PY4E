cnt = 0
tot = 0
while True:
    sval = input("enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue
    cnt = cnt + 1
    tot = tot + fval

print("total: ", tot, "count: ", cnt, "average: ", tot/cnt)
