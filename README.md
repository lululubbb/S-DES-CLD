## 1. 系统简介

S-DES(Simplified Data Encryption Standard)是一种简化版的DES算法，它被设计用于教育目的，以便更容易理解DES的工作原理。

S-DES使用一个10位的密钥和一个8位的明文进行加密,而标准的DES算法则使用一个56位的密钥和一个64位的数据块。

S-DES的加密过程包括初始置换IP、两轮的函数运算(每轮使用不同的8位子密钥)、交换和最终置换。

我们提供了8bit加解密、ASCII字符串加解密、文件加解密以及暴力破解等功能。

详细的系统配置见用户指南.md

## 2. S-DES项目结构
<pre>
<code class="tree">
│  README.md
│  requirements.txt
│  开发手册.md
│  测试文档.md
│  用户指南.md
│
├─assets                                         - 用户指南、测试文档中的图片
│
├─.idea
│
├─.vscode
│      settings.json                             - Live Sever的配置，端口号8080
│
├─S-DES-end                                      - S-DES后端文件
│  │  functions.py                               - 实现S-DES算法的函数，包括加密、解密、密钥生成等
│  │  main.py                                    - S-DES后端的主程序，负责处理HTTP请求和响应，连接前端和后端
│  │
│  ├─.idea
│  │
│  └─tmp                                         -  用于存放文件夹解密中涉及的临时文件
│
└─S-DES-front                                    - S-DES前端文件
    │  index.html                                - 前端页面的主文件，用于展示用户界面
    │
    ├─image	                                     - 存放前端页面中使用的图片资源
    │
    ├─scripts	                                 - 存放JavaScript脚本文件
    │      script.js
    │
    └─styles	                                 - 前端页面的CSS样式定义
            style.css
</code>
</pre>

## 3.开发者信息

• 开发团队：卟咯吩

• 开发人员：陈露、罗丹

• 联系方式：1055331355@qq.com

