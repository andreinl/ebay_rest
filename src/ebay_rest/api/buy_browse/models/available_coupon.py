# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AvailableCoupon(object):
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
        'constraint': 'CouponConstraint',
        'discount_amount': 'Amount',
        'discount_type': 'str',
        'message': 'str',
        'redemption_code': 'str',
        'terms_web_url': 'str'
    }

    attribute_map = {
        'constraint': 'constraint',
        'discount_amount': 'discountAmount',
        'discount_type': 'discountType',
        'message': 'message',
        'redemption_code': 'redemptionCode',
        'terms_web_url': 'termsWebUrl'
    }

    def __init__(self, constraint=None, discount_amount=None, discount_type=None, message=None, redemption_code=None, terms_web_url=None):  # noqa: E501
        """AvailableCoupon - a model defined in Swagger"""  # noqa: E501
        self._constraint = None
        self._discount_amount = None
        self._discount_type = None
        self._message = None
        self._redemption_code = None
        self._terms_web_url = None
        self.discriminator = None
        if constraint is not None:
            self.constraint = constraint
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_type is not None:
            self.discount_type = discount_type
        if message is not None:
            self.message = message
        if redemption_code is not None:
            self.redemption_code = redemption_code
        if terms_web_url is not None:
            self.terms_web_url = terms_web_url

    @property
    def constraint(self):
        """Gets the constraint of this AvailableCoupon.  # noqa: E501


        :return: The constraint of this AvailableCoupon.  # noqa: E501
        :rtype: CouponConstraint
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """Sets the constraint of this AvailableCoupon.


        :param constraint: The constraint of this AvailableCoupon.  # noqa: E501
        :type: CouponConstraint
        """

        self._constraint = constraint

    @property
    def discount_amount(self):
        """Gets the discount_amount of this AvailableCoupon.  # noqa: E501


        :return: The discount_amount of this AvailableCoupon.  # noqa: E501
        :rtype: Amount
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this AvailableCoupon.


        :param discount_amount: The discount_amount of this AvailableCoupon.  # noqa: E501
        :type: Amount
        """

        self._discount_amount = discount_amount

    @property
    def discount_type(self):
        """Gets the discount_type of this AvailableCoupon.  # noqa: E501

        The type of discount that the coupon applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CouponDiscountType'>eBay API documentation</a>  # noqa: E501

        :return: The discount_type of this AvailableCoupon.  # noqa: E501
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this AvailableCoupon.

        The type of discount that the coupon applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CouponDiscountType'>eBay API documentation</a>  # noqa: E501

        :param discount_type: The discount_type of this AvailableCoupon.  # noqa: E501
        :type: str
        """

        self._discount_type = discount_type

    @property
    def message(self):
        """Gets the message of this AvailableCoupon.  # noqa: E501

        A description of the coupon.<br /><br /><span class=\"tablenote\"><b> Note: </b> The value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying coupons. The value in the <b>availableCoupons.message</b> field must also be included, if returned in the API response.</span>  # noqa: E501

        :return: The message of this AvailableCoupon.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AvailableCoupon.

        A description of the coupon.<br /><br /><span class=\"tablenote\"><b> Note: </b> The value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying coupons. The value in the <b>availableCoupons.message</b> field must also be included, if returned in the API response.</span>  # noqa: E501

        :param message: The message of this AvailableCoupon.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def redemption_code(self):
        """Gets the redemption_code of this AvailableCoupon.  # noqa: E501

        The coupon code.  # noqa: E501

        :return: The redemption_code of this AvailableCoupon.  # noqa: E501
        :rtype: str
        """
        return self._redemption_code

    @redemption_code.setter
    def redemption_code(self, redemption_code):
        """Sets the redemption_code of this AvailableCoupon.

        The coupon code.  # noqa: E501

        :param redemption_code: The redemption_code of this AvailableCoupon.  # noqa: E501
        :type: str
        """

        self._redemption_code = redemption_code

    @property
    def terms_web_url(self):
        """Gets the terms_web_url of this AvailableCoupon.  # noqa: E501

        The URL to the coupon terms of use.<br /><br /><span class=\"tablenote\"><b> Note: </b> The value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying coupons. The value in the <b>availableCoupons.message</b> field must also be included, if returned in the API response.</span>  # noqa: E501

        :return: The terms_web_url of this AvailableCoupon.  # noqa: E501
        :rtype: str
        """
        return self._terms_web_url

    @terms_web_url.setter
    def terms_web_url(self, terms_web_url):
        """Sets the terms_web_url of this AvailableCoupon.

        The URL to the coupon terms of use.<br /><br /><span class=\"tablenote\"><b> Note: </b> The value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying coupons. The value in the <b>availableCoupons.message</b> field must also be included, if returned in the API response.</span>  # noqa: E501

        :param terms_web_url: The terms_web_url of this AvailableCoupon.  # noqa: E501
        :type: str
        """

        self._terms_web_url = terms_web_url

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
        if issubclass(AvailableCoupon, dict):
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
        if not isinstance(other, AvailableCoupon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
