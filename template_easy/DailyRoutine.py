from abc import ABC, abstractmethod
from typing import final


class DailyRoutine(ABC):
    """Template class defining a standard daily routine."""

    @final
    def follow_routine(self):
        """Template method defining the structure of the day."""
        self.wake_up()
        self.shower()
        self.go_to_work()
        self.eat()
        self.have_fun()
        self.sleep()

    def wake_up(self):
        print("Waking up... *Yawn*")

    def shower(self):
        print("Taking a shower... 🚿")

    @abstractmethod
    def go_to_work(self):
        """Abstract method for work-related activity (can be skipped on weekends)."""
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def have_fun(self):
        """Abstract method for fun activities (different every day)."""
        pass

    def sleep(self):
        print("Going to sleep... 😴💤")
