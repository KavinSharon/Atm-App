class Atm:
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin
    def cashWithdrawl(self,amount):
        newAmount=50000-amount
        print("You Have Withdrawn"+str(amount)+"your balance Amount is"+str(newAmount))
    def balanceEnquiry(self):
        print("Your Balance Is 50000")

def main():
    cardNo = input("Enter Your Card Number")
    pin = input("Enter Your Pin")

    user = Atm(cardNo,pin)

    print("1)CashWithdrawal 2)BalanceEnquiry")

    choice = int(input("Enter Your Preferance"))

    if(choice==1):
        amount=int(input("Enter Your Amount"))
        user.cashWithdrawl(amount)
    else:
        user.balanceEnquiry()
        
main()