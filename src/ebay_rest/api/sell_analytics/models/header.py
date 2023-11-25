# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns benchmark data and a metric rating pertaining to a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data and information that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns information pertaining to a seller's profile rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Header(object):
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
        'dimension_keys': 'list[Definition]',
        'metrics': 'list[Definition]'
    }

    attribute_map = {
        'dimension_keys': 'dimensionKeys',
        'metrics': 'metrics'
    }

    def __init__(self, dimension_keys=None, metrics=None):  # noqa: E501
        """Header - a model defined in Swagger"""  # noqa: E501
        self._dimension_keys = None
        self._metrics = None
        self.discriminator = None
        if dimension_keys is not None:
            self.dimension_keys = dimension_keys
        if metrics is not None:
            self.metrics = metrics

    @property
    def dimension_keys(self):
        """Gets the dimension_keys of this Header.  # noqa: E501

        A list of the dimension or metric keys returned in the report. The values for each are is returned in the associated <b>key</b> fields.  # noqa: E501

        :return: The dimension_keys of this Header.  # noqa: E501
        :rtype: list[Definition]
        """
        return self._dimension_keys

    @dimension_keys.setter
    def dimension_keys(self, dimension_keys):
        """Sets the dimension_keys of this Header.

        A list of the dimension or metric keys returned in the report. The values for each are is returned in the associated <b>key</b> fields.  # noqa: E501

        :param dimension_keys: The dimension_keys of this Header.  # noqa: E501
        :type: list[Definition]
        """

        self._dimension_keys = dimension_keys

    @property
    def metrics(self):
        """Gets the metrics of this Header.  # noqa: E501

        The list of metrics returned in the report. The values for each are is returned in the associated <b>key</b> fields.  # noqa: E501

        :return: The metrics of this Header.  # noqa: E501
        :rtype: list[Definition]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Header.

        The list of metrics returned in the report. The values for each are is returned in the associated <b>key</b> fields.  # noqa: E501

        :param metrics: The metrics of this Header.  # noqa: E501
        :type: list[Definition]
        """

        self._metrics = metrics

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
        if issubclass(Header, dict):
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
        if not isinstance(other, Header):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
