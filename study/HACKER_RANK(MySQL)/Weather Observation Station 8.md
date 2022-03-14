Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![Station](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

#풀이
-앞단어와 뒷단어에 모음단어가 포함되어 있는 도시들 추출

#첫번째 방법
select distinct city from station
where (city like 'a%'
or city like 'e%'
or city like 'i%'
or city like 'o%'
or city like 'u%')
and
(
city like '%a'
or city like '%e'
or city like '%i'
or city like '%o'
or city like '%u'
)

#정규표현식 사용
-정규표현식에서 ^는 시작하는 문자열에 $는 끝나는 문자열에 사용
-띄어쓰기로 이루어진 문자열은 띄어쓰기 기준으로 문자열 별 쿼리를 작성해 줘야함.
-작은따옴표는 모든 정규식을 감쌈
-각 정규표현식의 시작^과 끝$은 공존할 수 없음
SELECT  DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[AEIOU]' AND CITY REGEXP '^[AEIOU]$'

[정규표현식 참조](https://junyoung-developer.tistory.com/34?category=929724)
