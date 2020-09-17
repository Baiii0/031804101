import jieba.analyse
import re,sys
from math import ceil, sqrt
from zhon.hanzi import punctuation


class maintest():
    
    def calCos(f1, f2):
        try:
            global punctuation
            punctuation += '\n '
            s = open(f1, 'r', encoding='utf-8')
            line = s.read()
            if len(line) == 0:
                raise "文本内容不能为空"
            line = re.sub(r"[%s]+" % punctuation, "", line)
            wordSum = jieba.lcut(line)
            length = len(set(wordSum))
            keyWords = jieba.analyse.extract_tags(line, ceil(length/3), True)
            s.close()
            d1 = dict(keyWords)

            s = open(f2, 'r', encoding='utf-8')
            line = s.read()
            line = re.sub(r"[%s]+" % punctuation, "", line)
            wordSum = jieba.lcut(line)
            length = len(set(wordSum))
            keyWords = jieba.analyse.extract_tags(line, ceil(length/3), True)
            s.close()
            d2 = dict(keyWords)

            wordSet = set(d1.keys()).union(d2.keys())
            wordlist = list(wordSet)

            length = len(wordlist)
            vector1 = [0] * length
            keys = d1.keys()
            for i in range(length):
                if wordlist[i] in keys:
                    vector1[i] = d1[wordlist[i]]

            vector2 = [0] * length
            keys = d2.keys()
            for i in range(length):
                if wordlist[i] in keys:
                    vector2[i] = d2[wordlist[i]]

            vectorLength = len(vector1)
            B = sum(vector1[i]*vector2[i] for i in range(vectorLength))
            A1 = sum(i**2 for i in vector1)
            A2 = sum(i**2 for i in vector2)
            A = sqrt(A1*A2)
            return B/A
        except Exception as e:
            if e==ZeroDivisionError:
                return 0
            else:
                print(e)