# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CancelRequest(object):
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
        'cancel_completed_date': 'str',
        'cancel_initiator': 'str',
        'cancel_reason': 'str',
        'cancel_requested_date': 'str',
        'cancel_request_id': 'str',
        'cancel_request_state': 'str'
    }

    attribute_map = {
        'cancel_completed_date': 'cancelCompletedDate',
        'cancel_initiator': 'cancelInitiator',
        'cancel_reason': 'cancelReason',
        'cancel_requested_date': 'cancelRequestedDate',
        'cancel_request_id': 'cancelRequestId',
        'cancel_request_state': 'cancelRequestState'
    }

    def __init__(self, cancel_completed_date=None, cancel_initiator=None, cancel_reason=None, cancel_requested_date=None, cancel_request_id=None, cancel_request_state=None):  # noqa: E501
        """CancelRequest - a model defined in Swagger"""  # noqa: E501
        self._cancel_completed_date = None
        self._cancel_initiator = None
        self._cancel_reason = None
        self._cancel_requested_date = None
        self._cancel_request_id = None
        self._cancel_request_state = None
        self.discriminator = None
        if cancel_completed_date is not None:
            self.cancel_completed_date = cancel_completed_date
        if cancel_initiator is not None:
            self.cancel_initiator = cancel_initiator
        if cancel_reason is not None:
            self.cancel_reason = cancel_reason
        if cancel_requested_date is not None:
            self.cancel_requested_date = cancel_requested_date
        if cancel_request_id is not None:
            self.cancel_request_id = cancel_request_id
        if cancel_request_state is not None:
            self.cancel_request_state = cancel_request_state

    @property
    def cancel_completed_date(self):
        """Gets the cancel_completed_date of this CancelRequest.  # noqa: E501

        The date and time that the order cancellation was completed, if applicable. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the cancellation request has actually been approved by the seller. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :return: The cancel_completed_date of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_completed_date

    @cancel_completed_date.setter
    def cancel_completed_date(self, cancel_completed_date):
        """Sets the cancel_completed_date of this CancelRequest.

        The date and time that the order cancellation was completed, if applicable. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the cancellation request has actually been approved by the seller. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :param cancel_completed_date: The cancel_completed_date of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_completed_date = cancel_completed_date

    @property
    def cancel_initiator(self):
        """Gets the cancel_initiator of this CancelRequest.  # noqa: E501

        This string value indicates the party who made the initial cancellation request. Typically, either the 'Buyer' or 'Seller'. If a cancellation request has been made, this field should be returned.  # noqa: E501

        :return: The cancel_initiator of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_initiator

    @cancel_initiator.setter
    def cancel_initiator(self, cancel_initiator):
        """Sets the cancel_initiator of this CancelRequest.

        This string value indicates the party who made the initial cancellation request. Typically, either the 'Buyer' or 'Seller'. If a cancellation request has been made, this field should be returned.  # noqa: E501

        :param cancel_initiator: The cancel_initiator of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_initiator = cancel_initiator

    @property
    def cancel_reason(self):
        """Gets the cancel_reason of this CancelRequest.  # noqa: E501

        The reason why the cancelInitiator initiated the cancellation request. Cancellation reasons for a buyer might include 'order placed by mistake' or 'order won't arrive in time'. For a seller, a typical cancellation reason is 'out of stock'. If a cancellation request has been made, this field should be returned.  # noqa: E501

        :return: The cancel_reason of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, cancel_reason):
        """Sets the cancel_reason of this CancelRequest.

        The reason why the cancelInitiator initiated the cancellation request. Cancellation reasons for a buyer might include 'order placed by mistake' or 'order won't arrive in time'. For a seller, a typical cancellation reason is 'out of stock'. If a cancellation request has been made, this field should be returned.  # noqa: E501

        :param cancel_reason: The cancel_reason of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_reason = cancel_reason

    @property
    def cancel_requested_date(self):
        """Gets the cancel_requested_date of this CancelRequest.  # noqa: E501

        The date and time that the order cancellation was requested. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is returned for each cancellation request. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :return: The cancel_requested_date of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_requested_date

    @cancel_requested_date.setter
    def cancel_requested_date(self, cancel_requested_date):
        """Sets the cancel_requested_date of this CancelRequest.

        The date and time that the order cancellation was requested. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is returned for each cancellation request. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :param cancel_requested_date: The cancel_requested_date of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_requested_date = cancel_requested_date

    @property
    def cancel_request_id(self):
        """Gets the cancel_request_id of this CancelRequest.  # noqa: E501

        The unique identifier of the order cancellation request. This field is returned for each cancellation request.  # noqa: E501

        :return: The cancel_request_id of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_request_id

    @cancel_request_id.setter
    def cancel_request_id(self, cancel_request_id):
        """Sets the cancel_request_id of this CancelRequest.

        The unique identifier of the order cancellation request. This field is returned for each cancellation request.  # noqa: E501

        :param cancel_request_id: The cancel_request_id of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_request_id = cancel_request_id

    @property
    def cancel_request_state(self):
        """Gets the cancel_request_state of this CancelRequest.  # noqa: E501

        The current stage or condition of the cancellation request. This field is returned for each cancellation request. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:CancelRequestStateEnum'>eBay API documentation</a>  # noqa: E501

        :return: The cancel_request_state of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_request_state

    @cancel_request_state.setter
    def cancel_request_state(self, cancel_request_state):
        """Sets the cancel_request_state of this CancelRequest.

        The current stage or condition of the cancellation request. This field is returned for each cancellation request. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:CancelRequestStateEnum'>eBay API documentation</a>  # noqa: E501

        :param cancel_request_state: The cancel_request_state of this CancelRequest.  # noqa: E501
        :type: str
        """

        self._cancel_request_state = cancel_request_state

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
        if issubclass(CancelRequest, dict):
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
        if not isinstance(other, CancelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
