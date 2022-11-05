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

class Reference(object):
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
        'reference_id': 'str',
        'reference_type': 'str'
    }

    attribute_map = {
        'reference_id': 'referenceId',
        'reference_type': 'referenceType'
    }

    def __init__(self, reference_id=None, reference_type=None):  # noqa: E501
        """Reference - a model defined in Swagger"""  # noqa: E501
        self._reference_id = None
        self._reference_type = None
        self.discriminator = None
        if reference_id is not None:
            self.reference_id = reference_id
        if reference_type is not None:
            self.reference_type = reference_type

    @property
    def reference_id(self):
        """Gets the reference_id of this Reference.  # noqa: E501

        The identifier of the transaction as specified by the <strong>referenceType</strong>. For example, with a <strong>referenceType</strong> of <strong>item_id</strong>, the <strong>referenceId</strong> refers to a unique item. This item may have several <code>NON_SALE_CHARGE</code> transactions.  # noqa: E501

        :return: The reference_id of this Reference.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this Reference.

        The identifier of the transaction as specified by the <strong>referenceType</strong>. For example, with a <strong>referenceType</strong> of <strong>item_id</strong>, the <strong>referenceId</strong> refers to a unique item. This item may have several <code>NON_SALE_CHARGE</code> transactions.  # noqa: E501

        :param reference_id: The reference_id of this Reference.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def reference_type(self):
        """Gets the reference_type of this Reference.  # noqa: E501

        An enumeration value that identifies the reference type associated with the <strong>referenceId</strong>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:ReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reference_type of this Reference.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this Reference.

        An enumeration value that identifies the reference type associated with the <strong>referenceId</strong>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/finances/types/pay:ReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param reference_type: The reference_type of this Reference.  # noqa: E501
        :type: str
        """

        self._reference_type = reference_type

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
        if issubclass(Reference, dict):
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
        if not isinstance(other, Reference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
