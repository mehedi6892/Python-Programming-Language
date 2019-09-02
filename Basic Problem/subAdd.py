terminate_program =False
while not terminate_program:
     n1=input("Please enter a number: ")
     n1=int(n1)
     n2 = input("Please enter another number: ")
     n2=int(n1)

     while True:
          operation = input("Please input add/sub or quit to wxit: ")

          if operation == "quit":
               terminate_program= True
               break
          if operation not in ["add", "sub"]:
               print("Unknown Operation")
               continue

          if operation == "add":
               print("Result is", n1+n2)
               break
          if operation=="sub":
               print("result is", n1-n2 )
               break
