def diamond(a):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    alph=alphabet.split(a)
    alph_sub=alph[0]+a
    h=len(alph_sub) 
    if h==1: 
        print("A")  
        print("A")
    else:
        for j in range(h): 
           if j==0: 
              z=(" ")*(h-j)+ alph_sub[j] 
              print(z) 
           else: 
              m=((" ")*(h-j)) + alph_sub[j]+ (" ")*j +(" ")*(j-1) + alph_sub[j]
              print(m)

        for k in range(h-2,-1,-1):
           if k==0:  
              z=(" ")*(h-k)+ alph_sub[k]
              print(z) 
           else: 
              m=(" ")*(h-k) + alph_sub[k]+ ((" ")*(k)) +(" ")*(k-1) + alph_sub[k]
              print(m)

print(diamond("E"))

