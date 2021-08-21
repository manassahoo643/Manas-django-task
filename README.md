# django-task
In this project , i have created REST APIs based on Django with PostgreSQL database. It contains following things :-

1.Three user levels : 1. Super-admin, 2. Teacher, 3. Student.

http://127.0.0.1:8000/admin/login/?next=/admin/

2.Teacher can able to list all the students. Here is the permission given to the teacher by super user 'admin'.

3.Admin can be able to list every user in the database. Admin can add as many user. Admin can make new groups.

4..I have used JWT authentication in this project. JSON Web Token is an open standard for securely transferring data within parties using a JSON object. JWT is used for stateless authentication mechanisms for users and providers, this means maintaining session is on the client-side instead of storing sessions on the server. we need to authenticate and obtain the token

Student Login using JWT Authentication : http://127.0.0.1:8000/api-auth/login/?next=/student/
Teacher Login using JWT Authentication : http://127.0.0.1:8000/api-auth/login/?next=/teacher/

I have used the user name for JWT Authentication as 'admin' and password- 'admin'.

5..Student List :- Using Restful api in django.

Restful api for student using django - http://127.0.0.1:8000/student/

6.Teacher List :- Using Restful api in django
Restful api for teacher using django - http://127.0.0.1:8000/teacher/

