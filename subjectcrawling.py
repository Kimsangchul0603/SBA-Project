from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

# 질문 게시판 제목 데이터 가져오기
listS = []

for i in range(1, 1000):
    myparser = 'html.parser'
    myurl = 'http://www.hackers.co.kr/?c=s_toeic/toeic_board/b_toeic_ask' + '&p=' + str(i)
    response = urlopen(myurl)
    soup = BeautifulSoup(response, myparser)

    for subject in soup.select("td.sbj"):
        for sub in subject.select("a"):
            for subsub in sub.select("span"):   
                subsub = subsub.get_text()
                subsub.rstrip()
                subsub.lstrip()
                subsub.replace("                          ", "")
                " ".join(subsub.split())
                "                          ".join(subsub.split())
                
                # print(subsub)
                listS.append(subsub)
                
    print(str(i) + '번째 크롤링중......')



# csv파일 만들기
mycolumns = ['제목']
myframe = DataFrame(listS, columns=mycolumns)
'''
i = 1
for i in range(len(myframe)):
    if i % 2 == 1:
        myframe = myframe.drop(i, 0)
    else:
        pass
'''
filename = 'Subject.csv'
myframe.to_csv(filename, encoding='utf-8-sig', index=False)


print('파일로 저장됨')