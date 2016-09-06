#!/usr/bin/env python
# encoding: utf-8

import sys


class ProgressBar(object):
    """简易进度条
        例子：显示当前进度到 80%, 最大进度为 100%
             pb = ProgressBar()

             当前进度到80%
             pb.progress(percent=0.8)

            for i in range(1, 1001):
                pb.progress(percent=float(i) / 1000, msg='app id -> %d' % i)
                time.sleep(0.01)

            time.sleep(2)
    """
    max = 100
    space = ' '

    def __init__(self, base_char='=', progress_char='>'):

        self.base_char = base_char
        self.progress_char = progress_char
        self.start = 1
        self.sprint('  0% [' + base_char * self.max + ']')

    def sprint(self, content):
        sys.stdout.write(content + '\r')
        sys.stdout.flush()

    def progress(self, percent, msg=None):
        if percent > 1:
            percent = 1
        elif percent < 0:
            percent = 0

        for i in range(self.start, int(percent * self.max) + 1):
            p = str(i)
            ln = len(p)
            display = self.space * (
                3 - ln) + p + '% [' + self.progress_char * i + self.base_char * (
                self.max - i - 1) + '] '
            if msg:
                display += msg + self.space * self.max
            self.sprint(display)
            self.start = i
