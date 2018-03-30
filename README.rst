.. image:: https://travis-ci.org/kuzmoyev/beautiful-date.svg?branch=master
    :target: https://travis-ci.org/kuzmoyev/beautiful-date

**Before**:

::

    from datetime import date, datetime

    d = date(year=2018, month=3, day=25)
    t = datetime(year=2018, month=3, day=25, hour=23, minute=45)

**After**:

::

    from beautiful_date import *

    d = 25/Mar/2018
    t = (25/Mar/2018)[23:45]


Installation
==============

::

    pip install beautiful-date