#第一个爬虫实例
import requests  #导入爬虫库
response=requests.get('https://www.minecraft.net/zh-hans/') #发送请求
print('状态码'+str(response.status_code))      #获取状态码
print(response.text)        #得到网页信息
#把获取的图片保存到本地
f = open('E;\\高丞轩\\python\\爬虫\\网页源代码\\1','wd')
#绕过设置的反扒机制
headers={
    'User-Agent':'Mozilla/5.0(windows NT 10.0;Win64;x64)'
    }
response=requests.get('https://www.zhihu.com/')
print(response.text)
