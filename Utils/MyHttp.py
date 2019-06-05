import sys,json
import urllib,urllib3


class MyHttp(object):

    def __init__(self,*args,**kwargs):
        super(MyHttp,self).__init__(*args,**kwargs)
    
    def setHeader(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
        }
    
    def getNewPostList(self):
        url='http://localhost:8000/api/post/?format=json'
        headers=self.setHeader()
        http=urllib3.PoolManager()
        response=http.request('GET',url,headers=headers)
        data=response.data
        print(type(eval(data)))


if __name__ == "__main__":
    myhttp=MyHttp()
    myhttp.getNewPostList()