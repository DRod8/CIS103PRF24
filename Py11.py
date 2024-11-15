Import datetime

def Points_to_Grades (fpoints) :
    Grade= 'X'
    
    if (fpoints>=900) and (points<1000):
        Grade= 'A'
        print(' Grade is: ', Grades)

    else:
        if (fpoints>=800) and (points<899):
            Grade= 'B'
            print(' Grade is: ', Grades)

        else:
            if (fpoints>=700) and (points<799):
                Grade= 'C'
                print(' Grade is: ', Grades)

            else:
                if (fpoints>=600) and (points<699):
                    Grade= 'D'
                    print('' Grade is: '', Grades)

                else:
                    if (fpoints>=0) and (points<599):
                        Grade= 'F'
                        print(' Grade is: ', Grades)

    return Grades

def main()

    start_time = datetime.datetime.now()
    print('Program Started at: ', start_time)
    filenamein = 'c:/temp/points.txt'
    filenameout1 = 'c:/temp/grades.txt'
    filenameout2 = 'c:/temp/error.txt'

    rcdcnt = 0
    good_count = 0
    error_count=0

    Acount=0
    Bcount=0
