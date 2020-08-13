

#改正
def sum(**kwargs):
    sum_num =0    
    for arg in kwargs.values():
        sum_num += arg 
    print (sum_num)
        
sum(a1=1, a2 = 2, a3 = 3, a4 = 4)
      


        
