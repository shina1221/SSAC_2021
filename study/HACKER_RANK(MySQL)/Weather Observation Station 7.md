Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![Station](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

#풀이  
-'a%':a로 시작하는  
-'%a':a로 끝나는  

select distinct city  
from station  
where city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';  


#사이트에서 정규표현식 답을 안받음
SELECT DISTINCT CITY  
FROM STATION  
WHERE CITY REGEXP '[AEIOU]$';  

