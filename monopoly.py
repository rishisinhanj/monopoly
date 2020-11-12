def printBalance(balance):
    balanceList = ["{}: {}".format(item, amount) for item, amount in balance.items()]
    print(' | '.join(balanceList))

balance = {'fp': 0}
allowed = {'bank', 'fp'}
players = set()

#instructions for how to use program
print("The options for input are as follows: ")
print("go <name> = <name> passed Go, collect 200")
print("fp <name> = <name> landed on free parking, collect all free parking money")
print("<name> <amount> = transfer <amount> from <name> to bank")
print("<amount> <name> = transfer <amount> from bank to <name>") 
print("<name1> <amount> <name2> = transfer <amount> from <name1> to <name2>")
print("-----------------------------------------------------")

#enter starting values
print("set starting values (enter <name, amount>, and enter \"end\" when done)")
while True:
    inp = input('#')
    if inp == 'end':
        break
    try:
        split_inp = inp.split(',')
        name = str(split_inp[0])
        amt = int(split_inp[1])
        allowed.add(name)
        players.add(name)
        balance[name] = amt
    except Exception as e:
        print("Error with inputting pair of starting values, please re-enter.")          

print("Yayyy :D\nLet's start the game!")
printBalance(balance)

#loop that takes input throughout game, possible instructions described in branches below
while True:
    try:
        inp = input('#') #asking for input and splitting on spaces
        split_inp = inp.split()
        if len(split_inp) == 2:
            if str(split_inp[0]) == 'go': #go <name> = <name> passed Go, collect 200
                to = str(split_inp[1])
                balance[to] = balance[to] + 200
            elif str(split_inp[0]) == 'fp': #fp <name> = <name> landed on free parking, collect all free parking money
                to = str(split_inp[1])
                frm = 'fp'
                balance[to] = balance[to] + balance[frm]
                balance[frm] = 0
            elif str(split_inp[1]) in players: #<amount> <name> = transfer <amount> from bank to <name>
                amt = int(split_inp[0])
                frm = str(split_inp[1])
                balance[frm] = balance[frm] + amt
            elif str(split_inp[0]) in players: #<name> <amount> = transfer <amount> from <name> to bank
                frm, amt = str(split_inp[0]),int(split_inp[1])
                balance[frm] = balance[frm] - amt
            else:
                print("Entered invalid input, please correct and re-enter.")
        elif len(split_inp) == 3: #<name1> <amount> <name2> = transfer <amount> from <name1> to <name2>
            frm, amt, to = str(split_inp[0]),int(split_inp[1]),str(split_inp[2])
            if frm not in allowed or to not in allowed:
                print('Entered invalid names to transfer to/from, please correct and re-enter.')
            else:
                if frm != 'bank' and frm in balance:
                    balance[frm] = balance[frm] - amt
                if to != 'bank' and to in balance:
                    balance[to] = balance[to] + amt
        else:
            print("Input was not 2 or 3 names/numbers.")
        printBalance(balance)
    except Exception as e:
        print("Entered invalid input, please correct and re-enter.")
    
