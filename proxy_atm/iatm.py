
from abc import ABC, abstractmethod


# ABC -- not real cannot create instance
# atm = IAtm() # Should be Error

class IAtm(ABC):

    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    def get_total_cash(self) -> int:
        pass

    @abstractmethod
    def is_working(self) -> bool:
        pass

