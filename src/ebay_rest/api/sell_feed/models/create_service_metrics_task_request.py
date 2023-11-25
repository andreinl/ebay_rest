# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateServiceMetricsTaskRequest(object):
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
        'feed_type': 'str',
        'filter_criteria': 'CustomerServiceMetricsFilterCriteria',
        'schema_version': 'str'
    }

    attribute_map = {
        'feed_type': 'feedType',
        'filter_criteria': 'filterCriteria',
        'schema_version': 'schemaVersion'
    }

    def __init__(self, feed_type=None, filter_criteria=None, schema_version=None):  # noqa: E501
        """CreateServiceMetricsTaskRequest - a model defined in Swagger"""  # noqa: E501
        self._feed_type = None
        self._filter_criteria = None
        self._schema_version = None
        self.discriminator = None
        if feed_type is not None:
            self.feed_type = feed_type
        if filter_criteria is not None:
            self.filter_criteria = filter_criteria
        if schema_version is not None:
            self.schema_version = schema_version

    @property
    def feed_type(self):
        """Gets the feed_type of this CreateServiceMetricsTaskRequest.  # noqa: E501

        The <strong>feedType</strong> specified for the customer service metric task being created. The report lists the transaction details that contribute to the service metrics evaluation. Supported types include:<p><code>CUSTOMER_SERVICE_METRICS_REPORT</code></p>  # noqa: E501

        :return: The feed_type of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this CreateServiceMetricsTaskRequest.

        The <strong>feedType</strong> specified for the customer service metric task being created. The report lists the transaction details that contribute to the service metrics evaluation. Supported types include:<p><code>CUSTOMER_SERVICE_METRICS_REPORT</code></p>  # noqa: E501

        :param feed_type: The feed_type of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :type: str
        """

        self._feed_type = feed_type

    @property
    def filter_criteria(self):
        """Gets the filter_criteria of this CreateServiceMetricsTaskRequest.  # noqa: E501


        :return: The filter_criteria of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :rtype: CustomerServiceMetricsFilterCriteria
        """
        return self._filter_criteria

    @filter_criteria.setter
    def filter_criteria(self, filter_criteria):
        """Sets the filter_criteria of this CreateServiceMetricsTaskRequest.


        :param filter_criteria: The filter_criteria of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :type: CustomerServiceMetricsFilterCriteria
        """

        self._filter_criteria = filter_criteria

    @property
    def schema_version(self):
        """Gets the schema_version of this CreateServiceMetricsTaskRequest.  # noqa: E501

        The version number of the customer service metric.<br><br><span class=\"tablenote\"><b>Note:</b> This field <b>must</b> have a value of <code>1.0</code>.</span>  # noqa: E501

        :return: The schema_version of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this CreateServiceMetricsTaskRequest.

        The version number of the customer service metric.<br><br><span class=\"tablenote\"><b>Note:</b> This field <b>must</b> have a value of <code>1.0</code>.</span>  # noqa: E501

        :param schema_version: The schema_version of this CreateServiceMetricsTaskRequest.  # noqa: E501
        :type: str
        """

        self._schema_version = schema_version

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
        if issubclass(CreateServiceMetricsTaskRequest, dict):
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
        if not isinstance(other, CreateServiceMetricsTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
