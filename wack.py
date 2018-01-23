from difflib import get_close_matches
from random import shuffle,random
from time import sleep

def extractor(s,fh,spaces):
    shuffle(s)
    text=s[0]
    for i in range(1,len(s)):
        if spaces and random()>0.7:
            text+=' '
        text+=s[i]
    print(text)
    for word in text.split():
        #print(word)
        suggestions=get_close_matches(word.lower(),fh)
        if len(suggestions)>1:
            print(str(word)+" - "+str(suggestions))
    '''try:
        c=input("Try More(0/1): ")
        if int(c)==1:
            extractor(s,fh)
    except:
        pass
    '''

def main():
    s=input("Enter inital of words: ").split()
    fh=open("20k.txt")
    spaces=input("Consider spaces(0/1):")
    print("\nHere are some word combinations with possible word suggestions:\n(Press CTRL+C to exit)")
    try:
        while True:
            extractor(s,fh,int(spaces))
            sleep(1)
    except:
        pass

if __name__ == '__main__':
    main()
