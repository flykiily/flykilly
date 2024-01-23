import jieba
txt = input("请输入一段中文文本:")
ls=jieba.1cut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
