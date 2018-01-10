#author: Tushar Nitave

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('data.tsv', delimiter=',,,', quoting=3)

X = dataset.iloc[:,:-1].values
X = pd.DataFrame(data=X)
Y = dataset.iloc[:,1].values


#categorizing the types of questions
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)



#cleaning the question: removing punctuation marks
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
questions = re.sub('[^a-zA-z]', ' ', X[0][0])
questions = questions.lower()
questions = questions.split()
questions = [word for word in questions if word in set(stopwords.words('english'))]
questions = ' '.join(questions)