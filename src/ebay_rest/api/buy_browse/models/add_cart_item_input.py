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

class AddCartItemInput(object):
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
        'item_id': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'item_id': 'itemId',
        'quantity': 'quantity'
    }

    def __init__(self, item_id=None, quantity=None):  # noqa: E501
        """AddCartItemInput - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._quantity = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def item_id(self):
        """Gets the item_id of this AddCartItemInput.  # noqa: E501

        The eBay RESTful identifier of the item you want added to the cart. <br /><br /> <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code> <br /><b> For example: </b> <br /><code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code> <br /><br />For more information about item ID for RESTful APIs, see the <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a> section of the <i>Buy APIs Overview</i>.<br /><br /><b> Maximum number of items in a cart: </b> 100  # noqa: E501

        :return: The item_id of this AddCartItemInput.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this AddCartItemInput.

        The eBay RESTful identifier of the item you want added to the cart. <br /><br /> <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code> <br /><b> For example: </b> <br /><code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code> <br /><br />For more information about item ID for RESTful APIs, see the <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a> section of the <i>Buy APIs Overview</i>.<br /><br /><b> Maximum number of items in a cart: </b> 100  # noqa: E501

        :param item_id: The item_id of this AddCartItemInput.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def quantity(self):
        """Gets the quantity of this AddCartItemInput.  # noqa: E501

        The number of this item the buyer wants to purchase. If this value is greater than the number available, the service will change this value to the number available. If this happens, a warning is returned.<br /><br /><b> Maximum: </b> <i>number available</i>  # noqa: E501

        :return: The quantity of this AddCartItemInput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this AddCartItemInput.

        The number of this item the buyer wants to purchase. If this value is greater than the number available, the service will change this value to the number available. If this happens, a warning is returned.<br /><br /><b> Maximum: </b> <i>number available</i>  # noqa: E501

        :param quantity: The quantity of this AddCartItemInput.  # noqa: E501
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
        if issubclass(AddCartItemInput, dict):
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
        if not isinstance(other, AddCartItemInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
