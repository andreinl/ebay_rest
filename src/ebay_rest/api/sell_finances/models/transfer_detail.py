# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TransferDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'balance_adjustment': 'BalanceAdjustment',
        'charges': 'list[Charge]',
        'total_charge_net_amount': 'Amount'
    }

    attribute_map = {
        'balance_adjustment': 'balanceAdjustment',
        'charges': 'charges',
        'total_charge_net_amount': 'totalChargeNetAmount'
    }

    def __init__(self, balance_adjustment=None, charges=None, total_charge_net_amount=None):  # noqa: E501
        """TransferDetail - a model defined in Swagger"""  # noqa: E501
        self._balance_adjustment = None
        self._charges = None
        self._total_charge_net_amount = None
        self.discriminator = None
        if balance_adjustment is not None:
            self.balance_adjustment = balance_adjustment
        if charges is not None:
            self.charges = charges
        if total_charge_net_amount is not None:
            self.total_charge_net_amount = total_charge_net_amount

    @property
    def balance_adjustment(self):
        """Gets the balance_adjustment of this TransferDetail.  # noqa: E501


        :return: The balance_adjustment of this TransferDetail.  # noqa: E501
        :rtype: BalanceAdjustment
        """
        return self._balance_adjustment

    @balance_adjustment.setter
    def balance_adjustment(self, balance_adjustment):
        """Sets the balance_adjustment of this TransferDetail.


        :param balance_adjustment: The balance_adjustment of this TransferDetail.  # noqa: E501
        :type: BalanceAdjustment
        """

        self._balance_adjustment = balance_adjustment

    @property
    def charges(self):
        """Gets the charges of this TransferDetail.  # noqa: E501

        This container is an array of one or more charges related to the transfer. Charges can be related to an order cancellation, order return, case, payment dispute, etc.  # noqa: E501

        :return: The charges of this TransferDetail.  # noqa: E501
        :rtype: list[Charge]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this TransferDetail.

        This container is an array of one or more charges related to the transfer. Charges can be related to an order cancellation, order return, case, payment dispute, etc.  # noqa: E501

        :param charges: The charges of this TransferDetail.  # noqa: E501
        :type: list[Charge]
        """

        self._charges = charges

    @property
    def total_charge_net_amount(self):
        """Gets the total_charge_net_amount of this TransferDetail.  # noqa: E501


        :return: The total_charge_net_amount of this TransferDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._total_charge_net_amount

    @total_charge_net_amount.setter
    def total_charge_net_amount(self, total_charge_net_amount):
        """Sets the total_charge_net_amount of this TransferDetail.


        :param total_charge_net_amount: The total_charge_net_amount of this TransferDetail.  # noqa: E501
        :type: Amount
        """

        self._total_charge_net_amount = total_charge_net_amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TransferDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransferDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
