import abc

from opengsq.protocols.models.server import Server


class IProtocol(abc.ABC):
    @property
    @abc.abstractmethod
    def full_name(self):
        pass

    @abc.abstractmethod
    async def query(self) -> Server:
        pass
