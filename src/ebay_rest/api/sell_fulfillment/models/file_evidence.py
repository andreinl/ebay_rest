# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileEvidence(object):
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
        'file_id': 'str'
    }

    attribute_map = {
        'file_id': 'fileId'
    }

    def __init__(self, file_id=None):  # noqa: E501
        """FileEvidence - a model defined in Swagger"""  # noqa: E501
        self._file_id = None
        self.discriminator = None
        if file_id is not None:
            self.file_id = file_id

    @property
    def file_id(self):
        """Gets the file_id of this FileEvidence.  # noqa: E501

        If an <strong>uploadEvidenceFile</strong> call is successful, a unique identifier of this evidence file will be returned in the <strong>uploadEvidenceFile</strong> response payload.  This unique <strong>fileId</strong> value is then used to either add this evidence file to a new evidence set using the <strong>addEvidence</strong> method, or to add this file to an existing evidence set using the <strong>updateEvidence</strong> method.<br><br>Note that if an evidence set already exists for a payment dispute, the <strong>getPaymentDispute</strong> method will return both the <strong>evidenceId</strong> (unique identifier of evidence set) value, and the <strong>fileId</strong> (unique identifier of a file within that evidence set) value(s).  # noqa: E501

        :return: The file_id of this FileEvidence.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileEvidence.

        If an <strong>uploadEvidenceFile</strong> call is successful, a unique identifier of this evidence file will be returned in the <strong>uploadEvidenceFile</strong> response payload.  This unique <strong>fileId</strong> value is then used to either add this evidence file to a new evidence set using the <strong>addEvidence</strong> method, or to add this file to an existing evidence set using the <strong>updateEvidence</strong> method.<br><br>Note that if an evidence set already exists for a payment dispute, the <strong>getPaymentDispute</strong> method will return both the <strong>evidenceId</strong> (unique identifier of evidence set) value, and the <strong>fileId</strong> (unique identifier of a file within that evidence set) value(s).  # noqa: E501

        :param file_id: The file_id of this FileEvidence.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

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
        if issubclass(FileEvidence, dict):
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
        if not isinstance(other, FileEvidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
