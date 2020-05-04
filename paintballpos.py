# Matthias Pupillo
# Final Project

from datetime import date

class Item:
    #Items here
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def itemName(self):
        return self.name
    
    def itemPrice(self):
        return self.price
    
    def itemStock(self):
        return self.stock
    
    def setStock(self, stock):
        self.stock = stock

class Inventory:
    def __init__(self, catalog):
        self.catalog = []
    
    def getInventory(self):
        return self.catalog
    
    def setInventory(self, catalog):
        self.catalog = catalog
        
    def addItemtoInventory(self, item):
        self.catalog.append(item)
    
    def updateItemfromInventory(self):
        for obj in self.catalog: 
            obj.setStock(9)
        
class Receipt:
    def __init__(self):
        self.amount = 0
        self.date = ""
        self.customer = ""
    
    def setReceipt(self,amount, date, customer):
        self.amount = amount
        self.date = date
        self.customer = customer
    
    def getReceipt(self):
        return self.amount, self.date, self.customer

class Transaction:
    def __init__(self, amount, date, customer):
        self.amount =amount
        self.date = date
        self.customer = customer
    
    def printtransction(self):
        print("Amount {0}, Date {1}, Customer {2}".format(self.amount,self.date,self.customer))
    
class CreditTransaction(Transaction):
    def __init__(self,  amount, date, customer, ccn, ccv ):
          self.amount =amount
          self.date = date
          self.customer = customer
          self.ccn = ccn
          self.ccv = ccv
     
    def getCCN(self):
        return self.ccn
    
    def lastfour(self,ccn):
        string = str(ccn) 
        lastfour = string[-4:]
        self.ccn = "XXXXXXXXXXXX" + lastfour
    
    def printcredit(self):
        print("CCN: {0} CCV {1}".format(self.ccn, self.ccv))   
        
class CheckTransaction(Transaction):
    def __init__(self,  amount, date, customer, checknumber, routing ):
     self.amount =amount
     self.date = date
     self.customer = customer
     self.routing = routing
     self.checknumber = checknumber
     
    def printcheck(self):
        print("Check Number: {0} Routing Number {1}".format(self.checknumber, self.routing))


def createCatalog():
    catalog = []
    
    return catalog

def calcTotal(items):
    total = 0
    for obj in items: 
        total += obj.price
    return total

def paymentType(id):
    if(id == 1):
        
        return 1
    elif(id == 2):
       
        return 2
    elif(id == 3):
        
        return 3
    else:
        
        return 4

def main():
    transactionStatus = 0
    today = date.today()

    receipt = Receipt()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")

    print("Welcome to The Paintball Store");
    
    print("Catalog of Items")
    
    inventory = Inventory(createCatalog())
    inventory.addItemtoInventory( Item("Dye S3+",1200.00, 10))
    inventory.addItemtoInventory( Item("Dye i5 Mask",200.00, 10))
    inventory.addItemtoInventory( Item("Hopper",100.00, 10))
    inventory.addItemtoInventory( Item("Air Tank",159.00, 10))
    
    for obj in inventory.getInventory(): 
        print( obj.name, obj.price, sep =' ' )
    
    print("Items added to cart")
    
    #Could be improved to let the user choose Items
    print("Checkout")

    
    print("Total: " + '${:,.2f}'.format(calcTotal(inventory.getInventory())))
    input("Press Enter Continue")
    print("Payment Method")
    method = input("Credit (1), Cash (2) or Check (3):  ")
    customer = str(input("Customer Name [Awesome Customer]")  or "Awesome Customer")
    try:
        val = int(method)
        paymentType(val)
        if(paymentType(val) == 1):
            print("Payment Method: Credit")
            ccnumber = int(input("Credit Card Number [ 1234567823232345] ") or  1234567823232345)
            ccccv = int(input("CVV [321] ") or 321 )
            credit = CreditTransaction(calcTotal(inventory.getInventory()), d1, customer , ccnumber, ccccv)
            credit.lastfour(credit.getCCN())
            credit.printcredit()
            credit.printtransction()
            receipt.setReceipt(calcTotal(inventory.getInventory()), d1, customer)
            transactionStatus = 1
        elif(paymentType(val) == 2):
            print("Payment Method: Cash")
            transaction = Transaction(calcTotal(inventory.getInventory()), d1, customer)
            receipt.setReceipt(calcTotal(inventory.getInventory()), d1, customer)
            transactionStatus = 1
        elif(paymentType(val) == 3):
            print("Payment Method: Check")
            accountnumber = int(input("Credit Card Number [ 4212] ") or  4212)
            routingnumber = int(input("Routing Number [810022301] ") or 810022301 )
            check = CheckTransaction(calcTotal(createCatalog()), d1, customer , accountnumber, routingnumber)
            check.printcheck()
            check.printtransction()
            receipt.setReceipt(calcTotal(inventory.getInventory()), d1, customer)
            transactionStatus = 1
        else:
            print("Payment Method Not Accepted")
            transactionStatus = 0
    except ValueError:
        print("Please enter only the number of the checkout method")
        transactionStatus = 0
            
    
    
    if(transactionStatus == 1):
    
        print("Payment Successful")
        
        inventory.updateItemfromInventory()
        print("Inventory Updated")
       
        rec = receipt.getReceipt()
        print("###########################")
        print("Customer: " + rec[2])
        print("Data: " + rec[1])
        print("Amount: " + '${:,.2f}'.format(rec[0]))
        print("###########################")
        print("Thank you for shopping at the Paintball Store")
    
    else:
        print("Please Come again when you are ready to purchse")
    


main()
        
    
