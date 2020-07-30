#class methods 
#Michelle  Nthumo
class BankAccount:
  bank="KCB"
  
  def __init__(self,first_name,last_name,phone_number):
    self.first_name=first_name
    self.last_name=last_name
    self.phone_number=phone_number
    self.balance = 0
    self.deposits = []
    self.withdrawals=[]
    self.loan = 0
    self.loan_repayments =[]
    
    
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
        time=(datetime.now)()
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

def get_formatted_time(self,time):
      return time.strftime("%A, %d  /%B, /%Y, %H:%M:%P")
     
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
        time=datetimw.now()
        repayment ={
          "time":time,
          "amount":amount
        }
        self.loan_repayments.append(repayment)
       print("you have paid your loan with {}.your loan balance is {}".format(amount,self.loan))
     
def loan_repayment_statement(self):
      for repayment in self.loan_repayments:
            time = repayment['time']
            amount = repayment ['time']
            formatted_time= self.get_formatted_time(time)
            statement = ("you repaid {} on {}".format(amount,formatted_time)
            print(statement)



#INHERITANCE
class BankAccount(Account):
      def __init__(self, first_name, last_name, phone_number, bank):
            self.bank = bank
            super().__init__(first_name, last_name, phone_number)

class MobileMoneyAccount(Account):
      def __init__(self, first_name, last_name, phone_number, service_provider):
            self.service_provider = service_provider
            self.airtime = []
            super().__init__(first_name, last_name, phone_number)

      def buy_airtime(self, amount):
            try:
              amount + 1
            except TypeError:
                print("please enter the amount in figures")
                return
            if amount >self.balance:
                  print("You don't have enough balance. Your balance is {}".format(self.balance))
            else:
                  self.balance -= amount
                  time = datetime.now()
                  airtime = {
                    "time": time,
                    "airtime": amount
                  }
                  self.airtime.append(airtime)
                  print("You have bought airtime worth {} on {}".format(amount, self.get_formatted_time(time)))

            

            
      def Paybill(self, amount):
            try:
              amount + 1
            except TypeError:
                print("please enter the amount in figures")
                return
            if amount >self.balance:
                  print("You don't have enough balance. Your balance is {}".format(self.balance))
            else:
                  self.balance -= amount
                  time = datetime.now()
                  paybill = {
                    "time": time,
                    "airtime": amount
                  }
                  self.paybill.append(paybill)
                  print("You have paid your bill worth {} on {}".format(amount, self.get_formatted_time(time)))
    
      def send_money(self, amount):
            try:
              amount + 1
            except TypeError:
                print("please enter the amount in figures")
                return
            if amount >self.balance:
                  print("You don't have enough balance. Your balance is {}".format(self.balance))
            else:
                  self.balance -= amount
                  time = datetime.now()
                  send_money = {
                    "time": time,
                    "send_money": amount
                  }
                  self.send_money.append(send_money)
                  print("You have send money worth {} on {}".format(amount, self.getdef buy_airtime(self, amount):
      
      def receive_money(self, amount):
            try:
              amount + 1
            except TypeError:
                print("please enter the amount in figures")
                return
            if amount >self.balance:
                  print("You don't have enough balance. Your balance is {}".format(self.balance))
            else:
                  self.balance -= amount
                  time = datetime.now()
                  airtime = {
                    "time": time,
                    "receive_money": amount
                  }
                  self.receive_money.append(airtime)
                  print("You have received money worth {} on {}".format(amount, self.get_formatted_time(time)))

      

      
      
            



