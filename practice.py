"""a=['6654A5Z6D1485','6654A5Z6d486','6654A5Z61D487','6654A5Z6D1488','6654A5Z6D14489','6654A5Z6D1490','6654A5Z6D149871']
for i in a:
    print(i)
    value=i[4:9:2] #AZD location validation
    print(value)
    if value=='AZD': #value validation
        print('pass for value validation')
    else:
        print('fail for value validation')
    if len(i)==13: #length validation
        print('pass for length validdation')
    else:
        print('fail for length validdation')"""

a=81574451
b=48546441
c=24644751
d=98756561
e=14614613
f=48546433
g=94973131
if (a>b) and (a>c) and (a>d) and (a>e) and (a>f) and (a>g):
    greatest=a
elif (b>a) and (b>c) and (b>d) and (b>e) and (b>f) and (b>g):
    greatest=b
elif (c>a) and (c>b) and (c>d) and (c>e) and (c>f) and (c>g):
    greatest=c
elif (d>a) and (d>c) and (d>b) and (d>e) and (d>f) and (d>g):
    greatest=d
elif (e>a) and (e>c) and (e>d) and (e>b) and (e>f) and (e>g):
    greatest=e
elif (f>a) and (f>c) and (f>d) and (f>e) and (f>b) and (f>g):
    greatest=f
else:
    greatest=g
print(greatest)
