# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrderRefund(object):
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
        'amount': 'Amount',
        'refund_date': 'str',
        'refund_id': 'str',
        'refund_reference_id': 'str',
        'refund_status': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'refund_date': 'refundDate',
        'refund_id': 'refundId',
        'refund_reference_id': 'refundReferenceId',
        'refund_status': 'refundStatus'
    }

    def __init__(self, amount=None, refund_date=None, refund_id=None, refund_reference_id=None, refund_status=None):  # noqa: E501
        """OrderRefund - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._refund_date = None
        self._refund_id = None
        self._refund_reference_id = None
        self._refund_status = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if refund_date is not None:
            self.refund_date = refund_date
        if refund_id is not None:
            self.refund_id = refund_id
        if refund_reference_id is not None:
            self.refund_reference_id = refund_reference_id
        if refund_status is not None:
            self.refund_status = refund_status

    @property
    def amount(self):
        """Gets the amount of this OrderRefund.  # noqa: E501


        :return: The amount of this OrderRefund.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderRefund.


        :param amount: The amount of this OrderRefund.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def refund_date(self):
        """Gets the refund_date of this OrderRefund.  # noqa: E501

        The date and time that the refund was issued. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the refund has been issued. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The refund_date of this OrderRefund.  # noqa: E501
        :rtype: str
        """
        return self._refund_date

    @refund_date.setter
    def refund_date(self, refund_date):
        """Sets the refund_date of this OrderRefund.

        The date and time that the refund was issued. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the refund has been issued. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param refund_date: The refund_date of this OrderRefund.  # noqa: E501
        :type: str
        """

        self._refund_date = refund_date

    @property
    def refund_id(self):
        """Gets the refund_id of this OrderRefund.  # noqa: E501

        Unique identifier of a refund that was initiated for an order through the <b>issueRefund</b> method. If the <b>issueRefund</b> method was used to issue one or more refunds at the line item level, these refund identifiers are returned at the line item level instead (<b>lineItems.refunds.refundId</b> field).<br/><br/> A <b>refundId</b> value is returned in the response of the <b>issueRefund</b> method, and this same value will be returned in the <b>getOrders</b> and <b>getOrders</b> responses for pending and completed refunds. For other refunds, see the <b>refundReferenceId</b> field.  # noqa: E501

        :return: The refund_id of this OrderRefund.  # noqa: E501
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this OrderRefund.

        Unique identifier of a refund that was initiated for an order through the <b>issueRefund</b> method. If the <b>issueRefund</b> method was used to issue one or more refunds at the line item level, these refund identifiers are returned at the line item level instead (<b>lineItems.refunds.refundId</b> field).<br/><br/> A <b>refundId</b> value is returned in the response of the <b>issueRefund</b> method, and this same value will be returned in the <b>getOrders</b> and <b>getOrders</b> responses for pending and completed refunds. For other refunds, see the <b>refundReferenceId</b> field.  # noqa: E501

        :param refund_id: The refund_id of this OrderRefund.  # noqa: E501
        :type: str
        """

        self._refund_id = refund_id

    @property
    def refund_reference_id(self):
        """Gets the refund_reference_id of this OrderRefund.  # noqa: E501

        The eBay-generated unique identifier for the refund. This field is not returned until the refund has been issued.  # noqa: E501

        :return: The refund_reference_id of this OrderRefund.  # noqa: E501
        :rtype: str
        """
        return self._refund_reference_id

    @refund_reference_id.setter
    def refund_reference_id(self, refund_reference_id):
        """Sets the refund_reference_id of this OrderRefund.

        The eBay-generated unique identifier for the refund. This field is not returned until the refund has been issued.  # noqa: E501

        :param refund_reference_id: The refund_reference_id of this OrderRefund.  # noqa: E501
        :type: str
        """

        self._refund_reference_id = refund_reference_id

    @property
    def refund_status(self):
        """Gets the refund_status of this OrderRefund.  # noqa: E501

        This enumeration value indicates the current status of the refund to the buyer. This container is always returned for each refund. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:RefundStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The refund_status of this OrderRefund.  # noqa: E501
        :rtype: str
        """
        return self._refund_status

    @refund_status.setter
    def refund_status(self, refund_status):
        """Sets the refund_status of this OrderRefund.

        This enumeration value indicates the current status of the refund to the buyer. This container is always returned for each refund. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:RefundStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param refund_status: The refund_status of this OrderRefund.  # noqa: E501
        :type: str
        """

        self._refund_status = refund_status

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
        if issubclass(OrderRefund, dict):
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
        if not isinstance(other, OrderRefund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
