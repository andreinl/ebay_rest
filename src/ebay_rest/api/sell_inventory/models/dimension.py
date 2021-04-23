# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.13.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Dimension(object):
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
        'height': 'float',
        'length': 'float',
        'unit': 'str',
        'width': 'float'
    }

    attribute_map = {
        'height': 'height',
        'length': 'length',
        'unit': 'unit',
        'width': 'width'
    }

    def __init__(self, height=None, length=None, unit=None, width=None):  # noqa: E501
        """Dimension - a model defined in Swagger"""  # noqa: E501
        self._height = None
        self._length = None
        self._unit = None
        self._width = None
        self.discriminator = None
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if unit is not None:
            self.unit = unit
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this Dimension.  # noqa: E501

        The actual height (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :return: The height of this Dimension.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Dimension.

        The actual height (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :param height: The height of this Dimension.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this Dimension.  # noqa: E501

        The actual length (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :return: The length of this Dimension.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Dimension.

        The actual length (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :param length: The length of this Dimension.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def unit(self):
        """Gets the unit of this Dimension.  # noqa: E501

        The unit of measurement used to specify the dimensions of a shipping package. All fields of the dimensions container are required if package dimensions are specified. If the English system of measurement is being used, the applicable values for dimension units are FEET and INCH. If the metric system of measurement is being used, the applicable values for weight units are METER and CENTIMETER. The metric system is used by most countries outside of the US. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LengthUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :return: The unit of this Dimension.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Dimension.

        The unit of measurement used to specify the dimensions of a shipping package. All fields of the dimensions container are required if package dimensions are specified. If the English system of measurement is being used, the applicable values for dimension units are FEET and INCH. If the metric system of measurement is being used, the applicable values for weight units are METER and CENTIMETER. The metric system is used by most countries outside of the US. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:LengthUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :param unit: The unit of this Dimension.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def width(self):
        """Gets the width of this Dimension.  # noqa: E501

        The actual width (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :return: The width of this Dimension.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Dimension.

        The actual width (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &quot;dimensions&quot;: {  &quot;length&quot;: 21.5,  &quot;width&quot;: 15.0,  &quot;height&quot;: 12.0,  &quot;unit&quot;: &quot;INCH&quot;  }  # noqa: E501

        :param width: The width of this Dimension.  # noqa: E501
        :type: float
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
        if issubclass(Dimension, dict):
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
        if not isinstance(other, Dimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
