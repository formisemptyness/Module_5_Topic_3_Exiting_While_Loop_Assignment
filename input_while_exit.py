'''
Program: input_while_exit.py
Author: Joshua M. McGinley
Last date modified: 09/28/2022


Recall your input_while.py, make a copy called input_while_exit.py.
What if the user typed bad input because they wanted to quit the entire program? The algorithm as written does not
account for that.
You could add code to exit (aka break out of) the inner while if the user input a sentinel flag indicating they no
longer have input. Implement this option by adding the appropriate exit statement to the inner while loop.
Run the code.
Notice that the code does not exit the outer while loop. There are a few ways to fix the code so it will exit this
loop as well. Fix the code.
Add doctring to the top of your file, add comments at the bottom with your tests and observed output after a few test
 runs of your code.
Submit your input_while_exit.py.

Additional Note: Said another way, we are  essentially using what we have learned above and modifying out old code
to use a 'break' statement to exit the loop when a sentinal value matches. This will prevent the rest of the code in
the loop from running. In our code example, this doesn't save us much time as the break has us only skip ~10 lines
of code. However, if we had thousands of lines of code/checks left in the inner loop; that break statement would save
us tons of time.

'''

the_list = []
range1 = range(1, 101)
sentinel = "continue"
yrNum = 0

sentinel = (input('Enter exit to quit: '))

while (sentinel != "exit"):
    yrNum = 0
    while (yrNum not in range1):
        try:
            yrNum = int(input('Enter an integer between 1-100 (or 666 to end): '))
        except:
            print('Bad input!')
        if yrNum == 666:
                sentinel = "exit"
                break
    print('Thank you.')
    the_list.append(yrNum)
    if yrNum == 666:
        break
    sentinel = (input('Enter exit to quit: '))

for x in range(len(the_list)):
    print(the_list[x])
