#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail. The
#program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.

name = input("Enter file:")
handle = open(name)
my_dict=dict()
my_name=None
for line in handle:
    my_line=line.split()
    if not line.startswith('From'):
        continue
    else :
        my_name=my_line[1]
        #print(my_name)
        my_dict[my_name]=my_dict.get(my_name,0) + 1
#print(my_dict)
my_key=None
my_value=None
for word,count in my_dict.items():
    if my_key is None or count>my_value:
        my_key=word
        my_value=count
print(my_key,int((my_value/2)))
