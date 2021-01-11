# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from logging import Filter

import sys
from six import text_type, string_types, binary_type
from six.moves import queue


def is_python_version(*versions):
    for version in versions:
        if (sys.version_info[0] == version[0] and
                sys.version_info >= version):
            return True
    return False


try:
    from functools import total_ordering
except ImportError:
    def total_ordering(cls):  # noqa
        """Class decorator that fills in missing ordering methods"""
        convert = {
            '__lt__': [('__gt__', lambda self, other: other < self),
                       ('__le__', lambda self, other: not other < self),
                       ('__ge__', lambda self, other: not self < other)],
            '__le__': [('__ge__', lambda self, other: other <= self),
                       ('__lt__', lambda self, other: not other <= self),
                       ('__gt__', lambda self, other: not self <= other)],
            '__gt__': [('__lt__', lambda self, other: other > self),
                       ('__ge__', lambda self, other: not other > self),
                       ('__le__', lambda self, other: not self > other)],
            '__ge__': [('__le__', lambda self, other: other >= self),
                       ('__gt__', lambda self, other: not other >= self),
                       ('__lt__', lambda self, other: not self >= other)]
        }
        roots = set(dir(cls)) & set(convert)
        if not roots:
            raise ValueError('must define at least one ordering operation: < > <= >=')  # noqa
        root = max(roots)  # prefer __lt__ to __le__ to __gt__ to __ge__
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = str(opname)
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls


PY2 = sys.version_info[0] == 2


def as_text(v):
    if v is None:
        return None
    elif isinstance(v, binary_type):
        return v.decode('utf-8')
    elif isinstance(v, text_type):
        return v
    else:
        raise ValueError('Unknown type %r' % type(v))


def decode_redis_hash(h):
    return dict((as_text(k), h[k]) for k in h)


try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


try:
    from datetime import timezone
except ImportError:
    import pytz as timezone


class LoggingFilter(Filter):
    def __init__(self, method, name='', ):
        super(LoggingFilter, self).__init__(name)
        self.callable = method

    def filter(self, record):
        return self.callable(record)
