import pandas as pd
import numpy as np
import matplotlib as plt

"""
3. 데이터2 : 업종별 코로나 이전과 이후 총 사업장 수 추이분석

 구현목표
       - 연도별 총 신규 사업장 가입수 (선/바) 그래프 구현
       - 월별(업종별 증감폭 확인) 총 신규 사업장 가입수 (선/바) 그래프 구현
       - 신규 및 폐업 사업장 선별 및 그래프 구현(월별, 연도별 미정)
"""

#국민연금 가입 사업장 데이터 불러오기
test=pd.read_csv("G:\\SSAC\\SSAC_2021_playdata\\mini_project\\data\\국민연금 가입 사업장 내역 2018년 1월(2월 없음).csv", encoding='CP949')

#앞의 :는 전체행을 쓰겠다는 의미
#뒤는 몇번째 열을 쓰겠다는 의미

#원하는 열만 출력
test1=test.iloc[:,[1,3,6,9,12,13,14,18,20,21]]
test1

# 법정동주소광역시도코드
"""
참조 :https://www.code.go.kr/stdcode/regCodeL.do

강원도 : 42
경기도 : 41
경상남도 : 48
경상북도 47
광주광역시 29
대구광역시 : 27
대전광역시 : 30
부산광역시 26
서울특별시 : 11
세종특별자치시 36
울산광역시 :31
인천광역시 : 28
전라남도 : 46
전라북도 : 45
제주특별자치도 : 50
충청남도 :  44
충청북도 : 43
"""
# 법정동주소광역시도코드 리스트
local_list=[42, 41, 48, 47, 29, 27, 30, 26, 11, 36, 31, 28, 46, 45, 50, 44, 43]
local_result = []

#2021년 8월 지역별 사업장 갯수 
for i in local_list:
    local_result.append(len(test1[test1['법정동주소광역시도코드 LDONG_ADDR_MGPL_DG_CD\tVARCHAR(2)'] == i]))
local_result

#데이터테이블 내 업종별 갯수 카운트
test2=test1['사업장업종코드 WKPL_INTP_CD\t국세청업종코드참조 VARCHAR(6)'].groupby(test1['사업장업종코드 WKPL_INTP_CD\t국세청업종코드참조 VARCHAR(6)'])
test2.count()


#index 2

job_dict = {'1차 산업':0, '제조업':0, '자원':0, '건설업':0, '도매 및 소매업':0, '숙박 및 음식점':0, '운수 및 창고업, 임대':0, '서비스업':0, '부동산업':0, '정보통신업':0, '달리 분류되지 않은 개인 서비스업':0}
#인덱스(업종) 별 사업장 개수
for i in range(len(test3.index)):
    try:
        if int(test3.index[i]) in range(11000,151104):
            job_dict['1차 산업']+=test3.iloc[i]            
        if int(test3.index[i]) in range(151104,369909):
            job_dict['제조업']+=test3.iloc[i]              
        if int(test3.index[i]) in range(371000,410001):
            job_dict['자원']+=test3.iloc[i]           
        if int(test3.index[i]) in range(451101,453001):
            job_dict['건설업']+=test3.iloc[i]                
        if int(test3.index[i]) in range(501101,525913):
            job_dict['도매 및 소매업']+=test3.iloc[i]      
        if int(test3.index[i]) in range(551001,552310):
            job_dict['숙박 및 음식점']+=test3.iloc[i]  
        if int(test3.index[i]) in range(601000,630903):
            job_dict['운수 및 창고업, 임대']+=test3.iloc[i] 
        if int(test3.index[i]) in range(630903,672002):
            job_dict['서비스업']+=test3.iloc[i]
        if int(test3.index[i]) in range(701101,703025):
            job_dict['부동산업']+=test3.iloc[i]
        if int(test3.index[i]) in range(711100,713007):
            job_dict['운수 및 창고업, 임대']+=test3.iloc[i]          
        if int(test3.index[i]) in range(721000,729001):
            job_dict['정보통신업']+=test3.iloc[i]   
        if int(test3.index[i]) in range(741101,930922):
            job_dict['서비스업']+=test3.iloc[i] 
        if int(test3.index[i]) in range(930925,950003):
            job_dict['달리 분류되지 않은 개인 서비스업']+=test3.iloc[i]
        if int(test3.index[i]) ==999999:
            continue
    except:
        continue
#test3.iloc[0]
#test3.index[0]
job_dict


===============================

#202103 202107 나정

#데이터 프레임만들기
#pd.DataFrame({'A':[리스트], 'B':[리스트]})


import pandas as pd
test_1=pd.read_csv('G:\\SSAC\\SSAC_2021_playdata\\mini_project\\data\\국민연금 가입 사업장 내역 2021년 7월.csv',encoding='CP949')

job_dict_total = {'1차 산업':0, '제조업':0, '자원':0, '건설업':0, '도매 및 소매업':0, '숙박 및 음식점':0, '운수 및 창고업, 임대':0, '서비스업':0, '부동산업':0, '정보통신업':0, '달리 분류되지 않은 개인 서비스업':0}
job_df=pd.DataFrame([job_dict_total])
job_df

#업종 분류별 빈 딕셔너리 생성


data_1=test_1.iloc[:,[13]]
data_1


test1=test_1.iloc[:,[13]].groupby(data_1[' 사업장업종코드'])
test1.count().head()
len(test1)
test1.count()


#각 업종코드별 분류를 통해 사업장 수 파악하기

#업종 분류별 빈 딕셔너리 생성
job_dict202107= {'1차 산업':0, '제조업':0, '자원':0, '건설업':0, '도매 및 소매업':0, '숙박 및 음식점':0, '운수 및 창고업, 임대':0, '서비스업':0, '부동산업':0, '정보통신업':0, '달리 분류되지 않은 개인 서비스업':0}
job_dict202107

test1.count()

test1.count().index[0]

test1.count().iloc[1].iloc[0]


#인덱스(업종) 별 사업장 개수
for i in range(len(test1.count().index)):
    #업종코드가 없는것이 있으므로 try처리
    try:
        print(i,test1.count().index[i],test1.count().iloc[i].iloc[0])
        if int(test1.count().index[i]) in range(11000,151104):
            job_dict202107['1차 산업']+=test1.count().iloc[i].iloc[0]            
        if int(test1.count().index[i]) in range(151104,369909):
            job_dict202107['제조업']+=test1.count().iloc[i].iloc[0]              
        if int(test1.count().index[i]) in range(371000,410001):
            job_dict202107['자원']+=test1.count().iloc[i].iloc[0]           
        if int(test1.count().index[i]) in range(451101,453001):
            job_dict202107['건설업']+=test1.count().iloc[i].iloc[0]                           
        if int(test1.count().index[i]) in range(501101,525913):
            job_dict202107['도매 및 소매업']+=test1.count().iloc[i].iloc[0]                 
        if int(test1.count().index[i]) in range(551001,552310):
            job_dict202107['숙박 및 음식점']+=test1.count().iloc[i].iloc[0]             
        if int(test1.count().index[i]) in range(601000,630903):
            job_dict202107['운수 및 창고업, 임대']+=test1.count().iloc[i].iloc[0]            
        if int(test1.count().index[i]) in range(630903,672002):
            job_dict202107['서비스업']+=test1.count().iloc[i].iloc[0]           
        if int(test1.count().index[i]) in range(701101,703025):
            job_dict202107['부동산업']+=test1.count().iloc[i].iloc[0]           
        if int(test1.count().index[i]) in range(711100,713007):
            job_dict202107['운수 및 창고업, 임대']+=test1.count().iloc[i].iloc[0]                     
        if int(test1.count().index[i]) in range(721000,729001):
            job_dict202107['정보통신업']+=test1.count().iloc[i].iloc[0]              
        if int(test1.count().index[i]) in range(741101,930922):
            job_dict202107['서비스업']+=test1.count().iloc[i].iloc[0]            
        if int(test1.count().index[i]) in range(930925,950003):
            job_dict202107['달리 분류되지 않은 개인 서비스업']+=test1.count().iloc[i].iloc[0]  
        if int(test1.count().index[i]) ==999999:
            continue
    except:
        continue

job_dict202107

#통합 딕셔너리 생성
job_dict_total = {'1차 산업':0, '제조업':0, '자원':0, '건설업':0, '도매 및 소매업':0, '숙박 및 음식점':0, '운수 및 창고업, 임대':0, '서비스업':0, '부동산업':0, '정보통신업':0, '달리 분류되지 않은 개인 서비스업':0}
job_dict_total=pd.DataFrame([job_dict_total])

job_df=pd.DataFrame([job_dict1907])
#통합 df에 concat
job_dict_total=pd.concat([job_dict_total, job_df])
job_dict_total


===================

#https://yobro.tistory.com/207
#참고해서 재수정

#folium
from urllib.request import urlopen
import json
import folium

#각 시도별 geo정보를 담고 있는 json파일 가져오기
with urlopen('https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2018/json/skorea-provinces-2018-geo.json') as response:
    kor = json.load(response)
#https://raw.githubusercontent.com/southkorea/southkorea-maps/master/gadm/json/skorea-provinces-geo.json
#시도별 위도경도 받아오기    
len(kor)




m=folium.Map(
    location=[36.97884521132491, 127.86224884213675],
    zoom_start=6
    #title='Stamen Terrain'
)

folium.Choropleth(
    geo_data=kor,
    name='choropleth',
    data=each_local,
    columns=['name', '2021_07'],
    line_weight=2, #경계선 구분을 명확히 하기 위해 추가
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2
).add_to(m)

m

import folium 
import base64

img_path ='C:/Users/admin/Documents/GitHub/mini-Project/mini_project2'
pic = base64.b64encode(open(img_path+'/강원도.png','rb').read()).decode()
image_tag = '<img src="data:image/jpeg;base64,{}">'.format(pic)
iframe = folium.IFrame(image_tag, width=1500, height=1500)
popup = folium.Popup(iframe, max_width=2000)
 
    
mm = folium.Marker(location=[37.861971948097164, 127.75748769573207],
                 popup=popup)
mm.add_to(m)


mm = folium.Marker(location=[ 37.294687266303285, 127.03367657066224],
                 popup='경기도')
mm.add_to(m)

mm = folium.Marker(location=[35.2374008600027, 128.693589539166],
                 popup='경상남도')
mm.add_to(m)

mm = folium.Marker(location=[36.57798374279373, 128.5002429630932],
                 popup='경상북도')
mm.add_to(m)

mm = folium.Marker(location=[35.1537822701698, 126.800577524332],
                 popup='광주광역시')
mm.add_to(m)

mm = folium.Marker(location=[35.8295715327161, 128.633608695897],
                 popup='대구광역시')
mm.add_to(m)

mm = folium.Marker(location=[36.35459982630213, 127.3858798025016],
                 popup='대전광역시')
mm.add_to(m)

mm = folium.Marker(location=[35.179062965143665, 129.0743054210422],
                 popup='부산광역시')
mm.add_to(m)

mm = folium.Marker(location=[37.574883186068426, 126.97229701942572],
                 popup='서울특별시')
mm.add_to(m)

mm = folium.Marker(location=[36.4878707147471, 127.30158073162],
                 popup='세종특별자치시')
mm.add_to(m)

mm = folium.Marker(location=[35.5711799714271, 129.31533419043],
                 popup='울산광역시')
mm.add_to(m)

mm = folium.Marker(location=[37.4486688137974, 126.701815127031],
                 popup='인천광역시')
mm.add_to(m)

mm = folium.Marker(location=[34.817478142155196, 126.46950664961481],
                 popup='전라남도')
mm.add_to(m)

mm = folium.Marker(location=[35.8242446942156, 127.105073582353],
                 popup='전라북도')
mm.add_to(m)

mm = folium.Marker(location=[33.4890767517113, 126.499162205018],
                 popup='제주특별자치도')
mm.add_to(m)

mm = folium.Marker(location=[36.66117618384123, 126.67621571327705],
                 popup='충청남도')
mm.add_to(m)

mm = folium.Marker(location=[36.675242725309, 127.500799174506],
                 popup='충청북도')
mm.add_to(m)

m.save('filename.html')

m


