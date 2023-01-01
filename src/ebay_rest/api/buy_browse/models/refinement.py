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

class Refinement(object):
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
        'aspect_distributions': 'list[AspectDistribution]',
        'buying_option_distributions': 'list[BuyingOptionDistribution]',
        'category_distributions': 'list[CategoryDistribution]',
        'condition_distributions': 'list[ConditionDistribution]',
        'dominant_category_id': 'str'
    }

    attribute_map = {
        'aspect_distributions': 'aspectDistributions',
        'buying_option_distributions': 'buyingOptionDistributions',
        'category_distributions': 'categoryDistributions',
        'condition_distributions': 'conditionDistributions',
        'dominant_category_id': 'dominantCategoryId'
    }

    def __init__(self, aspect_distributions=None, buying_option_distributions=None, category_distributions=None, condition_distributions=None, dominant_category_id=None):  # noqa: E501
        """Refinement - a model defined in Swagger"""  # noqa: E501
        self._aspect_distributions = None
        self._buying_option_distributions = None
        self._category_distributions = None
        self._condition_distributions = None
        self._dominant_category_id = None
        self.discriminator = None
        if aspect_distributions is not None:
            self.aspect_distributions = aspect_distributions
        if buying_option_distributions is not None:
            self.buying_option_distributions = buying_option_distributions
        if category_distributions is not None:
            self.category_distributions = category_distributions
        if condition_distributions is not None:
            self.condition_distributions = condition_distributions
        if dominant_category_id is not None:
            self.dominant_category_id = dominant_category_id

    @property
    def aspect_distributions(self):
        """Gets the aspect_distributions of this Refinement.  # noqa: E501

        An array of containers for the all the aspect refinements.  # noqa: E501

        :return: The aspect_distributions of this Refinement.  # noqa: E501
        :rtype: list[AspectDistribution]
        """
        return self._aspect_distributions

    @aspect_distributions.setter
    def aspect_distributions(self, aspect_distributions):
        """Sets the aspect_distributions of this Refinement.

        An array of containers for the all the aspect refinements.  # noqa: E501

        :param aspect_distributions: The aspect_distributions of this Refinement.  # noqa: E501
        :type: list[AspectDistribution]
        """

        self._aspect_distributions = aspect_distributions

    @property
    def buying_option_distributions(self):
        """Gets the buying_option_distributions of this Refinement.  # noqa: E501

        An array of containers for the all the buying option refinements.  # noqa: E501

        :return: The buying_option_distributions of this Refinement.  # noqa: E501
        :rtype: list[BuyingOptionDistribution]
        """
        return self._buying_option_distributions

    @buying_option_distributions.setter
    def buying_option_distributions(self, buying_option_distributions):
        """Sets the buying_option_distributions of this Refinement.

        An array of containers for the all the buying option refinements.  # noqa: E501

        :param buying_option_distributions: The buying_option_distributions of this Refinement.  # noqa: E501
        :type: list[BuyingOptionDistribution]
        """

        self._buying_option_distributions = buying_option_distributions

    @property
    def category_distributions(self):
        """Gets the category_distributions of this Refinement.  # noqa: E501

        An array of containers for the all the category refinements.  # noqa: E501

        :return: The category_distributions of this Refinement.  # noqa: E501
        :rtype: list[CategoryDistribution]
        """
        return self._category_distributions

    @category_distributions.setter
    def category_distributions(self, category_distributions):
        """Sets the category_distributions of this Refinement.

        An array of containers for the all the category refinements.  # noqa: E501

        :param category_distributions: The category_distributions of this Refinement.  # noqa: E501
        :type: list[CategoryDistribution]
        """

        self._category_distributions = category_distributions

    @property
    def condition_distributions(self):
        """Gets the condition_distributions of this Refinement.  # noqa: E501

        An array of containers for the all the condition refinements.  # noqa: E501

        :return: The condition_distributions of this Refinement.  # noqa: E501
        :rtype: list[ConditionDistribution]
        """
        return self._condition_distributions

    @condition_distributions.setter
    def condition_distributions(self, condition_distributions):
        """Sets the condition_distributions of this Refinement.

        An array of containers for the all the condition refinements.  # noqa: E501

        :param condition_distributions: The condition_distributions of this Refinement.  # noqa: E501
        :type: list[ConditionDistribution]
        """

        self._condition_distributions = condition_distributions

    @property
    def dominant_category_id(self):
        """Gets the dominant_category_id of this Refinement.  # noqa: E501

        The identifier of the category that most of the items are part of.   # noqa: E501

        :return: The dominant_category_id of this Refinement.  # noqa: E501
        :rtype: str
        """
        return self._dominant_category_id

    @dominant_category_id.setter
    def dominant_category_id(self, dominant_category_id):
        """Sets the dominant_category_id of this Refinement.

        The identifier of the category that most of the items are part of.   # noqa: E501

        :param dominant_category_id: The dominant_category_id of this Refinement.  # noqa: E501
        :type: str
        """

        self._dominant_category_id = dominant_category_id

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
        if issubclass(Refinement, dict):
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
        if not isinstance(other, Refinement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
