L=[70,80,20,30,50]
# L.sort()
# print(sorted(L))
print(L.sort(reverse=True,key = lambda x:x*x))
print(L)
L1=['Pratik','Arun','Wani']
L1.sort(reverse=False,key=lambda x:len(x))
print(L1)
