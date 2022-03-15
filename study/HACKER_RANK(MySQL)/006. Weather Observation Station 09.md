Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![Station](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

#풀이

-[^가나다]: 정규표현식에서 가나다를 포함하지 않는으로 NOT의 의미로 사용

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^AEIOU]';
