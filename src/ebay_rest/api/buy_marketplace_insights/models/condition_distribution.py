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

class ConditionDistribution(object):
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
        'condition': 'str',
        'condition_id': 'str',
        'match_count': 'int',
        'refinement_href': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'condition_id': 'conditionId',
        'match_count': 'matchCount',
        'refinement_href': 'refinementHref'
    }

    def __init__(self, condition=None, condition_id=None, match_count=None, refinement_href=None):  # noqa: E501
        """ConditionDistribution - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._condition_id = None
        self._match_count = None
        self._refinement_href = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if condition_id is not None:
            self.condition_id = condition_id
        if match_count is not None:
            self.match_count = match_count
        if refinement_href is not None:
            self.refinement_href = refinement_href

    @property
    def condition(self):
        """Gets the condition of this ConditionDistribution.  # noqa: E501

        The text describing the condition of the item, such as New or Used. For a list of condition names, see <a href=\"https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html\" target=\"_blank\"\">ConditionEnum</a>.  <br /><br />Code so that your app gracefully handles any future changes to this list.  # noqa: E501

        :return: The condition of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ConditionDistribution.

        The text describing the condition of the item, such as New or Used. For a list of condition names, see <a href=\"https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html\" target=\"_blank\"\">ConditionEnum</a>.  <br /><br />Code so that your app gracefully handles any future changes to this list.  # noqa: E501

        :param condition: The condition of this ConditionDistribution.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def condition_id(self):
        """Gets the condition_id of this ConditionDistribution.  # noqa: E501

        The identifier of the condition. For example, 1000 is the identifier for NEW.  # noqa: E501

        :return: The condition_id of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this ConditionDistribution.

        The identifier of the condition. For example, 1000 is the identifier for NEW.  # noqa: E501

        :param condition_id: The condition_id of this ConditionDistribution.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

    @property
    def match_count(self):
        """Gets the match_count of this ConditionDistribution.  # noqa: E501

        The number of items having the condition.  # noqa: E501

        :return: The match_count of this ConditionDistribution.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this ConditionDistribution.

        The number of items having the condition.  # noqa: E501

        :param match_count: The match_count of this ConditionDistribution.  # noqa: E501
        :type: int
        """

        self._match_count = match_count

    @property
    def refinement_href(self):
        """Gets the refinement_href of this ConditionDistribution.  # noqa: E501

        The HATEOAS reference of this condition.  # noqa: E501

        :return: The refinement_href of this ConditionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._refinement_href

    @refinement_href.setter
    def refinement_href(self, refinement_href):
        """Sets the refinement_href of this ConditionDistribution.

        The HATEOAS reference of this condition.  # noqa: E501

        :param refinement_href: The refinement_href of this ConditionDistribution.  # noqa: E501
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
        if issubclass(ConditionDistribution, dict):
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
        if not isinstance(other, ConditionDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
