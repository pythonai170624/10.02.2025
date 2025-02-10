from proxy_card_rescue import CardRescueProxyATM
from real_atm import RealATM
from proxy_atm import OnlineProxyATM

# factory method:
# 1. RealATM
# 2. MonitorServices
def getAtm(online: bool, card_stuck: bool) -> "IAtm":
    if card_stuck:
        return CardRescueProxyATM()
    if online:
        return OnlineProxyATM()
    else:
        return RealATM()

if __name__ == "__main__":
    atm = RealATM()
    print(atm.get_total_cash())
    print(atm.withdraw(1000))
    atm.insert_card()

    proxy = OnlineProxyATM()
    print(proxy.get_total_cash())
    print(proxy.is_working())



# create Brinx proxy
# they can only withdraw money, other operations will get RuntimeError