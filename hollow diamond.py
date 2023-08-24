
width = int (input("  what do you want the width of the hollow diamond to be?  "))


initial =int (width/2)


j=initial
k=1
start = j
while j>0:
    if j==start:
        print(j*" "+"#")
    else:
         
        print(j*" "+"#"+k*" "+"#")
        k=k+2
    j=j-1

m = 0










#bottom half
k=2*initial-1
while m<=initial:
    if m==initial:
        print(m*" "+"#")
    else:
         
        print(m*" "+"#"+k*" "+"#")
        k=k-2
    m=m+1

 




