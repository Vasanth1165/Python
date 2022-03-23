def is_happy(n): 
    while n!=1 and n!=4:
        ss = 0
        while n:
            r = n%10
            ss += r*r
            n = n//10

        n = ss
    if(n==1):
        return True
    else:
        return False
    

while(True):
    x = input('Check or Range?:')
   
    if(x == 'Check'):
        num = int(input('Enter a number to check:')) 
        if(is_happy(num)): 
            print('Happy')
        else:
            print('Unhappy')
    elif(x == 'Range'):
        a, b = map(int, input('Enter two numbers:').split())
        choice = input('Happy or Unhappy:')
        if(choice == 'Happy'):
            for i in range(a,b+1):
                if(is_happy(i)):
                    print(i,end = ' ')
        else:
            for i in range(a,b+1):
                if(not is_happy(i)):
                    print(i,end=' ')
    else:
        print('Invalid Input')
        break
        
