import pandas as pd
import jieba
#import gensim
import re

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as sw:
        stopwords = sw.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list 


def cut_char(text):
	#print("processing cutting")
	return ("/".join(jieba.cut(text,cut_all=True)))

def cutData(filePath):
	cutData = pd.read_csv(filePath,index_col=0)
	cutData['title'] = pd.DataFrame(cutData['title'].astype(str))	
	cutData['title'] = cutData['title'].apply(lambda x: cut_char(x))
	cutData['content'] = pd.DataFrame(cutData['content'].astype(str))	
	cutData['content'] = cutData['content'].apply(lambda x: cut_char(x))
	#cutData['combine'] = cutData['content']+20*cutData['title']
	cutData['combine'] = pd.DataFrame(cutData['combine'].astype(str))	
	cutData['combine'] = cutData['combine'].apply(lambda x: cut_char(x))
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


	

	
		
