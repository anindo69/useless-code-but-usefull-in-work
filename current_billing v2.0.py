#Without using numpy

n = int(input("Enter the number of Electrical equipments : "))

print("Enter the number of kilowatts according to Elec. eqp. : ")
p = list(map(int,input("Enter : ").split()))

print("Enter the number of usage time according to watts :")
t = list(map(int,input("Enter : ").split()))
m = int(input("Enter the days of the month : "))
T = [x*m for x in t]


unit = float(input("Enter the amount per unit : "))
permonth = 0
perday = 0
res_list = [p[i]*T[i] for i in range(0,len(p))]
permonth = (sum(res_list)/1000)*unit
perday = permonth/m

print("Cost per month : ",round(permonth,4))
print("Cost per day : ",round(perday,4))