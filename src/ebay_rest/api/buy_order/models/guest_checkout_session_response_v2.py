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

class GuestCheckoutSessionResponseV2(object):
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
        'applied_coupons': 'list[Coupon]',
        'checkout_session_id': 'str',
        'line_items': 'list[LineItem]',
        'pricing_summary': 'PricingSummaryV2',
        'shipping_address': 'ShippingAddress',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'applied_coupons': 'appliedCoupons',
        'checkout_session_id': 'checkoutSessionId',
        'line_items': 'lineItems',
        'pricing_summary': 'pricingSummary',
        'shipping_address': 'shippingAddress',
        'warnings': 'warnings'
    }

    def __init__(self, applied_coupons=None, checkout_session_id=None, line_items=None, pricing_summary=None, shipping_address=None, warnings=None):  # noqa: E501
        """GuestCheckoutSessionResponseV2 - a model defined in Swagger"""  # noqa: E501
        self._applied_coupons = None
        self._checkout_session_id = None
        self._line_items = None
        self._pricing_summary = None
        self._shipping_address = None
        self._warnings = None
        self.discriminator = None
        if applied_coupons is not None:
            self.applied_coupons = applied_coupons
        if checkout_session_id is not None:
            self.checkout_session_id = checkout_session_id
        if line_items is not None:
            self.line_items = line_items
        if pricing_summary is not None:
            self.pricing_summary = pricing_summary
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if warnings is not None:
            self.warnings = warnings

    @property
    def applied_coupons(self):
        """Gets the applied_coupons of this GuestCheckoutSessionResponseV2.  # noqa: E501

        A container that returns the information for the coupons that were applied in the guest checkout session.  # noqa: E501

        :return: The applied_coupons of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._applied_coupons

    @applied_coupons.setter
    def applied_coupons(self, applied_coupons):
        """Sets the applied_coupons of this GuestCheckoutSessionResponseV2.

        A container that returns the information for the coupons that were applied in the guest checkout session.  # noqa: E501

        :param applied_coupons: The applied_coupons of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :type: list[Coupon]
        """

        self._applied_coupons = applied_coupons

    @property
    def checkout_session_id(self):
        """Gets the checkout_session_id of this GuestCheckoutSessionResponseV2.  # noqa: E501

        The eBay-assigned guest checkout session ID. This ID is created after a successful <b>initiateGuestCheckoutSession</b> call.  # noqa: E501

        :return: The checkout_session_id of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._checkout_session_id

    @checkout_session_id.setter
    def checkout_session_id(self, checkout_session_id):
        """Sets the checkout_session_id of this GuestCheckoutSessionResponseV2.

        The eBay-assigned guest checkout session ID. This ID is created after a successful <b>initiateGuestCheckoutSession</b> call.  # noqa: E501

        :param checkout_session_id: The checkout_session_id of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :type: str
        """

        self._checkout_session_id = checkout_session_id

    @property
    def line_items(self):
        """Gets the line_items of this GuestCheckoutSessionResponseV2.  # noqa: E501

        An array of line items associated with the guest checkout session.  # noqa: E501

        :return: The line_items of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this GuestCheckoutSessionResponseV2.

        An array of line items associated with the guest checkout session.  # noqa: E501

        :param line_items: The line_items of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def pricing_summary(self):
        """Gets the pricing_summary of this GuestCheckoutSessionResponseV2.  # noqa: E501


        :return: The pricing_summary of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: PricingSummaryV2
        """
        return self._pricing_summary

    @pricing_summary.setter
    def pricing_summary(self, pricing_summary):
        """Sets the pricing_summary of this GuestCheckoutSessionResponseV2.


        :param pricing_summary: The pricing_summary of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :type: PricingSummaryV2
        """

        self._pricing_summary = pricing_summary

    @property
    def shipping_address(self):
        """Gets the shipping_address of this GuestCheckoutSessionResponseV2.  # noqa: E501


        :return: The shipping_address of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: ShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this GuestCheckoutSessionResponseV2.


        :param shipping_address: The shipping_address of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :type: ShippingAddress
        """

        self._shipping_address = shipping_address

    @property
    def warnings(self):
        """Gets the warnings of this GuestCheckoutSessionResponseV2.  # noqa: E501

        An array of errors or warnings that were generated during the method processing.  # noqa: E501

        :return: The warnings of this GuestCheckoutSessionResponseV2.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this GuestCheckoutSessionResponseV2.

        An array of errors or warnings that were generated during the method processing.  # noqa: E501

        :param warnings: The warnings of this GuestCheckoutSessionResponseV2.  # noqa: E501
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
        if issubclass(GuestCheckoutSessionResponseV2, dict):
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
        if not isinstance(other, GuestCheckoutSessionResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
