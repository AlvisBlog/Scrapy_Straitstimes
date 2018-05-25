from scrapy import cmdline

from tkinter import *
import tkinter.messagebox

def run():
    cmdline.execute('scrapy crawl Straitstimes'.split())

run()

# root=Tk()#初始化
#
# root.title("Tester")#标题名称
#
# root.geometry('600x400')#窗口初始化大小
#
# root.resizable(0,1)#框体大小可调性，分别表示x,y方向的可变性,0不可调，其他数字表示可调
#
#
# Button( text="run", command=run).pack()  # command绑定获取文本框内容方法
#
# root.mainloop()