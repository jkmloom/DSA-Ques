# Problem: movie tickets are priced on age: $12 for adults (18 and above), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter age:\t"))
day_wed = 1

price = 12 if age >= 18 else 8

if day_wed == True:
    price -= 2
    print(f'Ticket price: ${float(price)}')
else:
    print(f'Ticket price: ${float(price)}')