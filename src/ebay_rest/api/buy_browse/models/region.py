# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Region(object):
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
        'region_name': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'region_name': 'regionName',
        'region_type': 'regionType'
    }

    def __init__(self, region_name=None, region_type=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501
        self._region_name = None
        self._region_type = None
        self.discriminator = None
        if region_name is not None:
            self.region_name = region_name
        if region_type is not None:
            self.region_type = region_type

    @property
    def region_name(self):
        """Gets the region_name of this Region.  # noqa: E501

        A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level or at the country level in the case of VAT tax.   # noqa: E501

        :return: The region_name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this Region.

        A localized text string that indicates the name of the region. Taxes are generally charged at the state/province level or at the country level in the case of VAT tax.   # noqa: E501

        :param region_name: The region_name of this Region.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_type(self):
        """Gets the region_type of this Region.  # noqa: E501

        An enumeration value that indicates the type of region for the tax jurisdiction. <br><br><b> Valid Values: </b> <ul><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li></ul>  Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The region_type of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this Region.

        An enumeration value that indicates the type of region for the tax jurisdiction. <br><br><b> Valid Values: </b> <ul><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li></ul>  Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param region_type: The region_type of this Region.  # noqa: E501
        :type: str
        """

        self._region_type = region_type

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
        if issubclass(Region, dict):
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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
