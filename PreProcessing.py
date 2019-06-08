
# -*- coding: utf-8 -*-

import pandas as pd
import glob



files = glob.glob("cinsiyet_kiz/*.txt")
df = pd.concat([pd.read_csv(fp,encoding="windows-1254",sep="\n",quotechar=None, quoting=3,header=None)for fp in files], ignore_index=True)
df.columns = ["Tweetler"]
df["Cinsiyet"] = 1

files = glob.glob("cinsiyet_erkek/*.txt")
df2 = pd.concat([pd.read_csv(fp,encoding="windows-1254",sep="\n",quotechar=None, quoting=3,header=None)for fp in files], ignore_index=True)
df2.columns = ["Tweetler"]
df2["Cinsiyet"] = 0

Tweets = pd.concat([df2, df], ignore_index=True)
Tweets = Tweets.sample(frac=1).reset_index(drop=True)   # tweetleri randomize ettik


import re
import nltk

#nltk.download('stopwords')
from nltk.corpus import stopwords

trStopWords = stopwords.words('turkish') # turkce stopword'ler
nrmDatas = Tweets.copy()
nrmDatas.to_csv("tweetsOriginal.csv")


for i in range(len(Tweets)): # NOT : islem uzun surebilir
    pivot = re.sub('[^a-zA-ZÇŞĞÜÖİçşğüöı]',' ',Tweets['Tweetler'][i]) #turkce kararkter harici herseyi sil
    pivot = re.sub(r'\b\w{1,1}\b', '',pivot) #tek harfleri sil
    pivot = pivot.lower() # tum harfleri kucult
    pivot = pivot.split() # kelimelere ayir
    pivot = [(word) for word in pivot if not word in set(trStopWords)] # stopword'leri sil
    pivot = ' '.join(pivot) # tekrar birlestir
    nrmDatas['Tweetler',i] = pivot



nrmDatas["Tweetler"].to_csv("normalizingDatas.txt")


