espresso_req=[250,0,16,1,-4]
latte_req=[350,75,20,1,-7]
capp_req=[200,100,12,1,-6]
stat=[400, 540, 120, 9, 550]
names=["water","milk","beans","cups","money"]

def check(n):
    for i in range(len(n)):
        if stat[i]>=n[i]:
            stat[i]-=n[i]
            text="I have enough resources, making you a coffee!"
        else:
            text= ("Sorry, not enough {}!".format(names[i]))
            break
    print (text)

def buy():
    caffee=str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if caffee=='1':
        check(espresso_req)
    elif caffee=='2':
        check(latte_req)
    elif caffee=='3':
        check(capp_req)
    elif caffee=="back":
        return

def fill():
    stat[0]+=int(input("Write how many ml of water do you want to add:"))
    stat[1]+=int(input("Write how many ml of milk do you want to add:"))
    stat[2]+=int(input("Write how many grams of coffee beans do you want to add:"))
    stat[3]+=int(input("Write how many disposable cups of coffee do you want to add:"))
        
def take():
    print ("I gave you ${}".format(stat[4]))
    stat[4]=0
        
def remaining():
    print("The coffee machine has:\n {} ml\t of water\n {} ml\t of milk\n {}\t of coffee beans\n {}\t disposable cups\n {} $\t of money".format(stat[0], stat[1], stat[2], stat[3], stat[4])) 

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    n=str(input())
    if n=="buy":
        (buy())
    elif n=="fill":
        fill()
    elif n=="take":
        take()
    elif n=="remaining":
        (remaining())
    elif n=="exit":
        break
