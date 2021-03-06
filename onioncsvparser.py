#!/usr/bin/env python3
from onionlog import LogLine, OnionLog, LogLineType
from typing import List
import csv        

class OnionCSVParser:
    """
    CSV Parser for Onion Log
    """
    def __init__(self, datetime_str_fmt = '%Y-%m-%d %H:%M:%S.%f'):
        self.datetime_str_fmt = datetime_str_fmt

    def parse(self, filepath, encoding='utf8', delimiter='\t') -> list:
        logs: [OnionLog] = []
        onion_log: OnionLog = None
        with open(filepath, encoding='utf8') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=delimiter)
            for row in csv_reader:                
                log_line: LogLine = LogLine(row)
                
                if log_line.type == LogLineType.START:
                    onion_log = OnionLog(log_line.group, log_line.category, log_line.code, log_line.log_time)
                    onion_log.set_datetime_format(self.datetime_str_fmt)

                onion_log.log_lines.append(log_line)
                
                if log_line.type == LogLineType.STOP:
                    onion_log.finalize(log_line.log_time)
                    logs.append(onion_log)
                    onion_log = None

        return logs

def main():
    parser = OnionCSVParser(datetime_str_fmt='%Y-%m-%d %H:%M:%S,%f')
    logs: List[OnionLog] = parser.parse('ver1.log')
    for log in logs:
        print(log)        
        log.print_info_lines()
        if log.len_log_lines > 0:
            print('Min:', log.min_executed_qty)
            print('Max:', log.max_executed_qty)


if __name__ == '__main__':
    main()