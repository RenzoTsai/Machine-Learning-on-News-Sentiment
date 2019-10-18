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


	

	
		
