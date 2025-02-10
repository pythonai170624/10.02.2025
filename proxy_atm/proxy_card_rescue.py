# proxy_atm/proxy_atm.py
from typing import override

from proxy_base import ProxyBase

class CardRescueProxyATM(ProxyBase):

    @override
    def eject_card(self):
        self.atm.eject_card()
