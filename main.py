#!/usr/bin/python
# =========================================================================
# It is for:
# https://.orangehrm.com/index.php
# This script generates:
#    random starttime
#    random launch period
# Counts 8 hours of working day
# =========================================================================

import random

from datetime import datetime, timedelta
from texttable import Texttable

table = Texttable()
for x in range(24):
    # Generate random start time hours:minutes
    start_h = random.randint(8, 9)
    start_m = random.randint(0, 59)
    start_time = str(start_h) + ':' + str(start_m)
    start = datetime.strptime(start_time, '%H:%M')

    # Generate launch in minutes
    launch_t = random.randint(27, 43)
    launch = datetime.strptime(str(launch_t), '%M')

    # Count time
    some_time = start + timedelta(hours=8, minutes=launch_t)
    # Fill table
    table.add_rows([
        ['Num', 'Start', 'Lunch', 'End'],
        [x, start.strftime('%H:%M'), some_time.strftime('%H:%M'), '00:{}'.format(launch_t)]])

print(table.draw())
