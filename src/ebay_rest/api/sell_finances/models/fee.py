# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Fee(object):
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
        'amount': 'Amount',
        'fee_memo': 'str',
        'fee_type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'fee_memo': 'feeMemo',
        'fee_type': 'feeType'
    }

    def __init__(self, amount=None, fee_memo=None, fee_type=None):  # noqa: E501
        """Fee - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._fee_memo = None
        self._fee_type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if fee_memo is not None:
            self.fee_memo = fee_memo
        if fee_type is not None:
            self.fee_type = fee_type

    @property
    def amount(self):
        """Gets the amount of this Fee.  # noqa: E501


        :return: The amount of this Fee.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Fee.


        :param amount: The amount of this Fee.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def fee_memo(self):
        """Gets the fee_memo of this Fee.  # noqa: E501

        A description of the fee that was deducted from the seller payout.  # noqa: E501

        :return: The fee_memo of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._fee_memo

    @fee_memo.setter
    def fee_memo(self, fee_memo):
        """Sets the fee_memo of this Fee.

        A description of the fee that was deducted from the seller payout.  # noqa: E501

        :param fee_memo: The fee_memo of this Fee.  # noqa: E501
        :type: str
        """

        self._fee_memo = fee_memo

    @property
    def fee_type(self):
        """Gets the fee_type of this Fee.  # noqa: E501

        The enumeration value returned here indicates the type of fee that was deducted from the seller payout. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/api:FeeTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The fee_type of this Fee.  # noqa: E501
        :rtype: str
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this Fee.

        The enumeration value returned here indicates the type of fee that was deducted from the seller payout. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/api:FeeTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param fee_type: The fee_type of this Fee.  # noqa: E501
        :type: str
        """

        self._fee_type = fee_type

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
        if issubclass(Fee, dict):
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
        if not isinstance(other, Fee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
