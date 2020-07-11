import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

news = pd.read_csv('news.csv')
X = news['text']
y = news['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=53)

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)

pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
#y_pred = pac.predict(tfidf_test)
#score = accuracy_score(y_test,y_pred)
#print('Accuracy',score*100)

pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')),('nbmodel', MultinomialNB())])

pipeline.fit(X_train, y_train)

pred = pipeline.predict(X_test)
str = " "
a = sys.argv[1]
input = a.split(":")
res = pipeline.predict(input)
#return render_template('index.html', prediction_text='The news is "{}"'.format(res))
print("The News is ")
print(str.join(res))

#print(classification_report(y_test, pred))
#print(confusion_matrix(y_test, pred))