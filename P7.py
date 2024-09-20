def miles_to_kilometers():
    miles = float(input('Enter Miles: '))
    kilometers = miles * 1.609344
    print('Kilometers is:', kilometers)

def fahrenheit_to_celsius():
    fahrenheit = float(input('Enter Fahrenheit: '))
    celsius = (fahrenheit-32) * 5/9
    print('Celsius is: ',celsius)

def pounds_to_kilograms():
    pounds = float(input('Enter Pounds: '))
    kilograms = pounds * 0.45659237  
    print('Kilogram is: ',kilograms)

def main():
    miles_to_kilometers()
    fahrenheit_to_celsius()
    pounds_to_kilograms()
  
    return
main()
