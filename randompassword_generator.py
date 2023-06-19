import random
n=int(input("Enter Password Length: "))
x=int(input("Enter how many random passwords you want: "))
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="{}?@!$%^&*()_+*"
all=lower+upper+numbers+symbols
length=n
for i in range(x):
    password="".join(random.sample(all,length))
    print(password)