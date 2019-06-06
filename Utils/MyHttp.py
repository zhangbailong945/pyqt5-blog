import sys,json
import urllib,urllib3,json


class MyHttp(object):
    '''
    笔记相关列表拉取
    '''

    def __init__(self,*args,**kwargs):
        super(MyHttp,self).__init__(*args,**kwargs)
    
    def setHeader(self):
        '''
        设置请求头
        '''
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
        }
    
    def getNewPostList(self):
        '''
        获取最新的六条笔记
        '''
        url='http://localhost:8000/api/post/?format=json&pageNumer=1&pageSize=5'
        headers=self.setHeader()
        http=urllib3.PoolManager()
        list1=[]
        try:
            response=http.request('GET',url,headers=headers)
            data=response.data.decode('utf-8')
            dict1=json.loads(data)
            list1=dict1['results']
            return list1
        except urllib3.exceptions.NewConnectionError:
            print('访问最新的六条笔记API失败！')
        return list1
    
    def getNewTagList(self):
        '''
        获取最新的六条标签
        '''
        url='http://localhost:8000/api/tags/?format=json&pageNumer=1&pageSize=6'
        headers=self.setHeader()
        list1=[]
        try:
            http=urllib3.PoolManager()
            response=http.request('GET',url,headers=headers)
            data=response.data.decode('utf-8')
            dict1=json.loads(data)
            list1=dict1['results']
            return list1
        except urllib3.exceptions.NewConnectionError:
            print('获取最新的六条标签API失败！')
        return list1
        
'''
if __name__ == "__main__":
    myhttp=MyHttp()
    print(myhttp.getNewTagList())
'''