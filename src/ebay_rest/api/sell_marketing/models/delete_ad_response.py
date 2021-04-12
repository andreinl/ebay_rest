# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeleteAdResponse(object):
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
        'ad_id': 'str',
        'errors': 'list[Error]',
        'listing_id': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'ad_id': 'adId',
        'errors': 'errors',
        'listing_id': 'listingId',
        'status_code': 'statusCode'
    }

    def __init__(self, ad_id=None, errors=None, listing_id=None, status_code=None):  # noqa: E501
        """DeleteAdResponse - a model defined in Swagger"""  # noqa: E501
        self._ad_id = None
        self._errors = None
        self._listing_id = None
        self._status_code = None
        self.discriminator = None
        if ad_id is not None:
            self.ad_id = ad_id
        if errors is not None:
            self.errors = errors
        if listing_id is not None:
            self.listing_id = listing_id
        if status_code is not None:
            self.status_code = status_code

    @property
    def ad_id(self):
        """Gets the ad_id of this DeleteAdResponse.  # noqa: E501

        The ID of the ad that was deleted.  # noqa: E501

        :return: The ad_id of this DeleteAdResponse.  # noqa: E501
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this DeleteAdResponse.

        The ID of the ad that was deleted.  # noqa: E501

        :param ad_id: The ad_id of this DeleteAdResponse.  # noqa: E501
        :type: str
        """

        self._ad_id = ad_id

    @property
    def errors(self):
        """Gets the errors of this DeleteAdResponse.  # noqa: E501

        An array of the errors or warnings associated with the request.  # noqa: E501

        :return: The errors of this DeleteAdResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DeleteAdResponse.

        An array of the errors or warnings associated with the request.  # noqa: E501

        :param errors: The errors of this DeleteAdResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def listing_id(self):
        """Gets the listing_id of this DeleteAdResponse.  # noqa: E501

        A unique eBay-assigned ID for a listing that is generated when the listing is created. Note: This field accepts both listing IDs, as generated by the Inventory API, and an item IDs, as used in the eBay Traditional API set (e.g., the Trading and Finding APIs).  # noqa: E501

        :return: The listing_id of this DeleteAdResponse.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this DeleteAdResponse.

        A unique eBay-assigned ID for a listing that is generated when the listing is created. Note: This field accepts both listing IDs, as generated by the Inventory API, and an item IDs, as used in the eBay Traditional API set (e.g., the Trading and Finding APIs).  # noqa: E501

        :param listing_id: The listing_id of this DeleteAdResponse.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

    @property
    def status_code(self):
        """Gets the status_code of this DeleteAdResponse.  # noqa: E501

        An HTTP status code that indicates the response-status of the request. Check this code to see if the ad was successfully deleted.  # noqa: E501

        :return: The status_code of this DeleteAdResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this DeleteAdResponse.

        An HTTP status code that indicates the response-status of the request. Check this code to see if the ad was successfully deleted.  # noqa: E501

        :param status_code: The status_code of this DeleteAdResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(DeleteAdResponse, dict):
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
        if not isinstance(other, DeleteAdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
