from abc import ABC, abstractmethod

#creates abstract class Rider
class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass
    def riders(self):
        pass


