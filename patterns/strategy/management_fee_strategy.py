"""
ManagementFeeStrategy module.

Implements a service charge strategy based on account age and management fees.
"""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on account age and management fee.

    Attributes:
        _date_created (date): The date the account was created.
        _management_fee (float): Fee applied if account is older than ten years.
        _TEN_YEARS_AGO (date): Threshold date for applying management fee.
    """

    _TEN_YEARS_AGO: date = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initialize the management fee strategy.

        Args:
            date_created (date): Account creation date.
            management_fee (float): Fee to apply if account is older than ten years.
        """
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges based on account age.

        Args:
            account: An instance of BankAccount.

        Returns:
            float: Total service charge including management fee if applicable.
        """
        if self._date_created < self._TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self._management_fee
        return self.BASE_SERVICE_CHARGE