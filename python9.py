#编写一个python程序读取此数据集的内容，并统计得到以下信息：
#1 一共有多少不同的用户
#2 一共有多少不同的电影
#3 一共有多少不同的电影种类
#4 一共有多少电影没有外部链接
#5 2018年一共有多少人进行过电影评分

#导入文件
import pandas as pd
file1 = open('E:/技术培训/ml-25m/genome-scores.csv', encoding='utf-8')
file2 = open('E:/技术培训/ml-25m/genome-tags.csv', encoding='utf-8')
file3 = open('E:/技术培训/ml-25m/links.csv', encoding='utf-8')
file4 = open('E:/技术培训/ml-25m/movies.csv', encoding='utf-8')
file5 = open('E:/技术培训/ml-25m/ratings.csv', encoding='utf-8')
file6 = open('E:/技术培训/ml-25m/tags.csv', encoding='utf-8')

genome_scores = pd.read_csv(file1)
genome_tags   = pd.read_csv(file2)
links         = pd.read_csv(file3)
movies        = pd.read_csv(file4)
ratings       = pd.read_csv(file5)
tags          = pd.read_csv(file6)


#1
user1 = tags['userId']
user2 = ratings['userId']
user3 = user1.append(user2)
user  = user3.drop_duplicates()
print('一共有不同的用户数：',len(user))

#2
movie1 = genome_scores['movieId']
movie2 = links['movieId']
movie3 = movies['movieId']
movie4 = movie1.append(movie2)
movie5 = movie4.append(movie3)
movie  = movie5.drop_duplicates() 
print('一共有不同的电影数：',len(movie))

#3
genres0 = movies['genres']
genres1 = list(genres0.str.split('|'));
genres=list(set([i for j in genres1 for i in j ])) # 以空格为分隔符，分隔成两个
print('一共有不同的电影种类数量：',len(genres))
#4
tm = links['tmdbId']
tmna = tm.dropna()
d= len(links)-len(tmna)
print('没有外部链接的电影数',d)
#5
import time

time_start= time.strptime("2018-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
time_end  = time.strptime("2019-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
timestamp_start = int(time.mktime(time_start))
timestamp_end   = int(time.mktime(time_end))
timestamp = ratings["timestamp"] 
ratings_2018 = ratings.loc[(timestamp < timestamp_end) & (timestamp>= timestamp_start)]
user_2018 = ratings_2018['userId']
user_2018 = user_2018.drop_duplicates()
print('2018年电影评分人数：',len(user_2018))




