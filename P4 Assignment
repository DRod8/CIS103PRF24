name = input('Enter Your Name: ')

#Cannot be blank -              Message: Name cannot be blank *
#Must be at least 3 characters -Message: Name to short *
#Must be alphabetic -           Message: Name must be alphabetic *

lenstr = len(name)

if (lenstr ==0):
    print('Name cannot be blank')

else:
    if name.isspace():
        print('Name cannot be blank')
    else:
        if len(name) < 3:
            print('Name too short')
       
        else:
            if name.isalpha():
                print('Valid')
            else:
                print('Name must be alphabetic')
                    
accountnumber = input('Enter Account Number: ')

#Cannot be blank -              Message: Account number cannot be blank *
#Must be numeric (digits) -     Message: Account number must be numeric *
#Must be 9 digits long -        Message: Account number must be 9 digits

lenstr = len(accountnumber)

if (lenstr == 0):
    print('Account Number cannot be blank')

else:
    if accountnumber.isspace():
        print('Name cannot be blank')

#switch isnumeric and ! = 9
        
    else:
        if len(accountnumber) != 9:
            print('Account Number must be 9 Digits')     
        else:
            if accountnumber.isnumeric():
                print('Valid')
            else:
                print('Account must be Numeric')

paymentamount = input('Enter Payment Amount: ')

if len(paymentamount) == 0:
    print('Payment Amount cannot be blank')
else:
    if paymentamount.isspace():
        print('Payment Amount cannot be blank')
    else:      
   
        amt = float(paymentamount)
        if amt == 0:
            print('Payment Amount cannot be zero')
        else:
            if amt < 0:
                print('Payment Amount cannot be negative')
            else:
                print('Valid')

