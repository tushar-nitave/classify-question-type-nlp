# classify-question-type-nlp

### This project classifies different question types using natural language processing. 

#### Different steps invovled in this process are:
#### 1. Spliting the dataset: Questions and Types
I created two labels namely X and Y to store questions and it's type respectively. Then, using sklearn's LabelEncoder I encoded different question types.

#### 2. Cleaning the dataset
This involves removing the extra characters such as punctuation marks, numbers etc. and keeping only the english alphabets because they have more emphasis on classifying the type of question. Also we need to remove words like 'this', 'that', 'is', 'the' etc. which does not help our algorithm to make any co-relation. I used **Natural Language Toolkit**(nltk) library for this purpose.

#### 3. Creating bag of words
A bag of words is a sparse vector of occurence counts of words. It is a method of extracting feature from text which can used for our machine learning algorithms.

#### 4. Training the model
I have naive bayes algorithm for training my classification model. When I used **1187** questions for training and **296** questions for testing. The model classified different types of question with the accuracy of **78%**.
