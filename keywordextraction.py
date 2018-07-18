
# coding: utf-8

# In[ ]:
# importing the libraries

import re
import nltk
import PyPDF2
import collections
import math


# In[ ]:
# importing the credencials 

nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


# In[ ]:

#opening the pdf file

pdf_file = open('C:/Users/Abhishek/Desktop/JavaBasics-notes.pdf','rb')


# In[ ]:
 
# reading the pdf file
read_pdf = PyPDF2.PdfFileReader(pdf_file)


# In[ ]:

# extracting the text from the pdf file 
fulltext=''
for i in range (read_pdf.getNumPages()):
    page=read_pdf.getPage(i)
    text=page.extractText()
    fulltext=fulltext+text
    
    


# In[ ]:

# avoiding all the characters except a-z and A-z
fulltext=re.sub('[^a-zA-Z]',' ',fulltext)


# In[ ]:

#tokenizing(spliting ) the text into words
tokens=word_tokenize(fulltext)
tokens = [lemmatizer.lemmatize(token) for token in tokens]


# In[ ]:


tokens


# In[ ]:

#avoiding the stopwords from the tokens
corpus=' '
corpus = [token for token in tokens if token not in stopwords]


# In[ ]:


corpus


# In[ ]:

# function for avoiding the words whose length is less than 5
def letter(word_list):
    words = []
    for word in word_list:
        if len(word)>4:
            words.append(word)
    return words


# In[ ]:

# initialize the letter function
corpus=letter(corpus)


# In[ ]:


len(corpus)


# In[ ]:

# count the frequency of the words
tf=Counter(corpus)


# In[ ]:


len(tf)


# In[ ]:


tf


# In[ ]:

# arranging the words in increasing to decreasing order 
tf=tf.most_common()


# In[ ]:


tf


# In[ ]:

#calculating the tf- term frequency of the words
tfvalue=[]
for i in range (len(tf)):
    u=tf[i][1]/len(tf)
    tfvalue.append(u)


# In[ ]:


tfvalue


# In[ ]:

#calculating the idf- inverse document frequency for the words
idfvalue=[]
for i in range (len(tf)):
    f=math.log((len(tf))/(1+(tf[i][1])))
    idfvalue.append(f)


# In[ ]:


idfvalue


# In[ ]:

# calculating the tf*idf 
tf_idf=[]
for i in range (len(tf)):
    f=tfvalue[i]*idfvalue[i]
    tf_idf.append(f)


# In[ ]:


tf_idf


# In[ ]:


for i in range (len(tf)):
    print("Word: {}, TF-IDF: {}".format(tf[i], tf_idf[i]))

