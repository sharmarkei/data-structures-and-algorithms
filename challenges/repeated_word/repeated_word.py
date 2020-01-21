import re

def repeated_words(str): 
  
    # Got the regex for puncation and whitespace from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    str = re.sub(r'[^\w\s]','',str)
    str = str.split()
    str2 = [] 
  
    for i in str:
        
        if i not in str2: 
            str2.append(i)  
              
    for i in range(len(str2)): 
        print(str2[0])

        return str2[0]

def main(): 
    str ='Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper.'
    repeated_words(str)                     
  
if __name__=="__main__": 
    main()             # call main function 