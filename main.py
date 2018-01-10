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
y = labelencoder_y.fit_transform(Y)



#cleaning the question: removing punctuation marks
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
corpus = []
for i in range(0, 1483):
    questions = re.sub('[^a-zA-z]', ' ', X[0][i])
    questions = questions.lower()
    questions = questions.split()
    questions = [word for word in questions if word in set(stopwords.words('english'))]
    questions = ' '.join(questions)
    corpus.append(questions)
    
#creating bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
