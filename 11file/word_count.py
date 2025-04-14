#coding:utf-8
def count_words(filename):
    '''计算一个文件大致包含了多少个单词'''
    try:
        with open(filename,encoding='utf-8') as file_object:#文件操作时要明确指定文件的编码，才能避免掉编码错误
            contents = file_object.read()
    except FileNotFoundError:
        msg = f"Sorry,the file {filename} does not exit"
        print(msg)
    else:
    # 计算文件大致包含了多少个单词
         words = contents.split()
         num_words = len(words)
         print(f"The file {filename} has about {num_words} words.")
filenames=['Alice.txt','almce.txt','pi_digits.txt']
for filename in filenames:
    count_words(filename)

#当捕获到的异常不需要告诉用户时，可以利用pass语句：
def count_words(filename):
    '''计算一个文件大致包含了多少个单词'''
    try:
        with open(filename,encoding='utf-8') as file_object:#文件操作时要明确指定文件的编码，才能避免掉编码错误
            contents = file_object.read()
    except FileNotFoundError:
        pass#pass能够在异常存在时忽略异常
    else:
    # 计算文件大致包含了多少个单词
         words = contents.split()
         num_words = len(words)
         print(f"The file {filename} has about {num_words} words.")
filenames=['Alice.txt','almce.txt','pi_digits.txt']
for filename in filenames:
    count_words(filename)