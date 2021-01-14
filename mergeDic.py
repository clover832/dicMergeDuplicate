# -*- coding: UTF-8 -*-
#! python3
# 在字典中添加新的字典

# 字典dic.txt
# 来源：Layer子域名挖掘机
dicFile = 'dic.txt'

# 字典dnspod-tlds.txt
# 来源：https://github.com/DNSPod/oh-my-free-data 
addFile = 'dnspod-tlds.txt'
newDic = 'dic_new.txt'

# 定义合并函数
def merge(dicFile, addFile):
    f1 = open(dicFile, 'a+', encoding='utf-8')
    with open(addFile, 'r', encoding='utf-8') as f2:
        f1.write('\n')
        for i in f2:
            f1.write(i)

# 定义去重函数
def depulicate(dicFile):
    a = 0
    # 创建无序不重复元素集
    lines_seen = set()
    outfile = open(newDic, 'w', encoding='utf-8')
    f = open(dicFile, 'r', encoding='utf-8')
    for line in f:
        if line not in lines_seen:
            a = a + 1
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print("success")

# 调用合并函数
merge(dicFile, addFile)

# 调用去重函数
depulicate(dicFile)


