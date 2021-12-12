# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Campaign(object):
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
        'campaign_criterion': 'CampaignCriterion',
        'campaign_id': 'str',
        'campaign_name': 'str',
        'campaign_status': 'str',
        'end_date': 'str',
        'funding_strategy': 'FundingStrategy',
        'marketplace_id': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'campaign_criterion': 'campaignCriterion',
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'campaign_status': 'campaignStatus',
        'end_date': 'endDate',
        'funding_strategy': 'fundingStrategy',
        'marketplace_id': 'marketplaceId',
        'start_date': 'startDate'
    }

    def __init__(self, campaign_criterion=None, campaign_id=None, campaign_name=None, campaign_status=None, end_date=None, funding_strategy=None, marketplace_id=None, start_date=None):  # noqa: E501
        """Campaign - a model defined in Swagger"""  # noqa: E501
        self._campaign_criterion = None
        self._campaign_id = None
        self._campaign_name = None
        self._campaign_status = None
        self._end_date = None
        self._funding_strategy = None
        self._marketplace_id = None
        self._start_date = None
        self.discriminator = None
        if campaign_criterion is not None:
            self.campaign_criterion = campaign_criterion
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if campaign_status is not None:
            self.campaign_status = campaign_status
        if end_date is not None:
            self.end_date = end_date
        if funding_strategy is not None:
            self.funding_strategy = funding_strategy
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if start_date is not None:
            self.start_date = start_date

    @property
    def campaign_criterion(self):
        """Gets the campaign_criterion of this Campaign.  # noqa: E501


        :return: The campaign_criterion of this Campaign.  # noqa: E501
        :rtype: CampaignCriterion
        """
        return self._campaign_criterion

    @campaign_criterion.setter
    def campaign_criterion(self, campaign_criterion):
        """Sets the campaign_criterion of this Campaign.


        :param campaign_criterion: The campaign_criterion of this Campaign.  # noqa: E501
        :type: CampaignCriterion
        """

        self._campaign_criterion = campaign_criterion

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Campaign.  # noqa: E501

        A unique eBay-assigned ID for a campaign. This ID is generated when a campaign is created.  # noqa: E501

        :return: The campaign_id of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Campaign.

        A unique eBay-assigned ID for a campaign. This ID is generated when a campaign is created.  # noqa: E501

        :param campaign_id: The campaign_id of this Campaign.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this Campaign.  # noqa: E501

        A seller-defined name for the campaign. This value must be unique for the seller. <p>You can use any alphanumeric characters in the name, except the less than (&lt;) or greater than (&gt;) characters.</p><b>Max length: </b>80 characters  # noqa: E501

        :return: The campaign_name of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this Campaign.

        A seller-defined name for the campaign. This value must be unique for the seller. <p>You can use any alphanumeric characters in the name, except the less than (&lt;) or greater than (&gt;) characters.</p><b>Max length: </b>80 characters  # noqa: E501

        :param campaign_name: The campaign_name of this Campaign.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def campaign_status(self):
        """Gets the campaign_status of this Campaign.  # noqa: E501

        Indicates the status of the campaign, such as <code>RUNNING</code>, <code>PAUSED</code>, and <code>ENDED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:CampaignStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The campaign_status of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this Campaign.

        Indicates the status of the campaign, such as <code>RUNNING</code>, <code>PAUSED</code>, and <code>ENDED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:CampaignStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param campaign_status: The campaign_status of this Campaign.  # noqa: E501
        :type: str
        """

        self._campaign_status = campaign_status

    @property
    def end_date(self):
        """Gets the end_date of this Campaign.  # noqa: E501

        The date and time the campaign ends, in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). If this field is blank (code>null</code>), it indicates a campaign that has no end date. For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The end_date of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Campaign.

        The date and time the campaign ends, in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). If this field is blank (code>null</code>), it indicates a campaign that has no end date. For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param end_date: The end_date of this Campaign.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def funding_strategy(self):
        """Gets the funding_strategy of this Campaign.  # noqa: E501


        :return: The funding_strategy of this Campaign.  # noqa: E501
        :rtype: FundingStrategy
        """
        return self._funding_strategy

    @funding_strategy.setter
    def funding_strategy(self, funding_strategy):
        """Sets the funding_strategy of this Campaign.


        :param funding_strategy: The funding_strategy of this Campaign.  # noqa: E501
        :type: FundingStrategy
        """

        self._funding_strategy = funding_strategy

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this Campaign.  # noqa: E501

        The ID of the eBay marketplace where the campaign is hosted. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this Campaign.

        The ID of the eBay marketplace where the campaign is hosted. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this Campaign.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def start_date(self):
        """Gets the start_date of this Campaign.  # noqa: E501

        The date and time the campaign starts, in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  <p>On the date specified, the service derives the keywords for each listing in the campaign, creates an ad for each listing, and associates each new ad with the campaign. The campaign starts after this process is completed. The amount of time it takes the service to start the campaign depends on the number of listings in the campaign. Call <b>getCampaign</b> to check the status of the campaign.</p>  # noqa: E501

        :return: The start_date of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Campaign.

        The date and time the campaign starts, in UTC format (<code>yyyy-MM-ddThh:mm:ssZ</code>). For display purposes, convert this time into the local time of the seller.  <p>On the date specified, the service derives the keywords for each listing in the campaign, creates an ad for each listing, and associates each new ad with the campaign. The campaign starts after this process is completed. The amount of time it takes the service to start the campaign depends on the number of listings in the campaign. Call <b>getCampaign</b> to check the status of the campaign.</p>  # noqa: E501

        :param start_date: The start_date of this Campaign.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(Campaign, dict):
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
        if not isinstance(other, Campaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
