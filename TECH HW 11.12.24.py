#1
class Password:
    def valid(text):
        if text[0].isupper():
            upper=0
            lower=0
            digit=0
            spl=0
            length=len(text)
            for i in text:
                if i.isupper():
                     upper+=1
                elif i.islower():
                    lower+=1
                elif i.isdigit():
                    digit=1
                else:
                    spl+=1
            if upper>=1 and lower>=1 and digit>=1 and spl>=1 and length>=8:
                print("Your password is Valid")
            else:
                print("Your password is Invalid")
        else:
            print("The First Letter Should be Capital")
txt=input("Enter the password:")
Password.valid(txt)
#2
class TextProcess:
    def __init__(self,text):
        self.text=text
        self.sentencelst=[]
    def split_sentences(self):
        punctuation=['.','?','!']
        sentence=''
        for char in self.text:
            sentence+=char
            if char in punctuation:
                self.sentencelst.append(sentence.strip())
                sentence=''
        if sentence.strip():
            self.sentencelst.append(sentence.strip())
        for i in self.sentencelst:
            print(i)
    def process_sentence(self):
        for sentence in self.sentencelst:
            word_count=len(sentence.split())
            print("Sentence:",sentence,"Word Count:",word_count)
txt=input()
p=TextProcess(txt)
p.split_sentences()
p.process_sentence()
            
