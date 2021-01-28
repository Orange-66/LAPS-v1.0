# LAPS - 左房压医疗影像分析系统

---
## 项目目录结构设计思路
- LAPS
    - Docs
        *用以存放所有 **文档** 文件*
    - PyUI <br>
        *用以存放所有的 使用Designer设计出来的.ui文件 编译而来的.py **界面**文件* <br>
        *使用的方法是用的external tool的中的 **PYUIC***
    - PyUI-test <br>
        *用以存放所有的 使用Designer设计出来的.ui文件 编译而来的.py **界面**文件，与PYUI文件夹存放的文件不同的是其中的文件是可直接执行的版本，用以测试使用。* <br>
        *使用的方法是用的external tool的中的 **PYUIC-X***
    - Resource <br>
        *用以存放所有的资源文件*
        - Images <br>
            *用以存放所有的 **图像资源** 文件*
        - Sounds <br>
            *用以存放所有的 **音频资源** 文件*
    - UI <br>
        *用以存放所有的 使用Designer设计出来的.ui文件*
    - Utils <br>
        *用以存放所有的 **工具**文件*
    - Win
        *用以存放所有的 借由PyUI文件夹中的文件生成的，实现业务需求的 **业务** 文件*
    - main.py <br>
        *用以启动整个项目的 **主文件***
    - requirements.txt <br>
        *使用 pipreqs 模块生成，使用该模块的方法为在项目的Terminal页面中输入如下命令：* <br>
        `pipreqs ./ --encoding utf-8`
    - setup.py <br>
        ***还没明白是干什么的怎么用2333***