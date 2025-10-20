"""
Module: observer
Description: Defines the Observer interface for receiving notifications from subjects.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract base class for all observers that subscribe to subjects.

    Methods:
        update(message: str): Called by the subject to notify the observer.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receives a notification message from the subject.

        Args:
            message (str): The notification content.
        """
        pass