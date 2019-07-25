# cli_cal

想做一款通过命令行和快捷键来控制的计算器

---



版本： v1

现在只能做做四则运算 !!!∑(ﾟДﾟノ)ノ



兼容性：windows 10 x64



---



## 使用

#### 下载

1. 进入[发布页面](https://github.com/cxwithyxy/cli_cal/releases)
2. 下载 cal.7z
3. 用压缩工具解压 cal.7z 到你想放的位置

#### 配置

1. win+r 打开运行窗口
2. 输入 control system
3. 打开 系统 -> 高级系统设置 -> 环境变量
4. 在系统变量中找到path，选中path并点击编辑
5. 点击新建，输入cal的路径（路径长这个样 D:\cal）
6. 一直点击确定直到关闭那些窗口

#### 日常使用

1. win+r 打开运行窗口
2. 输入 cal 加数学表达式，例如这样 cal 100+5-50*5%
3. 然后便会弹出结果窗口
4. 按快捷键 ctrl + c 直接复制计算结果
5. 按快捷键 ctrl + w 关闭结果窗口



----



## 开发

#### 安装依赖

```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

#### 打包EXE

```
pyinstaller index.spec
```