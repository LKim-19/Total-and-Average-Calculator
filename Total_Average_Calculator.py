total = 0.0
count = 0
average = 0.0

while True:
    x = input("Enter a number: ")

    try:
        inp = float(x)
    except:
        if x == 'done':
            break
        else:
            print('Invalid Input')
            continue

    total = total + inp
    count += 1

if average != 0.0:
    average = format(total/count, ".2f")
else:
    average = 0.0

print("\n")
print("The total is: ", total)
print("The amount of numbers entered: ", count)
print("The average is: ", average)
