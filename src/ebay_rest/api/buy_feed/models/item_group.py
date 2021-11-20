# coding: utf-8

"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.29.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemGroup(object):
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
        'item_group_id': 'str',
        'item_group_type': 'str',
        'title': 'str',
        'varies_by_localized_aspects': 'str',
        'image_url': 'str',
        'additional_image_urls': 'str',
        'image_altering_prohibited': 'bool'
    }

    attribute_map = {
        'item_group_id': 'itemGroupId',
        'item_group_type': 'itemGroupType',
        'title': 'title',
        'varies_by_localized_aspects': 'variesByLocalizedAspects',
        'image_url': 'imageUrl',
        'additional_image_urls': 'additionalImageUrls',
        'image_altering_prohibited': 'imageAlteringProhibited'
    }

    def __init__(self, item_group_id=None, item_group_type=None, title=None, varies_by_localized_aspects=None, image_url=None, additional_image_urls=None, image_altering_prohibited=None):  # noqa: E501
        """ItemGroup - a model defined in Swagger"""  # noqa: E501
        self._item_group_id = None
        self._item_group_type = None
        self._title = None
        self._varies_by_localized_aspects = None
        self._image_url = None
        self._additional_image_urls = None
        self._image_altering_prohibited = None
        self.discriminator = None
        if item_group_id is not None:
            self.item_group_id = item_group_id
        if item_group_type is not None:
            self.item_group_type = item_group_type
        if title is not None:
            self.title = title
        if varies_by_localized_aspects is not None:
            self.varies_by_localized_aspects = varies_by_localized_aspects
        if image_url is not None:
            self.image_url = image_url
        if additional_image_urls is not None:
            self.additional_image_urls = additional_image_urls
        if image_altering_prohibited is not None:
            self.image_altering_prohibited = image_altering_prohibited

    @property
    def item_group_id(self):
        """Gets the item_group_id of this ItemGroup.  # noqa: E501

        The unique identifier for the item group. This ID is returned in the <b> primaryItemGroupId</b> column of the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed\">Item Feed</a> file.  # noqa: E501

        :return: The item_group_id of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._item_group_id

    @item_group_id.setter
    def item_group_id(self, item_group_id):
        """Sets the item_group_id of this ItemGroup.

        The unique identifier for the item group. This ID is returned in the <b> primaryItemGroupId</b> column of the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed\">Item Feed</a> file.  # noqa: E501

        :param item_group_id: The item_group_id of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._item_group_id = item_group_id

    @property
    def item_group_type(self):
        """Gets the item_group_type of this ItemGroup.  # noqa: E501

        The item group type. For example:<code> SELLER_DEFINED_VARIATIONS</code>, indicates that the item group was created by the seller. <br /><br />Code so that your app gracefully handles any future changes to this list.  # noqa: E501

        :return: The item_group_type of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._item_group_type

    @item_group_type.setter
    def item_group_type(self, item_group_type):
        """Sets the item_group_type of this ItemGroup.

        The item group type. For example:<code> SELLER_DEFINED_VARIATIONS</code>, indicates that the item group was created by the seller. <br /><br />Code so that your app gracefully handles any future changes to this list.  # noqa: E501

        :param item_group_type: The item_group_type of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._item_group_type = item_group_type

    @property
    def title(self):
        """Gets the title of this ItemGroup.  # noqa: E501

        The seller created title of the item group. This text is an escaped string when special characters are present, using the following rules:</p>   <ul>     <li>Double quotes (&#34;) and backslashes (&#92;) in the Title are escaped with a backslash (&#92;) character</li>      <li>If there are any tabs (&#92;t), double quotes (&#34;), or backslashes (&#92;) in the Title, the entire Title will be wrapped in double quotes.</li>   </ul>   <p><b>For example</b></p>   <p>Before:</p>   <p><code>Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W<b>&#92;</b>Tracking</code>   </p>   <p><code>Marvel Legends HULK 8<b>&#34;</b> Figure Avengers Age of Ultron Studios 6<b>&#34;</b> Series</code>   </p>   <p>After:</p>   <p><code>&#34;Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W<b>&#92;&#92;</b> Tracking&#34;</code>   </p>   <p><code>&#34;Marvel Legends HULK 8<b>&#92;&#34;</b> Figure Avengers Age of Ultron Studios 6<b>&#92;&#34;</b> Series<b>&#34;</b> </code>   </p>  # noqa: E501

        :return: The title of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ItemGroup.

        The seller created title of the item group. This text is an escaped string when special characters are present, using the following rules:</p>   <ul>     <li>Double quotes (&#34;) and backslashes (&#92;) in the Title are escaped with a backslash (&#92;) character</li>      <li>If there are any tabs (&#92;t), double quotes (&#34;), or backslashes (&#92;) in the Title, the entire Title will be wrapped in double quotes.</li>   </ul>   <p><b>For example</b></p>   <p>Before:</p>   <p><code>Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W<b>&#92;</b>Tracking</code>   </p>   <p><code>Marvel Legends HULK 8<b>&#34;</b> Figure Avengers Age of Ultron Studios 6<b>&#34;</b> Series</code>   </p>   <p>After:</p>   <p><code>&#34;Misty Rainforest Modern Masters 2017 MTG Magic Fetch Land Free Ship W<b>&#92;&#92;</b> Tracking&#34;</code>   </p>   <p><code>&#34;Marvel Legends HULK 8<b>&#92;&#34;</b> Figure Avengers Age of Ultron Studios 6<b>&#92;&#34;</b> Series<b>&#34;</b> </code>   </p>  # noqa: E501

        :param title: The title of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def varies_by_localized_aspects(self):
        """Gets the varies_by_localized_aspects of this ItemGroup.  # noqa: E501

        A pipe separated (<code>|</code>) list of the aspect (variation) names for this item group. The aspect name is BASE64 encoded. <b>Note: </b> This column can contain multiple values.  <p>&nbsp;&nbsp;<b> Encoded Format:</b> <br />&nbsp;&nbsp;&nbsp;<code><em>aspectName</em>|<em>aspectName</em></code> </p>   <p>&nbsp;&nbsp;<b> Encoded Example</b> (The delimiters are <b style=\"font-family: 'Arial Black';\">emphasized</b>): <br />&nbsp;&nbsp;&nbsp;<code>Q29sb3I=<b style=\"font-family: 'Arial Black';\">|</b>U2l6ZQ==</code> </p>      <p>&nbsp;&nbsp;<b> Decoded: </b> <br />&nbsp;&nbsp;&nbsp;Color|Size </p>  # noqa: E501

        :return: The varies_by_localized_aspects of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._varies_by_localized_aspects

    @varies_by_localized_aspects.setter
    def varies_by_localized_aspects(self, varies_by_localized_aspects):
        """Sets the varies_by_localized_aspects of this ItemGroup.

        A pipe separated (<code>|</code>) list of the aspect (variation) names for this item group. The aspect name is BASE64 encoded. <b>Note: </b> This column can contain multiple values.  <p>&nbsp;&nbsp;<b> Encoded Format:</b> <br />&nbsp;&nbsp;&nbsp;<code><em>aspectName</em>|<em>aspectName</em></code> </p>   <p>&nbsp;&nbsp;<b> Encoded Example</b> (The delimiters are <b style=\"font-family: 'Arial Black';\">emphasized</b>): <br />&nbsp;&nbsp;&nbsp;<code>Q29sb3I=<b style=\"font-family: 'Arial Black';\">|</b>U2l6ZQ==</code> </p>      <p>&nbsp;&nbsp;<b> Decoded: </b> <br />&nbsp;&nbsp;&nbsp;Color|Size </p>  # noqa: E501

        :param varies_by_localized_aspects: The varies_by_localized_aspects of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._varies_by_localized_aspects = varies_by_localized_aspects

    @property
    def image_url(self):
        """Gets the image_url of this ItemGroup.  # noqa: E501

        The URL to the primary image of the item. The other images of the item group are returned in the <b> additionalImageUrls</b> column.  # noqa: E501

        :return: The image_url of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ItemGroup.

        The URL to the primary image of the item. The other images of the item group are returned in the <b> additionalImageUrls</b> column.  # noqa: E501

        :param image_url: The image_url of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def additional_image_urls(self):
        """Gets the additional_image_urls of this ItemGroup.  # noqa: E501

        A pipe separated (<code>|</code>) list of URLs for the additional images for the item group. These images are in addition to the primary image, which is returned in the <b>imageUrl</b> column. <b>Note: </b> This column can contain multiple values.  # noqa: E501

        :return: The additional_image_urls of this ItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._additional_image_urls

    @additional_image_urls.setter
    def additional_image_urls(self, additional_image_urls):
        """Sets the additional_image_urls of this ItemGroup.

        A pipe separated (<code>|</code>) list of URLs for the additional images for the item group. These images are in addition to the primary image, which is returned in the <b>imageUrl</b> column. <b>Note: </b> This column can contain multiple values.  # noqa: E501

        :param additional_image_urls: The additional_image_urls of this ItemGroup.  # noqa: E501
        :type: str
        """

        self._additional_image_urls = additional_image_urls

    @property
    def image_altering_prohibited(self):
        """Gets the image_altering_prohibited of this ItemGroup.  # noqa: E501

        A boolean that indicates whether the images can be altered. If the value is <code>true</code>, you cannot modify the image. <p><span class=\"tablenote\"><b>Note: </b> Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only. </span></p>  # noqa: E501

        :return: The image_altering_prohibited of this ItemGroup.  # noqa: E501
        :rtype: bool
        """
        return self._image_altering_prohibited

    @image_altering_prohibited.setter
    def image_altering_prohibited(self, image_altering_prohibited):
        """Sets the image_altering_prohibited of this ItemGroup.

        A boolean that indicates whether the images can be altered. If the value is <code>true</code>, you cannot modify the image. <p><span class=\"tablenote\"><b>Note: </b> Due to image licensing agreements and other legal concerns, modification (including resizing) of some images is strictly prohibited. These images are for display as-is only. </span></p>  # noqa: E501

        :param image_altering_prohibited: The image_altering_prohibited of this ItemGroup.  # noqa: E501
        :type: bool
        """

        self._image_altering_prohibited = image_altering_prohibited

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
        if issubclass(ItemGroup, dict):
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
        if not isinstance(other, ItemGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
