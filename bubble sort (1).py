class sort:
    def bubble_sort(self):
        lst=[]
        length=int(input("Enter length of the list"))
        for i in range (length):
            num=int(input("enter element"))
            lst.append(num)
        while length>0:
            for x in range (length-1):
                if lst[x]> lst[x+1]:
                    temp=lst[x]
                    lst[x]=lst[x+1]
                    lst[x+1]=temp
            length=length-1
        print(lst)
s1=sort()
s1.bubble_sort()
