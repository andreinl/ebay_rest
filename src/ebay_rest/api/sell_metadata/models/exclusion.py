# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Exclusion(object):
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
        'brands': 'list[str]'
    }

    attribute_map = {
        'brands': 'brands'
    }

    def __init__(self, brands=None):  # noqa: E501
        """Exclusion - a model defined in Swagger"""  # noqa: E501
        self._brands = None
        self.discriminator = None
        if brands is not None:
            self.brands = brands

    @property
    def brands(self):
        """Gets the brands of this Exclusion.  # noqa: E501

        A list of brands that are excluded from requiring a link to the eBay Catalog for the associated categoryId. If productRequired is set to true, items that are of a brand returned in this field are excluded from the need to specify a value for the ePID field in their item description in order to be listed in the associated category.  # noqa: E501

        :return: The brands of this Exclusion.  # noqa: E501
        :rtype: list[str]
        """
        return self._brands

    @brands.setter
    def brands(self, brands):
        """Sets the brands of this Exclusion.

        A list of brands that are excluded from requiring a link to the eBay Catalog for the associated categoryId. If productRequired is set to true, items that are of a brand returned in this field are excluded from the need to specify a value for the ePID field in their item description in order to be listed in the associated category.  # noqa: E501

        :param brands: The brands of this Exclusion.  # noqa: E501
        :type: list[str]
        """

        self._brands = brands

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
        if issubclass(Exclusion, dict):
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
        if not isinstance(other, Exclusion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
