from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

# 질문 게시판 제목 데이터 가져오기

listS = []
listQ = []
listA = []
listCSV = []

for i in range(1, 1000):
    myparser = 'html.parser'
    myurl = 'http://www.hackers.co.kr/?c=s_toeic/toeic_board/b_toeic_ask' + '&p=' + str(i)
    response = urlopen(myurl)
    soup = BeautifulSoup(response, myparser)

    myurlurl = soup.find_all('td', attrs={'class':'sbj'})
   
    for j in myurlurl:
        href = j.find('a').attrs['href']
        realhref = 'http://www.hackers.co.kr' + href
        # print(realhref)
        response = urlopen(realhref)
        soup = BeautifulSoup(response, myparser)

        # 제목
        for subject in soup.select("div.subject"):
            for sub in subject.select("h1"):   
                subsub = sub.get_text()
                listS.append(subsub)
                # print(sub)
        '''
        # 질문
        for question in soup.select("div.viewbox"):
            for ques in question.select("div.content"):
                quesques = ques.get_text()
                listQ.append(quesques)
                # print(quesques)
        
        # 답변
        try:
            for answer in soup.select("td.retext"):
                for anss in answer.select("div.text"):
                    answeranswer = anss.get_text()
                    listA.append(answeranswer)
        except ConnectionError as e :
            pass
        '''
    print(str(i) + '번째 크롤링중......')


# csv파일 만들기
mycolumns1 = ['제목']
myframe1 = DataFrame(listS, columns=mycolumns1)
filename1 = 'Subject.csv'
myframe1.to_csv(filename1, encoding='utf-8-sig', index=False)
'''
mycolumns2 = ['질문']
myframe2 = DataFrame(listQ, columns=mycolumns2)
filename2 = 'Question.csv'
myframe2.to_csv(filename2, encoding='utf-8', index=False)

mycolumns3 = ['답변']
myframe3 = DataFrame(listA, columns=mycolumns3)
filename3 = 'Answer.csv'
myframe3.to_csv(filename3, encoding='utf-8', index=False)
'''

print('파일로 저장됨')