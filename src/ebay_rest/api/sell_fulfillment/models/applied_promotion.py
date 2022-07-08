# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AppliedPromotion(object):
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
        'description': 'str',
        'discount_amount': 'Amount',
        'promotion_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'discount_amount': 'discountAmount',
        'promotion_id': 'promotionId'
    }

    def __init__(self, description=None, discount_amount=None, promotion_id=None):  # noqa: E501
        """AppliedPromotion - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._discount_amount = None
        self._promotion_id = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if promotion_id is not None:
            self.promotion_id = promotion_id

    @property
    def description(self):
        """Gets the description of this AppliedPromotion.  # noqa: E501

        A description of the applied sales promotion.  # noqa: E501

        :return: The description of this AppliedPromotion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppliedPromotion.

        A description of the applied sales promotion.  # noqa: E501

        :param description: The description of this AppliedPromotion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_amount(self):
        """Gets the discount_amount of this AppliedPromotion.  # noqa: E501


        :return: The discount_amount of this AppliedPromotion.  # noqa: E501
        :rtype: Amount
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this AppliedPromotion.


        :param discount_amount: The discount_amount of this AppliedPromotion.  # noqa: E501
        :type: Amount
        """

        self._discount_amount = discount_amount

    @property
    def promotion_id(self):
        """Gets the promotion_id of this AppliedPromotion.  # noqa: E501

        An eBay-generated unique identifier of the sales promotion.<br/><br/> Multiple types of sales promotions are available to eBay Store owners, including order size/volume discounts, shipping discounts, special coupons, and price markdowns. Sales promotions can be managed through the Marketing tab of Seller Hub in My eBay, or by using the Trading API's <b>SetPromotionalSale</b> call or the Marketing API's <b>createItemPromotion</b> method.  # noqa: E501

        :return: The promotion_id of this AppliedPromotion.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this AppliedPromotion.

        An eBay-generated unique identifier of the sales promotion.<br/><br/> Multiple types of sales promotions are available to eBay Store owners, including order size/volume discounts, shipping discounts, special coupons, and price markdowns. Sales promotions can be managed through the Marketing tab of Seller Hub in My eBay, or by using the Trading API's <b>SetPromotionalSale</b> call or the Marketing API's <b>createItemPromotion</b> method.  # noqa: E501

        :param promotion_id: The promotion_id of this AppliedPromotion.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

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
        if issubclass(AppliedPromotion, dict):
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
        if not isinstance(other, AppliedPromotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
