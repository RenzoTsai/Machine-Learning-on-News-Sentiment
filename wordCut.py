import pandas as pd
import jieba
import gensim
# from snownlp import SnowNLP
# from sklearn.model_selection import train_test_split
import re

def snow_result(comment):
    s = SnowNLP(comment)
    if s.sentiments >= 0.5:
        return 1
    else:
        return 0

def cut_char(text):
	#print("processing cutting")
	return ("/".join(jieba.cut(text)))

def cutData(filePath):
	cutData = pd.read_csv(filePath,index_col=0)
	cutData['content'] = pd.DataFrame(cutData['content'].astype(str))	
	cutData['cuted_words'] = cutData['content'].apply(lambda x: cut_char(x))
	print(cutData.head())
	return cutData


if __name__ =='__main__':
	jieba.load_userdict('dict.txt')
	jieba.enable_parallel(2)
	cutData = cutData('Train/preprocessed_train_data.csv')
	cutData.to_csv('Train/preprocessed_train_data.csv')
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


	

	
		
