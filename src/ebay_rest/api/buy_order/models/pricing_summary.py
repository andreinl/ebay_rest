# coding: utf-8

"""
    Order API

    The Order API provides interfaces that lets shoppers pay for items (for both eBay guest and eBay member buyers). It also returns payment and shipping status of the order. It enables eBay partners to use accept payment without being <a href=\"https://www.pcisecuritystandards.org/\">PCI compliant</a> and use the <a href=\"/api-docs/buy/static/api-order.html#Post\">Post Order API</a> for returns and cancellations for eBay member buyers.   <p>The Order API has the following resources:  </p>  <ul>  <li><b>checkout_session:</b> Lets eBay members purchase items using PayPal or a credit card.</li>  <li><b>guest_checkout_session:</b> Lets eBay guests purchase items using a credit card or the <a href=\"/api-docs/buy/static/api-order.html#spb-checkout\">PayPal Smart Button</a>.</li>   <li><b>proxy_guest_checkout_session:</b> Lets eBay guests purchase items through a <a href=\"/api-docs/buy/static/api-order.html#vsp-checkout\">vault service provider</a> (VSP). &nbsp;&nbsp;<b>*Note:* </b>Due to the requirement of having a VSP, this resource is not available in the eBay <a href=\"https://developer.ebay.com/my/api_test_tool?index=0\">API Explorer</a>.</li>  <li><b>guest_purchase_order</b> and <b>purchase_order:</b> Lets eBay partners track the payment status and show the buyers their purchase order. </li> </ul>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PricingSummary(object):
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
        'additional_savings': 'Amount',
        'adjustment': 'Adjustment',
        'delivery_cost': 'Amount',
        'delivery_discount': 'Amount',
        'fee': 'Amount',
        'import_charges': 'Amount',
        'import_tax': 'ImportTax',
        'price_discount': 'Amount',
        'price_subtotal': 'Amount',
        'tax': 'Amount',
        'total': 'Amount'
    }

    attribute_map = {
        'additional_savings': 'additionalSavings',
        'adjustment': 'adjustment',
        'delivery_cost': 'deliveryCost',
        'delivery_discount': 'deliveryDiscount',
        'fee': 'fee',
        'import_charges': 'importCharges',
        'import_tax': 'importTax',
        'price_discount': 'priceDiscount',
        'price_subtotal': 'priceSubtotal',
        'tax': 'tax',
        'total': 'total'
    }

    def __init__(self, additional_savings=None, adjustment=None, delivery_cost=None, delivery_discount=None, fee=None, import_charges=None, import_tax=None, price_discount=None, price_subtotal=None, tax=None, total=None):  # noqa: E501
        """PricingSummary - a model defined in Swagger"""  # noqa: E501
        self._additional_savings = None
        self._adjustment = None
        self._delivery_cost = None
        self._delivery_discount = None
        self._fee = None
        self._import_charges = None
        self._import_tax = None
        self._price_discount = None
        self._price_subtotal = None
        self._tax = None
        self._total = None
        self.discriminator = None
        if additional_savings is not None:
            self.additional_savings = additional_savings
        if adjustment is not None:
            self.adjustment = adjustment
        if delivery_cost is not None:
            self.delivery_cost = delivery_cost
        if delivery_discount is not None:
            self.delivery_discount = delivery_discount
        if fee is not None:
            self.fee = fee
        if import_charges is not None:
            self.import_charges = import_charges
        if import_tax is not None:
            self.import_tax = import_tax
        if price_discount is not None:
            self.price_discount = price_discount
        if price_subtotal is not None:
            self.price_subtotal = price_subtotal
        if tax is not None:
            self.tax = tax
        if total is not None:
            self.total = total

    @property
    def additional_savings(self):
        """Gets the additional_savings of this PricingSummary.  # noqa: E501


        :return: The additional_savings of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._additional_savings

    @additional_savings.setter
    def additional_savings(self, additional_savings):
        """Sets the additional_savings of this PricingSummary.


        :param additional_savings: The additional_savings of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._additional_savings = additional_savings

    @property
    def adjustment(self):
        """Gets the adjustment of this PricingSummary.  # noqa: E501


        :return: The adjustment of this PricingSummary.  # noqa: E501
        :rtype: Adjustment
        """
        return self._adjustment

    @adjustment.setter
    def adjustment(self, adjustment):
        """Sets the adjustment of this PricingSummary.


        :param adjustment: The adjustment of this PricingSummary.  # noqa: E501
        :type: Adjustment
        """

        self._adjustment = adjustment

    @property
    def delivery_cost(self):
        """Gets the delivery_cost of this PricingSummary.  # noqa: E501


        :return: The delivery_cost of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._delivery_cost

    @delivery_cost.setter
    def delivery_cost(self, delivery_cost):
        """Sets the delivery_cost of this PricingSummary.


        :param delivery_cost: The delivery_cost of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._delivery_cost = delivery_cost

    @property
    def delivery_discount(self):
        """Gets the delivery_discount of this PricingSummary.  # noqa: E501


        :return: The delivery_discount of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._delivery_discount

    @delivery_discount.setter
    def delivery_discount(self, delivery_discount):
        """Sets the delivery_discount of this PricingSummary.


        :param delivery_discount: The delivery_discount of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._delivery_discount = delivery_discount

    @property
    def fee(self):
        """Gets the fee of this PricingSummary.  # noqa: E501


        :return: The fee of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this PricingSummary.


        :param fee: The fee of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._fee = fee

    @property
    def import_charges(self):
        """Gets the import_charges of this PricingSummary.  # noqa: E501


        :return: The import_charges of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._import_charges

    @import_charges.setter
    def import_charges(self, import_charges):
        """Sets the import_charges of this PricingSummary.


        :param import_charges: The import_charges of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._import_charges = import_charges

    @property
    def import_tax(self):
        """Gets the import_tax of this PricingSummary.  # noqa: E501


        :return: The import_tax of this PricingSummary.  # noqa: E501
        :rtype: ImportTax
        """
        return self._import_tax

    @import_tax.setter
    def import_tax(self, import_tax):
        """Sets the import_tax of this PricingSummary.


        :param import_tax: The import_tax of this PricingSummary.  # noqa: E501
        :type: ImportTax
        """

        self._import_tax = import_tax

    @property
    def price_discount(self):
        """Gets the price_discount of this PricingSummary.  # noqa: E501


        :return: The price_discount of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._price_discount

    @price_discount.setter
    def price_discount(self, price_discount):
        """Sets the price_discount of this PricingSummary.


        :param price_discount: The price_discount of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._price_discount = price_discount

    @property
    def price_subtotal(self):
        """Gets the price_subtotal of this PricingSummary.  # noqa: E501


        :return: The price_subtotal of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._price_subtotal

    @price_subtotal.setter
    def price_subtotal(self, price_subtotal):
        """Sets the price_subtotal of this PricingSummary.


        :param price_subtotal: The price_subtotal of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._price_subtotal = price_subtotal

    @property
    def tax(self):
        """Gets the tax of this PricingSummary.  # noqa: E501


        :return: The tax of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PricingSummary.


        :param tax: The tax of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._tax = tax

    @property
    def total(self):
        """Gets the total of this PricingSummary.  # noqa: E501


        :return: The total of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PricingSummary.


        :param total: The total of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._total = total

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
        if issubclass(PricingSummary, dict):
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
        if not isinstance(other, PricingSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
