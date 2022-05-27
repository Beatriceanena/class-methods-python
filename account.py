class Account:
    def _init_(self,account_name,account_number,current_balance, account_type):
         self.account_name=account_name
         self.account_number=account_number
         self.current_balance=current_balance
         self.account_type=account_type

    def deposit(self,amount):
        self.current_balance+=amount
        return f"hello {self.account_name} your new balance is{self.current_balance}"

    def withdraw(self,amount):
        self.current_balance-=amount
        return  f"Hello {self.account_name} your new balnce is{self.current_balance} "     


