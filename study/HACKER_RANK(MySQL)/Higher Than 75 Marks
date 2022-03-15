Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

Input Format

The STUDENTS table is described as follows:

![fig1](https://s3.amazonaws.com/hr-challenge-images/12896/1443815243-94b941f556-1.png)

The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

Sample Input
![fig2](https://s3.amazonaws.com/hr-challenge-images/12896/1443815209-cf4b260993-2.png)

Sample Output

Ashley
Julia
Belvet
Explanation

Only Ashley, Julia, and Belvet have Marks > . If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.  

#풀이  
-점수가 75를 넘는 학생의 이름 출력  
-단 이름의 마지막 세글자를 기준으로 정렬  
-세글자가 같을 경우는 2차적으로 ID기준으로 정렬  
  
-RIGHT(column, n):오른쪽에서 n개의 문자열을 가져옴  

SELECT Name  
FROM STUDENTS  
WHERE Marks>75   
ORDER BY RIGHT(Name, 3), ID;  
