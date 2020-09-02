import unittest
from table_information_snapshot import TableInformationSnapshot, TableInformationSnapshotParser, TableSnapshot

class TestTableInformationSnapshot(unittest.TestCase):
    def test_parser(self):
        parser = TableInformationSnapshotParser('%Y-%m-%d %H:%M:%S,%f')
        snapshot = parser.parse('data/table_information_snapshot.csv')
        self.assertIsInstance(snapshot, TableInformationSnapshot)
        
    def test_table_information_snapshot(self):
        parser = TableInformationSnapshotParser('%Y-%m-%d %H:%M:%S,%f')
        snapshot = parser.parse('data/table_information_snapshot.csv')
        self.assertEqual(len(snapshot.table_snapshots), 1457)