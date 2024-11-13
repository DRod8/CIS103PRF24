def main():

    roNum = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 
        9: 'IX', 10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX', 21: 'XXI', 
        22: 'XXII', 23: 'XXIII', 24: 'XXIV'}

    print('----Roman Numerals----')
    print(roNum)
    
    inputNum = int(input("Enter a number: "))
    
    while inputNum > 0:
        if inputNum in roNum:
            outNum=roNum[inputNum]
            print(inputNum, 'Roman Number is: ', outNum)
        
        else:
            #inputNum in romanNumerals:
            print(inputNum, 'Number is not in Dictionary') 
            addtoDict = input('Add to Dictionay?: y/n: ')
            
           
            if addtoDict == 'y':
                addNum=input('Add Number and Roman Numeral to Dictionary (Roman number must be Alphabetic): ')
                roNum[inputNum]=addNum
                print('-----------------')
            
            #print(romanNumerals [inputNum]) 
        inputNum = int(input("Enter another number: "))
            #print("Roman numeral must be ALPHABETIC")

    print("Roman Numerics Dictionary")
    print(roNum)

main()
