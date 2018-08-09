# -*- coding:utf-8 -*-


def strToList(transStr):
    returnCode = '0'
    returnMessage = ''
    returnStr = ''

    try:
        returnStr = eval('[' + transStr.replace('}{', '},{') + ']')
    except BaseException:
        returnCode = '-1'
        returnMessage = '字符串转换对象异常'

    return returnStr
