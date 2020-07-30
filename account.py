#class methods 
#Michelle  Nthumo
class BankAccount:
  bank="KCB"
  
  def __init__(self,first_name,last_name,phone_number):
    self.first_name=first_name
    self.last_name=last_name
    self.phone_number=phone_number
    self.balance=0
    
    
  def account_name(self):
    name="{} account for {} {}".format(self.first_name,self.last_name, self.phone_number)
    return  name
    

  def deposit(self,amount):
        try:
          amount + 1
          except TypeError:
            print("please enter amount in figures")

    
    if amount>0:
      print("You cannot deposit zero or negative")
      
    else:
      self.balance+=amount
      self.deposits.append(amount)
      print("You have deposited {} to {} {}".format(amount,self.account_name()))
      
  def withdrawal (self, amount):
    try:
      amount + 1
          except TypeError:
            print("please enter amount in figures")
            return

    if amount<=0:        
      print("You cannot withdrawal zero or negative")

    elif amount>self.balance:
       print ("You don't have enough balance")

    else:
          time=datetime.now)()
          formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
          withdrawal={
            "time":"time",
            "amount":"amount"
          }

        self.balance-=amount
    self.withdrawals.append(amount)
    print("You have withdrawn {} from {}".format(amount,self.account_name()))
    
def show_deposit_statement(self):
     for deposit in self.deposits:
       print("deposit")
     
def show_withdrawals_statement(self):
     for withdrawal in self.withdrawals:
           time=withdrawal(['time'])
           amount=withdrawal(['amount'])
           formatted_time=time.strftime("%A,%d /%B /%Y, %H:%M:%P")
           withdrawals_statement="You have withdrawn {} on {}".format(amount)
       print("withdrawal")
       
def request_loan(self,amount):
      try:
        amount + 1
      except TypeError:
        print("please enter amount in figures")
        return

   if amount<=0:
     print ("you cannot request a loan of that amount")

   else:
     self.loan=amount
     print("you have been given a loan of {}".format(amount))
     
def repay_loan(self, amount):
      try:
        amount + 1
        except TypeError:
          print("please enter amount in figures")
          return
   if amount<=0:
     print("you cannot repay with that amount")

   elif self.loan==0:
     print ("you dont have a loan at the moment")

   elif amount>self.loan:
     print("your loan is {}, please enter an amount that is less or equal". format (self.loan))

   else:
     self.loan-=amount
     print("you have paid your loan with {}.your loan balance is {}".format(amount,self.loan))
     


acc2=BankAccount("Michelle", +254720604378, "Nthumo")
acc1=BankAccount("Charl", +254789568467, "Olivia")
acc2.deposit(10)
acc1.deposit(700)
acc2.deposit(500)
acc1.deposit(60)

#acc1.withdraw(5)
#acc2.withdraw(45)
#acc2.withdraw(600)
#acc1.withdraw(750)