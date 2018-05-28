# -*- coding: utf-8 -*-




class SpiderblogPipeline(object):
    def process_item(self, item, spider):
        with open("data.text",'a+') as fp:
            fp.write("文章链接为:"+item['link'] + '\n')
            fp.write("文章标题为:"+item['title'] + '\n')
            fp.write("文章作者为:"+item['author'] + '\n' )
            fp.write("文章发布时间为:"+item['pubdate'].strip() + '\n')
            fp.write("文章阅读量为:"+item['read_num'].strip() + '\n')
            fp.write("文章评论数为:"+item['comment_num'].strip() + '\n'+"\n")
        return item
