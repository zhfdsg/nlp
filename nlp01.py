import jieba
import math
import os
import re
# -*- coding:utf-8 -*-
book_dir='D:/下载/jyxstxtqj_downcc.com/'
wen=[]
words = []
count=0
cishu = 0
cishu2=0
cishu3=0
words_dir = {}
words_dir2 = {}
words_dir3 = {}
def fenci(filedir):
    with open(os.path.abspath(filedir), "r", encoding='ansi') as file:
        filecontext = file.read()
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        final = re.sub(pattern, '', filecontext)
        final = final.replace("\n", '')
        final = final.replace(" ", '')
        final = final.replace("本书来自免费小说下载站更多更新免费电子书请关注", '')
        return final
        # print(final)
def yiyuan(wen):
    global count,words,cishu,cishu2,cishu3,words_dir,words_dir2,words_dir3
    for wenzhang in wen:
        count+=len(wenzhang)
        # 基于词
        for x in jieba.cut(wenzhang,cut_all=False):
            words.append(x)
        # 基于字
        # for x in range(len(wenzhang)):
        #     words.append(wenzhang[x])
            cishu += 1

    for i in range(len(words)):
        words_dir[words[i]]=words_dir.get(words[i],0)+1
    print("总字数:", count)
    print("总词数:", cishu)
    entropy = []
    for word in words_dir.items():
        entropy.append(-(word[1]/cishu)*math.log(word[1]/cishu,2))
    print("基于词的一元模型的中文信息熵为:", round(sum(entropy), 5), "比特/词")
def eryuan(wen):
    global count, words, cishu, cishu2, cishu3, words_dir, words_dir2, words_dir3

    for i in range(len(words)-1):
        words_dir2[(words[i],words[i+1])]=words_dir2.get((words[i],words[i+1]),0)+1
    cishu2 = cishu-1
    entropy = []
    for word in words_dir2.items():
        entropy.append(-(word[1]/cishu2)*math.log(word[1]/words_dir[word[0][0]],2))
    print("二元模型的中文信息熵为:", round(sum(entropy), 5), "比特/词")
def sanyuan(wen):
    global count, words, cishu, cishu2, cishu3, words_dir, words_dir2, words_dir3
    for i in range(len(words)-2):
        words_dir3[((words[i],words[i+1]),words[i+2])]=words_dir3.get(((words[i],words[i+1]),words[i+2]),0)+1
    cishu3 = cishu2-1
    entropy = []
    for word in words_dir3.items():
        entropy.append(-(word[1]/cishu3)*math.log(word[1]/words_dir2[word[0][0]],2))
    print("三元模型的中文信息熵为:", round(sum(entropy), 5), "比特/词")

if __name__ == '__main__':
    files=os.listdir(book_dir)
    for i,item in enumerate(files):
        wen.append(fenci(book_dir+item))
    yiyuan(wen)
    eryuan(wen)
    sanyuan(wen)