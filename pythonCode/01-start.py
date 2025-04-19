# 我是一个注释
print("hello")
print("*" * 10)

# 变量
students_count = 1000
print(students_count)
rating = 4.99  # 浮点数
is_published = False  # 布尔类型
course_name = "Python Programming"

# 字符串
course_name = "Python Programming"
message = """

Hi, I am 

"""
print(f"字符串的长度是:{len(course_name)}")
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])  # [0, 3)
print(course_name[:])  # 返回整个字符串

# 转义字符
course_name = "Python 'Programming"
print(course_name)
course_name = 'Python "Programming'
print(course_name)

# 字符串格式化
first = "Wang"
last = "Zesheng"
full = f"{first} {last}"
print(full)

# 字符串方法
course_name = "Python Programming"
print(course_name.upper())  # 转换为大写
print(course_name.lower())  # 转换为小写
print(course_name.title())  # 首字母大写
print(course_name.strip())  # 去除开头和结尾空格 lstrip rstrip
print(course_name.find("Python"))  #  查找字符串，返回第一次出现的索引
print(course_name.replace("P", "J"))
print("gram" in course_name)

# 数据
x = 1
x = 1.1
x = 1 + 2j

# 算术运算符
# + - * / // % **

import math

print(round(2.9))  # 四舍五入
print(abs(-2.9))  # 绝对值

# 类型转换
print(int(3.9))


# Falsy : "" 、0、 None

