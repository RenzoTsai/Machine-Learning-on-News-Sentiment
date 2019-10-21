import pandas as pd
import re

def deleteNoneSense(text):
	html  = re.compile('<.*?>')
	http  = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	src   = re.compile(r'\b(?!src|href)\w+=[\'\"].*?[\'\"](?=[\s\>])')
	space = re.compile(r'[\\][n]')
	ids   = re.compile('[(]["微信"]?id:(.*?)[)]')
	wopen = re.compile('window.open[(](.*?)[)]')
	english = re.compile('[a-zA-Z]')
	others= re.compile(u'[^\u4e00-\u9fa5\u0041-\u005A\u0061-\u007A\u0030-\u0039\u3002\uFF1F\uFF01\uFF0C\u3001\uFF1B\uFF1A\u300C\u300D\u300E\u300F\u2018\u2019\u201C\u201D\uFF08\uFF09\u3014\u3015\u3010\u3011\u2014\u2026\u2013\uFF0E\u300A\u300B\u3008\u3009\!\@\#\$\%\^\&\*\(\)\-\=\[\]\{\}\\\|\;\'\:\"\,\.\/\<\>\?\/\*\+\_"\u0020]+')
	text  = re.sub(html,'',text)
	text  = re.sub(http,'',text)
	text  = re.sub(space,'',text)
	text  = re.sub(wopen,'',text)
	text  = re.sub('window.open','',text)
	text  = re.sub(ids,'',text)
	text  = re.sub(others,'',text)
	text  = re.sub(r'\s','',text)
	text  = re.sub(src,'',text)
	text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",text)
	text = re.sub(english,'',text)
	return text



def loadData(train_filePath,label_filePath,test_filePath):
	trainData = pd.read_csv(train_filePath,index_col=0)
	labelData = pd.read_csv(label_filePath,index_col=0)
	testData  = pd.read_csv(test_filePath,index_col=0)
	trainData = trainData.merge(labelData, on='id', how='left')
	# trainData['content'] = trainData['content'].fillna('NaN')
	# trainData['title']   = trainData['title'].fillna('NaN')
	trainData = trainData.dropna()
	trainData['content'] = trainData['content'].apply(lambda x: deleteNoneSense(x))
	print(trainData.duplicated(subset = ['title','content']))
	print(trainData.drop_duplicates(subset = ['title','content']))
	trainData['combine'] = trainData['content']+30*trainData['title']

	testData['content'] = testData['content'].fillna('NaN')
	testData['title']   = testData['title'].fillna('NaN')
	testData = testData.dropna()
	testData['content'] = testData['content'].apply(lambda x: deleteNoneSense(x))
	testData['combine'] = testData['content']+30*testData['title']

	#trainData['title'] = trainData['title'].apply(lambda x: deleteNoneSense(x))
	return trainData,testData


if __name__ =='__main__':
	trainData,testData=loadData('Train/Train_DataSet_Label.csv','Train/Train_DataSet.csv','Test/Test_DataSet.csv')
	trainData.to_csv('Train/preprocessed_train_data.csv')
	testData.to_csv('Test/Test_DataSet.csv')
	print(trainData.head())
	print(testData.head())
	# test = "(微信)《fine》(hhh123)\\nhao this is a http: https://blog.csdn.net/hawkzy/article/details/85110213 (id:1001蔡润泽)如果我后面还有)12okthen ►750px;\"\"/>图片:/home/alidata/www/data/tmp/qfupload/4_291085_1514981471478952.jpg 施全军实名举报50天后，上黄镇党委政府回复如下图： =750) window.open(\'http://img.jsly001.com/attachment/mon_1801/4_291085_a9b11b7ea2b1ce9.jpg?90');\"\" onload=\"\"if(this.offsetwidth>\'750\')this.width='750';\"\" src=\"\"http://img.jsly001.com/attachment/mon_1801/4_291085_a9b11b7ea2b1ce9.jpg?90\"\" style=\"\"max-width:750px;\"\"/>图片:/home/alidata/www/data/tmp/qfupload/4_291085_1514981472631668.jpg =750) 如果我中间有window.open(\'http://img.jsly001.com/attachment/mon_1801/4_291085_9cde9b3943fe20c.jpg?75'); 好的asbhu12a呢么"
	# test = deleteNoneSense(test)
	# print(test)
	

	

	
		
