<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Python `datetime` Module — Student Guide for Django

This guide explains Python’s `datetime` module in a practical way, focused on what you need when building Django projects: creating dates, formatting them, parsing user input, doing date math, and—critically—handling time zones correctly in Django.[^1][^2][^3]

***

## 1) Why `datetime` matters in Django

- Django models often store `DateTimeField` and `DateField`.
- Templates display dates in human-readable formats.
- Forms accept date/time strings from users and must convert them to Python objects.
- Time zones affect correctness when users are in different regions.[^2][^4][^1]

In Django, you should **prefer timezone-aware datetimes** and use `django.utils.timezone` instead of raw `datetime.datetime.now()` in most cases.[^3][^1][^2]

***

## 2) Importing and basic usage

```python
import datetime

# Current local date and time (naive — no timezone info)
now = datetime.datetime.now()
print(now)              # e.g. 2026-08-24 17:25:00.123456
print(now.year)         # 2026
print(now.month)        # 8
print(now.day)          # 24
print(now.strftime("%A"))  # e.g. "Monday"
```

Key points:

- `datetime` is a **module**, and also a **class** inside that module: `datetime.datetime`.
- A `datetime` object contains year, month, day, hour, minute, second, and microsecond.[^5][^6]

***

## 3) Creating date and datetime objects

### Date only

```python
import datetime

d = datetime.date(2026, 8, 24)   # year, month, day
print(d)          # 2026-08-24
print(d.year)     # 2026
```


### Date + time

```python
import datetime

dt = datetime.datetime(2026, 8, 24, 14, 30, 0)  # year, month, day, hour, minute, second
print(dt)         # 2026-08-24 14:30:00
```

Optional parameters: `microsecond`, `tzinfo` (for time zones).[^6][^5]

***

## 4) Formatting dates: `strftime()`

Use `strftime()` to turn a `datetime` (or `date`) into a **string** for display.

```python
import datetime

dt = datetime.datetime(2026, 8, 24, 14, 5, 9)

print(dt.strftime("%Y-%m-%d"))          # 2026-08-24
print(dt.strftime("%d/%m/%Y"))          # 24/08/2026
print(dt.strftime("%B %d, %Y"))         # August 24, 2026
print(dt.strftime("%A, %B %d, %Y"))     # Monday, August 24, 2026
print(dt.strftime("%I:%M %p"))          # 02:05 PM
print(dt.strftime("%Y-%m-%d %H:%M:%S")) # 2026-08-24 14:05:09
```


### Common format codes

| Code | Meaning | Example |
| :-- | :-- | :-- |
| `%Y` | 4-digit year | 2026 |
| `%y` | 2-digit year | 26 |
| `%m` | Month (01–12) | 08 |
| `%B` | Full month name | August |
| `%b` | Short month name | Aug |
| `%d` | Day of month (01–31) | 24 |
| `%A` | Full weekday name | Monday |
| `%a` | Short weekday name | Mon |
| `%H` | Hour (00–23) | 14 |
| `%I` | Hour (01–12) | 02 |
| `%M` | Minute (00–59) | 05 |
| `%S` | Second (00–59) | 09 |
| `%p` | AM/PM | PM |
| `%f` | Microsecond (000000–999999) | 123456 |
| `%z` | UTC offset (+0200, -0500, etc.) | +0300 |
| `%Z` | Timezone name (if available) | EEST |

These are the codes you’ll use most in Django templates and logs.[^7][^8][^9][^5][^6]

***

## 5) Parsing strings: `strptime()`

When users send dates as strings (forms, APIs), use `strptime()` to convert them to `datetime` objects.

```python
import datetime

s = "24/08/2026"
dt = datetime.datetime.strptime(s, "%d/%m/%Y")
print(dt)        # 2026-08-24 00:00:00
print(dt.date()) # 2026-08-24
```

Common patterns:

```python
datetime.datetime.strptime("2026-08-24", "%Y-%m-%d")
datetime.datetime.strptime("24-08-2026 14:30", "%d-%m-%Y %H:%M")
datetime.datetime.strptime("Aug 24, 2026", "%b %d, %Y")
```

Rule of thumb: **inside your code, keep dates as `datetime`/`date` objects**; only convert to strings at the boundaries (templates, APIs, files).[^10][^6][^7]

***

## 6) Date arithmetic with `timedelta`

Use `timedelta` to add/subtract days, hours, etc.

```python
import datetime

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
last_week = now - datetime.timedelta(weeks=1)
two_hours_later = now + datetime.timedelta(hours=2)

print(tomorrow.date())      # date part only
print((tomorrow - now).days)  # 1
```

Typical Django uses:

- “Show posts from the last 7 days.”
- “Expire tokens after 1 hour.”
- “Calculate due dates.”[^6][^10]

***

## 7) Time zones: naive vs aware

This is crucial in Django.

- **Naive datetime**: no timezone info (`tzinfo=None`). Example: `datetime.datetime.now()`.
- **Aware datetime**: has timezone info (`tzinfo` set). Example: `django.utils.timezone.now()` when `USE_TZ=True`.[^1][^2][^3]

Django’s default (and recommended) setting:

```python
# settings.py
USE_TZ = True  # store datetimes in UTC, convert to local time when displaying
```

With `USE_TZ = True`:

- `django.utils.timezone.now()` → **aware** datetime in UTC.
- `datetime.datetime.now()` → **naive** local time (dangerous in Django).[^2][^3][^1]


### Correct pattern in Django

```python
from django.utils import timezone
import datetime

# Recommended: timezone-aware now (UTC)
now = timezone.now()

# If you must create a specific datetime in UTC:
dt_utc = timezone.make_aware(
    datetime.datetime(2026, 8, 24, 14, 30),
    timezone=datetime.timezone.utc
)
```

Never compare naive and aware datetimes directly; Django/Python will raise:

> TypeError: naive and aware datetime objects cannot be compared

Fix by making all datetimes aware (using `timezone.make_aware` or `timezone.now()`).[^11][^3][^1]

***

## 8) Using `datetime` in Django models

Example model:

```python
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    published_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)
```

Notes:

- Use `default=timezone.now` (the function), **not** `default=timezone.now()`.
- `DateTimeField` stores timezone-aware datetimes when `USE_TZ=True`.[^1][^2]

Creating instances:

```python
from django.utils import timezone
from myapp.models import Article

article = Article(
    title="Hello",
    published_at=timezone.now(),
    expires_at=timezone.now() + timezone.timedelta(days=7)
)
article.save()
```


***

## 9) Formatting dates in Django templates

In templates, use the `date` and `time` filters instead of calling `strftime()` directly.

```django
{{ article.published_at|date:"F d, Y" }}        <!-- August 24, 2026 -->
{{ article.published_at|date:"d/m/Y" }}         <!-- 24/08/2026 -->
{{ article.published_at|date:"l, F d, Y" }}     <!-- Monday, August 24, 2026 -->
{{ article.published_at|time:"H:i" }}           <!-- 14:30 -->
{{ article.published_at|date:"Y-m-d H:i:s" }}   <!-- 2026-08-24 14:30:00 -->
```

Template format codes are similar but not identical to Python’s; think of them as Django’s version of `strftime`.[^2][^1]

***

## 10) Common pitfalls and how to avoid them

1. **Using `datetime.now()` in Django code**
    - Problem: returns naive local time.
    - Fix: use `timezone.now()` instead.[^3][^1][^2]
2. **Mixing naive and aware datetimes**
    - Problem: comparisons and arithmetic fail.
    - Fix: ensure all datetimes are aware; use `timezone.make_aware()` when needed.[^11][^3]
3. **Hardcoding format strings everywhere**
    - Problem: inconsistent date formats.
    - Fix: define constants, e.g.:

```python
DATETIME_DISPLAY_FORMAT = "%Y-%m-%d %H:%M"
```

and reuse them.[^12]
4. **Storing formatted strings in the database**
    - Problem: can’t do date queries or arithmetic.
    - Fix: store `DateTimeField`/`DateField`, format only for display.[^10]

***

## 11) Quick reference cheat sheet

```python
import datetime
from django.utils import timezone

# Now (Django-safe, aware, UTC)
now = timezone.now()

# Create a date
d = datetime.date(2026, 8, 24)

# Create a datetime (naive)
dt_naive = datetime.datetime(2026, 8, 24, 14, 30)

# Make it aware (UTC)
dt_aware = timezone.make_aware(dt_naive, timezone=datetime.timezone.utc)

# Format to string
s = dt_aware.strftime("%Y-%m-%d %H:%M:%S")

# Parse string to datetime
dt_parsed = datetime.datetime.strptime("2026-08-24 14:30:00", "%Y-%m-%d %H:%M:%S")

# Date arithmetic
future = now + datetime.timedelta(days=7)
past = now - datetime.timedelta(hours=3)
```


***

If you tell me your students’ level (beginner/intermediate) and whether you want examples tied to a specific Django feature (e.g., blogs, events, deadlines), I can adapt this into a shorter handout or add exercises with solutions.[^6][^1][^2]
<span style="display:none">[^13][^14][^15]</span>

<div align="center">⁂</div>

[^1]: https://blog.mikihands.com/en/whitedec/2025/11/10/django-datetime-timezone/

[^2]: https://pylandschool.com/en/blog/article/django-timezones-explained/

[^3]: https://blog.mikihands.com/en/whitedec/2025/11/14/django-utils-timezone-guide/

[^4]: https://www.educative.io/courses/master-modern-django-admin-customization-and-architecture/handling-timezone-aware-admin-logic

[^5]: https://docs.kanaries.net/topics/Python/python-datetime

[^6]: https://coddy.tech/docs/python/datetime

[^7]: https://www.datacamp.com/tutorial/converting-strings-datetime-objects

[^8]: https://pytutorial.com/python-datetime-strftime-guide/

[^9]: https://geratools.com/python-datetime-format-codes

[^10]: https://python-academy.org/en/guide/datetime-handling

[^11]: https://openillumi.com/en/en-python-datetime-naive-aware-error-fix/

[^12]: https://www.pyinns.com/python/regular-expressions/formatting-datetime-in-python-complete-guide-for-data-science-2026

[^13]: https://mkaz.blog/working-with-python/dates/

[^14]: https://strftime.dev/

[^15]: https://fossies.org/linux/django/django/utils/timezone.py

