# proxy_atm/real_atm.py
from typing import override

from iatm import IAtm

class RealATM(IAtm):

    def __init__(self):
        self.total_money = 1_000_000

    @override
    def deposit(self, amount: int):
        print(f"Deposit {amount}")

    @override
    def withdraw(self, amount: int) -> bool:
        print(f"Withdrawing {amount}")
        return amount < self.total_money

    @override
    def insert_card(self):
        print("Inserting card")

    @override
    def eject_card(self):
        print("Ejecting card")

    @override
    def get_total_cash(self) -> int:
        return self.total_money

    @override
    def is_working(self) -> bool:
        return self.total_money > 0
