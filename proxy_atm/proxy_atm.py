# proxy_atm/proxy_atm.py
from typing import override

from iatm import IAtm
from proxy_atm.proxy_base import ProxyBase
from real_atm import RealATM

class OnlineProxyATM(ProxyBase):

    @override
    def get_total_cash(self) -> int:
        return self.atm.get_total_cash()

    @override
    def is_working(self) -> bool:
        return self.atm.is_working()
