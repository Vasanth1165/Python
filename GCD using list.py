a,b=map(int,input().split())
a_div=[i for i in range(1,a//2+1) if a%i==0]
print(a_div)
b_div=[i for i in range(1,b//2+1) if b%i==0]
print(b_div)
c_div=list(set(a_div).intersection(set(b_div)))
print(c_div)
print("GCD of",a,"and",b,"is",max(c_div))