#!/usr/bin/env python3
# encoding:utf-8
# name:settings.py


import pygame
from pygame.locals import *

TIMER_ID = pygame.USEREVENT + 1  # 获得计时器的事件ID
COUNT = 60 # 总计60秒
INTERVAL = 100 # 以0.1秒的形式倒计时
INCREASE_SPEED = 20
DECREASE_SPEED = 5
END_CHARACTER = [' ', ',', '?', '!', ':', ';', '-', '——', '(' , ')', '[', ']', '{', '}', '"',"'"]  # 单词可能结束符
FONT_PATH = './resources/msyh.ttf'
ICON_PATH = './resources/icon.png'
TXT_PATH = './resources/MyWords.txt'

CLICK_EFFECT_TIME = 100