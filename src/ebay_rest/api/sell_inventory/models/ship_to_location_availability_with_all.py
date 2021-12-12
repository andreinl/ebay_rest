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

class ShipToLocationAvailabilityWithAll(object):
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
        'allocation_by_format': 'FormatAllocation',
        'availability_distributions': 'list[AvailabilityDistribution]',
        'quantity': 'int'
    }

    attribute_map = {
        'allocation_by_format': 'allocationByFormat',
        'availability_distributions': 'availabilityDistributions',
        'quantity': 'quantity'
    }

    def __init__(self, allocation_by_format=None, availability_distributions=None, quantity=None):  # noqa: E501
        """ShipToLocationAvailabilityWithAll - a model defined in Swagger"""  # noqa: E501
        self._allocation_by_format = None
        self._availability_distributions = None
        self._quantity = None
        self.discriminator = None
        if allocation_by_format is not None:
            self.allocation_by_format = allocation_by_format
        if availability_distributions is not None:
            self.availability_distributions = availability_distributions
        if quantity is not None:
            self.quantity = quantity

    @property
    def allocation_by_format(self):
        """Gets the allocation_by_format of this ShipToLocationAvailabilityWithAll.  # noqa: E501


        :return: The allocation_by_format of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :rtype: FormatAllocation
        """
        return self._allocation_by_format

    @allocation_by_format.setter
    def allocation_by_format(self, allocation_by_format):
        """Sets the allocation_by_format of this ShipToLocationAvailabilityWithAll.


        :param allocation_by_format: The allocation_by_format of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :type: FormatAllocation
        """

        self._allocation_by_format = allocation_by_format

    @property
    def availability_distributions(self):
        """Gets the availability_distributions of this ShipToLocationAvailabilityWithAll.  # noqa: E501

        This container is used to set the available quantity of the inventory item at one or more warehouse locations.<br /><br /> This container will be returned if the available quantity is set for one or more inventory locations.  # noqa: E501

        :return: The availability_distributions of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :rtype: list[AvailabilityDistribution]
        """
        return self._availability_distributions

    @availability_distributions.setter
    def availability_distributions(self, availability_distributions):
        """Sets the availability_distributions of this ShipToLocationAvailabilityWithAll.

        This container is used to set the available quantity of the inventory item at one or more warehouse locations.<br /><br /> This container will be returned if the available quantity is set for one or more inventory locations.  # noqa: E501

        :param availability_distributions: The availability_distributions of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :type: list[AvailabilityDistribution]
        """

        self._availability_distributions = availability_distributions

    @property
    def quantity(self):
        """Gets the quantity of this ShipToLocationAvailabilityWithAll.  # noqa: E501

        This container is used to set the total 'ship-to-home' quantity of the inventory item that will be available for purchase through one or more published offers. This container is not immediately required, but 'ship-to-home' quantity must be set before an offer of the inventory item can be published.<br/><br/>If an existing inventory item is being updated, and the 'ship-to-home' quantity already exists for the inventory item record, this container should be included again, even if the value is not changing, or the available quantity data will be lost.  # noqa: E501

        :return: The quantity of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ShipToLocationAvailabilityWithAll.

        This container is used to set the total 'ship-to-home' quantity of the inventory item that will be available for purchase through one or more published offers. This container is not immediately required, but 'ship-to-home' quantity must be set before an offer of the inventory item can be published.<br/><br/>If an existing inventory item is being updated, and the 'ship-to-home' quantity already exists for the inventory item record, this container should be included again, even if the value is not changing, or the available quantity data will be lost.  # noqa: E501

        :param quantity: The quantity of this ShipToLocationAvailabilityWithAll.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(ShipToLocationAvailabilityWithAll, dict):
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
        if not isinstance(other, ShipToLocationAvailabilityWithAll):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
