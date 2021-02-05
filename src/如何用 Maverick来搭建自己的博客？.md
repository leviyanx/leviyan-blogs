---
layout: post
title: 我是如何用 Maverick来搭建自己的博客？
slug: how-to-build-my-blog-with-Maverick
date: 2021-02-04 23:13:55
status: publish
categories:
- wiki
tags:
- wiki


---



参考文章

- [用 GitHub 搭建静态博客太繁琐？用这个小工具实现「傻瓜式」发布](https://sspai.com/post/58013)
- [Blog-With-GitHub-Boilerplate](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate)（这是博客文章《完全用 GitHub 写博客》所提出流程的示例仓库。）
- [Maverick](https://github.com/AlanDecode/Maverick)



默认都是在master（后面改名为source）分支下操作。



## 搭建过程

准备好文件/文件夹

- .github（先用复制的，后期自己改）
- assets
- src（这里是放博客的，请准备至少一篇博客（md格式），放在这里）
  - images
  - static
- config.py（先用复制的，后期自己修改）
- Makefile（先用复制的，后期自己修改）
- README.md

---



修改master分支名

1.在github修改master分支名为source

2.在本地执行以下操作

```bash
git branch -m master source
git fetch origin
git branch -u origin/source source
```

---



操作cache分支

1.创建cache分支。

```bash
git branch cache
```

2.在cache分支下创建文件`sizeinfo.json`。

3.把分支提交到github

```bash
# 此时处于cache分支
git push origin HEAD -u
```

---



操作gh-pages分支（gh-pages分支是用来展示的）

1.创建gh-pages分支，并提交到github

```bash
git branch gh-pages
git checkout gh-pages

# 可以修改一些文件，并提交commit

git push origin HEAD -u
```

2.在github，进入仓库`settings`，在`Github Pages`选项下把`Source`换成gh-pages分支。

---



准备一个token，并为这个仓库添加token

准备token的过程省略，现在假设已经得到一个token。

1.进入`settings`-`Secrets`，选择`New repository secret`，创建一个secret。

- Name填`PERSONAL_TOKEN`。
- Value填得到的token。

2.选择添加。

---



使用Maverick和Galileo（Maverick的一个主题）

1.创建一个文件`.gitmodules`，不填内容。

2.执行命令

```bash
#现在在source分支，如果不是请切换到source

# 添加子模块——Maverick
git submodule add https://github.com/AlanDecode/Maverick.git

# 添加子模块——Galileo主题的latest分支
git submodule add -b latest https://github.com/AlanDecode/Maverick-Theme-Galileo.git ./Galileo
```

3.提交到github。

---



自定义配置来适配自己的博客

1.编辑`conf.py`，修改以下内容（只挑出现在最必要改的）

- `site_prefix`：改成自己博客的名字

---



至此博客已经可以正常运行了，可以进入网址`https://用户名.github.io/仓库名称/`查看是否成功。



## 自定义步骤

自动化上传博客流程

复制两个文件

- update_site.bat（windows下使用）
- update_site.sh（linux/macos下使用）

---



修改博客的一些信息/配置

- `conf.py`
  - `template`：可以切换主题
    - 可选的主题有：Galileo、
  - `site_name`
  - `site_logo`
    - 要求
  - `site_build_date`
  - `author`
  - `email`
  - `author_homepage`
  - `description`
  - `key_words`
  - `external_links`
  - `nav`
  - `social_links`

---



写文章的注意事项

- 支持的格式是`markdown`。
- 在文章的首部位置，需要写上文章的元数据，必须要填的有如下
  - layout
  - title
  - slug（文章的链接）
  - date

- 元数据使用的数据格式是YAML，注意使用规则——空格之类的。

- 更多详细的要求，看[这里](https://github.com/AlanDecode/Maverick)。

