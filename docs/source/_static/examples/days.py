#!/usr/bin/env python

import random
import datetime as dt

numdays = random.randint(1,365)         # random number between 1 and 365
now = dt.date.today()                   # today's date
then = now - dt.timedelta(days=numdays) # date in the past 'numdays' ago

print ("Today is %s and %d days ago it was %s" % (now,numdays,then))
