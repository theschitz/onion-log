import csv
from typing import List

class TableInformationSnapshotParser:
    def __init__(self, datetime_str_format='%Y-%m-%d %H:%M:%S.%f'):
        self._dt_str_fmt = datetime_str_format

    def parse(self, filepath, encoding='utf8', delimiter='\t'):
        with open(filepath, encoding=encoding) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=delimiter)
            table_information_snapshot = TableInformationSnapshot()
            first = True
            for row in csv_reader:
                if not first:
                    table_information_snapshot.table_snapshots.append(TableSnapshot(row))
                first = False
        return table_information_snapshot

class TableInformationSnapshot():
    def __init__(self):
        self.group = None
        self.table_snapshots: List[TableSnapshot] = []


class TableSnapshot():
    def __init__(self, row):
        self.company_name: str = row['Company Name']
        self.table_no: int = int(row['Table No'])
        self.table_name = row['Table Name']
        self.no_of_records: int = int(row['No. of Records'])
        self.record_size: float = self.get_float(row['Record Size'])
        self.size_kb: float = self.get_float(row['Size (KB)'])
        self.no_of_records_after: int = int(row['No. of Records After'])
        self.record_size_after: float = self.get_float(row['Record Size After'])
        self.size_kb_after: float = self.get_float(row['Size (KB) After'])
        self.delta_no_of_records: int = int(row['No. of Records Delta'])
        self.delta_record_size: float = self.get_float(row['Record Size Delta'])
        self.delta_size_kb: float = self.get_float(row['Size (KB) Delta'])
        self.entry_no: int = int(row['Entry No'])
        self.logged_datetime = row['Logged Datetime']
        self.text: str = row['Text']
        self.group: str = row['Group']

    @staticmethod
    def get_float(val: str) -> float:
        val = val.replace(u'\xa0', '').replace(',', '.')
        return float(val)