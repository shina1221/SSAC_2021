Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![Station](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

#풀이

- 여러개의 중복조건은 각각 표시 >> ex) CITY LIKE 'A%' OR CITY LIKE '%B' ....
SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%');

#정규표현식
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '^A|^E|^I|^O|^U');
