# coding: utf-8

"""
    Notification API

    The eBay Notification API enables management of the entire end-to-end eBay notification experience by allowing users to:<ul><li>Browse for supported notification topics and retrieve topic details</li><li>Create, configure, and manage notification destination endpionts</li><li>Configure, manage, and test notification subscriptions</li><li>Process eBay notifications and verify the integrity of the message payload</li></ul>  # noqa: E501

    OpenAPI spec version: v1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SubscriptionPayloadDetail(object):
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
        'format': 'str',
        'schema_version': 'str',
        'delivery_protocol': 'str'
    }

    attribute_map = {
        'format': 'format',
        'schema_version': 'schemaVersion',
        'delivery_protocol': 'deliveryProtocol'
    }

    def __init__(self, format=None, schema_version=None, delivery_protocol=None):  # noqa: E501
        """SubscriptionPayloadDetail - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._schema_version = None
        self._delivery_protocol = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if schema_version is not None:
            self.schema_version = schema_version
        if delivery_protocol is not None:
            self.delivery_protocol = delivery_protocol

    @property
    def format(self):
        """Gets the format of this SubscriptionPayloadDetail.  # noqa: E501

        The supported format. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The format of this SubscriptionPayloadDetail.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SubscriptionPayloadDetail.

        The supported format. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param format: The format of this SubscriptionPayloadDetail.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def schema_version(self):
        """Gets the schema_version of this SubscriptionPayloadDetail.  # noqa: E501

        The supported schema version.  # noqa: E501

        :return: The schema_version of this SubscriptionPayloadDetail.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this SubscriptionPayloadDetail.

        The supported schema version.  # noqa: E501

        :param schema_version: The schema_version of this SubscriptionPayloadDetail.  # noqa: E501
        :type: str
        """

        self._schema_version = schema_version

    @property
    def delivery_protocol(self):
        """Gets the delivery_protocol of this SubscriptionPayloadDetail.  # noqa: E501

        The supported protocol. For exmaple: <code>HTTPS</code> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:ProtocolEnum'>eBay API documentation</a>  # noqa: E501

        :return: The delivery_protocol of this SubscriptionPayloadDetail.  # noqa: E501
        :rtype: str
        """
        return self._delivery_protocol

    @delivery_protocol.setter
    def delivery_protocol(self, delivery_protocol):
        """Sets the delivery_protocol of this SubscriptionPayloadDetail.

        The supported protocol. For exmaple: <code>HTTPS</code> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/commerce/notification/types/api:ProtocolEnum'>eBay API documentation</a>  # noqa: E501

        :param delivery_protocol: The delivery_protocol of this SubscriptionPayloadDetail.  # noqa: E501
        :type: str
        """

        self._delivery_protocol = delivery_protocol

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
        if issubclass(SubscriptionPayloadDetail, dict):
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
        if not isinstance(other, SubscriptionPayloadDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
