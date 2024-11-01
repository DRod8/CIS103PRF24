def fact(n):
    print(n)
    if n == 1:
        return n
    else:
        return n + fact(n-1)

def main():
    ans= 'y'
    while ans.upper()=="Y":
        print('--Sum Up Numbers--')
        numb=input('Enter a Number -> ')
        if numb == '':
            print("Input cannot be blank")
  
            
        try:
            numb=int(numb)
            if numb <0:
                print("Input Cannot be Negative")
                
            a = fact(numb)
            print(numb, ' factorial is -> ',a)
        
        except:
            print("Input must be a Number")
        ans=input('Again y/n :')
        print('--------------')

main()
