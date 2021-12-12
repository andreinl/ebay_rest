# coding: utf-8

"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemPriority(object):
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
        'item_id': 'str',
        'priority_listing_payload': 'str',
        'change_metadata': 'str'
    }

    attribute_map = {
        'item_id': 'itemId',
        'priority_listing_payload': 'priorityListingPayload',
        'change_metadata': 'changeMetadata'
    }

    def __init__(self, item_id=None, priority_listing_payload=None, change_metadata=None):  # noqa: E501
        """ItemPriority - a model defined in Swagger"""  # noqa: E501
        self._item_id = None
        self._priority_listing_payload = None
        self._change_metadata = None
        self.discriminator = None
        if item_id is not None:
            self.item_id = item_id
        if priority_listing_payload is not None:
            self.priority_listing_payload = priority_listing_payload
        if change_metadata is not None:
            self.change_metadata = change_metadata

    @property
    def item_id(self):
        """Gets the item_id of this ItemPriority.  # noqa: E501

        The unique identifier of an item in eBay RESTful format. An example would be <code>v1|1********2|4********2</code>.  # noqa: E501

        :return: The item_id of this ItemPriority.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ItemPriority.

        The unique identifier of an item in eBay RESTful format. An example would be <code>v1|1********2|4********2</code>.  # noqa: E501

        :param item_id: The item_id of this ItemPriority.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def priority_listing_payload(self):
        """Gets the priority_listing_payload of this ItemPriority.  # noqa: E501

        EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items. <br /><br /><b>Example:</b><code>_trkparms=ispr%3D1&amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3D</code><br/><br />See <a  href=\"https://developer.ebay.com/api-docs/buy/static/ref-epn-link.html\">Creating an EPN Tracking Link</a> for information on EPN tracking links.  # noqa: E501

        :return: The priority_listing_payload of this ItemPriority.  # noqa: E501
        :rtype: str
        """
        return self._priority_listing_payload

    @priority_listing_payload.setter
    def priority_listing_payload(self, priority_listing_payload):
        """Sets the priority_listing_payload of this ItemPriority.

        EPN (eBay Partner Network) publishers append this value to their affiliate tracking URL when using an EPN tracking link to track changes that occur to Priority Listing items. <br /><br /><b>Example:</b><code>_trkparms=ispr%3D1&amdata=enc%3AAQAFAAAAkB1DmsmXf%2BqZ%2BCEMGdebW6oR75GCMdBmc4MCQ%2FCEPqgKHbT0jdWhPwfY5LdUs6HTaP0eBlwKE7Smy2eDslewF7l3xjwWxjqwzNAnsYgxn2PiGkTKbiQSQytFUiymdtANpk1qOnBOoMGMK%2BWsji7jYlvySSs9o9s24TxD6RqWZpNrltzOU7mfnv3H40SZ3YESzg%3D%3D</code><br/><br />See <a  href=\"https://developer.ebay.com/api-docs/buy/static/ref-epn-link.html\">Creating an EPN Tracking Link</a> for information on EPN tracking links.  # noqa: E501

        :param priority_listing_payload: The priority_listing_payload of this ItemPriority.  # noqa: E501
        :type: str
        """

        self._priority_listing_payload = priority_listing_payload

    @property
    def change_metadata(self):
        """Gets the change_metadata of this ItemPriority.  # noqa: E501

        Status change indicator of the listing.<br /><br /><b>Values:</b> <ul><li><code>ADDED_TO_CAMPAIGN</code></li><li><code>REMOVED_FROM_CAMPAIGN</code></li><li><code>TRACKING_PAYLOAD_REFRESHED</code></li></ul><span class=\"tablenote\"><b>Note:</b> When a listing is removed from the campaign, <b>PriorityListingPayload</b> will be empty.</span><br /><br />When multiple status changes are returned for a listing, the <b>changeMetadata</b> value will be a pipe-separated string (e.g., <code>ADDED_TO_CAMPAIGN|TRACKING_PAYLOAD_REFRESHED</code>).<br ><br >To use the returned value, you will need to separate the string by pipe (|).  # noqa: E501

        :return: The change_metadata of this ItemPriority.  # noqa: E501
        :rtype: str
        """
        return self._change_metadata

    @change_metadata.setter
    def change_metadata(self, change_metadata):
        """Sets the change_metadata of this ItemPriority.

        Status change indicator of the listing.<br /><br /><b>Values:</b> <ul><li><code>ADDED_TO_CAMPAIGN</code></li><li><code>REMOVED_FROM_CAMPAIGN</code></li><li><code>TRACKING_PAYLOAD_REFRESHED</code></li></ul><span class=\"tablenote\"><b>Note:</b> When a listing is removed from the campaign, <b>PriorityListingPayload</b> will be empty.</span><br /><br />When multiple status changes are returned for a listing, the <b>changeMetadata</b> value will be a pipe-separated string (e.g., <code>ADDED_TO_CAMPAIGN|TRACKING_PAYLOAD_REFRESHED</code>).<br ><br >To use the returned value, you will need to separate the string by pipe (|).  # noqa: E501

        :param change_metadata: The change_metadata of this ItemPriority.  # noqa: E501
        :type: str
        """

        self._change_metadata = change_metadata

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
        if issubclass(ItemPriority, dict):
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
        if not isinstance(other, ItemPriority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
