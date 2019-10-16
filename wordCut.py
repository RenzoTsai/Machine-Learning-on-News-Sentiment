import pandas as pd
import jieba
import gensim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
# from snownlp import SnowNLP
# from sklearn.model_selection import train_test_split
import re

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as sw:
        stopwords = sw.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list 


def cut_char(text):
	#print("processing cutting")
	return ("/".join(jieba.cut(text)))

def cutData(filePath):
	cutData = pd.read_csv(filePath,index_col=0)
	cutData['title'] = pd.DataFrame(cutData['title'].astype(str))	
	cutData['title'] = cutData['title'].apply(lambda x: cut_char(x))
	cutData['content'] = pd.DataFrame(cutData['content'].astype(str))	
	cutData['content'] = cutData['content'].apply(lambda x: cut_char(x))
	print(cutData.head())
	return cutData


if __name__ =='__main__':
	jieba.load_userdict('dict.txt')
	jieba.enable_parallel(2)
	print("Processing: cutting train data...")
	cut_Train_Data = cutData('Train/preprocessed_train_data.csv')
	cut_Train_Data.to_csv('Train/preprocessed_train_data.csv')
	print("Processing: cutting test data...")
	cut_Test_Data = cutData('Test/Test_DataSet.csv')
	cut_Test_Data.to_csv('Test/result.csv')

	# stop_words = get_custom_stopwords('ChineseStopWords.txt')
	# trainData= cutData
	# X = trainData['cuted_content']
	# y = trainData.label
	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20191016)
	# Vectorizer = CountVectorizer( max_df = 0.8,
 #                            	  min_df = 3,
 #                            	  token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
 #                                  stop_words =frozenset(stop_words) )
	# test = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(), columns=Vectorizer.get_feature_names())
	# print(test.head())

	# nb = MultinomialNB()
	# X_train_vect = Vectorizer.fit_transform(X_train)
	# nb.fit(X_train_vect, y_train)
	# train_score = nb.score(X_train_vect, y_train)
	# print(train_score)

	# print(trainData['label'].unique())
	# seg_list = jieba.cut("我爱自然语言处理", cut_all=False)   
	# print(" ".join(seg_list))
	# text1 = '这个一般般！'
	# text2 = '这个太棒了！'
	# s1 = SnowNLP(text1)
	# s2 = SnowNLP(text2)
	# print(s1.sentiments,s2.sentiments)
	# trainData['snlp_result'] = trainData.content.apply(snow_result)
	# print(trainData.snlp_result)


	

	
		
