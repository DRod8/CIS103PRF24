def main():


    thetext = '''

    Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.

'''

    print(thetext)

    lentext = len(thetext)
    print('The length of the text is: ',lentext)

    thetext2 = thetext.strip()
    print('Length after is: ', len(thetext2))

    countthe = thetext.count('the')
    print("'THE' was found",countthe, "TIMES!")

    findlittle = thetext.find('little')
    if thetext in thetext2:
        print('LITTLE was found',findlittle)

    else:
        print('LITTLE NOT found')

        findtitan = thetext.find('titan')
        if thetext in thetext2:
            print('TITAN Found')

        else:
            print('TITAN NOT Found')

            appli = 'appl'
            findappl = thetext.find(appli)
            print('Position of APPL is: ', findappl)
     
    thetext2=thetext2.replace('Python','PYTHON')
    print(thetext2)

    return
main()
