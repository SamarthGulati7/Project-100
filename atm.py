class Atm(object):
    def __init__(self,account_holder,account_type,account_no,cash_withdrawal,balance_enquiry):
        self.account_holder=account_holder
        self.account_type=account_type
        self.account_no=account_no
        self.cash_withdrawal=cash_withdrawal
        self.balance_enquiry=balance_enquiry
    def account_details(self):
        print("The account holder name is : ", self.account_holder)
        print("The type of the account is : ", self.account_type)
        print("The account type is : ", self.account_no)
        print("The account balance is : ", self.balance_enquiry)
        print("The cash withdrawn is : ", self.cash_withdrawal)
        
user1 = Atm("Ramesh","Savings","246378O179216","₹24000","₹250000")
print(user1.account_details())
