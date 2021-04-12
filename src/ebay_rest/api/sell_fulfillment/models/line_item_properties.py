# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LineItemProperties(object):
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
        'buyer_protection': 'bool',
        'from_best_offer': 'bool',
        'sold_via_ad_campaign': 'bool'
    }

    attribute_map = {
        'buyer_protection': 'buyerProtection',
        'from_best_offer': 'fromBestOffer',
        'sold_via_ad_campaign': 'soldViaAdCampaign'
    }

    def __init__(self, buyer_protection=None, from_best_offer=None, sold_via_ad_campaign=None):  # noqa: E501
        """LineItemProperties - a model defined in Swagger"""  # noqa: E501
        self._buyer_protection = None
        self._from_best_offer = None
        self._sold_via_ad_campaign = None
        self.discriminator = None
        if buyer_protection is not None:
            self.buyer_protection = buyer_protection
        if from_best_offer is not None:
            self.from_best_offer = from_best_offer
        if sold_via_ad_campaign is not None:
            self.sold_via_ad_campaign = sold_via_ad_campaign

    @property
    def buyer_protection(self):
        """Gets the buyer_protection of this LineItemProperties.  # noqa: E501

        A value of true indicates that the line item is covered by eBay's Buyer Protection program.  # noqa: E501

        :return: The buyer_protection of this LineItemProperties.  # noqa: E501
        :rtype: bool
        """
        return self._buyer_protection

    @buyer_protection.setter
    def buyer_protection(self, buyer_protection):
        """Sets the buyer_protection of this LineItemProperties.

        A value of true indicates that the line item is covered by eBay's Buyer Protection program.  # noqa: E501

        :param buyer_protection: The buyer_protection of this LineItemProperties.  # noqa: E501
        :type: bool
        """

        self._buyer_protection = buyer_protection

    @property
    def from_best_offer(self):
        """Gets the from_best_offer of this LineItemProperties.  # noqa: E501

        This field is only returned if true and indicates that the purchase occurred by the buyer and seller mutually agreeing on a Best Offer amount. The Best Offer feature can be set up for any listing type, but if this feature is set up for an auction listing, it will no longer be available once a bid has been placed on the listing.  # noqa: E501

        :return: The from_best_offer of this LineItemProperties.  # noqa: E501
        :rtype: bool
        """
        return self._from_best_offer

    @from_best_offer.setter
    def from_best_offer(self, from_best_offer):
        """Sets the from_best_offer of this LineItemProperties.

        This field is only returned if true and indicates that the purchase occurred by the buyer and seller mutually agreeing on a Best Offer amount. The Best Offer feature can be set up for any listing type, but if this feature is set up for an auction listing, it will no longer be available once a bid has been placed on the listing.  # noqa: E501

        :param from_best_offer: The from_best_offer of this LineItemProperties.  # noqa: E501
        :type: bool
        """

        self._from_best_offer = from_best_offer

    @property
    def sold_via_ad_campaign(self):
        """Gets the sold_via_ad_campaign of this LineItemProperties.  # noqa: E501

        This field is only returned if true and indicates that the line item was sold as a result of a seller's ad campaign.  # noqa: E501

        :return: The sold_via_ad_campaign of this LineItemProperties.  # noqa: E501
        :rtype: bool
        """
        return self._sold_via_ad_campaign

    @sold_via_ad_campaign.setter
    def sold_via_ad_campaign(self, sold_via_ad_campaign):
        """Sets the sold_via_ad_campaign of this LineItemProperties.

        This field is only returned if true and indicates that the line item was sold as a result of a seller's ad campaign.  # noqa: E501

        :param sold_via_ad_campaign: The sold_via_ad_campaign of this LineItemProperties.  # noqa: E501
        :type: bool
        """

        self._sold_via_ad_campaign = sold_via_ad_campaign

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
        if issubclass(LineItemProperties, dict):
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
        if not isinstance(other, LineItemProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
