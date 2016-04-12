#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from inotify.skeleton import fib

__author__ = "Brian Bruggeman"
__copyright__ = "Brian Bruggeman"
__license__ = "apache"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
