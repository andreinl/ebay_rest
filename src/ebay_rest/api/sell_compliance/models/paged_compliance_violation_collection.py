# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PagedComplianceViolationCollection(object):
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
        'offset': 'int',
        'href': 'str',
        'total': 'int',
        'next': 'str',
        'prev': 'str',
        'limit': 'int',
        'listing_violations': 'list[ComplianceViolation]'
    }

    attribute_map = {
        'offset': 'offset',
        'href': 'href',
        'total': 'total',
        'next': 'next',
        'prev': 'prev',
        'limit': 'limit',
        'listing_violations': 'listingViolations'
    }

    def __init__(self, offset=None, href=None, total=None, next=None, prev=None, limit=None, listing_violations=None):  # noqa: E501
        """PagedComplianceViolationCollection - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._href = None
        self._total = None
        self._next = None
        self._prev = None
        self._limit = None
        self._listing_violations = None
        self.discriminator = None
        if offset is not None:
            self.offset = offset
        if href is not None:
            self.href = href
        if total is not None:
            self.total = total
        if next is not None:
            self.next = next
        if prev is not None:
            self.prev = prev
        if limit is not None:
            self.limit = limit
        if listing_violations is not None:
            self.listing_violations = listing_violations

    @property
    def offset(self):
        """Gets the offset of this PagedComplianceViolationCollection.  # noqa: E501

        This integer value shows the offset of the current page of results. The offset value controls the first listing violation in the result set that will be displayed at the top of the response. The offset and limit query parameters are used to control the pagination of the output. For example, if offset is set to 10 and limit is set to 10, the call retrieves listing violations 11 thru 20 from the resulting collection of violations. Note: This feature employs a zero-based index, where the first item in the list has an offset of 0. Default: 0 {zero)  # noqa: E501

        :return: The offset of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PagedComplianceViolationCollection.

        This integer value shows the offset of the current page of results. The offset value controls the first listing violation in the result set that will be displayed at the top of the response. The offset and limit query parameters are used to control the pagination of the output. For example, if offset is set to 10 and limit is set to 10, the call retrieves listing violations 11 thru 20 from the resulting collection of violations. Note: This feature employs a zero-based index, where the first item in the list has an offset of 0. Default: 0 {zero)  # noqa: E501

        :param offset: The offset of this PagedComplianceViolationCollection.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def href(self):
        """Gets the href of this PagedComplianceViolationCollection.  # noqa: E501

        The URI of the getListingViolations call request that produced the current page of the result set.  # noqa: E501

        :return: The href of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PagedComplianceViolationCollection.

        The URI of the getListingViolations call request that produced the current page of the result set.  # noqa: E501

        :param href: The href of this PagedComplianceViolationCollection.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def total(self):
        """Gets the total of this PagedComplianceViolationCollection.  # noqa: E501

        The total number of listing violations in the result set. If this value is higher than the limit value, there are multiple pages in the result set to view.  # noqa: E501

        :return: The total of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PagedComplianceViolationCollection.

        The total number of listing violations in the result set. If this value is higher than the limit value, there are multiple pages in the result set to view.  # noqa: E501

        :param total: The total of this PagedComplianceViolationCollection.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def next(self):
        """Gets the next of this PagedComplianceViolationCollection.  # noqa: E501

        The getListingViolations call URI to use to view the next page of the result set. For example, the following URI returns listing violations 21 thru 30 from the collection of policy violations: path/listing_violation?limit=10&amp;offset=20 This field is only returned if an additional page of listing violations exists.  # noqa: E501

        :return: The next of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PagedComplianceViolationCollection.

        The getListingViolations call URI to use to view the next page of the result set. For example, the following URI returns listing violations 21 thru 30 from the collection of policy violations: path/listing_violation?limit=10&amp;offset=20 This field is only returned if an additional page of listing violations exists.  # noqa: E501

        :param next: The next of this PagedComplianceViolationCollection.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def prev(self):
        """Gets the prev of this PagedComplianceViolationCollection.  # noqa: E501

        The getListingViolations call URI to use to view the previous page of the result set. For example, the following URI returns listing violations 1 thru 10 from the collection of policy violations: path/listing_violation?limit=10&amp;offset=0 This field is only returned if an previous page of listing violations exists.  # noqa: E501

        :return: The prev of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this PagedComplianceViolationCollection.

        The getListingViolations call URI to use to view the previous page of the result set. For example, the following URI returns listing violations 1 thru 10 from the collection of policy violations: path/listing_violation?limit=10&amp;offset=0 This field is only returned if an previous page of listing violations exists.  # noqa: E501

        :param prev: The prev of this PagedComplianceViolationCollection.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def limit(self):
        """Gets the limit of this PagedComplianceViolationCollection.  # noqa: E501

        The maximum number of listing violations returned per page of the result set. The limit and offset query parameters are used to control the pagination of the output. Note: If this is the last or only page in the result set, it may contain fewer listing violations than the limit value. To determine the number of pages in the result set, divide this value into the value of total and round up to the next integer. Default: 50 Max: 200  # noqa: E501

        :return: The limit of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PagedComplianceViolationCollection.

        The maximum number of listing violations returned per page of the result set. The limit and offset query parameters are used to control the pagination of the output. Note: If this is the last or only page in the result set, it may contain fewer listing violations than the limit value. To determine the number of pages in the result set, divide this value into the value of total and round up to the next integer. Default: 50 Max: 200  # noqa: E501

        :param limit: The limit of this PagedComplianceViolationCollection.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def listing_violations(self):
        """Gets the listing_violations of this PagedComplianceViolationCollection.  # noqa: E501

        An array of listing violations that match the criteria in the call request, including pagination control {if set). As long as there is at least one listing violation that matches the input criteria, this container will be returned. If no listing violations are found for the seller, an HTTP status code of 204 No Content is returned, and there is no response body.  # noqa: E501

        :return: The listing_violations of this PagedComplianceViolationCollection.  # noqa: E501
        :rtype: list[ComplianceViolation]
        """
        return self._listing_violations

    @listing_violations.setter
    def listing_violations(self, listing_violations):
        """Sets the listing_violations of this PagedComplianceViolationCollection.

        An array of listing violations that match the criteria in the call request, including pagination control {if set). As long as there is at least one listing violation that matches the input criteria, this container will be returned. If no listing violations are found for the seller, an HTTP status code of 204 No Content is returned, and there is no response body.  # noqa: E501

        :param listing_violations: The listing_violations of this PagedComplianceViolationCollection.  # noqa: E501
        :type: list[ComplianceViolation]
        """

        self._listing_violations = listing_violations

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
        if issubclass(PagedComplianceViolationCollection, dict):
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
        if not isinstance(other, PagedComplianceViolationCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
