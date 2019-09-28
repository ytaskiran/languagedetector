# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:58:05 2019

@author: ytask
"""


def detectLang(text):
    import langid
    lang = langid.classify(text)[0]
    return lang

