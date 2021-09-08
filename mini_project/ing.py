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
