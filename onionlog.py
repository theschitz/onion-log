#!/usr/bin/env python3
from datetime import datetime
from duration import Duration
from typing import List
from onion_enums import LogLineType


class OnionLog:
    """
    Onion Log Class
    """
    def __init__(self, group, category, code, start_dt: datetime):
        self._datetime_format = '%Y-%m-%d %H:%M:%S.%f'
        self.group = group
        self.category = category
        self.code = code
        self.start_datetime = start_dt
        self.end_datetime = None
        self.log_lines: List[LogLine] = []        
        self.average_executed: float = 0

    def __repr__(self):
        return f'{self.__class__.__name__}(group={self.group}, category={self.category}, code={self.code}, start_dt={self.start_datetime})'

    def __str__(self):
        return f'{self.group} {self.code} {self.duration_timedelta} AVG: {self.average_executed}'

    def set_datetime_format(self, dt_str_fmt):
        self._datetime_format = dt_str_fmt

    def finalize(self, end_datetime: datetime):
        self.end_datetime = end_datetime
        self.calculate_average()

    @property
    def min_executed_qty(self) -> int:
        return 0 if len(self.executed_qty_list) == 0 else min(self.executed_qty_list)         

    @property
    def max_executed_qty(self) -> int:
        return 0 if len(self.executed_qty_list) == 0 else max(self.executed_qty_list)

    @property
    def len_log_lines(self) -> int:
        return len(self.executed_qty_list)
    
    @property
    def sum_log_lines(self) -> int:
        return sum(self.executed_qty_list)
    
    @property
    def executed_qty_list(self) -> List[int]:
        return [line.executed_qty_since_last_log for line in self.log_lines if line.type == LogLineType.RUNNING]

    @property
    def info_lines(self):
        return [line for line in self.log_lines if line.type == LogLineType.INFO]

    @property
    def duration(self):
        return Duration(self.start_datetime, self.end_datetime, dt_format=self._datetime_format)

    @property
    def duration_timedelta(self):
        return self.duration.datetime_delta

    @property
    def running_lines(self):
        return [line for line in self.log_lines if line.type == LogLineType.RUNNING]

    def get_log_timestamps(self):
        return [line.log_time for line in self.running_lines]

    def calculate_average(self) -> float:
        self.average_executed = self.sum_log_lines / self.len_log_lines if self.len_log_lines > 0 else 0          
    
    def print_info_lines(self):
        for info in self.info_lines:
            print(info.text)


class LogLine:
    """
    Log Line Class
    """
    def __init__(self, log_line: str, delimiter: str = '\t'):
        line = log_line.split(delimiter)
        self.entry_no: int = int(line[0])
        self.category = line[1]
        self.code = line[2]
        self.group =  line[3]
        self.type: LogLineType =  LogLineType.get_line_type(line[4])
        self.period = line[5]
        self.log_time = line[6]
        self.executed_qty_since_last_log: int = int(line[7])
        self.inital_count: int =  int(line[8])
        self.text = line[9]

