from datetime import datetime, timedelta


class Duration():
    def __init__(self, start_datetime, end_datetime, dt_format='%Y-%m-%d %H:%M:%S.%f'):
        self.dt_str_fmt = dt_format
        self.start_datetime: datetime = datetime.strptime(start_datetime, self.dt_str_fmt)
        self.end_datetime: datetime = datetime.strptime(end_datetime, self.dt_str_fmt)

    def __repr__(self):
        return f'{self.__class__.__name__}(start_datetime={self.start_datetime}, end_datetime={self.end_datetime}, dt_format={self.dt_str_fmt})'

    def __str__(self):
        return f'Start datetime: {self.start_datetime} End Datetime: {self.end_datetime} Datetime delta: {self.datetime_delta}'

    @property
    def datetime_delta(self) -> timedelta:
        return self.end_datetime - self.start_datetime
