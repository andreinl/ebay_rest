# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingQuote(object):
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
        'creation_date': 'str',
        'expiration_date': 'str',
        'orders': 'list[Order]',
        'package_specification': 'PackageSpecification',
        'rates': 'list[Rate]',
        'ship_from': 'Contact',
        'shipping_quote_id': 'str',
        'ship_to': 'Contact',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'expiration_date': 'expirationDate',
        'orders': 'orders',
        'package_specification': 'packageSpecification',
        'rates': 'rates',
        'ship_from': 'shipFrom',
        'shipping_quote_id': 'shippingQuoteId',
        'ship_to': 'shipTo',
        'warnings': 'warnings'
    }

    def __init__(self, creation_date=None, expiration_date=None, orders=None, package_specification=None, rates=None, ship_from=None, shipping_quote_id=None, ship_to=None, warnings=None):  # noqa: E501
        """ShippingQuote - a model defined in Swagger"""  # noqa: E501
        self._creation_date = None
        self._expiration_date = None
        self._orders = None
        self._package_specification = None
        self._rates = None
        self._ship_from = None
        self._shipping_quote_id = None
        self._ship_to = None
        self._warnings = None
        self.discriminator = None
        if creation_date is not None:
            self.creation_date = creation_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if orders is not None:
            self.orders = orders
        if package_specification is not None:
            self.package_specification = package_specification
        if rates is not None:
            self.rates = rates
        if ship_from is not None:
            self.ship_from = ship_from
        if shipping_quote_id is not None:
            self.shipping_quote_id = shipping_quote_id
        if ship_to is not None:
            self.ship_to = ship_to
        if warnings is not None:
            self.warnings = warnings

    @property
    def creation_date(self):
        """Gets the creation_date of this ShippingQuote.  # noqa: E501

        The date and time this quote was created, expressed as an ISO 8601 UTC string.  # noqa: E501

        :return: The creation_date of this ShippingQuote.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ShippingQuote.

        The date and time this quote was created, expressed as an ISO 8601 UTC string.  # noqa: E501

        :param creation_date: The creation_date of this ShippingQuote.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ShippingQuote.  # noqa: E501

        The last date and time that this quote will be honored, expressed as an ISO 8601 UTC string. After this time the quote expires and the expressed rates can no longer be purchased.  # noqa: E501

        :return: The expiration_date of this ShippingQuote.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ShippingQuote.

        The last date and time that this quote will be honored, expressed as an ISO 8601 UTC string. After this time the quote expires and the expressed rates can no longer be purchased.  # noqa: E501

        :param expiration_date: The expiration_date of this ShippingQuote.  # noqa: E501
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def orders(self):
        """Gets the orders of this ShippingQuote.  # noqa: E501

        This list value is optionally assigned by the seller. When present, each element in the returned list contains seller-assigned information about an order (such as an order number). Because a package can contain all or part of one or more orders, this field provides a way for sellers to identify the packages that contain specific orders.  # noqa: E501

        :return: The orders of this ShippingQuote.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this ShippingQuote.

        This list value is optionally assigned by the seller. When present, each element in the returned list contains seller-assigned information about an order (such as an order number). Because a package can contain all or part of one or more orders, this field provides a way for sellers to identify the packages that contain specific orders.  # noqa: E501

        :param orders: The orders of this ShippingQuote.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

    @property
    def package_specification(self):
        """Gets the package_specification of this ShippingQuote.  # noqa: E501


        :return: The package_specification of this ShippingQuote.  # noqa: E501
        :rtype: PackageSpecification
        """
        return self._package_specification

    @package_specification.setter
    def package_specification(self, package_specification):
        """Sets the package_specification of this ShippingQuote.


        :param package_specification: The package_specification of this ShippingQuote.  # noqa: E501
        :type: PackageSpecification
        """

        self._package_specification = package_specification

    @property
    def rates(self):
        """Gets the rates of this ShippingQuote.  # noqa: E501

        A list of rates where each rate, as identified by a rateId, contains information about a specific shipping service offered by a carrier. Rates include shipping carrier and service, the to and from locations, the pickup and delivery windows, the seller's shipping parameters, the service constraints, and the cost for the base service and a list of additional shipping options. Each rate offered is supported by a label service where you can purchase the rate, and associated shipping label, via a call to createFromShippingQuote.  # noqa: E501

        :return: The rates of this ShippingQuote.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this ShippingQuote.

        A list of rates where each rate, as identified by a rateId, contains information about a specific shipping service offered by a carrier. Rates include shipping carrier and service, the to and from locations, the pickup and delivery windows, the seller's shipping parameters, the service constraints, and the cost for the base service and a list of additional shipping options. Each rate offered is supported by a label service where you can purchase the rate, and associated shipping label, via a call to createFromShippingQuote.  # noqa: E501

        :param rates: The rates of this ShippingQuote.  # noqa: E501
        :type: list[Rate]
        """

        self._rates = rates

    @property
    def ship_from(self):
        """Gets the ship_from of this ShippingQuote.  # noqa: E501


        :return: The ship_from of this ShippingQuote.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_from

    @ship_from.setter
    def ship_from(self, ship_from):
        """Sets the ship_from of this ShippingQuote.


        :param ship_from: The ship_from of this ShippingQuote.  # noqa: E501
        :type: Contact
        """

        self._ship_from = ship_from

    @property
    def shipping_quote_id(self):
        """Gets the shipping_quote_id of this ShippingQuote.  # noqa: E501

        The unique eBay-assigned ID for this shipping quote. The value of this field is associated with a specific package, based on its origin, destination, and size.  # noqa: E501

        :return: The shipping_quote_id of this ShippingQuote.  # noqa: E501
        :rtype: str
        """
        return self._shipping_quote_id

    @shipping_quote_id.setter
    def shipping_quote_id(self, shipping_quote_id):
        """Sets the shipping_quote_id of this ShippingQuote.

        The unique eBay-assigned ID for this shipping quote. The value of this field is associated with a specific package, based on its origin, destination, and size.  # noqa: E501

        :param shipping_quote_id: The shipping_quote_id of this ShippingQuote.  # noqa: E501
        :type: str
        """

        self._shipping_quote_id = shipping_quote_id

    @property
    def ship_to(self):
        """Gets the ship_to of this ShippingQuote.  # noqa: E501


        :return: The ship_to of this ShippingQuote.  # noqa: E501
        :rtype: Contact
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this ShippingQuote.


        :param ship_to: The ship_to of this ShippingQuote.  # noqa: E501
        :type: Contact
        """

        self._ship_to = ship_to

    @property
    def warnings(self):
        """Gets the warnings of this ShippingQuote.  # noqa: E501

        A list of any warnings triggered by the request.  # noqa: E501

        :return: The warnings of this ShippingQuote.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ShippingQuote.

        A list of any warnings triggered by the request.  # noqa: E501

        :param warnings: The warnings of this ShippingQuote.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(ShippingQuote, dict):
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
        if not isinstance(other, ShippingQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
