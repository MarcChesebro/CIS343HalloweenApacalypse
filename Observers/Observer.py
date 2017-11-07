from abc import ABCMeta, abstractmethod

class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, info=None):
        pass
