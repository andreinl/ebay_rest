# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns data on a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns data pertaining to a seller's performance rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Cycle(object):
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
        'cycle_type': 'str',
        'evaluation_date': 'str',
        'evaluation_month': 'str'
    }

    attribute_map = {
        'cycle_type': 'cycleType',
        'evaluation_date': 'evaluationDate',
        'evaluation_month': 'evaluationMonth'
    }

    def __init__(self, cycle_type=None, evaluation_date=None, evaluation_month=None):  # noqa: E501
        """Cycle - a model defined in Swagger"""  # noqa: E501
        self._cycle_type = None
        self._evaluation_date = None
        self._evaluation_month = None
        self.discriminator = None
        if cycle_type is not None:
            self.cycle_type = cycle_type
        if evaluation_date is not None:
            self.evaluation_date = evaluation_date
        if evaluation_month is not None:
            self.evaluation_month = evaluation_month

    @property
    def cycle_type(self):
        """Gets the cycle_type of this Cycle.  # noqa: E501

        The cycle type, either CURRENT or PROJECTED. CURRENT means the profile's metrics values are from the most recent official eBay monthly standards evaluation. PROJECTED means the profile values were determined when the profile was requested. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/ssp:CycleTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The cycle_type of this Cycle.  # noqa: E501
        :rtype: str
        """
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, cycle_type):
        """Sets the cycle_type of this Cycle.

        The cycle type, either CURRENT or PROJECTED. CURRENT means the profile's metrics values are from the most recent official eBay monthly standards evaluation. PROJECTED means the profile values were determined when the profile was requested. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/ssp:CycleTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param cycle_type: The cycle_type of this Cycle.  # noqa: E501
        :type: str
        """

        self._cycle_type = cycle_type

    @property
    def evaluation_date(self):
        """Gets the evaluation_date of this Cycle.  # noqa: E501

        The date and time at which the standard compliance values were determined for the profile. The time stamp is formatted as an ISO 8601 string, which is based on the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z  # noqa: E501

        :return: The evaluation_date of this Cycle.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_date

    @evaluation_date.setter
    def evaluation_date(self, evaluation_date):
        """Sets the evaluation_date of this Cycle.

        The date and time at which the standard compliance values were determined for the profile. The time stamp is formatted as an ISO 8601 string, which is based on the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z  # noqa: E501

        :param evaluation_date: The evaluation_date of this Cycle.  # noqa: E501
        :type: str
        """

        self._evaluation_date = evaluation_date

    @property
    def evaluation_month(self):
        """Gets the evaluation_month of this Cycle.  # noqa: E501

        The month in which the currently effective seller level was computed. The value is always formatted as YYYY-MM. If the cycle is CURRENT, this value is the month and year the of the last eBay compliance evaluation. If this is for a PROJECTED cycle, the value is the month and year of the next scheduled evaluation. Because eBay does official evaluations around the 20th of each month, a PROJECTED value may indicate either the current or the next month.  # noqa: E501

        :return: The evaluation_month of this Cycle.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_month

    @evaluation_month.setter
    def evaluation_month(self, evaluation_month):
        """Sets the evaluation_month of this Cycle.

        The month in which the currently effective seller level was computed. The value is always formatted as YYYY-MM. If the cycle is CURRENT, this value is the month and year the of the last eBay compliance evaluation. If this is for a PROJECTED cycle, the value is the month and year of the next scheduled evaluation. Because eBay does official evaluations around the 20th of each month, a PROJECTED value may indicate either the current or the next month.  # noqa: E501

        :param evaluation_month: The evaluation_month of this Cycle.  # noqa: E501
        :type: str
        """

        self._evaluation_month = evaluation_month

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
        if issubclass(Cycle, dict):
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
        if not isinstance(other, Cycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
