Python 3.13.11 (tags/v3.13.11:6278944, Dec  5 2025, 16:26:58) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> string1= "Hello "
>>> name = "Zara"
>>> string3 = ", welcome to Python Programming"
>>> string= string1 + name +string3
>>> print(string)
Hello Zara, welcome to Python Programming
>>> string[0]
'H'
>>> string[-1]
'g'
>>> string[:5]
'Hello'
>>> string[-11:]
'Programming'
>>> string=[::-1]
SyntaxError: invalid syntax
>>> string[::-1]
'gnimmargorP nohtyP ot emoclew ,araZ olleH'
>>> string[23:29]
'Python'
>>> strM = "Python beginner tutorial"
>>> strM.upper()
'PYTHON BEGINNER TUTORIAL'
>>> strM.lower()
'python beginner tutorial'
>>> strM,capitalise()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    strM,capitalise()
NameError: name 'capitalise' is not defined
>>> strM.capitalize()
'Python beginner tutorial'
>>> KeyboardInterrupt
>>> strM.count("t")
3
>>> strM.replace("Python" , "Machine Learning")
'Machine Learning beginner tutorial'
>>> tuple1=(10,20,30)
>>> tuple2=(40,50,60)
>>> t_combine= tuple1+tuple2
>>> print(t_combine)
(10, 20, 30, 40, 50, 60)
>>> t_repeat =t_combine*3
>>> print(t_repeat)
(10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)
t_combine[2]
30
t_combine[:3]
(10, 20, 30)
t_combine[-3:]
(40, 50, 60)
