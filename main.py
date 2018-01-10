#author: Tushar Nitave

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('data.tsv', delimiter=',,,', quoting=3)

#cleaning the question: removing punctuation marks
import re
questions = re.sub('[^a-zA-z]', ' ', dataset['question'][0])