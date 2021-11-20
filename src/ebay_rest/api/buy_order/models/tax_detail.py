# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> This version of the Order API (v2) currently only supports the guest payment flow for eBay managed payments. To view the v1_beta version of the Order API, which includes both member and guest checkout payment flows, refer to the <a href=\"/api-docs/buy/order_v1/resources/methods\">Order_v1 API</a> documentation.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TaxDetail(object):
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
        'included_in_price': 'bool',
        'tax_jurisdiction': 'TaxJurisdiction',
        'tax_type': 'str'
    }

    attribute_map = {
        'included_in_price': 'includedInPrice',
        'tax_jurisdiction': 'taxJurisdiction',
        'tax_type': 'taxType'
    }

    def __init__(self, included_in_price=None, tax_jurisdiction=None, tax_type=None):  # noqa: E501
        """TaxDetail - a model defined in Swagger"""  # noqa: E501
        self._included_in_price = None
        self._tax_jurisdiction = None
        self._tax_type = None
        self.discriminator = None
        if included_in_price is not None:
            self.included_in_price = included_in_price
        if tax_jurisdiction is not None:
            self.tax_jurisdiction = tax_jurisdiction
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def included_in_price(self):
        """Gets the included_in_price of this TaxDetail.  # noqa: E501

        A field that indicates whether tax was applied for the cost of the item and its shipping.  # noqa: E501

        :return: The included_in_price of this TaxDetail.  # noqa: E501
        :rtype: bool
        """
        return self._included_in_price

    @included_in_price.setter
    def included_in_price(self, included_in_price):
        """Sets the included_in_price of this TaxDetail.

        A field that indicates whether tax was applied for the cost of the item and its shipping.  # noqa: E501

        :param included_in_price: The included_in_price of this TaxDetail.  # noqa: E501
        :type: bool
        """

        self._included_in_price = included_in_price

    @property
    def tax_jurisdiction(self):
        """Gets the tax_jurisdiction of this TaxDetail.  # noqa: E501


        :return: The tax_jurisdiction of this TaxDetail.  # noqa: E501
        :rtype: TaxJurisdiction
        """
        return self._tax_jurisdiction

    @tax_jurisdiction.setter
    def tax_jurisdiction(self, tax_jurisdiction):
        """Sets the tax_jurisdiction of this TaxDetail.


        :param tax_jurisdiction: The tax_jurisdiction of this TaxDetail.  # noqa: E501
        :type: TaxJurisdiction
        """

        self._tax_jurisdiction = tax_jurisdiction

    @property
    def tax_type(self):
        """Gets the tax_type of this TaxDetail.  # noqa: E501

        A field that indicates the type of tax that may be collected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/gct:TaxType'>eBay API documentation</a>  # noqa: E501

        :return: The tax_type of this TaxDetail.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this TaxDetail.

        A field that indicates the type of tax that may be collected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/gct:TaxType'>eBay API documentation</a>  # noqa: E501

        :param tax_type: The tax_type of this TaxDetail.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

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
        if issubclass(TaxDetail, dict):
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
        if not isinstance(other, TaxDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
