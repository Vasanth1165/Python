def is_prime(n):
    fc=0
    for i in range(1,n+1):
    	if(n%i==0):
    		fc+=1
    		print(i)
    if(fc!=2):
    	print('composite number')
    else:
    	print('prime number')
n=int(input())
is_prime(n)