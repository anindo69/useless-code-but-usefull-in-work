#currentrig:

m1 = int(input("please enter the price of your current motherboard : "))
mu1 = int(input("please enter the usage time of ur motherboard: "))
spm1 = 0 
if mu1 == 1:
    spm1 = m1 - 1500
    print(spm1)
if mu1 == 2:
    spm1 = m1 - 3000
    print(spm1)
if mu1 >= 3:
    spm1 = m1 - 5000
    print(spm1)

    
g1 = int(input("please enter the price of your current graphics card: "))
gu1 = int(input("please enter the graphics card usage : "))
spg1 = 0 
if gu1 == 1:
    spg1 = g1 - 1500
    print(spg1)
if gu1 == 2:
    spg1 = g1 - 3000
    print(spg1)
if gu1 >= 3:
    spg1 = g1 - 5000
    print(spg1)


p1 = int(input("please enter the price of your current processor:"))
pu1 = int(input("please enter the processor usage : "))
spp1 = 0 
if pu1 == 1:
    spp1 = p1 - 1500
    print(spp1)
if pu1 == 2:
    spp1 = p1 - 3000
    print(spp1)
if pu1 >= 3:
    spp1 = p1 - 5000
    print(spp1)

s1 = spm1 + spg1 + spp1

print("total price of selling rig is : ",s1)




print("******************-------------------------***********************-------------------**********************---------------")




#targetrig:

m2 = int(input("please enter the price of ur wished motherboard : "))
g2 = int(input("please enter the price of ur wished graphics card : "))
p2 = int(input("please enter the price of ur wished processor : "))

s2 = m2 + g2 + p2 

print("total price of ur wished pc is : ",s2)

print("******************--------------------------************************---------------------******************----------------")

#finalstandinganswer:

k = s1 - s2

if (k>0):
    print("the sells man will give u :",k)
if(k<0):
    print("u have to give the sells man : ",abs(k))
if(k==0):
    print("no one lose")





    

    










  