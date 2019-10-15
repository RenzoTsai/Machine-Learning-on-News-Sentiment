import pandas as pd
import re


def deleteNoneSense(text):
	html  = re.compile('<.*?>')
	http  = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	src  = re.compile(r'\b(?!src|href)\w+=[\'\"].*?[\'\"](?=[\s\>])')
	space = re.compile(r'\n')
	ids= re.compile(r'\(["微信"]?id:(.*)\)')
	others= re.compile(u'[^\u4e00-\u9fa5\u0041-\u005A\u0061-\u007A\u0030-\u0039\u3002\uFF1F\uFF01\uFF0C\u3001\uFF1B\uFF1A\u300C\u300D\u300E\u300F\u2018\u2019\u201C\u201D\uFF08\uFF09\u3014\u3015\u3010\u3011\u2014\u2026\u2013\uFF0E\u300A\u300B\u3008\u3009\!\@\#\$\%\^\&\*\(\)\-\=\[\]\{\}\\\|\;\'\:\"\,\.\/\<\>\?\/\*\+\_"\u0020]+')

	text  = re.sub(html,'',text)
	text  = re.sub(http,'',text)
	text  = re.sub(space,'',text)
	text  = re.sub('window.open','',text)
	text  = re.sub(src,'',text)
	text  = re.sub(ids,'',text)
	text  = re.sub(others,'',text)
	text  = re.sub("\\n",'',text)
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


	test = "(微信)《fine》(hhh123)\nhao this is a htttp: https://blog.csdn.net/hawkzy/article/details/85110213 (id:1001蔡润泽)okthen ►"
	test = deleteNoneSense(test)

	print(test)

	
		
