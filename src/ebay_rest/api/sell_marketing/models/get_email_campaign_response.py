# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.19.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetEmailCampaignResponse(object):
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
        'audiences': 'list[CampaignAudience]',
        'category_id': 'str',
        'category_type': 'str',
        'creation_date': 'str',
        'email_campaign_id': 'str',
        'email_campaign_status': 'str',
        'email_campaign_type': 'str',
        'item_ids': 'list[str]',
        'item_select_mode': 'str',
        'marketplace_id': 'str',
        'modification_date': 'str',
        'personalized_message': 'str',
        'price_range': 'PriceRange',
        'promotion_id': 'str',
        'promotion_select_mode': 'str',
        'schedule_date': 'str',
        'schedule_date_type': 'str',
        'sent_date': 'str',
        'sort': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'audiences': 'audiences',
        'category_id': 'categoryId',
        'category_type': 'categoryType',
        'creation_date': 'creationDate',
        'email_campaign_id': 'emailCampaignId',
        'email_campaign_status': 'emailCampaignStatus',
        'email_campaign_type': 'emailCampaignType',
        'item_ids': 'itemIds',
        'item_select_mode': 'itemSelectMode',
        'marketplace_id': 'marketplaceId',
        'modification_date': 'modificationDate',
        'personalized_message': 'personalizedMessage',
        'price_range': 'priceRange',
        'promotion_id': 'promotionId',
        'promotion_select_mode': 'promotionSelectMode',
        'schedule_date': 'scheduleDate',
        'schedule_date_type': 'scheduleDateType',
        'sent_date': 'sentDate',
        'sort': 'sort',
        'subject': 'subject'
    }

    def __init__(self, audiences=None, category_id=None, category_type=None, creation_date=None, email_campaign_id=None, email_campaign_status=None, email_campaign_type=None, item_ids=None, item_select_mode=None, marketplace_id=None, modification_date=None, personalized_message=None, price_range=None, promotion_id=None, promotion_select_mode=None, schedule_date=None, schedule_date_type=None, sent_date=None, sort=None, subject=None):  # noqa: E501
        """GetEmailCampaignResponse - a model defined in Swagger"""  # noqa: E501
        self._audiences = None
        self._category_id = None
        self._category_type = None
        self._creation_date = None
        self._email_campaign_id = None
        self._email_campaign_status = None
        self._email_campaign_type = None
        self._item_ids = None
        self._item_select_mode = None
        self._marketplace_id = None
        self._modification_date = None
        self._personalized_message = None
        self._price_range = None
        self._promotion_id = None
        self._promotion_select_mode = None
        self._schedule_date = None
        self._schedule_date_type = None
        self._sent_date = None
        self._sort = None
        self._subject = None
        self.discriminator = None
        if audiences is not None:
            self.audiences = audiences
        if category_id is not None:
            self.category_id = category_id
        if category_type is not None:
            self.category_type = category_type
        if creation_date is not None:
            self.creation_date = creation_date
        if email_campaign_id is not None:
            self.email_campaign_id = email_campaign_id
        if email_campaign_status is not None:
            self.email_campaign_status = email_campaign_status
        if email_campaign_type is not None:
            self.email_campaign_type = email_campaign_type
        if item_ids is not None:
            self.item_ids = item_ids
        if item_select_mode is not None:
            self.item_select_mode = item_select_mode
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if modification_date is not None:
            self.modification_date = modification_date
        if personalized_message is not None:
            self.personalized_message = personalized_message
        if price_range is not None:
            self.price_range = price_range
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_select_mode is not None:
            self.promotion_select_mode = promotion_select_mode
        if schedule_date is not None:
            self.schedule_date = schedule_date
        if schedule_date_type is not None:
            self.schedule_date_type = schedule_date_type
        if sent_date is not None:
            self.sent_date = sent_date
        if sort is not None:
            self.sort = sort
        if subject is not None:
            self.subject = subject

    @property
    def audiences(self):
        """Gets the audiences of this GetEmailCampaignResponse.  # noqa: E501

        An array of one or more audiences associated with the email campaign.  # noqa: E501

        :return: The audiences of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: list[CampaignAudience]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this GetEmailCampaignResponse.

        An array of one or more audiences associated with the email campaign.  # noqa: E501

        :param audiences: The audiences of this GetEmailCampaignResponse.  # noqa: E501
        :type: list[CampaignAudience]
        """

        self._audiences = audiences

    @property
    def category_id(self):
        """Gets the category_id of this GetEmailCampaignResponse.  # noqa: E501

        The unique identifier of an eBay category or an eBay store category. This field is returned if a seller has applied the email campaign to a specific category.<br><br>The <b>categoryType</b> value will indicate if the category ID is for an eBay category or an eBay store category.  # noqa: E501

        :return: The category_id of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this GetEmailCampaignResponse.

        The unique identifier of an eBay category or an eBay store category. This field is returned if a seller has applied the email campaign to a specific category.<br><br>The <b>categoryType</b> value will indicate if the category ID is for an eBay category or an eBay store category.  # noqa: E501

        :param category_id: The category_id of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def category_type(self):
        """Gets the category_type of this GetEmailCampaignResponse.  # noqa: E501

        The enumeration value returned here indicates if the <b>categoryId</b> value is the identifier of an eBay category or an eBay store category.<br><br>This field is returned if a seller has applied the email campaign to a specific category. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The category_type of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this GetEmailCampaignResponse.

        The enumeration value returned here indicates if the <b>categoryId</b> value is the identifier of an eBay category or an eBay store category.<br><br>This field is returned if a seller has applied the email campaign to a specific category. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param category_type: The category_type of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._category_type = category_type

    @property
    def creation_date(self):
        """Gets the creation_date of this GetEmailCampaignResponse.  # noqa: E501

        The date and time that the email campaign was created, given in UTC format.  # noqa: E501

        :return: The creation_date of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this GetEmailCampaignResponse.

        The date and time that the email campaign was created, given in UTC format.  # noqa: E501

        :param creation_date: The creation_date of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def email_campaign_id(self):
        """Gets the email_campaign_id of this GetEmailCampaignResponse.  # noqa: E501

        The unique identifier of the email campaign.  # noqa: E501

        :return: The email_campaign_id of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_campaign_id

    @email_campaign_id.setter
    def email_campaign_id(self, email_campaign_id):
        """Sets the email_campaign_id of this GetEmailCampaignResponse.

        The unique identifier of the email campaign.  # noqa: E501

        :param email_campaign_id: The email_campaign_id of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._email_campaign_id = email_campaign_id

    @property
    def email_campaign_status(self):
        """Gets the email_campaign_status of this GetEmailCampaignResponse.  # noqa: E501

        The email campaign status. See <a href=\"/api-docs/sell/marketing/types/api:EmailCampaignStatusEnum\">EmailCampaignStatusEnum</a> for a list of valid statuses. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:EmailCampaignStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The email_campaign_status of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_campaign_status

    @email_campaign_status.setter
    def email_campaign_status(self, email_campaign_status):
        """Sets the email_campaign_status of this GetEmailCampaignResponse.

        The email campaign status. See <a href=\"/api-docs/sell/marketing/types/api:EmailCampaignStatusEnum\">EmailCampaignStatusEnum</a> for a list of valid statuses. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:EmailCampaignStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param email_campaign_status: The email_campaign_status of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._email_campaign_status = email_campaign_status

    @property
    def email_campaign_type(self):
        """Gets the email_campaign_type of this GetEmailCampaignResponse.  # noqa: E501

        The email campaign type. See <a href=\"/api-docs/sell/marketing/types/api:CampaignTypeEnum\">CampaignTypeEnum</a> for valid email campaign types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CampaignTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The email_campaign_type of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_campaign_type

    @email_campaign_type.setter
    def email_campaign_type(self, email_campaign_type):
        """Sets the email_campaign_type of this GetEmailCampaignResponse.

        The email campaign type. See <a href=\"/api-docs/sell/marketing/types/api:CampaignTypeEnum\">CampaignTypeEnum</a> for valid email campaign types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:CampaignTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param email_campaign_type: The email_campaign_type of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._email_campaign_type = email_campaign_type

    @property
    def item_ids(self):
        """Gets the item_ids of this GetEmailCampaignResponse.  # noqa: E501

        The listing IDs of the items that were manually added to the email campaign.<br><br>Only listings added manually by the seller are returned. Returns a null array if no listings were added.  # noqa: E501

        :return: The item_ids of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this GetEmailCampaignResponse.

        The listing IDs of the items that were manually added to the email campaign.<br><br>Only listings added manually by the seller are returned. Returns a null array if no listings were added.  # noqa: E501

        :param item_ids: The item_ids of this GetEmailCampaignResponse.  # noqa: E501
        :type: list[str]
        """

        self._item_ids = item_ids

    @property
    def item_select_mode(self):
        """Gets the item_select_mode of this GetEmailCampaignResponse.  # noqa: E501

        The mode used to select the items listed in the email campaign. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The item_select_mode of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._item_select_mode

    @item_select_mode.setter
    def item_select_mode(self, item_select_mode):
        """Sets the item_select_mode of this GetEmailCampaignResponse.

        The mode used to select the items listed in the email campaign. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :param item_select_mode: The item_select_mode of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._item_select_mode = item_select_mode

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this GetEmailCampaignResponse.  # noqa: E501

        The eBay marketplace where the email campaign is active. See <a href=\"/api-docs/sell/marketing/types/ba:MarketplaceIdEnum\">MarketplaceIdEnum</a> for a list of marketplace IDs.  # noqa: E501

        :return: The marketplace_id of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this GetEmailCampaignResponse.

        The eBay marketplace where the email campaign is active. See <a href=\"/api-docs/sell/marketing/types/ba:MarketplaceIdEnum\">MarketplaceIdEnum</a> for a list of marketplace IDs.  # noqa: E501

        :param marketplace_id: The marketplace_id of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def modification_date(self):
        """Gets the modification_date of this GetEmailCampaignResponse.  # noqa: E501

        The date and time the email campaign was last modified, given in UTC format.  # noqa: E501

        :return: The modification_date of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this GetEmailCampaignResponse.

        The date and time the email campaign was last modified, given in UTC format.  # noqa: E501

        :param modification_date: The modification_date of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._modification_date = modification_date

    @property
    def personalized_message(self):
        """Gets the personalized_message of this GetEmailCampaignResponse.  # noqa: E501

        The body of the email campaign sent to the audience.  # noqa: E501

        :return: The personalized_message of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._personalized_message

    @personalized_message.setter
    def personalized_message(self, personalized_message):
        """Sets the personalized_message of this GetEmailCampaignResponse.

        The body of the email campaign sent to the audience.  # noqa: E501

        :param personalized_message: The personalized_message of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._personalized_message = personalized_message

    @property
    def price_range(self):
        """Gets the price_range of this GetEmailCampaignResponse.  # noqa: E501


        :return: The price_range of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: PriceRange
        """
        return self._price_range

    @price_range.setter
    def price_range(self, price_range):
        """Sets the price_range of this GetEmailCampaignResponse.


        :param price_range: The price_range of this GetEmailCampaignResponse.  # noqa: E501
        :type: PriceRange
        """

        self._price_range = price_range

    @property
    def promotion_id(self):
        """Gets the promotion_id of this GetEmailCampaignResponse.  # noqa: E501

        The ID of the promotion that was assigned to the email campaign.  # noqa: E501

        :return: The promotion_id of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this GetEmailCampaignResponse.

        The ID of the promotion that was assigned to the email campaign.  # noqa: E501

        :param promotion_id: The promotion_id of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def promotion_select_mode(self):
        """Gets the promotion_select_mode of this GetEmailCampaignResponse.  # noqa: E501

        Indicates whether the listings that the promotion was applied to were selected manually or automatically.<br><br>This field will only return if a promotion was applied. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:PromotionSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_select_mode of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._promotion_select_mode

    @promotion_select_mode.setter
    def promotion_select_mode(self, promotion_select_mode):
        """Sets the promotion_select_mode of this GetEmailCampaignResponse.

        Indicates whether the listings that the promotion was applied to were selected manually or automatically.<br><br>This field will only return if a promotion was applied. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:PromotionSelectModeEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_select_mode: The promotion_select_mode of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._promotion_select_mode = promotion_select_mode

    @property
    def schedule_date(self):
        """Gets the schedule_date of this GetEmailCampaignResponse.  # noqa: E501

        The date and time that the email campaign newsletter is scheduled to send, given in UTC format. This field is only returned if the seller set the start of the email campaign to a date in the future.  # noqa: E501

        :return: The schedule_date of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this GetEmailCampaignResponse.

        The date and time that the email campaign newsletter is scheduled to send, given in UTC format. This field is only returned if the seller set the start of the email campaign to a date in the future.  # noqa: E501

        :param schedule_date: The schedule_date of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._schedule_date = schedule_date

    @property
    def schedule_date_type(self):
        """Gets the schedule_date_type of this GetEmailCampaignResponse.  # noqa: E501

        The schedule type of the email campaign. See <a href=\"/api-docs/sell/marketing/types/api:ScheduleDateTypeEnum\">ScheduleDateTypeEnum</a>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ScheduleDateTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The schedule_date_type of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date_type

    @schedule_date_type.setter
    def schedule_date_type(self, schedule_date_type):
        """Sets the schedule_date_type of this GetEmailCampaignResponse.

        The schedule type of the email campaign. See <a href=\"/api-docs/sell/marketing/types/api:ScheduleDateTypeEnum\">ScheduleDateTypeEnum</a>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ScheduleDateTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param schedule_date_type: The schedule_date_type of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._schedule_date_type = schedule_date_type

    @property
    def sent_date(self):
        """Gets the sent_date of this GetEmailCampaignResponse.  # noqa: E501

        The date and time that the email campaign was sent, given in UTC format.  # noqa: E501

        :return: The sent_date of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._sent_date

    @sent_date.setter
    def sent_date(self, sent_date):
        """Sets the sent_date of this GetEmailCampaignResponse.

        The date and time that the email campaign was sent, given in UTC format.  # noqa: E501

        :param sent_date: The sent_date of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._sent_date = sent_date

    @property
    def sort(self):
        """Gets the sort of this GetEmailCampaignResponse.  # noqa: E501

        The sort rule is used to display the items in the email campaign. If no sort rule was selected, the default will be <code>NEWLY_LISTED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSortEnum'>eBay API documentation</a>  # noqa: E501

        :return: The sort of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this GetEmailCampaignResponse.

        The sort rule is used to display the items in the email campaign. If no sort rule was selected, the default will be <code>NEWLY_LISTED</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/api:ItemSortEnum'>eBay API documentation</a>  # noqa: E501

        :param sort: The sort of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def subject(self):
        """Gets the subject of this GetEmailCampaignResponse.  # noqa: E501

        The email campaign subject.  # noqa: E501

        :return: The subject of this GetEmailCampaignResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetEmailCampaignResponse.

        The email campaign subject.  # noqa: E501

        :param subject: The subject of this GetEmailCampaignResponse.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if issubclass(GetEmailCampaignResponse, dict):
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
        if not isinstance(other, GetEmailCampaignResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
