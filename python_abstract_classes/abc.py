from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self, device: str) -> str:
        return f"turn on {device}"

    @abstractmethod
    def turn_off(self, device: str) -> str:
        return f"turn off {device}"

    @property
    def brand(self):
        return "LG"


class TVControl(RemoteControl):

    def turn_on(self, device: str) -> str:
        return f"turn on {device}"

    def turn_off(self, device: str) -> str:
        return f"turn off {device}"

    @property
    def brand(self) -> str:
        return 'Philips'


control = TVControl()
print(control.turn_on('TV'))
print(control.turn_off('TV'))
print(control.brand)
