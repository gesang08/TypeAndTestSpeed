## 打字测速游戏
### 要求：
利用面向对象的方式实现逻辑层显示层分离，用pygame完成响应键盘敲击速度的游戏：
随机截取一段英文短文。统计一分钟内用户对照输入的正确的单词数量并实时根据键盘敲击的速度显示屏幕背景色。
越快屏幕颜色就越偏向绿色。越慢越偏向红色。</br>

### 功能：
1.根据界面显示的英文文章，敲击键盘，英文从左向右滚动；</br>
2.敲击正确单词的速度越快，屏幕背景就越偏向绿色，否则就越慢越偏向红色</br>
3.显示倒计时时间，敲击的正确单词数量，敲击的准确率等；</br>
4.点击Restart按钮可以重新开始游戏，点击Exit按钮可以退出游戏</br>

### 运行界面:
![image](https://github.com/gesang08/TypeAndTestSpeed/raw/master/result/running.png)
</br>
### 结果显示：
![image](https://github.com/gesang08/TypeAndTestSpeed/raw/master/result/end.jpg)
</br>
### other idea:
1.构建UI界面，点击开始游戏，运行游戏主函数；</br>
2.菜单栏有注册、登陆、设置（时间、速度、背景等参数）、英文输入富文本写入txt文件、帮助（游戏相关介绍等）；</br>
3.不限制与英文，可以是中文，或者中文英文混合等。</br>