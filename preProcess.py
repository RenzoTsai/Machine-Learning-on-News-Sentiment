import pandas as pd
import re


def deleteNoneSense(text):
	html  = re.compile('<.*?>')
	http  = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	more  = re.compile(r'\b(?!src|href)\w+=[\'\"].*?[\'\"](?=[\s\>])')
	space = re.compile(r'\s')
	someid= re.compile(r'(id:.*)')
	text  = re.sub(html,'',text)
	text  = re.sub(http,'',text)
	text  = re.sub(space,'',text)
	text  = re.sub('window.open','',text)
	text  = re.sub(more,'',text)
	return text

def loadData(train_filePath,label_filePath):
	trainData = pd.read_csv(train_filePath)
	labelData = pd.read_csv(label_filePath)
	trainData = trainData.merge(labelData, on='id', how='left')
	trainData['content'] = trainData['content'].fillna('NaN')
	trainData['title']   = trainData['title'].fillna('NaN')
	trainData = trainData.dropna()
	trainData['content'] = trainData['content'].apply(lambda x: deleteNoneSense(x))
	trainData['title'] = trainData['title'].apply(lambda x: deleteNoneSense(x))
	return trainData


if __name__ =='__main__':
	trainData=loadData('Train/Train_DataSet_Label.csv','Train/Train_DataSet.csv')
	trainData.to_csv('Train/preprocessed_train_data.csv')
	test= 'https://myapple.coms.cn/cn/123 3413 (id:1001蔡润泽)okthen'
	deleteNoneSense(test)
	print(test)

	
		
