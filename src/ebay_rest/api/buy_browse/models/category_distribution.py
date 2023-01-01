# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CategoryDistribution(object):
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
        'category_id': 'str',
        'category_name': 'str',
        'match_count': 'int',
        'refinement_href': 'str'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_name': 'categoryName',
        'match_count': 'matchCount',
        'refinement_href': 'refinementHref'
    }

    def __init__(self, category_id=None, category_name=None, match_count=None, refinement_href=None):  # noqa: E501
        """CategoryDistribution - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_name = None
        self._match_count = None
        self._refinement_href = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if match_count is not None:
            self.match_count = match_count
        if refinement_href is not None:
            self.refinement_href = refinement_href

    @property
    def category_id(self):
        """Gets the category_id of this CategoryDistribution.  # noqa: E501

        The identifier of the category.  # noqa: E501

        :return: The category_id of this CategoryDistribution.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CategoryDistribution.

        The identifier of the category.  # noqa: E501

        :param category_id: The category_id of this CategoryDistribution.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this CategoryDistribution.  # noqa: E501

        The name of the category, such as Baby & Toddler Clothing.  # noqa: E501

        :return: The category_name of this CategoryDistribution.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this CategoryDistribution.

        The name of the category, such as Baby & Toddler Clothing.  # noqa: E501

        :param category_name: The category_name of this CategoryDistribution.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def match_count(self):
        """Gets the match_count of this CategoryDistribution.  # noqa: E501

        The number of items in this category.  # noqa: E501

        :return: The match_count of this CategoryDistribution.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this CategoryDistribution.

        The number of items in this category.  # noqa: E501

        :param match_count: The match_count of this CategoryDistribution.  # noqa: E501
        :type: int
        """

        self._match_count = match_count

    @property
    def refinement_href(self):
        """Gets the refinement_href of this CategoryDistribution.  # noqa: E501

        The HATEOAS reference of this category.  # noqa: E501

        :return: The refinement_href of this CategoryDistribution.  # noqa: E501
        :rtype: str
        """
        return self._refinement_href

    @refinement_href.setter
    def refinement_href(self, refinement_href):
        """Sets the refinement_href of this CategoryDistribution.

        The HATEOAS reference of this category.  # noqa: E501

        :param refinement_href: The refinement_href of this CategoryDistribution.  # noqa: E501
        :type: str
        """

        self._refinement_href = refinement_href

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
        if issubclass(CategoryDistribution, dict):
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
        if not isinstance(other, CategoryDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
