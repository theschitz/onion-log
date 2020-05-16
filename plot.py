#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, time
from onionlog import LogLine, OnionLog, LogLineType
from typing import List
from onionparser import OnionParser

class OnionPlot:
    def __init__(self):
        pass

def main():
    parser = OnionParser(datetime_str_fmt='%Y-%m-%d %H:%M:%S,%f')
    logs: List[OnionLog] = parser.parse('prod.log')
    for log in (x for x in logs if x.code == 'CREATE-INV.CR-MEMO'):
        print(log)
        plt.plot(range(len(log.executed_qty_list)), log.executed_qty_list, label=format_datetime(log.start_datetime))
    if plt:
        plt.ylabel('Processed Contracts')
        plt.title('Create Invoices')
        plt.xlabel('Log point (1 step = 15 minutes)')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'plot/{log.code}.png', dpi=300)

def format_datetime(dt_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S,%f')
    return dt.strftime('%Y-%m-%d')

if __name__ == "__main__":
    main()
