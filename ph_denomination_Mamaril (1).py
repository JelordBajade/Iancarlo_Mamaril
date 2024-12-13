n = input("Enter your name: ")
m = eval(input("Enter amount of deposit: "))

a = m // 1000
aa = m % 1000

b = aa // 500
bb = aa % 500

c = bb // 200
cc = bb % 200

d = cc // 100
dd = cc % 100

e = dd // 50
ee = dd % 50

f = ee // 20
ff = ee % 20

g = ff // 10
gg = ff % 10

h = gg // 5
hh = gg % 5

i = hh // 1 



print ("Hello", n, "the break down of your deposit is ------->")
print (a, "-   1000")
print (b, "-   500")   
print (c, "-   200")    
print (d, "-   100")
print (e, "-   50")
print (f, "-   20")
print (g, "-   10")
print (h, "-   5")
print (i, "-   1")
