#this file focus on the lamdba func`
map(lambda x: x*x, [1, 2, 3, 4])
#lambda is a anor func as:

def f(x):
    return x*x

f1 = lambda x: x*x

print f1(3)
print f(3)

#Given a dic here
dic = {'Tim':10.5, 'Jim':20.3, 'Bob': 13.3}
#what if we want to sort the dic items by its values?

print sorted(dic.items(), key = lambda d:d[1])

