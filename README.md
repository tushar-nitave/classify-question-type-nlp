# classify-question-type-nlp

### This project classifies different question types using natural language processing. 

#### There are few steps invovled in making the machine classify these different questions.
#### 1. Cleaning the dataset
This involves removing the extra characters such as punctuation marks, numbers etc. and keeping only the english alphabets because they have more emphasis on classifying the type of question. Also we need to remove words like 'this', 'that', 'is', 'the' etc. which does not help our algorithm to make any co-relation. I used **Natural Language Toolkit**(nltk) library for this purpose.
