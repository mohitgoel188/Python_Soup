import datetime
import glob2
def merge(filenames,newfile):
    r'''Function to merge files defined in filenames and return new file name as given by user 
       if filename is missing all files of directory is taken
       if filename is missing timestamp is taken as filename'''
    if len(newfile)<1:
        newfile=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    if len(filenames)<1:
        filenames=glob2.glob('*.txt')
    nf=open(newfile,'w')
    for filename in filenames:
        fh=open(filename,'r')
        content=fh.read()
        nf.write(content+'\n')
        fh.close()
    nf.close()
    return newfile

def main():
    print("Enter file names:(Enter done to end ) ")
    filenames=[]
    while True:
        name=input()
        if name=="done":
            break
        filenames.append(input())
    newfilename=input("Enter new file name: ")
    newfilename=merge(filenames,newfilename)
    fh=open(newfilename)
    content=fh.read()
    print(content)

if __name__ == '__main__':
    main()