import datetime


class Data():
    def __init__(self, source_data, symbol_data):
        self.source_data = source_data
        self.symbol_data = symbol_data

    def get_new_bar(self, symbol):
        for bar in self.source_data[symbol].itertuples():
            yield tuple(
                [symbol, datetime.datetime.strptime(bar[0], '%Y-%m-%d %H:%M'), bar[1], bar[2], bar[3], bar[4], bar[5]])

    def update_bars(self, symbol, generator):
        try:
            bar = generator.__next__()
            self.symbol_data[symbol].append(bar)

        except Exception as e:
            print("ERROR: ", e)

    def get_latest_bars(self, symbol, N=1):
        bars = self.symbol_data[symbol]
        symbol_data = bars[-N:]

        return symbol_data


