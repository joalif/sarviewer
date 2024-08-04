#!/usr/bin/env python2
"""
Author        :Julio Sanz
Website       :www.elarraydejota.com
Email         :juliojosesb@gmail.com
Description   :Generate tasks graph from loadaverage.dat file
Dependencies  :Python 2.x, matplotlib
Usage         :python tasks.py
License       :GPLv3
"""

import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import csv
from datetime import datetime
import matplotlib.dates

# ======================
# VARIABLES
# ======================

# Aesthetic parameters
plt.rcParams.update({'font.size': 8})
plt.rcParams['lines.linewidth'] = 0.5
time_format = matplotlib.dates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(time_format)
plt.gcf().autofmt_xdate()

# Time (column 0)
x = []
# Data arrays
aqu_sz = []
r_await = []
util = []

# ======================
# FUNCTIONS
# ======================

def generate_graph():
    with open('../../data/dm-2.dat', 'r') as csvfile:
        data_source = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
        for row in data_source:
            # [0] column is a time column
            # Convert to datetime data type
            a = datetime.strptime((row[0]),'%H:%M:%S')
            x.append((a))
            # The remaining columns contain data
            aqu_sz.append(float(row[7]))
            r_await.append(float(row[8]))
            # util.append(float(row[9]))
    
    # Plot lines
    plt.plot(x,aqu_sz, label='Avg queue size', color='g')
    plt.plot(x,r_await, label='AVG wait', color='r')
    # plt.plot(x,util, label='Bandwidth util for dev', color='m')
    
    # Graph properties
    plt.xlabel('Time',fontstyle='italic')
    # plt.ylabel('Tasks',fontstyle='italic')
    plt.title('DM-2')
    # plt.grid(linewidth=0.4, antialiased=True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)
    # plt.legend(loc=0)
    plt.tight_layout()
    plt.autoscale(True)
    
    # Graph saved to PNG file
    # plt.savefig('../../graphs/tasks.png', bbox_inches='tight')
    plt.savefig('../../graphs/dm-2.pdf')
    #plt.show()

# ======================
# MAIN
# ======================

if __name__ == '__main__':
    generate_graph()
