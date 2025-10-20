"""
MinimumBalanceStrategy module.

Implements a service charge strategy based on minimum balance requirements.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on minimum balance.

    Attributes:
        _minimum_balance (float): Required minimum balance to avoid premium charges.
        SERVICE_CHARGE_PREMIUM (float): Additional charge if balance is below minimum.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initialize the minimum balance strategy.

        Args:
            minimum_balance (float): Threshold below which premium charges apply.
        """
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges based on account balance.

        Args:
            account: An instance of BankAccount.

        Returns:
            float: Total service charge including premium if balance is below threshold.
        """
        if account.balance < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE