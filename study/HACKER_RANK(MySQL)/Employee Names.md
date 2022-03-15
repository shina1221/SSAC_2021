Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

Input Format

The Employee table containing employee data for a company is described as follows:

![image](https://user-images.githubusercontent.com/38153316/158310885-6a9e14b5-d016-4500-a631-69a21f9267d3.png)


where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.  

Sample Input  

![image](https://user-images.githubusercontent.com/38153316/158310913-80b53f23-6d19-413d-8ce3-16a5cc044754.png)


Sample Output  

Angela  
Bonnie  
Frank  
Joe  
Kimberly  
Lisa  
Michael  
Patrick  
Rose  
Todd  

#풀이  
SELECT name FROM Employee ORDER BY name;
