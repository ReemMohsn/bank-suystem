def nettotal(acount,amount,operation):
    if operation=="-":
        last_line = int((acount.readlines())[-1])
        net_total = last_line - amount
        return net_total
    elif operation=="+":
        last_line = int((acount.readlines())[-1])
        net_total = last_line + amount
        return net_total
def cearch(id):
    import os.path
    if os.path.exists(id):
        fail=open(f"{id}","r+")
        return fail
class customer:
    id="0"
    id2="0"
    def creat(self,name,birthdat,job,phon_num,address,type_account,amount):
        self.name=name
        self.birthdat=birthdat
        self.job=job
        self.phon_num=phon_num
        self.address=address
        self.type_account=type_account
        self.amount=amount
        file = open(f"{self.id}", "w")
        file.write(f"the information of client:\nthe name: {self.name}\n the birthdat: {self.birthdat}\n the job: {self.job}\nthe phone number: {self.phon_num}\nthe address: {self.address}\ntype of account:{self.type_account} \n{self.amount}\n")
        file.close()

    def transfer(self):
        acount_send=cearch(self.id)
        name_sending=input("enter the name of sending:")
        acount_receive=cearch(self.id2)
        name_receive=input("enter the name of receive:")
        if acount_send != None and acount_receive != None:
            amount=int(input("enter the amount :"))
            net_total_send=nettotal(acount_send,amount,"-")
            acount_send.write(f"\nthe amount transferred to {name_receive} ={amount} ,in{datetime.date.today()}\nnet total :\n{net_total_send}")
            acount_send.close()
            net_total_receive=nettotal(acount_receive,amount,"+")
            acount_receive.write(f"\nthe amount transferred from {name_sending} ={amount} ,in{datetime.date.today()}\nnet total :\n{net_total_receive}")
            acount_receive.close()
        elif acount_send != None and acount_receive == None:
            amount = int(input("enter the amount :"))
            net_total_send=nettotal(acount_send,amount,"-")
            acount_send.write(f"\nthe amount transferred to {name_receive} ={amount} ,in{datetime.date.today()}\nnet total :\n{net_total_send}")
            acount_send.close()
            print(f" there is amount transferred for {name_receive} from {name_sending} ={amount} ")
        elif acount_send == None and acount_receive == None:
            print("sorry for you ,you don't have any account with us ..if you want transferred you should create account first")

    def withdraw(self):
        your_acount=cearch(self.id)
        if  your_acount!= None:
            amount = int(input("enter the amount :"))
            net_total=nettotal(your_acount,amount,"-")
            your_acount.write(f"\nthe amount withdrow ={amount} ,in{datetime.date.today()}\nnet total after withdrow:{net_total}\n{net_total}")
            your_acount.close()
        else:
            print("you do not have any account with us ,pleas create account first")
    def deposit(self):
        acount_deposit=cearch(self.id)
        if  acount_deposit!= None:
            amount = int(input("enter the amount :"))
            net_total=nettotal(acount_deposit,amount,"+")
            acount_deposit.write(f"\nthe amount deposit ={amount} ,in{datetime.date.today()}\nnet total after deposit:{net_total}\n{net_total}")
            acount_deposit.close()
        else:
            print("the person does not have account ,sorry for you, we cna not help you")
    def read(self):
        your_acount=cearch(self.id)
        if your_acount!= None:
            print(your_acount.read())
            print("pleas,see to your account.")
            your_acount.close()
        else:
            print("you don't have account")
    def report(self):
        faill = open("daily report", "a")
        faill.write(f"daily report for {datetime.date.today()}")
        faill.write(f"---------------------------------\ntype opetion\t\tid\t\tTime\n")
        all = creat + trnsfer + withdraw + deposit + read
        for i in list:
            faill.write(f"{i}\n")
        faill.write(f"create operation:{creat}\ntrnsfer operation:{trnsfer}\nwithdraw operation:{withdraw}\ndeposit operation:{deposit}\nread operation:{read}\nthe total of all operation :{all}")
        faill.write("\n-----------------------------------------------\n")
        faill.close()
import datetime
list=[]
creat=trnsfer=withdraw=deposit=read=0
while True:
    costemer1=customer()
    print("Wellcome to R.KH.S.F bank")
    print("if you want creat account enter 1 :")
    print("if you want trnsfer enter 2 :")
    print("if you want withdraw enter 3 :")
    print("if you want deposit enter 4 :")
    print("if you want to read your fail of account enter 5 :")
    print("if you want to read  all dailies report enter 6 :")
    print("if you want exit enter 7 :")
    operation = int(input("enter num: "))
    data=""
    if operation == 1:
        creat+=1
        costemer1.id = input("enter the id:")
        costemer1.creat(input("enter the full name:"), input("enter your birthday:"), input("enter the job:"),int(input("enter the phone number:")), input("enter address:"),input("enter the type of account current account or transfers:"),int(input("enter the amount:")))
        data=f"creat account\t\t{costemer1.id}\t\t{datetime.datetime.now().time()}"
    elif operation == 2:
        trnsfer+=1
        costemer1.id = input("enter the id of sending account:")
        costemer1.id2=input("enter the id of receive account:")
        costemer1.transfer()
        data =f"trnsfer operation\t\tfrom:{costemer1.id}\tto:{costemer1.id2}\t{datetime.datetime.now().time()}"
    elif operation == 3:
        withdraw+=1
        costemer1.id = input("enter the id of your account:")
        costemer1.withdraw()
        data=f"withdraw operation\t\t{costemer1.id}\t\t{datetime.datetime.now().time()}"
    elif operation == 4:
        deposit+=1
        costemer1.id=input("enter the id of deposit account:")
        costemer1.deposit()
        data = f"deposit operation\t\t{costemer1.id}\t\t{datetime.datetime.now().time()}"
    elif operation == 5:
        read+=1
        costemer1.id=input("enter your id:")
        costemer1.read()
        data = f"read file \t\t{costemer1.id}\t\t{datetime.datetime.now().time()}"
    elif operation == 6:
        fail=open("daily report","r")
        print(fail.read())
        fail.close()
    elif operation == 7:
        costemer1.report()
        break
    else:
        print("enter 1 or 2 or 3 or 4 or 5 or 6")
    list.append(data)


