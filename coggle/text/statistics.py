"""
Package: coggle
Author: finlay
Date: 2024
"""

from typing import AnyStr
import string
import re
import emoji


chinese_re = re.compile(r'[\u4e00-\u9fff]+')
ENGLISH_PUNCTUATION = string.punctuation
CHINESE_PUNCTUATION = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."


def sentence_length(s: AnyStr) -> int:
    '''
    文本字符长度
    '''
    return len(s)


def character_count(s: AnyStr) -> int:
    '''
    文本字符个数
    '''
    return len(set(s))


def whitespaces_count(s: AnyStr) -> int:
    '''
    文本中空格个数
    '''
    return len([x for x in s if x == ' '])


def duplicates_character_count(s: AnyStr) -> int:
    '''
    重复字符个数
    '''
    count = 0
    for idx, c in enumerate(s):
        if c in s[:idx]:
            count += 1
    return count


def emoji_character_count(s: AnyStr) -> int:
    '''
    emoji字符个数
    '''
    return len([c for c in s if c in emoji.EMOJI_DATA])


def english_character_count(s: AnyStr) -> int:
    '''
    英文字符个数
    '''
    return len([c for c in s if c in string.ascii_letters])


def chinese_character_count(s: AnyStr) -> int:
    '''
    中文字符个数
    '''
    result = chinese_re.findall(s)
    return len(''.join(result))


def punctuations_count(s: AnyStr) -> int:
    '''
    标点符号个数
    '''
    return len([c for c in s if c in ENGLISH_PUNCTUATION or c in CHINESE_PUNCTUATION])
