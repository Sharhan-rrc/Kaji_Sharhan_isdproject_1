"""
OverdraftStrategy module.

Implements a service charge strategy for accounts with overdraft conditions.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on overdraft conditions.

    Attributes:
        _overdraft_limit (float): Maximum allowed overdraft before additional fees apply.
        _overdraft_rate (float): Rate applied to the overdraft amount.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize the overdraft strategy with limit and rate.

        Args:
            overdraft_limit (float): Allowed overdraft threshold.
            overdraft_rate (float): Rate applied to overdraft balance.
        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges based on overdraft status.

        Args:
            account: An instance of BankAccount.

        Returns:
            float: Total service charge including overdraft fees if applicable.
        """
        if account.balance < 0 and abs(account.balance) <= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE + (abs(account.balance) * self._overdraft_rate)
        return self.BASE_SERVICE_CHARGE