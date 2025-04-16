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
