# -*- coding: utf-8 -*-


def uweb(*args):
    print("utils: %s" % args)


def get(url):
    print("url: ", url)


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
