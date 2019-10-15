import pandas as pd
import re

def deleteNoneSense(text):
	html=re.compile('<.*?>')
	text = re.sub(html,'',text)
	text = re.sub('[\s]*','',text)
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
	
		
