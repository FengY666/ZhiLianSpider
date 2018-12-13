# ZhiLianSpider
scrrapy + selenium爬取智联招聘。
智联列表页的招聘信息是通过ajax加载的,抓取这种网页的信息,主要有两种方式：
    1.通过分析ajax请求url拿到json数据来提取我们需要的数据
    2.使用selenium请求网页拿到js渲染过后的html页面.
分析axaj的代码就不说了,很简单.
这个程序主要是selenium+scrapy来爬取智联的程序.网站很简单,主要目的是熟悉scrapy框架的使用，熟悉框架的各个组件的调度情况。
因为智联网站的列表页是通过ajax加载的,而详情页并不是这样，如果全部使用selenium来访问的话效率太低了。
所以采用列表页使用selenium请求,详情页采用Request请求,大大的提高了爬取的速度。（当然最高的还是分析ajax请求）

在两种请求Request中我使用mata携带了是否需要要selenium访问的参数,以便于区别使用什么方式请求.

数据量很小,代码也很简单,写的不好的地方大家见谅.刚开始做爬虫,记录以后写过的爬虫代码。谢谢大家
