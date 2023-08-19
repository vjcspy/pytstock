import pandas as pd
from datetime import datetime
from marshmallow import Schema, fields, ValidationError, validate
from modules.core.util.df_get_row_by_column_value import df_get_row_by_column_value


def average_price(row):
    return (row['high'] + row['low']) / 2


class PriceHistorySchema(Schema):
    date = fields.Date(required=True)
    high = fields.Integer(required=True, validate=validate.Range(min=0))
    low = fields.Integer(required=True, validate=validate.Range(min=0))
    close = fields.Integer(required=True, validate=validate.Range(min=0))
    open = fields.Integer(required=True, validate=validate.Range(min=0))
    volume = fields.Integer(required=True, validate=validate.Range(min=0))
    trade = fields.Integer(required=True, validate=validate.Range(min=0))
    value = fields.Integer(required=True, validate=validate.Range(min=0))
    buy = fields.Integer(required=True, validate=validate.Range(min=0))
    buyQuantity = fields.Integer(required=True, validate=validate.Range(min=0))
    sell = fields.Integer(required=True, validate=validate.Range(min=0))
    sellQuantity = fields.Integer(required=True, validate=validate.Range(min=0))


schema = PriceHistorySchema()


class PriceHistoryHelper:
    _date: str = datetime.today().strftime('%Y-%m-%d')

    def __init__(self, data):
        if not isinstance(data, pd.DataFrame) and len(data) > 0:
            schema.load(data[0])
        self._data = data

    def _get_df(self):
        df = pd.DataFrame(self._data)
        sorted_df = df.sort_values(by='date', ascending=False)

        return sorted_df

    def _get_start_date(self, end_date, length):
        data_df = self._get_df()
        end_date = pd.to_datetime(end_date)
        data_df['date'] = pd.to_datetime(data_df['date'])
        data_df = data_df[data_df['date'] <= end_date]
        data_df = data_df.head(length)
        start_date = data_df.iloc[-1]['date']

        return start_date

    def set_date(self, date: str) -> object:
        self._date = date

        return self

    def sma(self, length: int) -> float | None:
        df = self._get_df()
        target_date = self._date

        # Sắp xếp dữ liệu theo ngày giảm dần
        df_sorted = df.sort_values(by="date", ascending=False)

        # Tìm chỉ số của ngày cần tính trong DataFrame
        idx = df_sorted[df_sorted["date"] == target_date].index[0]

        # Kiểm tra xem có đủ dữ liệu để tính SMA không
        if idx + length > len(df_sorted):
            return None

        # Lấy phần dữ liệu cho việc tính SMA
        sma_data = df_sorted.iloc[idx:idx + length]

        # Tính và trả về SMA
        return sma_data["close"].mean()

    def stdev(self, length: int, cal_source_func=lambda row: row['close']):
        df = self._get_df()
        date = self._date
        df['date'] = pd.to_datetime(df['date'])
        end_date = pd.to_datetime(date)
        start_date = self._get_start_date(self._date, length)

        filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

        if len(filtered_df.index) != length:
            return None

        # Sử dụng hàm func để biến đổi dữ liệu
        transformed_data = filtered_df.apply(cal_source_func, axis=1)

        return transformed_data.std()

    def get_current_price(self):
        return df_get_row_by_column_value(self._get_df(), 'date', self._date)
