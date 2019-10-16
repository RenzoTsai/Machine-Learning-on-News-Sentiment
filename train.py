import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as sw:
        stopwords = sw.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list 


if __name__ =='__main__':
	stop_words = get_custom_stopwords('ChineseStopWords.txt')
	print("stop words is:\n",stop_words)

	trainData = pd.read_csv('Train/preprocessed_train_data.csv')

	X = trainData['content'].astype('U')
	y = trainData.label
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2019)
	Vectorizer = CountVectorizer( max_df = 0.8,
                            	  min_df = 3,
                            	  token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                                  stop_words =frozenset(stop_words) )
	test = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(), columns=Vectorizer.get_feature_names())
	print(test.head())

	nb = MultinomialNB()
	X_train_vect = Vectorizer.fit_transform(X_train)
	nb.fit(X_train_vect, y_train)
	train_score = nb.score(X_train_vect, y_train)
	print("content train score is : ",train_score)

	X_test_vect = Vectorizer.transform(X_test)
	print("content test score is : ", nb.score(X_test_vect, y_test))

	print("Apply to Test Data...")
	testData = pd.read_csv('Test/result.csv',index_col=0)
	testResult = nb.predict(Vectorizer.transform(testData['content'].astype('U')))
	testData['label_content'] = testResult



	X = trainData['title'].astype('U')
	y = trainData.label
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2019)
	Vectorizer_Title = CountVectorizer( max_df = 0.8,
                            	  min_df = 3,
                            	  token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                                  stop_words =frozenset(stop_words) )
	test = pd.DataFrame(Vectorizer_Title.fit_transform(X_train).toarray(), columns=Vectorizer_Title.get_feature_names())
	print(test.head())

	nb = MultinomialNB()
	X_train_vect = Vectorizer_Title.fit_transform(X_train)
	print(Vectorizer_Title.fit_transform(X_train))
	nb.fit(X_train_vect, y_train)
	train_score = nb.score(X_train_vect, y_train)
	print("title train score is : ",train_score)

	X_test_vect = Vectorizer_Title.transform(X_test)
	print("title test score is : ", nb.score(X_test_vect, y_test))


	print("Apply to Test Data...")
	testResult = nb.predict(Vectorizer_Title.transform(testData['title'].astype('U')))
	testData['label_title'] = testResult
	testData.to_csv ('Test/result.csv')



	