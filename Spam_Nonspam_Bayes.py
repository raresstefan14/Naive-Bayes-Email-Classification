import pandas as pd #for csv
from sklearn.model_selection import train_test_split#splits the data in training/test
from sklearn.feature_extraction.text import CountVectorizer#frequency of the words
from sklearn.naive_bayes import MultinomialNB #naive bayes for words
from sklearn.metrics import accuracy_score#accuracy for the model
file=pd.read_csv("s.csv",encoding ="latin-1")[['v1','v2']]
file.columns=['label','text']
file = file.dropna(subset=['text'])
file['label']=file['label'].map({'ham':0,'spam':1})
file['label'].value_counts()
x_train,x_test,y_train,y_test=train_test_split(file['text'],file['label'],test_size=0.2,random_state=41)
vectorizer=CountVectorizer()
x_train_v=vectorizer.fit_transform(x_train)
x_test_v=vectorizer.transform(x_test)
model=MultinomialNB()
model.fit(x_train_v,y_train)
pred=model.predict(x_test_v)
print(f"Accuracy:{accuracy_score(y_test,pred):.5f}")
def predict_message(message):
    v=vectorizer.transform([message])
    pre=model.predict(v)[0]
    if pre==1:
        return "SPAM"
    else:
        return "HAM"
while True:
    user_input=input("Write a message(if not please write 'exit')")
    if user_input.lower()=='exit':
        break
    print(" Your message is:", predict_message(user_input))

print(file.shape)