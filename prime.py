b=int(input())
if(b>1):
      for n in range(2,b):
        if(b%n)==0:
              print("no")
              break
      else:
            print("yes")
else:
      print("no")
