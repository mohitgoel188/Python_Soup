def bsearch(num,x,beg,last,order):
        if beg<last:
                mid=(beg+last)/2
                if order==0:
                        if num[mid]>x:
                                return bsearch(num,x,beg,mid-1,0)
                        elif num[mid]<x:
                                return bsearch(num,x,mid+1,last,0)
                        else:
                                return mid
                else:
                        if num[mid]<x:
                                return bsearch(num,x,beg,mid-1,1)
                        elif num[mid]>x:
                                return bsearch(num,x,mid+1,last,1)
                        else:
                                return mid
        elif num[beg]==x:
                return beg
        return -1
def bitonicS(num,x,beg,last):
        if beg<last:
                mid=(beg+last)/2
                if num[mid]>num[mid-1]:
                        index=bsearch(num,x,beg,mid,0)
                        if index!=-1:
                                return index
                        else:
                                return bitonicS(num,x,mid+1,last)
                elif num[mid]<num[mid-1]:
                        index=bsearch(num,x,mid-1,last,1)
                        if index!=-1:
                                return index
                        else:
                                return bitonicS(num,x,beg,mid-2)
                else:
                        return mid
        elif num[beg]==x:
                return beg
        return -1

def main():
        num=[]
        l=input("How Many Numbers?")
        print "Input Numbers: (For bitonic array)"
        for i in range(l):
                N=input()
                num.append(N)
        while True:
                x=input("No. need to be find: ")
                index=bitonicS(num,x,0,l-1)
                print "Index: ",index
                choice=input("More?(0/1)")
                if choice==0:
                        break
main()        
