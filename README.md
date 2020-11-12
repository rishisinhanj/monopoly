# Monopoly Banking Program

## To run the program:
```git clone https://github.com/rishisinhanj/monopoly.git```

```python3 monopoly.py```

or alternatively, run the program in IDLE or editor of your choice

## Commands:
```go <name>```

*__name__* passed Go, collect 200

```fp <name>```

*__name__* landed on free parking, collect all free parking money

```<name> <amount>```

transfer  *__amount__* from  *__name__* to bank

```<amount> <name>``` 

transfer  *__amount__* from bank to  *__name__* 

```<name1> <amount> <name2>```

transfer  *__amount__* from  *__name1__* to  *__name2__*

## Sample Game:
```
The options for input are as follows: 
go <name> = <name> passed Go, collect 200
fp <name> = <name> landed on free parking, collect all free parking money
<name> <amount> = transfer <amount> from <name> to bank
<amount> <name> = transfer <amount> from bank to <name>
<name1> <amount> <name2> = transfer <amount> from <name1> to <name2>
-----------------------------------------------------
set starting values (enter <name, amount>, and enter "end" when done)
#pr, 1000
#ri, 1000
#end
Yayyy :D
Let's start the game!
fp: 0 | pr: 1000 | ri: 1000
#pr 100
fp: 0 | pr: 900 | ri: 1000
#ri 10 pr
fp: 0 | pr: 910 | ri: 990
#pr 15 fp
fp: 15 | pr: 895 | ri: 990
#go pr
fp: 15 | pr: 1095 | ri: 990
#50 ri
fp: 15 | pr: 1095 | ri: 1040
#fp ri
fp: 0 | pr: 1095 | ri: 1055
#
```
