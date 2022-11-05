# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EbayFulfillmentProgram(object):
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
        'fulfilled_by': 'str'
    }

    attribute_map = {
        'fulfilled_by': 'fulfilledBy'
    }

    def __init__(self, fulfilled_by=None):  # noqa: E501
        """EbayFulfillmentProgram - a model defined in Swagger"""  # noqa: E501
        self._fulfilled_by = None
        self.discriminator = None
        if fulfilled_by is not None:
            self.fulfilled_by = fulfilled_by

    @property
    def fulfilled_by(self):
        """Gets the fulfilled_by of this EbayFulfillmentProgram.  # noqa: E501

        The value returned in this field indicates the party that is handling fulfillment of the order line item. <br /><br />Valid value: <code>EBAY</code>  # noqa: E501

        :return: The fulfilled_by of this EbayFulfillmentProgram.  # noqa: E501
        :rtype: str
        """
        return self._fulfilled_by

    @fulfilled_by.setter
    def fulfilled_by(self, fulfilled_by):
        """Sets the fulfilled_by of this EbayFulfillmentProgram.

        The value returned in this field indicates the party that is handling fulfillment of the order line item. <br /><br />Valid value: <code>EBAY</code>  # noqa: E501

        :param fulfilled_by: The fulfilled_by of this EbayFulfillmentProgram.  # noqa: E501
        :type: str
        """

        self._fulfilled_by = fulfilled_by

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
        if issubclass(EbayFulfillmentProgram, dict):
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
        if not isinstance(other, EbayFulfillmentProgram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
