import scrapy
from tutorial.item import DmozItem
# scrapy shell 'url'
# response.xpath()相当于一个选择器，根据节点来获取查找
# response.xpath('//title') 获取title的元素
# response.xpath('//title').extract() 提取title的元素
# response.xpath('//title/text()').extract() 提取title的文档元素
# response.xpath('//ul/li/text()').extract()获取li上的文档元素
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # 定义爬取的网址
    allowed_domains = ['demoz.org']
    start_urls = [
        'https://www.cnblogs.com/zkwarrior/p/9625858.html',
        'https://www.cnblogs.com/zengsf/p/9801966.html'
    ]

    def parse(self,res):
        # filename = res.url.split("/")[-1]
        # with open(filename,'wb') as f:
        #     f.write(res.body)
        sel = scrapy.selector.Selector(res)
        # xpath 为路径查询语言，功能为确定位置./从根节点选取。
        # //从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
        # @ 为选取节点属性
        sites = sel.xpath('//ul[@class="menu"]/li')
        items = []
        for site in sites:
            # 实例化
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
            # print(title, link, desc)

        # 最后返回一个列表
        return items