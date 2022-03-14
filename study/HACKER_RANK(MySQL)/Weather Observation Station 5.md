Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows:

![Station](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where LAT_N is the northern latitude and LONG_W is the western longitude.

Sample Input

For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output

ABC 3
PQRS 4
Explanation

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths 3,3,4 and 3. The longest name is PQRS, but there are 3 options for shortest named city. Choose ABC, because it comes first alphabetically.

Note
You can write two separate queries to get the desired output. It need not be a single query.

#풀이
-복수의 답변은 복수의 쿼리문으로 뽑을수도 있다.

1. 문자열의 길이 출력 = LENGTH() 
2. 문자열의 길이에 따른 정렬, 문자열에 대한 정렬은 ORDER BY 내에서 한번에 처리
3. LIMIT로 상위 1개만 추출

SELECT CITY, LENGHT(CITY)
FROM STATION
ORDER BY LENGHT(CITY) DESC, CITY   /*ORDER BY LENGHT(CITY) AS DESC, CITY ASC*/
LIMIT 1;

SELECT CITY, LENGHT(CITY)
FROM STATION
ORDER BY LENGHT(CITY), CITY
LIMIT 1;



