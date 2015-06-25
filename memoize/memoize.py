# coding: utf-8

""" Cached decorater MixIn.
"""
class Mem(object):
    @staticmethod
    def memoize(f):
        def _cache(*args, **kwargs):
            if not hasattr(f, 'cache'):
                f.cache = { }
            result = f.cache.get(f.__name__)
            if result:
                return result
            result = f(*args, **kwargs)
            f.cache[f.__name__] = result
            return result
        return _cache

    @staticmethod
    def has_memo(f):
        if '_cache' in f.__name__:
            return True
        return False
