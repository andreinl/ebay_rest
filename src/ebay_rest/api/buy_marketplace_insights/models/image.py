# coding: utf-8

"""
    Marketplace Insights API

    <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> The Marketplace Insights API provides the ability to search for sold items on eBay by keyword, GTIN, category, and product and returns the of sales history of those items.  # noqa: E501

    OpenAPI spec version: v1_beta.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Image(object):
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
        'height': 'int',
        'image_url': 'str',
        'width': 'int'
    }

    attribute_map = {
        'height': 'height',
        'image_url': 'imageUrl',
        'width': 'width'
    }

    def __init__(self, height=None, image_url=None, width=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._height = None
        self._image_url = None
        self._width = None
        self.discriminator = None
        if height is not None:
            self.height = height
        if image_url is not None:
            self.image_url = image_url
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this Image.  # noqa: E501

        <b> Reserved for future use. </b>   # noqa: E501

        :return: The height of this Image.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Image.

        <b> Reserved for future use. </b>   # noqa: E501

        :param height: The height of this Image.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def image_url(self):
        """Gets the image_url of this Image.  # noqa: E501

        The URL of the image.  # noqa: E501

        :return: The image_url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Image.

        The URL of the image.  # noqa: E501

        :param image_url: The image_url of this Image.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def width(self):
        """Gets the width of this Image.  # noqa: E501

        <b> Reserved for future use. </b>   # noqa: E501

        :return: The width of this Image.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Image.

        <b> Reserved for future use. </b>   # noqa: E501

        :param width: The width of this Image.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
