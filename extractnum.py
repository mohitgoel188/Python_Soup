import re
def num_extractor(filehandle):
    num=[]
    for line in filehandle:
        nlist=re.findall("[0-9]+[0-9.]*",line)
        if len(nlist)>0:
            for nstring in nlist:
                num.append(float(nstring))
    return num
def main():
    filename=input("Enter File Name:")
    fh=open(filename)
    print(int(sum(num_extractor(fh))))

if __name__ == '__main__':
    main()