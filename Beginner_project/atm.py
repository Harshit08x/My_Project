import time 

print("Please input your card")

time.sleep(3)

password = 1234

pin = int(input("Enter your pin "))

balance = 5000

if pin == password :
         
         print(""" 
          1 == Balance 
          2 == Withdraw balance 
          3== Deposit balance 
          4 == Exit """)
     
try:
            option = int(input("Please enter your choice "))

except:
            
            print("Please enter valid option ")
    
if option == 1 :

        print(f"Your current balance is {balance}")

if option == 2:

        withdrawl_amount = int(input("Please enter valid amount "))
        balance = balance - withdrawl_amount
        print(f"{withdrawl_amount} is debited from your account")
        print(f"Your current balance is {balance}")

if option == 3:

        deposit_amount = int(input("Please enter deposit amount "))
        balance = balance+deposit_amount
        print(f"{deposit_amount} is credited to your account ")
        print(f"Your updated balance is {balance}")
if option == 4:
         pass 