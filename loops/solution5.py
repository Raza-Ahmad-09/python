inp_string = input("Enter string : ")

for rep in inp_string:
   # print(rep)
   if inp_string.count(rep) == 1:
      print("Char is: ", rep)
      break 
      # if we need all non-repeating characters then don't use break