class search:
    def linear(self):
        lst=[]
        length=int(input("Enter length of the list"))
        for i in range (length):
            num=int(input("enter element"))
            lst.append(num)
        print(lst)
        find=int(input("enter number to be found"))
        n=0
        while n< length:
            if lst[n]==find:
                print("number found at index",n)
                break
            else:
         
                n=n+1
                continue
        if n>=length:
            print("Not found")
        else:
            print()

                
s1=search()
s1.linear()
