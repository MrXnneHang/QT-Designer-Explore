对要做的QT项目中每个part和难点拆分制作，主要是边学边做，顺便记录markdown和代码。适合同样入门QT Designer的人。

仓库:

[MrXnneHang/QT-Designer-Explore (github.com)](https://github.com/MrXnneHang/QT-Designer-Explore)

# 大体思路和布局：

## 模块分布的参考(b5对战平台)

![image-20240719093651656](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/07/202407190936817.png)

动态效果，音效。直接明了。

特地去下了个CSGO。绑定了下b5，直接抄应该不会被告吧=-=

每个chapter做一个模块。

## 用气泡替换文本框参考

气泡+tag

* 把输入文本框替换成手动点选的tags

* 回复不用一次性给出，可以一段一段给，发气泡。

* 并且在右边给出一个像纸飞机一样的东西，可以直达上一个tag所在位置。
* 左侧的频道换成LLM模型选项

![image-20240719093357102](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/07/202407190934237.png)



## 进入模块后的布局：

![UI设计](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/07/202407190958209.jpeg)



# 任务拆分（难点合集）

## 1.点击模块进去后不新建Window但更新布局。【★★★★】

以及还需要做一个log out的选项，能够回退到主界面进行再次选择。

如何Hidden，如何做动画。

## 2.聊天式。【★★★★★】

* 气泡随着字符长度变化而变化

* 以及查看历史记录的滚轮。
* 保留历史记录。
* 自动更新窗口

## 3.纸飞机，快速回到定位的某一个段。【★★★】

## 4.保留上一次选项中的excel路径。【★★】

## 5.做一个路径选择框。【★】