#!/usr/bin/env python
# coding: utf-8

# In[1]:


# datetime.date (Y, M, D)
# datetime.time(h, m, s, ms)
# datetime.datetime(Y, M, D, H, m, s, ms)


# In[2]:


from datetime import date

today = date.today()  # date object

print(today)  # gives year, month, and day


# In[3]:


print(today.month, today.day, today.year)
print(today.month)
print(today.day)
print(today.year)

# Monday starts at 0, Sunday is 6 (last day of week)
print(today.weekday())


# In[4]:


import datetime
birthday = datetime.date(2000, 12, 17)
print(birthday)


# In[5]:


# add 10 hours to current date
hour_delta = datetime.timedelta(hours=10)

print(datetime.datetime.now())
print(datetime.datetime.now() + hour_delta)


# In[6]:


# time zones

# Date times are not aware by default
# naive means it doesn't understand time zones (mountain, pacific, etc.)
# aware means not naive

datetime.datetime.now()


# In[7]:


# pip install pytz
# python time zones
import pytz

# (Y, M, D, H, m, s, ms) UTC enabled, it is now time zone aware
datetime.datetime.now(tz=pytz.UTC)


# In[8]:


datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_central = datetime_today.astimezone(pytz.timezone('US/Central'))
print(datetime_central)


# In[9]:


# to find all timezones
for tz in pytz.all_timezones:
    print(tz)


# In[10]:


# String formatting with dates
# 2019-08-23 -> August 23, 2019
# %B is Month, %d is day, %Y is year
datetime_central.strftime('%B %d, %Y')  # f means formatting


# In[11]:


# March 09, 2019 -> datetime(2019, 3, 9)
#strptime  , p means parse
# format into number format
datetime_thing = datetime.datetime.strptime('March 09, 2019', '%B %d, %Y')
print(repr(datetime_thing))


# In[12]:


# use Maya which is already time zone aware
# Delorean, Arrow, & Pendulum


# In[ ]:




