# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Amount(object):
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
        'converted_from_currency': 'str',
        'converted_from_value': 'str',
        'currency': 'str',
        'value': 'str'
    }

    attribute_map = {
        'converted_from_currency': 'convertedFromCurrency',
        'converted_from_value': 'convertedFromValue',
        'currency': 'currency',
        'value': 'value'
    }

    def __init__(self, converted_from_currency=None, converted_from_value=None, currency=None, value=None):  # noqa: E501
        """Amount - a model defined in Swagger"""  # noqa: E501
        self._converted_from_currency = None
        self._converted_from_value = None
        self._currency = None
        self._value = None
        self.discriminator = None
        if converted_from_currency is not None:
            self.converted_from_currency = converted_from_currency
        if converted_from_value is not None:
            self.converted_from_value = converted_from_value
        if currency is not None:
            self.currency = currency
        if value is not None:
            self.value = value

    @property
    def converted_from_currency(self):
        """Gets the converted_from_currency of this Amount.  # noqa: E501

        A three-letter ISO 4217 code that indicates the currency of the amount in the <b>convertedFromValue</b> field. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The converted_from_currency of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._converted_from_currency

    @converted_from_currency.setter
    def converted_from_currency(self, converted_from_currency):
        """Sets the converted_from_currency of this Amount.

        A three-letter ISO 4217 code that indicates the currency of the amount in the <b>convertedFromValue</b> field. This value is required or returned only if currency conversion/localization is required, and represents the pre-conversion currency. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param converted_from_currency: The converted_from_currency of this Amount.  # noqa: E501
        :type: str
        """

        self._converted_from_currency = converted_from_currency

    @property
    def converted_from_value(self):
        """Gets the converted_from_value of this Amount.  # noqa: E501

        The monetary amount before any conversion is performed, in the currency specified by the <b>convertedFromCurrency</b> field. This value is required or returned only if currency conversion/localization is required. The <b>value</b> field contains the converted amount of this value, in the currency specified by the <b>currency</b> field.  # noqa: E501

        :return: The converted_from_value of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._converted_from_value

    @converted_from_value.setter
    def converted_from_value(self, converted_from_value):
        """Sets the converted_from_value of this Amount.

        The monetary amount before any conversion is performed, in the currency specified by the <b>convertedFromCurrency</b> field. This value is required or returned only if currency conversion/localization is required. The <b>value</b> field contains the converted amount of this value, in the currency specified by the <b>currency</b> field.  # noqa: E501

        :param converted_from_value: The converted_from_value of this Amount.  # noqa: E501
        :type: str
        """

        self._converted_from_value = converted_from_value

    @property
    def currency(self):
        """Gets the currency of this Amount.  # noqa: E501

        A three-letter ISO 4217 code that indicates the currency of the amount in the <b>value</b> field. If currency conversion/localization is required, this is the post-conversion currency of the amount in the <b>value</b> field.<br /><br /><b>Default:</b> The default currency of the eBay marketplace that hosts the listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The currency of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Amount.

        A three-letter ISO 4217 code that indicates the currency of the amount in the <b>value</b> field. If currency conversion/localization is required, this is the post-conversion currency of the amount in the <b>value</b> field.<br /><br /><b>Default:</b> The default currency of the eBay marketplace that hosts the listing. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param currency: The currency of this Amount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def value(self):
        """Gets the value of this Amount.  # noqa: E501

        The monetary amount, in the currency specified by the <b>currency</b> field. If currency conversion/localization is required, this value is the converted amount, and the <b>convertedFromValue</b> field contains the amount in the original currency.  <br><br><i>Required in</i> the <b>amount</b> type.  # noqa: E501

        :return: The value of this Amount.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Amount.

        The monetary amount, in the currency specified by the <b>currency</b> field. If currency conversion/localization is required, this value is the converted amount, and the <b>convertedFromValue</b> field contains the amount in the original currency.  <br><br><i>Required in</i> the <b>amount</b> type.  # noqa: E501

        :param value: The value of this Amount.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Amount, dict):
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
        if not isinstance(other, Amount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
