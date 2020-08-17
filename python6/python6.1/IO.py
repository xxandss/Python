#IO流
#使用StringIO或BytesIO可以把任意一个字符串或字节串当做文件流来使用。
#多数时候，为了进行测试，我们不希望产生难以清理的临时文件。比如，当我们希望下载一张图片，并检查是否正确的下载了该图片的时候。
#请编写python代码以实现：

#用requests库下载图片https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
import requests
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
response = requests.get(url)
img = response.content
with open( './baidu.jpg','wb' ) as f:
     f.write(img)

#用PIL库以流的方式读取此图片的内容
from PIL import Image
img = Image.open('baidu.jpg')
print(img.format) 
print(img.size) 
print(img.mode)  
img.show() 

#用matplotlib中的matplotlib.pyplot.imshow函数显示该图片
import matplotlib.pyplot as plt
im = plt.imread('baidu.jpg')
plt.imshow(im)

