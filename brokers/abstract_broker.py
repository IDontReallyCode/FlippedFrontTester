from abc import ABC, abstractmethod

class Broker(ABC):
    @abstractmethod
    def connect_broker(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'connect_broker' method."
        )

    @abstractmethod
    def get_market_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_market_order' method."
        )

    @abstractmethod
    def get_stop_limit_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_stop_limit_order' method."
        )

    @abstractmethod
    def get_limit_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_limit_order' method."
        )

    @abstractmethod
    def get_stop_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_stop_order' method."
        )

    @abstractmethod
    def send_oto_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'send_oto_order' method."
        )

    @abstractmethod
    def send_oco_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'send_oco_order' method."
        )

    @abstractmethod
    def send_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'send_order' method."
        )

    @abstractmethod
    def get_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_order' method."
        )

    @abstractmethod
    def get_all_orders(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_all_orders' method."
        )

    @abstractmethod
    def get_position(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_position' method."
        )

    @abstractmethod
    def get_all_positions(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'get_all_positions' method."
        )

    @abstractmethod
    def cancel_order(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'cancel_order' method."
        )

    @abstractmethod
    def cancel_all_orders(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'cancel_all_orders' method."
        )

    @abstractmethod
    def close_position(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'close_position' method."
        )

    @abstractmethod
    def close_all_positions(self, *kwargs):
        raise NotImplementedError(
            "Each broker must implement the 'close_all_positions' method."
        )


