"""
Module: subject
Description: Defines the Subject class for managing observer subscriptions.
"""

from patterns.observer.observer import Observer


class Subject:
    """
    Represents a subject that maintains a list of observers and notifies them of changes.

    Attributes:
        _observers (list[Observer]): A protected list of subscribed observers.
    """

    def __init__(self) -> None:
        """
        Initializes the Subject with an empty list of observers.
        """
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the list.

        Args:
            observer (Observer): The observer to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the list.

        Args:
            observer (Observer): The observer to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notifies all attached observers with a message.

        Args:
            message (str): The notification content.
        """
        for observer in self._observers:
            observer.update(message)