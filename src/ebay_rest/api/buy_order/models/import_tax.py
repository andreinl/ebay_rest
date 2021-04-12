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

class ImportTax(object):
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
        'amount': 'Amount',
        'import_tax_type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'import_tax_type': 'importTaxType'
    }

    def __init__(self, amount=None, import_tax_type=None):  # noqa: E501
        """ImportTax - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._import_tax_type = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if import_tax_type is not None:
            self.import_tax_type = import_tax_type

    @property
    def amount(self):
        """Gets the amount of this ImportTax.  # noqa: E501


        :return: The amount of this ImportTax.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ImportTax.


        :param amount: The amount of this ImportTax.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def import_tax_type(self):
        """Gets the import_tax_type of this ImportTax.  # noqa: E501

        This enumeration value indicates the type of import tax applicable to the order. Currently, the only applicable import tax is 'Goods and Services' tax (indicated with GST). 'Goods and Services' tax is only applicable to orders on the eBay Australia marketplace. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/gct:ImportTaxTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The import_tax_type of this ImportTax.  # noqa: E501
        :rtype: str
        """
        return self._import_tax_type

    @import_tax_type.setter
    def import_tax_type(self, import_tax_type):
        """Sets the import_tax_type of this ImportTax.

        This enumeration value indicates the type of import tax applicable to the order. Currently, the only applicable import tax is 'Goods and Services' tax (indicated with GST). 'Goods and Services' tax is only applicable to orders on the eBay Australia marketplace. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/gct:ImportTaxTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param import_tax_type: The import_tax_type of this ImportTax.  # noqa: E501
        :type: str
        """

        self._import_tax_type = import_tax_type

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
        if issubclass(ImportTax, dict):
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
        if not isinstance(other, ImportTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
