"""
ServiceChargeStrategy module.

Defines the abstract base class for service charge calculation strategies.
Each subclass must implement the calculate_service_charges method.
"""

from abc import ABC, abstractmethod


class ServiceChargeStrategy(ABC):
    """
    Abstract base class for service charge strategies.

    Attributes:
        BASE_SERVICE_CHARGE (float): Default base charge applied to all accounts.
    """

    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges for a given bank account.

        Args:
            account: An instance of BankAccount.

        Returns:
            float: The calculated service charge.
        """
        pass