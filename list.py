# Take input of list from user and combine the two lists also add the two lists 

def take_input():
      a=[]  # Declaration of 1st list
      n=int(input("Enter the no. of elements for 1st list"))
      for i in range(n):
          num=int(input("Enter number :  "))
          a.append(num)

      b=[]  # Declaration of 2nd list 
      n=int(input("Enter the no. of elements for 2nd list"))
      for i in range(n):
         num=int(input("Enter number : "))
         b.append(num)

      print("List 1: " ,a)
      print("List 2: ", b)
 
      c=(a+b)
      print("Concatenation of listes : " ,c)

      d=[]
      for i in range(0, len(a)):
            d.append(a[i] + b[i])  
      print("The sum of two lists : ",d)

take_input()
