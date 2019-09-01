#!/usr/bin/env python3
# encoding:utf-8
# name:game.py

import pygame
import sys
import os
from pygame.locals import *


class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_txt(self):
        """
        读取txt文件方法
        :return: txt文件所有信息 or False
        """
        if os.path.exists(self.file_path):
            try:
                file_obj = open(self.file_path, 'r', encoding='UTF-8')
            except:
                return False
            else:
                info = file_obj.read()
                file_obj.close()
                return info
        else:
            return False

    def read_image(self):
        """
        用pygame库读取图片数据
        :return: 图片数据Surface类型 or False
        """
        if os.path.exists(self.file_path):
            try:
                file_obj = pygame.image.load(self.file_path)
            except:
                return False
            else:
                image = file_obj.convert_alpha()
                return image
        else:
            return False


def init():
    """
    生成主屏幕screen，设置icon，设置title
    :return:
    """
    global screen  # screen是一个Surface类型的全局变量
    pygame.init()  # 初始化模块
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)  # 设置screen左上角坐标
    screen = pygame.display.set_mode(size=(800, 600), flags=0, depth=32, display=0)  # 生成主屏screen
    icon = ReadFile('./resources/MySQL.jpg').read_image()
    # icon = pygame.image.load('./resources/MySQL.jpg').convert_alpha()  # 加载图片，并将图片数据转成Surface类型
    if icon:
        pygame.display.set_icon(icon)  # 设置screen标题栏最左边的图标
    pygame.display.set_caption("打字测速游戏")  # 设置screen的标题栏标题信息


def move_mouse_with_image(mouse_cursor):
    """
    鼠标光标处带一张小图片icon
    :param mouse_cursor:图片的Surface数据
    :return:移动后的鼠标位置
    """
    x, y = pygame.mouse.get_pos()  # 获取鼠标位置
    # 计算鼠标左上角的位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    return x, y


def main():
    init()
    mouse_cursor = ReadFile('./resources/icon.png').read_image()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                print(event.key)
            elif event.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            screen.fill((0, 255, 255))
            if mouse_cursor:
                screen.blit(mouse_cursor, move_mouse_with_image(mouse_cursor))
        pygame.display.update()


if __name__ == '__main__':
    main()