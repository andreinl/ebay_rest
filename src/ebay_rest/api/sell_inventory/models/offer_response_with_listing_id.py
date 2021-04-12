# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OfferResponseWithListingId(object):
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
        'errors': 'list[Error]',
        'listing_id': 'str',
        'offer_id': 'str',
        'status_code': 'int',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'errors': 'errors',
        'listing_id': 'listingId',
        'offer_id': 'offerId',
        'status_code': 'statusCode',
        'warnings': 'warnings'
    }

    def __init__(self, errors=None, listing_id=None, offer_id=None, status_code=None, warnings=None):  # noqa: E501
        """OfferResponseWithListingId - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._listing_id = None
        self._offer_id = None
        self._status_code = None
        self._warnings = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if listing_id is not None:
            self.listing_id = listing_id
        if offer_id is not None:
            self.offer_id = offer_id
        if status_code is not None:
            self.status_code = status_code
        if warnings is not None:
            self.warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this OfferResponseWithListingId.  # noqa: E501

        This container will be returned if there were one or more errors associated with publishing the offer.  # noqa: E501

        :return: The errors of this OfferResponseWithListingId.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this OfferResponseWithListingId.

        This container will be returned if there were one or more errors associated with publishing the offer.  # noqa: E501

        :param errors: The errors of this OfferResponseWithListingId.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def listing_id(self):
        """Gets the listing_id of this OfferResponseWithListingId.  # noqa: E501

        The unique identifier of the newly-created eBay listing. This field is only returned if the seller successfully published the offer and created the new eBay listing.  # noqa: E501

        :return: The listing_id of this OfferResponseWithListingId.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this OfferResponseWithListingId.

        The unique identifier of the newly-created eBay listing. This field is only returned if the seller successfully published the offer and created the new eBay listing.  # noqa: E501

        :param listing_id: The listing_id of this OfferResponseWithListingId.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

    @property
    def offer_id(self):
        """Gets the offer_id of this OfferResponseWithListingId.  # noqa: E501

        The unique identifier of the offer that the seller published (or attempted to publish).  # noqa: E501

        :return: The offer_id of this OfferResponseWithListingId.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this OfferResponseWithListingId.

        The unique identifier of the offer that the seller published (or attempted to publish).  # noqa: E501

        :param offer_id: The offer_id of this OfferResponseWithListingId.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def status_code(self):
        """Gets the status_code of this OfferResponseWithListingId.  # noqa: E501

        The HTTP status code returned in this field indicates the success or failure of publishing the offer specified in the offerId field. See the HTTP status codes table to see which each status code indicates.  # noqa: E501

        :return: The status_code of this OfferResponseWithListingId.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this OfferResponseWithListingId.

        The HTTP status code returned in this field indicates the success or failure of publishing the offer specified in the offerId field. See the HTTP status codes table to see which each status code indicates.  # noqa: E501

        :param status_code: The status_code of this OfferResponseWithListingId.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def warnings(self):
        """Gets the warnings of this OfferResponseWithListingId.  # noqa: E501

        This container will be returned if there were one or more warnings associated with publishing the offer.  # noqa: E501

        :return: The warnings of this OfferResponseWithListingId.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this OfferResponseWithListingId.

        This container will be returned if there were one or more warnings associated with publishing the offer.  # noqa: E501

        :param warnings: The warnings of this OfferResponseWithListingId.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(OfferResponseWithListingId, dict):
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
        if not isinstance(other, OfferResponseWithListingId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
