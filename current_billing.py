#for finding out the current bill of everyday and month
import numpy as np

n = int(input("Enter the number of Electrical equipments : "))

print("Enter the number of kilowatts according to Elec. eqp. : ")
p = list(map(int,input("Enter : ").split()))

print("Enter the number of usage time according to watts :")
t = list(map(int,input("Enter : ").split()))
m = int(input("Enter the days of the month : "))
T = [x*m for x in t]


unit = float(input("Enter the amount per unit : "))
money = 0

for i in range(n):
    money = ((np.multiply(p,T))/1000)*unit
    permonth= sum(money)
    perday = sum(money/m)

print("Cost per month : ",round(permonth,4))
print("Cost per day : ",round(perday,4))

    

