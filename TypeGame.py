#!/usr/bin/env python3
# encoding:utf-8
# name:TypeGame.py
# @author：gs
# @time：20190831
# @address：tju
"""
main function:打字测速游戏
studied:
1.有关pygame的简单运用
2.按键事件的运用
3.定时器事件的运用
4.字符串去除多个连续空格字符的运用
5.txt文件的ASCII首个字符的注意事项
6.pygame之Button的使用
"""
__doc__ = {'class':['ReadFile', 'Show', 'Operate'], 'function': ['init', 'game', 'restart', 'my_exit']}


import pygame
import sys
import os
from pygame.locals import *
from settings import *
from MyButton import BFButton
import re
import traceback
import threading


class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_txt(self):
        """
        读取txt文件方法
        :return: txt文件所有信息 or None
        """
        if os.path.exists(self.file_path):
            try:
                file_obj = open(self.file_path, 'r', encoding='UTF-8')
            except:
                return None
            else:
                info = file_obj.read()
                file_obj.close()
                return info
        else:
            return None

    def read_image(self):
        """
        用pygame.image.load()方法读取图片数据
        :return: 图片数据Surface类型 or None
        """
        if os.path.exists(self.file_path):
            try:
                file_obj = pygame.image.load(self.file_path)
            except:
                return None
            else:
                image = file_obj.convert_alpha()
                return image
        else:
            return None

    def read_font(self, font_size):
        """
        pygame.font.Font类读取字体数据
        :param font_size: 字体大小
        :return: 字体数据Font类型 or None
        """
        if os.path.exists(self.file_path):
            try:
                pygame.font.init()
                font_obj = pygame.font.Font(self.file_path, font_size)
            except:
                return None
            else:
                return font_obj
        else:
            return None


class Show:
    def __init__(self):
        self.read_file = ReadFile(FONT_PATH)  # 实例化类，用于获取字体

    def show_prompt(self, down_time, right_words_num):
        """
        显示总时间，当前倒计时时间，正确的单词数量
        :param down_time:
        :param right_words_num:
        :return:
        """
        font = self.read_file.read_font(40)
        count_time = "您有%.1f秒的时间玩打字游戏！" % COUNT
        down_time = "倒计时时间：%.1f秒" % down_time
        right_words_num = "正确单词数量：%s个" % right_words_num
        if font:
            show_count_time = font.render(count_time, True, (0, 0, 0), (0, 255, 255))
            show_down_time = font.render(down_time, True, (255, 255, 255))
            show_right_words_num = font.render(right_words_num, True, (255, 255, 255))
            screen.blit(show_count_time, (120, 20))
            screen.blit(show_down_time, (20, 100))
            screen.blit(show_right_words_num, (20, 180))

    def show_words(self, words):
        """
        将words英文短片显示出来
        :param words:
        :return:
        """
        font = self.read_file.read_font(30)
        if font:
            show_words = font.render(words, True, (0, 0, 0))
            screen.blit(show_words, (10, 300))  # 将words显示到该窗口上

    def show_result(self, press_num, right_press_num, right_words_num):
        font1 = self.read_file.read_font(40)
        font2 = self.read_file.read_font(55)
        if font1 and font2:
            right_words = "正确单词数量：%d个" % right_words_num
            press = "总敲击数量：%d" % press_num
            right_press = "正确敲击率：%.2f" % (right_press_num * 100 / (press_num + 10 ** (-6)))  # 加10^-6防止分母为0
            game_over = "GAME OVER!"
            right_words = font1.render(right_words, True, (0, 0, 0))
            press = font1.render(press, True, (0, 0, 0))
            right_press = font1.render(right_press, True, (0, 0, 0))
            game_over = font2.render(game_over, True, (0, 0, 0))
            screen.blit(right_words, (200, 100))
            screen.blit(press, (200, 180))
            screen.blit(right_press, (200, 260))
            screen.blit(game_over, (200, 400))


class Operate:
    def __init__(self, words):
        self.color_green = 0
        self.right_words_num = 0
        self.press_num = 0
        self.right_press_num = 0
        self.current_time = COUNT
        self.words = words

    def press_key(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 电脑键盘按键按下事件
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self.press_num += 1
                if event.key == ord(self.words[0]):  # 按下的健值与字符的ASCII值相等，该字符打字正确
                    if self.words[0] in END_CHARACTER:  # 可能的英文结束符
                        self.right_words_num += 1  # 正确单词数量统计
                    self.words = self.words[1:]  # 向右移动一个字符
                    self.color_green += INCREASE_SPEED  # 向绿色靠近调整变色速度
                    self.right_press_num += 1
                    if self.color_green > 255:
                        self.color_green = 255
            if event.type == TIMER_ID:  # 定时器定时事件
                self.color_green -= DECREASE_SPEED
                if self.color_green < 0:
                    self.color_green = 0
                self.current_time -= INTERVAL * 0.001

    def time_out(self, button):
        for event in pygame.event.get():
            if event.type == TIMER_ID:
                self.current_time -= INTERVAL * 0.001
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            button[0].update(event)
            button[1].update(event)
        button[0].draw()
        button[1].draw()


def init():
    """
    生成主屏幕screen，设置icon，设置title
    :return:
    """
    global screen  # screen是一个Surface类型的全局变量
    pygame.init()  # 初始化模块
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)  # 设置screen左上角坐标
    screen = pygame.display.set_mode(size=(800, 600), flags=0, depth=32, display=0)  # 生成主屏screen
    icon = ReadFile(ICON_PATH).read_image()
    if icon:
        pygame.display.set_icon(icon)  # 设置screen标题栏最左边的图标
    pygame.time.set_timer(TIMER_ID, INTERVAL)  # set_timer(eventid, millsecond)添加定时器，创建一个事件事件
    pygame.display.set_caption("打字测速游戏")  # 设置screen的标题栏标题信息


def restart(btn):
    try:
        game()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        sys.exit()


def my_exit(btn):
    pygame.quit()
    exit()


def game():
    init()
    words = ReadFile(TXT_PATH).read_txt()
    if words:
        words = words.replace('\n', '')  # 去除换行
        words = re.sub(r"\s{2,}", " ", words)  # 把一个字符串中的空格都处理为一个空格形式
        words = words.lower()[1:]  # 由于Windows系统开发的编码为UTF-8(BOM)导致在文件前3个字节加上了EE,BB,BF，char的ASCII码值=65279，显示是一个空字符)
        operate = Operate(words)
        show = Show()
        while operate.current_time > 0:
            screen.fill((255 - operate.color_green, operate.color_green, 0))
            show.show_prompt(operate.current_time, operate.right_words_num)
            show.show_words(operate.words)
            operate.press_key()
            pygame.display.update()

        button_restart = BFButton(screen, (150,500,100,40), text="Restart", click=restart)
        button_exit = BFButton(screen, (550, 500, 100, 40), text="Exit", click=my_exit)
        while operate.current_time <= 0:
            screen.fill((255 - operate.color_green, operate.color_green, 0))
            show.show_result(operate.press_num, operate.right_press_num, operate.right_words_num)
            operate.time_out([button_restart, button_exit])
            pygame.display.update()


if __name__ == '__main__':
    try:
        game()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        sys.exit()