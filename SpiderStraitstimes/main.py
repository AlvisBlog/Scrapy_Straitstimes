from scrapy import cmdline
from PIL import Image, ImageTk
import PIL
from tkinter import *
import tkinter.messagebox

def run():
    cmdline.execute('scrapy crawl Straitstimes'.split())

def quit():
    quit=tkinter.messagebox.askokcancel('Do you want to quit the spider？')
    if quit==True:
     root.destroy()


root=Tk()#初始化

root.title("涉华舆情分析系统")#标题名称

root.geometry('600x400')#窗口初始化大小

root.resizable(0,1)#框体大小可调性，分别表示x,y方向的可变性,0不可调，其他数字表示可调


Button( text="Run Straitstimes Spider", command=run,height=1,width=20).pack()  # command绑定获取文本框内容方法
Button( text="Run Quora Spider", command=run,height=1,width=20).pack()
Button( text="Stop Straitstimes Spider", command=quit,height=1,width=20).pack()
Button( text="Stop Quora Spider", command=quit,width=20,height=1).pack()

canvas = Canvas(root,
                        width=2000,
                        height=2000,
                        bg='white')

image = PIL.Image.open("bg.gif")
im = ImageTk.PhotoImage(image)

canvas.create_image(300, 100, image=im)
canvas.create_text(302, 220,
                   text='涉华舆情分析系统,该系统主要用于言论涉华研究的毕业设计，不用于商业范畴，如有侵权行为,'
                        '将保留追究责任'
                   , fill='black')
canvas.create_text(302, 240,
                   text='备案号:GASNS63890-0-0987'
                   , fill='black')
canvas.create_text(302, 260,
                   text='作者:漂泊的浪子'
                   , fill='black')
canvas.pack()

root.mainloop()