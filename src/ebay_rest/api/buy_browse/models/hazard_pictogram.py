# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  </ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HazardPictogram(object):
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
        'pictogram_description': 'str',
        'pictogram_id': 'str',
        'pictogram_url': 'str'
    }

    attribute_map = {
        'pictogram_description': 'pictogramDescription',
        'pictogram_id': 'pictogramId',
        'pictogram_url': 'pictogramUrl'
    }

    def __init__(self, pictogram_description=None, pictogram_id=None, pictogram_url=None):  # noqa: E501
        """HazardPictogram - a model defined in Swagger"""  # noqa: E501
        self._pictogram_description = None
        self._pictogram_id = None
        self._pictogram_url = None
        self.discriminator = None
        if pictogram_description is not None:
            self.pictogram_description = pictogram_description
        if pictogram_id is not None:
            self.pictogram_id = pictogram_id
        if pictogram_url is not None:
            self.pictogram_url = pictogram_url

    @property
    def pictogram_description(self):
        """Gets the pictogram_description of this HazardPictogram.  # noqa: E501

        The description of the hazard pictogram, such as Flammable.  # noqa: E501

        :return: The pictogram_description of this HazardPictogram.  # noqa: E501
        :rtype: str
        """
        return self._pictogram_description

    @pictogram_description.setter
    def pictogram_description(self, pictogram_description):
        """Sets the pictogram_description of this HazardPictogram.

        The description of the hazard pictogram, such as Flammable.  # noqa: E501

        :param pictogram_description: The pictogram_description of this HazardPictogram.  # noqa: E501
        :type: str
        """

        self._pictogram_description = pictogram_description

    @property
    def pictogram_id(self):
        """Gets the pictogram_id of this HazardPictogram.  # noqa: E501

        The ID of the hazard pictogram.  # noqa: E501

        :return: The pictogram_id of this HazardPictogram.  # noqa: E501
        :rtype: str
        """
        return self._pictogram_id

    @pictogram_id.setter
    def pictogram_id(self, pictogram_id):
        """Sets the pictogram_id of this HazardPictogram.

        The ID of the hazard pictogram.  # noqa: E501

        :param pictogram_id: The pictogram_id of this HazardPictogram.  # noqa: E501
        :type: str
        """

        self._pictogram_id = pictogram_id

    @property
    def pictogram_url(self):
        """Gets the pictogram_url of this HazardPictogram.  # noqa: E501

        The URL of the hazard pictogram.  # noqa: E501

        :return: The pictogram_url of this HazardPictogram.  # noqa: E501
        :rtype: str
        """
        return self._pictogram_url

    @pictogram_url.setter
    def pictogram_url(self, pictogram_url):
        """Sets the pictogram_url of this HazardPictogram.

        The URL of the hazard pictogram.  # noqa: E501

        :param pictogram_url: The pictogram_url of this HazardPictogram.  # noqa: E501
        :type: str
        """

        self._pictogram_url = pictogram_url

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
        if issubclass(HazardPictogram, dict):
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
        if not isinstance(other, HazardPictogram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
