import pandas as pd

class IB():
    def __init__(self):
        self.acc_dict = {}
        self.order_list = []
        self.pos_list = []

    # Prepare Orders
    def get_market_order(self, order_dict):
        mkt_order = {"ticker": order_dict["ticker"],
                     "order_id": order_dict["mkt_order_id"],
                     "action": order_dict["mkt_action"],
                     "orderType": 'MKT',
                     "quantity": order_dict["mkt_quantity"],
                     "parentId": order_dict["mkt_parent_order_id"],
                     "tif": order_dict["mkt_time_in_force"],
                     "gtd": order_dict["mkt_good_till_date"]
        }

        return mkt_order

    def get_stop_limit_order(self, order_dict):
        stp_lmt_order = {"ticker": order_dict["ticker"],
                         "order_id": order_dict["slo_order_id"],
                         "action": order_dict["slo_action"],
                         "orderType": 'STP LMT',
                         "quantity": order_dict["slo_quantity"],
                         "lmt_price": order_dict["slo_limit_price"],
                         "stop_price": order_dict["slo_stop_price"],
                         "parentId": order_dict["slo_parent_order_id"],
                         "tif": order_dict["slo_time_in_force"],
                         "gtd": order_dict["slo_good_till_date"]
                        }

        return stp_lmt_order

    def get_limit_order(self, order_dict):
        lmt_order = {"ticker": order_dict["ticker"],
                     "order_id": order_dict["lo_order_id"],
                     "action": order_dict["lo_action"],
                     "orderType": 'LMT',
                     "quantity": order_dict["lo_quantity"],
                     "lmt_price": order_dict["lo_limit_price"],
                     "parentId": order_dict["lo_parent_order_id"],
                     "tif": order_dict["lo_time_in_force"],
                     "gtd": order_dict["lo_good_till_date"]
                     }

        return lmt_order

    def get_stop_order(self, order_dict):
        stp_order = {"ticker": order_dict["ticker"],
                     "order_id": order_dict["so_order_id"],
                     "action": order_dict["so_action"],
                     "orderType": 'STP',
                     "quantity": order_dict["so_quantity"],
                     "stp_price": order_dict["so_stop_price"],
                     "parentId": order_dict["so_parent_order_id"],
                     "tif": order_dict["so_time_in_force"],
                     "gtd": order_dict["so_good_till_date"]
                     }

        return stp_order

    # Send Orders

    def send_oco_order(self):
        pass

    def send_order(self, order_dict):
        self.order_list.append(order_dict)

    # Get Orders/Positions
    def get_order(self, ticker):
        for i in range(0, len(self.order_list)):
            if ticker in self.order_list[i].values():
                return self.order_list[i]

    def get_all_orders(self):
        return self.order_list

    def execute_order(self, order_dict):
        self.pos_list.append(order_dict)


    def get_position(self, ticker):
        for i in range(0, len(self.pos_list)):
            if ticker in self.pos_list[i].values():
                return self.pos_list[i]

    def get_all_positions(self, order_dict):
        return self.pos_list

    # Cancel Orders/Close Positions
    def cancel_order(self):
        pass

    def cancel_all_orders(self):
        pass

    def close_position(self):
        pass

    def close_all_positions(self, order_dict, underlying=False):
        pass