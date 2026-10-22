


def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    if number != 0:
        print(number) 
        countdown(number-1) 
    else:
        print(0)
countdown(10)
# check if correct output is produced
countdown(30)    # 30 ... 0 (Note: each number is printed in a separate line)
countdown(5)     # 5 ... 0  (Note: each number in printed in a separate line)


# Once you have completed, your next task is to write an equivalent function that
# uses a loop.
