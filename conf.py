# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/leviyan-blogs/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "树下躲雨要撑伞"
site_logo = "${static_prefix}logo.png"
site_build_date = "2021-02-04 23:28:48"
author = "树下躲雨要撑伞"
email = "leviyanx@gmail.com"
# author_homepage = "https://www.imalan.cn"
description = "一个现实的理想主义者"
key_words = ['Maverick', '树下躲雨要撑伞', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    # {
    #     "name": "三無計劃",
    #     "url": "https://www.imalan.cn",
    #     "brief": "熊猫小A的主页。"
    # }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "标签",
        "url": "${site_prefix}tags/",
        "target": "_self"
    }
    # {
    #     "name": "关于",
    #     "url": "${site_prefix}about/",
    #     "target": "_self"
    # }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    # {
    #     "name": "Weibo",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
