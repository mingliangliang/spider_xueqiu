昨天领导安排我整理知名网站上的选股策略，整理了半天，全部手敲的，因为APP没办法复制文本，很蛋疼，今天闲下来了就写了这个爬虫，将所有的策略抓取并保存到MySQL数据库，这样下次连拷贝都剩了，直接MySQL导出excel，一分钟就解决问题，喜欢请 **star**，谢谢。

<iframe src="https://ghbtns.com/github-btn.html?user=mingliangliang&repo=spider_xueqiu&type=star&count=true&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe>    
      
## Git地址
* URL [https://github.com/mingliangliang/spider_xueqiu](https://github.com/mingliangliang/spider_xueqiu)

## 策略截图
{% capture images %}
	http://res.cloudinary.com/changzhou-university/image/upload/v1502875478/20170816172354_fzywfu.jpg
	http://res.cloudinary.com/changzhou-university/image/upload/v1502875478/20170816172346_q3uyja.jpg
{% endcapture %}
{% include gallery images=images caption="运行截图和结果" cols=2 %}     
## MySQL建表
建表语句已经上传git，直接刷一下脚本即可。

## 运行python
{% capture images %}
	http://res.cloudinary.com/changzhou-university/image/upload/v1502875478/2017-08-16_171956_nx2umb.jpg
	http://res.cloudinary.com/changzhou-university/image/upload/v1502875479/2017-08-16_172054_cavae2.jpg
{% endcapture %}
{% include gallery images=images caption="运行截图和结果" cols=2 %}            

## 运行环境
- 操作系统：Windows7_X64
- python版本：python2.7
- SQL:MySQL5.7  
- 编译器：Spyder

## 版本遗留问题
只取了策略的基本信息，没有把此策略包含股票取下来，下一版实现。