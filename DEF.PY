account={}
while(True):
    print("""1.Create Account
2.Deposit Money
3.Withdraw Money
4.Balance
5.Exit""")
    ch=int(input("Enter your choice"))
    def createbank(acc_no):
        if acc_no in account:
            print("The account already exits!!")
            return "No need To create A account"
        else:
            account[acc_no]=0
            return "Account Created"
    def depositmoney(acc_no,amt):
        if acc_no in account:
            if amt>0:
               account[acc_no]+=amt
               return "Deposit Completed"
            else:
                return "This is amount is unacceptable"
        else:
            return "There is no such accounts!!"
    def withdrawmoney(acc_no,amt):
        if acc_no in account:
            if amt>0:
                amt=account[acc_no]-amt
                if(amt<=0):
                    return "Can't withdraw this amount it will make your account freeze!!"
                else:
                    account[acc_no]=amt
                    return "Withdrawal done....!!!"
            else:
                return "This amount can't be withdrawal!!"
        else:
            return "There is no such accounts!!"
    def balance(acc_no):
        if acc_no in account:
            return account[acc_no]
        else:
            return "There is no such accounts !!"
    def exit():
       return 
    if ch==1:
        acc_no=int(input("Enter a unique account number:"))
        s=createbank(acc_no)
        print(s)
    elif ch==2:
        acc_no=int(input("Enter your account number:"))
        amt=int(input("Enter amount to be deposited:"))
        p=depositmoney(acc_no,amt)
        print(p)
    elif ch==3:
        acc_no=int(input("Enter your account number:"))
        amt=int(input("Enter amount to be withdrawn:"))
        s=withdrawmoney(acc_no,amt)
        print(s)
    elif ch==4:
        acc_no=int(input("Enter your account no:"))
        s=balance(acc_no)
        print("The balance in account",acc_no,"is",s)
    elif ch==5:
        exit()
        break
    else:
        print("INVALID CHOICE")
            




            
