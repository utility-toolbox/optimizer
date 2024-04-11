# -*- coding=utf-8 -*-
r"""

"""
import mimetypes


__all__ = ['get_mimetype']


def get_mimetype(filename: str) -> str:
    mime, _encoding = mimetypes.guess_type(filename)
    return mime or "unknown/unknown"
