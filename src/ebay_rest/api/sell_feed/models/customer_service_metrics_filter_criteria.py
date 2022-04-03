# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomerServiceMetricsFilterCriteria(object):
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
        'customer_service_metric_type': 'str',
        'evaluation_marketplace_id': 'str',
        'listing_categories': 'list[str]',
        'shipping_regions': 'list[str]'
    }

    attribute_map = {
        'customer_service_metric_type': 'customerServiceMetricType',
        'evaluation_marketplace_id': 'evaluationMarketplaceId',
        'listing_categories': 'listingCategories',
        'shipping_regions': 'shippingRegions'
    }

    def __init__(self, customer_service_metric_type=None, evaluation_marketplace_id=None, listing_categories=None, shipping_regions=None):  # noqa: E501
        """CustomerServiceMetricsFilterCriteria - a model defined in Swagger"""  # noqa: E501
        self._customer_service_metric_type = None
        self._evaluation_marketplace_id = None
        self._listing_categories = None
        self._shipping_regions = None
        self.discriminator = None
        if customer_service_metric_type is not None:
            self.customer_service_metric_type = customer_service_metric_type
        if evaluation_marketplace_id is not None:
            self.evaluation_marketplace_id = evaluation_marketplace_id
        if listing_categories is not None:
            self.listing_categories = listing_categories
        if shipping_regions is not None:
            self.shipping_regions = shipping_regions

    @property
    def customer_service_metric_type(self):
        """Gets the customer_service_metric_type of this CustomerServiceMetricsFilterCriteria.  # noqa: E501

        An enumeration value that specifies the customer service metric that eBay tracks to measure seller performance. See <strong>CustomerServiceMetricTypeEnum</strong> for values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:CustomerServiceMetricTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The customer_service_metric_type of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :rtype: str
        """
        return self._customer_service_metric_type

    @customer_service_metric_type.setter
    def customer_service_metric_type(self, customer_service_metric_type):
        """Sets the customer_service_metric_type of this CustomerServiceMetricsFilterCriteria.

        An enumeration value that specifies the customer service metric that eBay tracks to measure seller performance. See <strong>CustomerServiceMetricTypeEnum</strong> for values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/api:CustomerServiceMetricTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param customer_service_metric_type: The customer_service_metric_type of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :type: str
        """

        self._customer_service_metric_type = customer_service_metric_type

    @property
    def evaluation_marketplace_id(self):
        """Gets the evaluation_marketplace_id of this CustomerServiceMetricsFilterCriteria.  # noqa: E501

        An enumeration value that specifies the eBay marketplace where the evaluation occurs. See <strong>MarketplaceIdEnum</strong> for values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/bas:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The evaluation_marketplace_id of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_marketplace_id

    @evaluation_marketplace_id.setter
    def evaluation_marketplace_id(self, evaluation_marketplace_id):
        """Sets the evaluation_marketplace_id of this CustomerServiceMetricsFilterCriteria.

        An enumeration value that specifies the eBay marketplace where the evaluation occurs. See <strong>MarketplaceIdEnum</strong> for values. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/feed/types/bas:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param evaluation_marketplace_id: The evaluation_marketplace_id of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :type: str
        """

        self._evaluation_marketplace_id = evaluation_marketplace_id

    @property
    def listing_categories(self):
        """Gets the listing_categories of this CustomerServiceMetricsFilterCriteria.  # noqa: E501

        A list of listing category IDs on which the service metric is measured. A seller can use one or more L1 (top-level) eBay categories to get metrics specific to those L1 categories. The Category IDs for each L1 category are required. Category ID values for L1 categories can be retrieved using the Taxonomy API.<p> <span class=\"tablenote\"><strong>Note: </strong>Pass this attribute to narrow down your filter results for the <code>ITEM_NOT_AS_DESCRIBED</code> customerServiceMetricType.</span></p> <p>Supported categories include:</p><p><code>primary(L1) category Id</code></p>  # noqa: E501

        :return: The listing_categories of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._listing_categories

    @listing_categories.setter
    def listing_categories(self, listing_categories):
        """Sets the listing_categories of this CustomerServiceMetricsFilterCriteria.

        A list of listing category IDs on which the service metric is measured. A seller can use one or more L1 (top-level) eBay categories to get metrics specific to those L1 categories. The Category IDs for each L1 category are required. Category ID values for L1 categories can be retrieved using the Taxonomy API.<p> <span class=\"tablenote\"><strong>Note: </strong>Pass this attribute to narrow down your filter results for the <code>ITEM_NOT_AS_DESCRIBED</code> customerServiceMetricType.</span></p> <p>Supported categories include:</p><p><code>primary(L1) category Id</code></p>  # noqa: E501

        :param listing_categories: The listing_categories of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :type: list[str]
        """

        self._listing_categories = listing_categories

    @property
    def shipping_regions(self):
        """Gets the shipping_regions of this CustomerServiceMetricsFilterCriteria.  # noqa: E501

        A list of shipping region enumeration values on which the service metric is measured. This comma delimited array allows the seller to customize the report to focus on domestic or international shipping. <p> <span class=\"tablenote\"><strong>Note: </strong>Pass this attribute to narrow down your filter results for the <code>ITEM_NOT_RECEIVED</code> customerServiceMetricType.</span></p> <p>Supported categories include:</p><p><code>primary(L1) category Id</code></p>See <strong>ShippingRegionTypeEnum</strong> for values  # noqa: E501

        :return: The shipping_regions of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._shipping_regions

    @shipping_regions.setter
    def shipping_regions(self, shipping_regions):
        """Sets the shipping_regions of this CustomerServiceMetricsFilterCriteria.

        A list of shipping region enumeration values on which the service metric is measured. This comma delimited array allows the seller to customize the report to focus on domestic or international shipping. <p> <span class=\"tablenote\"><strong>Note: </strong>Pass this attribute to narrow down your filter results for the <code>ITEM_NOT_RECEIVED</code> customerServiceMetricType.</span></p> <p>Supported categories include:</p><p><code>primary(L1) category Id</code></p>See <strong>ShippingRegionTypeEnum</strong> for values  # noqa: E501

        :param shipping_regions: The shipping_regions of this CustomerServiceMetricsFilterCriteria.  # noqa: E501
        :type: list[str]
        """

        self._shipping_regions = shipping_regions

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
        if issubclass(CustomerServiceMetricsFilterCriteria, dict):
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
        if not isinstance(other, CustomerServiceMetricsFilterCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
