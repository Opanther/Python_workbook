from random import randrange

ticket_number = []
rand = randrange(1,50)


for i in range(6):
    rand = randrange(1, 50)
    while rand in ticket_number:
        rand = randrange(1, 50)
    ticket_number.append(rand)

ticket_number.sort()

print("Your Ticket number are:" )
for i in ticket_number:
    print(i)

