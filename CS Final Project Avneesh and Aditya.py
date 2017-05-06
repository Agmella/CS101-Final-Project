from Tkinter import *
from collections import Counter
import re
wordfreq = {}
master = Tk()

e1 = Text(master,height=50,width=50,wrap=WORD) #This is for the size of the text box
e2 = Text(master,height=50,width=50)

def find():
    c = Counter()
    wordfreq={}
    e2.delete("1.0",END) #This part erases the document everytime it opens
    string = open('https://rawgit.com/Agmella/CS101-Final-Project/master/PrideandPrejudice.txt').read()
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)      #this part removes all special characters in the text
    open('https://rawgit.com/Agmella/CS101-Final-Project/master/PrideandPrejudice.txt', 'w').write(new_str)   
    with open('https://rawgit.com/Agmella/CS101-Final-Project/master/PrideandPrejudice.txt') as f:
        for line in f:
            for word in re.findall(r'[\w]+', line.lower()):    #http://stackoverflow.com/questions/21852066/counting-word-frequency-and-making-a-dictionary-from-it
                c += Counter(word)
                wordfreq[word] = wordfreq.setdefault(word, 0) + 1  #This part heps find the word and letter frequency in the text
    e2.insert("1.0",wordfreq) #This part puts the words and letters frequency in the text box
    e4.insert("1.0",c)
def analyse():
    open('https://rawgit.com/Agmella/CS101-Final-Project/master/PrideandPrejudice.txt',"w").close()
    text = e1.get("1.0", "end-1c")
    with open("https://rawgit.com/Agmella/CS101-Final-Project/master/PrideandPrejudice.txt","a") as f:
        f.write(text.encode('utf-8'))
    find()

Label(master, text="Enter Text to be Analysed").grid(row=0,column=0)  #This entire part is the GUI using Tkinter
Label(master, text="Word Frequency").grid(row=0,column=5)
Label(master, text="Letter Frequency").grid(row=0,column=10)
e1 = Text(master,height=50,width=30,wrap=WORD)  
e2 = Text(master,height=50,width=30)
e4 = Text(master,height=50,width=30)
e3 = Button(text="ANALYSE",command=analyse) 
e3.grid(row=0,column=3)
e1.grid(row=1, column=0)
e2.grid(row=1, column=5)
e4.grid(row=1, column=10)
mainloop()


