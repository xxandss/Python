import  json

csvfile = open('student.csv','r',encoding = 'utf-8')
data=[]
for line in csvfile:
    data.append(list(line.strip().split(',')))
    
for i in range(1,len(data)):
      data[i] = dict(zip(data[0],data[i]))
ff=open("student.json","w",encoding='UTF-8')  #打开json文件
json.dump(data[1:],ff)

with open('./student.json', 'r', encoding='utf8') as f:
            students = json.load(f)


