import json
import string
import random 

class Bank:

    database = "bank.json"
    data = []

    try:
        with open(database) as fs:
            data = json.loads(fs.read())

    except Exception as err:
        print(err)

    @classmethod
    def updatedata(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def randomifsc(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        number = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k=2)
        id = alpha + number + spchar
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def createaccount(cls):
        info = {
        "name"    : input("Enter your name: "),
        "email"   : input("Enter your email: "),
        "numbers" : int(input("Enter your number: ")),
        "accountnumber" : cls.randomifsc(),
        "pin"     : int(input("Enter your 4 digit pin: ")),
        "balance" : 0,
        }
        cls.data.append(info)
        cls.updatedata()
        
    @classmethod
    def depositmoney(cls):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        user = [i for i in cls.data if i["accountnumber"] == accno and i ["pin"] == pin]
        if not user:
            print("no user found")

        else:
            print(f"ypur current balance: {user[0]['balance']}")
            amt = int(input("How much amount you want to withdraw: "))
            if amt > 9999:
                print("You can't deposit money")

            else:
                user[0]["balance"] += amt
                print(f"Blance left: {user[0]['balance']}")
                print("Deposit successful.")
                cls.updatedata()

    @classmethod
    def withdrawmoney(cls):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        user = [i for i in cls.data if i["accountnumber"] == accno and i ["pin"] == pin]
        if not user:
            print("No user found")

        else:
            print(f"your available balance: {user[0]['balance']}")
            amt = int(input("How much amount you want to withdraw: "))

            if amt > 9999 or amt > user[0]['balance']:
                print("Sorry you canot withdraw this money either you have insuficient balance or you are withrawing money above 9999")
            
            else:
                user[0]["balance"] -= amt
                print(f"Blance left: {user[0]['balance']}")
                print("Withdraw successful.")
                cls.updatedata()

    @classmethod
    def updateinfo(cls):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        user = [i for i in cls.data if i["accountnumber"] == accno and i ["pin"] == pin]
        if not user:
            print("No user found")

        else:
            print("you cannot change the account number and balance")
            print("press enter to skip and fill the field if you want to change: ")

            newdata = {
                "name": input("press enter to skip or write your new name: "),
                "email" : input("press enter to skip or write your new email: "),
                "pin"   : int(input("press enter to skip or write your new pin: ")),
                "number": int(input("press enter to skip or write your new number: "))
                }
            
            if newdata["name"] == "":
                newdata["name"] = user[0]["name"]

            if newdata["email"] == "":
                newdata["email"] = user[0]["email"]
            
            if newdata["pin"] == "":
                newdata["pin"] = user[0]["pin"]
            
            if newdata["numbers"] == "":
                newdata["numbers"] = user[0]["numbers"]

            for i in newdata:
                user[0][i] = newdata[i]

            cls.updatedata()
            print("your details have been succussfully ")
    
    @classmethod
    def displaydetails(cls):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        user = [i for i in cls.data if i["accountnumber"] == accno and i ["pin"] == pin]
        if not user:
            print("No user found")

        else:
            for i in user[0]:
                print(f"{i}: {user[0][i]}")

while True:
    print("Press 1 for creating a account ")
    print("Press 2 to Deposit response ")
    print("Press 3 for withdraw money  ")
    print("Press 4 to update your details ")
    print("Press 5 to display your details")
    print("Press 0 to exit")

    check = input("Tell your response: ")
    if check == "1":
        Bank.createaccount()

    elif check == "2":
        Bank.depositmoney()

    elif check == "3":
        Bank.withdrawmoney()

    elif check == "4":
        Bank.updateinfo()

    elif check == "5":
        Bank.displaydetails()

    elif check == "0":
        break

    Bank.createaccount()