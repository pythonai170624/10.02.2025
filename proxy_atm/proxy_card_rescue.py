# proxy_atm/proxy_atm.py
from typing import override

from proxy_atm import IAtm
from real_atm import RealATM


class CardRescueProxyATM(IAtm):
    def __init__(self):
        self.atm = RealATM()  # Proxy holds a reference to the real object

    @override
    def deposit(self, amount: int):
        raise RuntimeError("cannot do this operation online")

    @override
    def withdraw(self, amount: int) -> bool:
        raise RuntimeError("cannot do this operation online")

    @override
    def insert_card(self):
        raise RuntimeError("cannot do this operation online")

    @override
    def eject_card(self):
        self.atm.eject_card()

    @override
    def get_total_cash(self) -> int:
        raise RuntimeError("cannot do this operation online")

    @override
    def is_working(self) -> bool:
        raise RuntimeError("cannot do this operation online")
