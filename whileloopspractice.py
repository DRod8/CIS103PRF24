#**Gross Pay**

print('-Start-')
answer='y'
grosspay=0.0

employee_name=(input('Employee Name: '))
               
while((answer=='y')or(answer=='Y')):
    print('---------')
    payrate =float(input('Enter Pay Rate: '))
    hours =float(input('Enter Hours: '))
    grosspay = payrate * hours
    print('Gross Pay:',grosspay)

    answer=input('\nContinue y/n->')

    employee_name=(input('Employee Name: '))

print('-Done-')

#**BOUNCE**

print('-Start-')
answer='y'
               
while((answer=='y')or(answer=='Y')):
    print('Bouncing Ball')
    bouncefactor=0.5
    height=float(input('Enter Starting Height: '))
    bcount=0

    while(height>0.1):
        print('Bounced Height is at',height,'Feet')
        height=height * bouncefactor
        bcount=bcount + 1

    print('Bounced Ball',bcount,'Times')
    answer=input('Run Again y/n->')

print('-Done-')

#**BOUNCE with 0 as stop**

print('-Start-')
height=float(input('Enter Starting Height: '))
               
while height>0:
    print('Bouncing Ball')
    bouncefactor=0.5   
    bcount=0

    while(height>0.1):
        print('Bounced Height is at',height,'Feet')
        height=height * bouncefactor
        bcount=bcount + 1

    print('Bounced Ball',bcount,'Times\n')
    height=float(input('Enter Starting Height or 0 to Quit->'))

print('-Done-')
