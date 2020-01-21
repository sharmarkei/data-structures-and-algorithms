import re

def repeated_words(str): 
  
    # Got the regex for puncation and whitespace from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    str = re.sub(r'[^\w\s]','',str)
    words = str.lower().split()
    str2 = [] 
  
    for i in words:  
        if i not in str2: 
            str2.append(i) 
            # print(str2)
        else:
            print(i)
            return i 
            
    return None
def main(): 
    str ='It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only'
    repeated_words(str)                     
  
if __name__=="__main__": 
    main()             # call main function 