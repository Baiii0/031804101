import re,sys
from math import ceil,sqrt
import jieba.analyse
from zhon.hanzi import punctuation

# 余弦相似度算法适合短文本，所以短文本的关键词数/总词数可以尽量大些
def wordsNum(num):
    if num<10:
        return num
    elif num<200:
        return ceil(num/2)
    else:
        return ceil(num/3)


def extractKeywords(path):
    s = open(path, 'r', encoding='utf-8')
    line = s.read()
    # punctuation是从zhon.hanzi导入的包含很多符号的字符串，punctuation += '\n '(有个空格)，再用正则表达式替换就能得到一个纯中文字符串
    line = re.sub(r"[%s]+" % punctuation, "", line)
    wordSum = jieba.lcut(line)
    # 根据词语数量来确定提取关键词数量，用set去除重复元素
    length = len(set(wordSum))
    # 利用jieba.analyse.extract_tags()函数，返回关键词及其权重(需要设置withWeight=True)
    keyWords = jieba.analyse.extract_tags(line, wordsNum(length), True)
    s.close()
    # 原来的keyWords是一个列表，里面的元素都是元组，转成字典有利用后续操作
    return dict(keyWords)


# 求两个关键词并集，先用集合去重，返回list是为了方便遍历
def mergeWords(d1, d2):
    wordSet = set(d1.keys()).union(d2.keys())
    return list(wordSet)


# 求关键词向量
def calVector(d, wordlist):
    length = len(wordlist)
    vector = [0] * length
    keys = d.keys()
    for i in range(length):
        if wordlist[i] in keys:
            vector[i] = d[wordlist[i]]
    return vector


# 求余弦相似度
def calCos(v1, v2):
    try:
        vectorLength = len(v1)
        B = sum(v1[i]*v2[i] for i in range(vectorLength))
        A1 = sum(i**2 for i in v1)
        A2 = sum(i**2 for i in v2)
        A = sqrt(A1*A2)
        return B/A
    # 如果有一篇或者两篇为空文本，则返回余弦相似度为0
    except ZeroDivisionError as e:
        print(e)
        return 0


def saveData(path,data):
    with open(path, 'w') as file_object:
        file_object.write(format(data, ".2f"))
        file_object.close()
        print("写入"+path+"文件完成")
        

if __name__ == "__main__":
    # 出现异常就直接输出信息
    try:
        # sys.argv[0] : main.py
        filePath1,filePath2,savePath = sys.argv[1],sys.argv[2],sys.argv[3]
        # 加上换行和空格，结合正则表达式可去除所有非中文的字符
        punctuation += '\n '
        # 分别提取两篇文本的关键词及其权重
        t1 = extractKeywords(filePath1)
        t2 = extractKeywords(filePath2)
        # 求出关键词并集
        words = mergeWords(t1, t2)
        # 分计算词向量
        v1 = calVector(t1, words)
        v2 = calVector(t2, words)
        # 计算余弦相似度
        cos = calCos(v1, v2)
        # 在指定路径存储数据
        saveData(savePath,cos)
        print('相似度为 = ' + format(cos, ".2f"))
    except Exception as e:
        print(e)
        print("请输入正确的参数")
    finally:
        # 程序结束，返回0
        sys.exit(0)