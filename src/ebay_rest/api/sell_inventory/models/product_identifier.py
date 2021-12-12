# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductIdentifier(object):
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
        'epid': 'str',
        'gtin': 'str',
        'ktype': 'str'
    }

    attribute_map = {
        'epid': 'epid',
        'gtin': 'gtin',
        'ktype': 'ktype'
    }

    def __init__(self, epid=None, gtin=None, ktype=None):  # noqa: E501
        """ProductIdentifier - a model defined in Swagger"""  # noqa: E501
        self._epid = None
        self._gtin = None
        self._ktype = None
        self.discriminator = None
        if epid is not None:
            self.epid = epid
        if gtin is not None:
            self.gtin = gtin
        if ktype is not None:
            self.ktype = ktype

    @property
    def epid(self):
        """Gets the epid of this ProductIdentifier.  # noqa: E501

        This field can be used if the seller already knows the eBay catalog product ID (ePID) associated with the motor vehicle that is to be added to the compatible product list. If this eBay catalog product ID is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle.  # noqa: E501

        :return: The epid of this ProductIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._epid

    @epid.setter
    def epid(self, epid):
        """Sets the epid of this ProductIdentifier.

        This field can be used if the seller already knows the eBay catalog product ID (ePID) associated with the motor vehicle that is to be added to the compatible product list. If this eBay catalog product ID is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle.  # noqa: E501

        :param epid: The epid of this ProductIdentifier.  # noqa: E501
        :type: str
        """

        self._epid = epid

    @property
    def gtin(self):
        """Gets the gtin of this ProductIdentifier.  # noqa: E501

        This field can be used if the seller knows the Global Trade Item Number for the motor vehicle that is to be added to the compatible product list. If this GTIN value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim will automatically get picked up for that motor vehicle.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> This field is for future use.</span>  # noqa: E501

        :return: The gtin of this ProductIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this ProductIdentifier.

        This field can be used if the seller knows the Global Trade Item Number for the motor vehicle that is to be added to the compatible product list. If this GTIN value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim will automatically get picked up for that motor vehicle.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> This field is for future use.</span>  # noqa: E501

        :param gtin: The gtin of this ProductIdentifier.  # noqa: E501
        :type: str
        """

        self._gtin = gtin

    @property
    def ktype(self):
        """Gets the ktype of this ProductIdentifier.  # noqa: E501

        This field can be used if the seller knows the K Type Number for the motor vehicle that is to be added to the compatible product list. If this K Type value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle. <br/><br/> Only the DE, UK, and AU sites support the use of K Type Numbers.  # noqa: E501

        :return: The ktype of this ProductIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._ktype

    @ktype.setter
    def ktype(self, ktype):
        """Sets the ktype of this ProductIdentifier.

        This field can be used if the seller knows the K Type Number for the motor vehicle that is to be added to the compatible product list. If this K Type value is found in the eBay product catalog, the motor vehicle properties (e.g. make, model, year, engine, and trim) will automatically get picked up for that motor vehicle. <br/><br/> Only the DE, UK, and AU sites support the use of K Type Numbers.  # noqa: E501

        :param ktype: The ktype of this ProductIdentifier.  # noqa: E501
        :type: str
        """

        self._ktype = ktype

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
        if issubclass(ProductIdentifier, dict):
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
        if not isinstance(other, ProductIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
