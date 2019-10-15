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
	cutData = pd.read_csv(filePath)
	cutData = pd.DataFrame(cutData['content'].astype(str))	
	cutData['cut_words'] = cutData['content'].apply(lambda x: cut_char(x))
	print(cutData.head())
	return cutData


if __name__ =='__main__':
	jieba.load_userdict('dict.txt')
	jieba.enable_parallel(2)
	cutData = cutData('Train/preprocessed_train_data.csv')

	test= "问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？),\"这几天看了有人举报施某某的贴子，经与举报人联系证实，是宣某当天中午请举报人和枪手喝酒后，晚上才发的贴子！本人不去讨论前二天的举报，相信总归会有说法的！今天一看施全军2017年1月2日实名举报上黄镇宣国才的贴子（仍被锁定禁止评论）已经正好一整年了=750)this.width='750';""src=\"\"\"\"style=\"\"max-width:750px;\"\"/>图片:/home/alidata/www/data/tmp/qfupload/4_291085_1514981471478952.jpg施全军实名"
	print("/".join(jieba.cut(test)))
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


	

	
		
