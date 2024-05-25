SELECT Department.NAME AS Department_Name, COUNT(Users.ID) AS Employee_Count, AVG(Users.SALARY) AS Average_Salary
FROM Department
JOIN Users ON Department.ID = Users.DEPARTMENT_ID
GROUP BY Department.NAME;