def area_rect(l,b):
	a=l*b
	p=2*(l+b)
	print('area is',a,'perimeter is',p)
l,b=map(int,input().split())
area_rect(l,b)