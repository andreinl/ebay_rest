# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingService(object):
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
        'additional_shipping_cost': 'Amount',
        'buyer_responsible_for_pickup': 'bool',
        'buyer_responsible_for_shipping': 'bool',
        'cash_on_delivery_fee': 'Amount',
        'free_shipping': 'bool',
        'shipping_carrier_code': 'str',
        'shipping_cost': 'Amount',
        'shipping_service_code': 'str',
        'ship_to_locations': 'RegionSet',
        'sort_order': 'int',
        'surcharge': 'Amount'
    }

    attribute_map = {
        'additional_shipping_cost': 'additionalShippingCost',
        'buyer_responsible_for_pickup': 'buyerResponsibleForPickup',
        'buyer_responsible_for_shipping': 'buyerResponsibleForShipping',
        'cash_on_delivery_fee': 'cashOnDeliveryFee',
        'free_shipping': 'freeShipping',
        'shipping_carrier_code': 'shippingCarrierCode',
        'shipping_cost': 'shippingCost',
        'shipping_service_code': 'shippingServiceCode',
        'ship_to_locations': 'shipToLocations',
        'sort_order': 'sortOrder',
        'surcharge': 'surcharge'
    }

    def __init__(self, additional_shipping_cost=None, buyer_responsible_for_pickup=None, buyer_responsible_for_shipping=None, cash_on_delivery_fee=None, free_shipping=None, shipping_carrier_code=None, shipping_cost=None, shipping_service_code=None, ship_to_locations=None, sort_order=None, surcharge=None):  # noqa: E501
        """ShippingService - a model defined in Swagger"""  # noqa: E501
        self._additional_shipping_cost = None
        self._buyer_responsible_for_pickup = None
        self._buyer_responsible_for_shipping = None
        self._cash_on_delivery_fee = None
        self._free_shipping = None
        self._shipping_carrier_code = None
        self._shipping_cost = None
        self._shipping_service_code = None
        self._ship_to_locations = None
        self._sort_order = None
        self._surcharge = None
        self.discriminator = None
        if additional_shipping_cost is not None:
            self.additional_shipping_cost = additional_shipping_cost
        if buyer_responsible_for_pickup is not None:
            self.buyer_responsible_for_pickup = buyer_responsible_for_pickup
        if buyer_responsible_for_shipping is not None:
            self.buyer_responsible_for_shipping = buyer_responsible_for_shipping
        if cash_on_delivery_fee is not None:
            self.cash_on_delivery_fee = cash_on_delivery_fee
        if free_shipping is not None:
            self.free_shipping = free_shipping
        if shipping_carrier_code is not None:
            self.shipping_carrier_code = shipping_carrier_code
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_service_code is not None:
            self.shipping_service_code = shipping_service_code
        if ship_to_locations is not None:
            self.ship_to_locations = ship_to_locations
        if sort_order is not None:
            self.sort_order = sort_order
        if surcharge is not None:
            self.surcharge = surcharge

    @property
    def additional_shipping_cost(self):
        """Gets the additional_shipping_cost of this ShippingService.  # noqa: E501


        :return: The additional_shipping_cost of this ShippingService.  # noqa: E501
        :rtype: Amount
        """
        return self._additional_shipping_cost

    @additional_shipping_cost.setter
    def additional_shipping_cost(self, additional_shipping_cost):
        """Sets the additional_shipping_cost of this ShippingService.


        :param additional_shipping_cost: The additional_shipping_cost of this ShippingService.  # noqa: E501
        :type: Amount
        """

        self._additional_shipping_cost = additional_shipping_cost

    @property
    def buyer_responsible_for_pickup(self):
        """Gets the buyer_responsible_for_pickup of this ShippingService.  # noqa: E501

        This field is only applicable to vehicle categories on eBay Motors (US and Canada). If set to <code>true</code>, the buyer is responsible for picking up the vehicle. Otherwise, the seller should specify the vehicle pickup arrangements in the item description. <br><br>The seller cannot modify this flag if the vehicle has bids or if the listing ends within 12 hours. <br><br><b>Default</b>: false  # noqa: E501

        :return: The buyer_responsible_for_pickup of this ShippingService.  # noqa: E501
        :rtype: bool
        """
        return self._buyer_responsible_for_pickup

    @buyer_responsible_for_pickup.setter
    def buyer_responsible_for_pickup(self, buyer_responsible_for_pickup):
        """Sets the buyer_responsible_for_pickup of this ShippingService.

        This field is only applicable to vehicle categories on eBay Motors (US and Canada). If set to <code>true</code>, the buyer is responsible for picking up the vehicle. Otherwise, the seller should specify the vehicle pickup arrangements in the item description. <br><br>The seller cannot modify this flag if the vehicle has bids or if the listing ends within 12 hours. <br><br><b>Default</b>: false  # noqa: E501

        :param buyer_responsible_for_pickup: The buyer_responsible_for_pickup of this ShippingService.  # noqa: E501
        :type: bool
        """

        self._buyer_responsible_for_pickup = buyer_responsible_for_pickup

    @property
    def buyer_responsible_for_shipping(self):
        """Gets the buyer_responsible_for_shipping of this ShippingService.  # noqa: E501

        This field is applicable for only items listed in vehicle categories on eBay Motors (US and Canada). If set to <code>true</code>, the buyer is responsible for the shipment of the vehicle. Otherwise, the seller should specify the vehicle shipping arrangements in the item description. <br><br>The seller cannot modify this flag if the vehicle has bids or if the listing ends within 12 hours. <br><br><b>Default</b>: false  # noqa: E501

        :return: The buyer_responsible_for_shipping of this ShippingService.  # noqa: E501
        :rtype: bool
        """
        return self._buyer_responsible_for_shipping

    @buyer_responsible_for_shipping.setter
    def buyer_responsible_for_shipping(self, buyer_responsible_for_shipping):
        """Sets the buyer_responsible_for_shipping of this ShippingService.

        This field is applicable for only items listed in vehicle categories on eBay Motors (US and Canada). If set to <code>true</code>, the buyer is responsible for the shipment of the vehicle. Otherwise, the seller should specify the vehicle shipping arrangements in the item description. <br><br>The seller cannot modify this flag if the vehicle has bids or if the listing ends within 12 hours. <br><br><b>Default</b>: false  # noqa: E501

        :param buyer_responsible_for_shipping: The buyer_responsible_for_shipping of this ShippingService.  # noqa: E501
        :type: bool
        """

        self._buyer_responsible_for_shipping = buyer_responsible_for_shipping

    @property
    def cash_on_delivery_fee(self):
        """Gets the cash_on_delivery_fee of this ShippingService.  # noqa: E501


        :return: The cash_on_delivery_fee of this ShippingService.  # noqa: E501
        :rtype: Amount
        """
        return self._cash_on_delivery_fee

    @cash_on_delivery_fee.setter
    def cash_on_delivery_fee(self, cash_on_delivery_fee):
        """Sets the cash_on_delivery_fee of this ShippingService.


        :param cash_on_delivery_fee: The cash_on_delivery_fee of this ShippingService.  # noqa: E501
        :type: Amount
        """

        self._cash_on_delivery_fee = cash_on_delivery_fee

    @property
    def free_shipping(self):
        """Gets the free_shipping of this ShippingService.  # noqa: E501

        If set to <code>true</code>, the seller offers free shipping to the buyer. This field can only be included and set to 'true' for the first domestic shipping service option specified in the <b>shippingServices</b> container (it is ignored if set for subsequent shipping services). The first specified shipping service option has a <b>sortOrder</b> value of <code>1</code> or (if the sortOrderId field is not used) it is the shipping service option that's specified first in the <b>shippingServices</b> container.  # noqa: E501

        :return: The free_shipping of this ShippingService.  # noqa: E501
        :rtype: bool
        """
        return self._free_shipping

    @free_shipping.setter
    def free_shipping(self, free_shipping):
        """Sets the free_shipping of this ShippingService.

        If set to <code>true</code>, the seller offers free shipping to the buyer. This field can only be included and set to 'true' for the first domestic shipping service option specified in the <b>shippingServices</b> container (it is ignored if set for subsequent shipping services). The first specified shipping service option has a <b>sortOrder</b> value of <code>1</code> or (if the sortOrderId field is not used) it is the shipping service option that's specified first in the <b>shippingServices</b> container.  # noqa: E501

        :param free_shipping: The free_shipping of this ShippingService.  # noqa: E501
        :type: bool
        """

        self._free_shipping = free_shipping

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this ShippingService.  # noqa: E501

        The shipping carrier, such as 'USPS', 'FedEx', 'UPS', and so on.  # noqa: E501

        :return: The shipping_carrier_code of this ShippingService.  # noqa: E501
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this ShippingService.

        The shipping carrier, such as 'USPS', 'FedEx', 'UPS', and so on.  # noqa: E501

        :param shipping_carrier_code: The shipping_carrier_code of this ShippingService.  # noqa: E501
        :type: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ShippingService.  # noqa: E501


        :return: The shipping_cost of this ShippingService.  # noqa: E501
        :rtype: Amount
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ShippingService.


        :param shipping_cost: The shipping_cost of this ShippingService.  # noqa: E501
        :type: Amount
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_service_code(self):
        """Gets the shipping_service_code of this ShippingService.  # noqa: E501

        The shipping service that the shipping carrier uses to ship an item. For example, an overnight, two-day delivery, or other type of service. For details on how shipping services are configured, see <a href=\"/api-docs/sell/static/seller-accounts/ht_shipping-setting-shipping-carrier-and-service-values.html\" target=\"_blank\">Setting the shipping carrier and shipping service values</a> and <a href=\"/api-docs/sell/static/seller-accounts/using-the-ebay-standard-envelope-service.html\" target=\"_blank\">Using eBay standard envelope (eSE) service</a>.  # noqa: E501

        :return: The shipping_service_code of this ShippingService.  # noqa: E501
        :rtype: str
        """
        return self._shipping_service_code

    @shipping_service_code.setter
    def shipping_service_code(self, shipping_service_code):
        """Sets the shipping_service_code of this ShippingService.

        The shipping service that the shipping carrier uses to ship an item. For example, an overnight, two-day delivery, or other type of service. For details on how shipping services are configured, see <a href=\"/api-docs/sell/static/seller-accounts/ht_shipping-setting-shipping-carrier-and-service-values.html\" target=\"_blank\">Setting the shipping carrier and shipping service values</a> and <a href=\"/api-docs/sell/static/seller-accounts/using-the-ebay-standard-envelope-service.html\" target=\"_blank\">Using eBay standard envelope (eSE) service</a>.  # noqa: E501

        :param shipping_service_code: The shipping_service_code of this ShippingService.  # noqa: E501
        :type: str
        """

        self._shipping_service_code = shipping_service_code

    @property
    def ship_to_locations(self):
        """Gets the ship_to_locations of this ShippingService.  # noqa: E501


        :return: The ship_to_locations of this ShippingService.  # noqa: E501
        :rtype: RegionSet
        """
        return self._ship_to_locations

    @ship_to_locations.setter
    def ship_to_locations(self, ship_to_locations):
        """Sets the ship_to_locations of this ShippingService.


        :param ship_to_locations: The ship_to_locations of this ShippingService.  # noqa: E501
        :type: RegionSet
        """

        self._ship_to_locations = ship_to_locations

    @property
    def sort_order(self):
        """Gets the sort_order of this ShippingService.  # noqa: E501

        This integer value controls the order that this shipping service option appears in the View Item and Checkout pages, as related to the other specified shipping service options. <br><br>Sellers can specify up to four domestic shipping services (in four separate <b>shippingService</b> containers), so valid values are 1, 2, 3, and 4. A shipping service option with a <b>sortOrder</b> value of '1' appears at the top of View Item and Checkout pages. Conversely, a shipping service option with a <b>sortOrder</b> value of '4' appears at the bottom of the list. <br><br>Sellers can specify up to five international shipping services (in five separate <b>shippingService</b> containers, so valid values for international shipping services are 1, 2, 3, 4, and 5. Similarly to domestic shipping service options, the <b>sortOrder</b> value of a international shipping service option controls the placement of that shipping service option in the View Item and Checkout pages. Set up different domestic and international services by configuring two <b>shippingOptions</b> containers, where you set <b>shippingOptions.optionType</b> to either <code>DOMESTIC</code> or <code>INTERNATIONAL</code> to indicate the area supported by the listed shipping services. <br><br>If the <b>sortOrder</b> field is not supplied, the order of domestic and international shipping service options is determined by the order in which they are listed in the API call. <br><br><b>Min</b>: 1. <b>Max</b>: 4 (for domestic shipping service) or 5 (for international shipping service).  # noqa: E501

        :return: The sort_order of this ShippingService.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ShippingService.

        This integer value controls the order that this shipping service option appears in the View Item and Checkout pages, as related to the other specified shipping service options. <br><br>Sellers can specify up to four domestic shipping services (in four separate <b>shippingService</b> containers), so valid values are 1, 2, 3, and 4. A shipping service option with a <b>sortOrder</b> value of '1' appears at the top of View Item and Checkout pages. Conversely, a shipping service option with a <b>sortOrder</b> value of '4' appears at the bottom of the list. <br><br>Sellers can specify up to five international shipping services (in five separate <b>shippingService</b> containers, so valid values for international shipping services are 1, 2, 3, 4, and 5. Similarly to domestic shipping service options, the <b>sortOrder</b> value of a international shipping service option controls the placement of that shipping service option in the View Item and Checkout pages. Set up different domestic and international services by configuring two <b>shippingOptions</b> containers, where you set <b>shippingOptions.optionType</b> to either <code>DOMESTIC</code> or <code>INTERNATIONAL</code> to indicate the area supported by the listed shipping services. <br><br>If the <b>sortOrder</b> field is not supplied, the order of domestic and international shipping service options is determined by the order in which they are listed in the API call. <br><br><b>Min</b>: 1. <b>Max</b>: 4 (for domestic shipping service) or 5 (for international shipping service).  # noqa: E501

        :param sort_order: The sort_order of this ShippingService.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def surcharge(self):
        """Gets the surcharge of this ShippingService.  # noqa: E501


        :return: The surcharge of this ShippingService.  # noqa: E501
        :rtype: Amount
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """Sets the surcharge of this ShippingService.


        :param surcharge: The surcharge of this ShippingService.  # noqa: E501
        :type: Amount
        """

        self._surcharge = surcharge

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
        if issubclass(ShippingService, dict):
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
        if not isinstance(other, ShippingService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
