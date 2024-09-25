answer='y'
calorieburn=4.9              

while(answer=='y')or(answer=='Y'):
    
    print('-Calorie Calculation-')
    print('---------------------')
    runtime=5
    run=(input('Enter Run in Minutes: '))

    if(len(run)==0 or run.isspace() or float(run)<5):
        print('ERROR: Time must be greater than 5')

    else:
        run=float(run)

        while(runtime<run+1):

            caloriesburn= runtime * calorieburn
            print('Minutes:' ,runtime, 'Calories Burned: ', caloriesburn, 'Calories')
            runtime=runtime+5

    answer=input('Again y/n->')

print('**Done**')
