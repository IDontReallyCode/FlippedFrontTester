from data.generic import Data
from brokers.ib import IB
import pandas as pd
import os

# MOVE TO STRATEGY FILE LATER
symbol_data = {}
source_data = {}

symbol_list = ["AAPL", "MSFT"]
csv_dir = "./"

xxx = Data(source_data, symbol_data)
broker = IB()

for s in symbol_list:
    # Load the CSV file with no header information, indexed on date
    source_data[s] = pd.io.parsers.read_csv(
        os.path.join(csv_dir, '%s.csv' % s),
        header=0, index_col=0,
        names=['datetime', 'open', 'low', 'high', 'close', 'volume', 'oi']
    )

    # Create separate lists for each symbol
    symbol_data[s] = []


for s in symbol_list:


    generator = xxx.get_new_bar(s)
    i = 0

    while i<10:
        current_orders = broker.get_order(s)

        if current_orders is None or not current_orders["ticker"] == s:
            xxx.update_bars(s, generator)

            if i>3:
                my_bars = xxx.get_latest_bars(s, 3)
                # print(my_bars)

                high_1 = my_bars[-2][3]

                date = my_bars[-1][1]
                high_0 = my_bars[-1][3]
                close_0 = my_bars[-1][5]


                order_dict = {
                    "ticker": s,
                    "entry": close_0,

                    "slo_order_id": 1,
                    "slo_action": "BUY",
                    "slo_quantity": 1,
                    "slo_stop_price": 5,
                    "slo_limit_price": 5,
                    "slo_parent_order_id": "",
                    "slo_time_in_force": "GTD",
                    "slo_good_till_date": "datetime-here",

                    "lo_order_id": 1,
                    "lo_action": "BUY",
                    "lo_quantity": 1,
                    "lo_limit_price": 5,
                    "lo_parent_order_id": "",
                    "lo_time_in_force": "GTD",
                    "lo_good_till_date": "datetime-here",

                    "so_order_id": 1,
                    "so_action": "BUY",
                    "so_quantity": 1,
                    "so_stop_price": 5,
                    "so_parent_order_id": "",
                    "so_time_in_force": "GTD",
                    "so_good_till_date": "datetime-here"

                }

                if high_0 < high_1:
                    if current_orders is not None:
                        print(current_orders["ticker"])

                    entry = broker.get_stop_limit_order(order_dict)
                    tp = broker.get_limit_order(order_dict)
                    sl = broker.get_stop_order(order_dict)


                    order = {"ticker": s, "entry": entry, "tp":tp, "sl":sl}
                    broker.send_order(order)

                    print(broker.order_list)



                    # print(broker.order_list)
                    #
                    # broker.execute_order(order_dict)
                    # print("POSTIONS:", broker.pos_list)
                    #

        i += 1
