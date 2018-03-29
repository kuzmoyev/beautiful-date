# Beautiful Date
Simple and beautiful way to create date and datetime objects in Python.
       
**Before**:

    from datetime import date, datetime
    
    d = date(year=2018, month=3, day=25)
    t = datetime(year=2018, month=3, day=25, hour=23, minute=45)
    
**After**:

    from beautiful_date import *
    
    d = 25/Mar/2018
    t = (25/Mar/2018)[23:45]


## Examples

### Create Date

Using months names:

    >>> from beautiful_date import *
    
    >>> 25/Mar/2018  # European format
    BeautifulDate(2018, 3, 25)
    >>> Mar/25/2018  # US format
    BeautifulDate(2018, 3, 25)
    
Using months numbers:

    >>> D @ 25/3/2018  # European format (default)
    BeautifulDate(2018, 3, 25)
    
    >>> D = MDY()  # Add this at the top of your script to use US format. 
    >>> d = D @ 3/25/2018  # US format
    BeautifulDate(2018, 3, 25)
    
Available formats:
    
    class DMY(BaseDateFormat):
        _format = 'day', 'month', 'year'

    class MDY(BaseDateFormat):
        _format = 'month', 'day', 'year'
    
    class YMD(BaseDateFormat):
        _format = 'year', 'month', 'day'
    
    class YDM(BaseDateFormat):
        _format = 'year', 'day', 'month'
 
 
### Create Datetime

Previous methods create `BeautifulDate` objects which are inherited from `date` but can be 
easily extended to `datetime` using indexing/slicing:
 
    >>> (Oct/16/1995)[:]
    datetime.datetime(1995, 10, 16, 0, 0)

    >>> (Oct/16/1995)[23]
    datetime.datetime(1995, 10, 16, 23, 0)

    >>> (Oct/16/1995)[23:14]
    datetime.datetime(1995, 10, 16, 23, 14)

    >>> (Oct/16/1995)[23:14:10]
    datetime.datetime(1995, 10, 16, 23, 14, 10)

You can also use prefix `D @` if you need months by their numbers:    
    
    >>> (D @ 16/10/1995)[:]
    datetime.datetime(1995, 10, 16, 0, 0)

    >>> (D @ 16/10/1995)[23]
    datetime.datetime(1995, 10, 16, 23, 0)

    >>> (D @ 16/10/1995)[23:14]
    datetime.datetime(1995, 10, 16, 23, 14)

    >>> (D @ 16/10/1995)[23:14:10]
    datetime.datetime(1995, 10, 16, 23, 14, 10)
    
### Date/Datetime manipulations:

This library also provides simple interface for 
[relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html) from 
[dateutil](http://dateutil.readthedocs.io/en/stable/index.html)

#### Adding/Subtracting/Setting timedeltas:

Notice singular time unit (year, month, ...) sets given value, plural (years, months,) adds it.


    >>> d = 26/Mar/2018
    >>> t = d[12:23:15]
    
    >>> d + 2 * years
    BeautifulDate(2020, 3, 26)
    >>> d - 2 * days
    BeautifulDate(2018, 3, 24)
    
    >>> t + 25 * hours
    datetime.datetime(2018, 3, 27, 13, 23, 15)
    
Available deltas: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, 
`seconds`, `microseconds`, `leapdays`
(see [relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html)).


    >>> d = 26/Mar/2018
    >>> t = d[12:23:15]
    
    >>> d + 2 * year
    BeautifulDate(2, 3, 26)
    >>> d += 2 * day
    >>> d
    BeautifulDate(2018, 3, 2)
    
    >>> t + 22 * hours
    datetime.datetime(2018, 3, 26, 22, 23, 15)
    >>> t += 22 * hours
    >>> t
    datetime.datetime(2018, 3, 26, 22, 23, 15)

Available setters: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`,
`yearday` and `nlyearday`
(see [relativedelta](http://dateutil.readthedocs.io/en/stable/relativedelta.html)).


#### Weekdays:

Get next Monday:

    >>> d = 29/Mar/2018  # Thursday
    >>> d + MO  # Equivalent to MO(1)
    BeautifulDate(2018, 4, 2)

Get second to next Monday:

    >>> d = 29/Mar/2018
    >>> d + MO(2)
    BeautifulDate(2018, 4, 9)

Get last Saturday:

    >>> d = 29/Mar/2018
    >>> d - SA
    BeautifulDate(2018, 3, 24)

Get second to last Saturday:

    >>> d = 29/Mar/2018
    >>> d - SA(2)
    BeautifulDate(2018, 3, 17)

Get second to last Saturday (same as previous):

    >>> d = 29/Mar/2018
    >>> d + SA(-2)
    BeautifulDate(2018, 3, 17)