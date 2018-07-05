#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'dreamapple'

SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, a_kilobyte_is_1024_bytes=False):
    """
    Convert a file size to human-readable form.

    :param size: file size in bytes
    :param a_kilobyte_is_1024_bytes: if True (default), use multiples of 1024
                                     if False, use multiples of 1000
    :return: string

    """

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)


if __name__ == '__main__':
    print(approximate_size(1000000, True))
    print(approximate_size(1000000))
