
def diamond(a): # Defining a function  called "diamond", where "a" represents any capital letter from A to Z.
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Here "alphabet" is a string containing all letters from the alphabet
    alph=alphabet.split(a) # Spliting the string "alphabet" at letter "a", this gives an array with two elements, 
    # where the first element of the array is a string from letter A to and inlcuding a letter before "a",
    #  and second element is a string of letters from a to "Z".
    alph_sub=alph[0]+a # Here I am taking the first element of array "alph", then I am concatenating this with letter "a".
    h=len(alph_sub) # Here "h" is the length of the string alph_sub.
    if h==1: # If the input letter of function "diamond" is "A", then h=1, but if h=1 then the for loop from line 21 to line 28
        # would have k going from -1 to 0 and value of k increases by 1 each time
        # i.e. line 23 becomes "for k in range(-1,0,-1)" which gives an error in python.
        # Also h can only be equal to 1 if alph_sub="A".
        print("A") # printing "A" 
        print("A")
    else:
        for j in range(h): # In line 16, j will take integer value from 0 to and including h-1
           if j==0: 
              z=(" ")*(h-j)+ alph_sub[j] # Here the "+" sign concatenates the characters (" ")*(h-j) and alph_sub[j] together
              #i.e if t= "A" +"B" the print(t) gives output "AB" in the terminal.
              print(z) # Here printing letter A once, and alph_sub[j]="A" only if "j=0".
           else: # Line 22 and line 23 will execute only when j has value from 1 to h-1 (assuming h>1).
              m=((" ")*(h-j)) + alph_sub[j]+ (" ")*j +(" ")*(j-1) + alph_sub[j]
              print(m)

        # Consider a="E", if h>1, then the for loop from line 16 to line 23, would give an output:
        #    A
        #   B B
        #  C   C
        # D     D
        #E       E
        #
        for k in range(h-2,-1,-1):
           if k==0:  
              z=(" ")*(h-k)+ alph_sub[k]
              print(z) ## Here since alph_sub[k]="A" if and only if k=0, then lines 33 to line 34 will give output of "A"
           else: # Lines 38 and 39 will execute only when k has value from 1 to h-1 (assuming h>1)
              m=(" ")*(h-k) + alph_sub[k]+ ((" ")*(k)) +(" ")*(k-1) + alph_sub[k]
              print(m)
        # Again consider a="E", if h>1, then the for loop from line 32 to line 38 , would give an output:
        # D     D
        #  C   C
        #   B B
        #    A

# In line 47, I am going print the output of the function diamond where the input is letter "E"
print(diamond("E"))


# below comments are some extra information on how I got to the solution:

# Consider the diamond below:

#    A
#   B B
#  C   C
# D     D
#E       E
# D     D
#  C   C
#   B B
#    A
#
# Now consider the letters that appear first from line 33 of this code to line 37, i.e. consider the letters with speech marks shown below:
# 
# 
#   "A"
#  "B" B
# "C"   C
#"D"     D
#"E"       E
# D     D
#  C   C
#   B B
#    A

#  suppose that "a"=E, then the length of string "alph_sub" is 5, and in line 53 of this code,
#  I see that there are 4 (which is length of alph_sub minus 1) spaces then there is letter A, in line 
# 54 of this code first there is 3 spaces, then there is letter "B" , in line 55 of this code, there is 2 spaces then there is letter "C", 
# in line 56 there is 1 space then there is letter "D", and in line 57 there is 0 space thne there is "E". So to get from line 53 to line 57,
#  we keep subtracting 1 from length of alph_sub.
# Now to get the letters in speech marks shown below:

#    A
#   B "B"
#  C   "C"
# D     "D"
#E       "E"
# D     D
#  C   C
#   B B
#    A
# 
# In line 84, I see that between the 1st and 2nd letter, there is 1 space (where 1=len(alph_sub)-4) plus 0 space (where 0 is the index of A in alph_sub).
# In line 85, between the 1st and 2nd letter, there are 2 spaces (where 2=len(alpha_sub)-3) plus 1 space (where 1 is the index of "B" in alpha_sub).
# In line 86, between the 1st and 2nd letter there are 3 spaces (where 3=len(alpha_sub)-2) plus 2 spaces (where 2 is the index of C in alph_sub)
# In line 87, between the 1st and 2nd letter there are 4 spaces (where 4=len(alpha_sub)-1) plus 3 spaces (where 3 is the index of D in alph_sub)
# Hence if we execute the following we will get line 53 to 57, 
# a=((" ")*4)+"A"
# b=((" ")*3)+"B"+((" ")*1)+ ((" ")*0)+"B"
# c=((" ")*2)+"C"+((" ")*2)+ ((" ")*1)+"C"
# d=((" ")*1)+"D"+((" ")*3)+ ((" ")*2)+"D"
# e=((" ")*0)+"E"+((" ")*4)+ ((" ")*3)+"E"
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# To check this, you can try running the code from line 98 to line 107 on a seperate python file.
# The code from line 98 to line 107 is where the for loop from line 16 to line 23 comes from.
#