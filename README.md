# LAPS - 左房压医疗影像分析系统

---

## 项目目录结构设计思路
- LAPS  
    - Database  
      *用以存放所有 **应用程序中运行的数据的** 文件*
      
    - Docs  
      *用以存放所有 **文档** 文件*
      
    - Preinstall  
      *用以存放所有 **预装** 文件以及**相应的添加路径脚本**文件*
      
    - PyUI  
      *用以存放所有的 使用Designer设计出来的.ui文件 编译而来的.py **界面**文件*  
      *使用的方法是用的external tool的中的 **PYUIC***
      
    - PyUI-test  
      *用以存放所有的 使用Designer设计出来的.ui文件 编译而来的.py **界面**文件，与PYUI文件夹存放的文件不同的是其中的文件是可直接执行的版本，用以测试使用。*  
      *使用的方法是用的external tool的中的 **PYUIC-X***
      
    - Resource  
      *用以存放所有的资源文件*
        - Images  
          *用以存放所有的 **图像资源** 文件*
        - Sounds  
          *用以存放所有的 **音频资源** 文件*
        - Qss  
          *用以存放所有的 **样式** 文件*
        - Sample  
          *用以存放所有的 **初次使用时候提供的样例** 文件*
      
    - UI  
      *用以存放所有的 使用Designer设计出来的.ui文件*
      
    - Utils  
      *用以存放所有的 **工具**文件*
      
    - Widget  
      *用以存放所有的 **组件**文件*
      
    - Window  
      *用以存放所有的 借由PyUI文件夹中的文件生成的，实现业务需求的 **业务** 文件*
      
    - **main.py**  
      *用以启动整个项目的 **主文件***
      
    - **requirements.txt**  
      *使用 pip 模块生成，生成该模块的方法为在项目的Terminal页面中输入如下命令：*  
      pip freeze > requirements.txt
      
      使用如下命令即可完成环境的配置，从而运行该项目(注意该命令运行时，应所处该文件的文件夹下)
      
      pip install -r requirements.txt
---

## 功能性需求

---

## 非功能性需求

---

## 参考书籍
    [1] 《Python Qt GUI与数据可视化编程》 王维波 栗宝鹃 张晓东 著 人民邮电出版社
    [2] 《PyQt5 快速开发与实战》 王硕 孙洋洋 著 电子工业出版社
    [3] 《Python编程 从入门到时间》 [美]埃里克·马瑟斯 著 袁国忠 译 人民邮电出版社
    [4] 《Python编程快速上手--让繁琐工作自动化》 AI Sweigart 著 王海鹏 人民邮电出版社
    [5] https://sites.google.com/site/yao27bat/home/basic/bat1