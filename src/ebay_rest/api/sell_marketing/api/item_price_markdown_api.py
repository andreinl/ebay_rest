# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.19.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_marketing.api_client import ApiClient


class ItemPriceMarkdownApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_item_price_markdown_promotion(self, content_type, **kwargs):  # noqa: E501
        """create_item_price_markdown_promotion  # noqa: E501

        This method creates an <b>item price markdown promotion</b> (know simply as a \"markdown promotion\") where a discount amount is applied directly to the items included the promotion. Discounts can be specified as either a monetary amount or a percentage off the standard sales price. eBay highlights promoted items by placing teasers for the items throughout the online sales flows.  <p>Unlike an <a href=\"/api-docs/sell/marketing/resources/item_promotion/methods/createItemPromotion\">item promotion</a>, a markdown promotion does not require the buyer meet a \"threshold\" before the offer takes effect. With markdown promotions, all the buyer needs to do is purchase the item to receive the promotion benefit.</p>  <p class=\"tablenote\"><b>Important:</b> There are some restrictions for which listings are available for price markdown promotions. For details, see <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager requirements and restrictions</a>. <br><br>In addition, we recommend you list items at competitive prices before including them in your markdown promotions. For an extensive list of pricing recommendations, see the <b>Growth</b> tab in Seller Hub.</p> <p>There are two ways to add items to markdown promotions:</p> <ul><li><b>Key-based promotions</b> select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the <b>inventoryReferenceId</b> and the associated <b>inventoryReferenceType</b> of the item(s) you want to include the promotion.</li>  <li><b>Rule-based promotions</b> select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions.</li></ul>  <p>New promotions must be created in either a <code>DRAFT</code> or a <code>SCHEDULED</code> state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it's correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the <b>Location</b> response header. Use this ID to reference the promotion in subsequent requests (such as to schedule a promotion that's in a DRAFT state).</p>  <p class=\"tablenote\"><b>Tip:</b> Refer to <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a> in the <i>Selling Integration Guide</i> for details and examples showing how to create and manage seller promotions.</p>  <p>Markdown promotions are available on all eBay marketplaces. For more information, see <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager requirements and restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_item_price_markdown_promotion(content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param ItemPriceMarkdown body: This type defines the fields that describe an item price markdown promotion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_item_price_markdown_promotion_with_http_info(content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_item_price_markdown_promotion_with_http_info(content_type, **kwargs)  # noqa: E501
            return data

    def create_item_price_markdown_promotion_with_http_info(self, content_type, **kwargs):  # noqa: E501
        """create_item_price_markdown_promotion  # noqa: E501

        This method creates an <b>item price markdown promotion</b> (know simply as a \"markdown promotion\") where a discount amount is applied directly to the items included the promotion. Discounts can be specified as either a monetary amount or a percentage off the standard sales price. eBay highlights promoted items by placing teasers for the items throughout the online sales flows.  <p>Unlike an <a href=\"/api-docs/sell/marketing/resources/item_promotion/methods/createItemPromotion\">item promotion</a>, a markdown promotion does not require the buyer meet a \"threshold\" before the offer takes effect. With markdown promotions, all the buyer needs to do is purchase the item to receive the promotion benefit.</p>  <p class=\"tablenote\"><b>Important:</b> There are some restrictions for which listings are available for price markdown promotions. For details, see <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager requirements and restrictions</a>. <br><br>In addition, we recommend you list items at competitive prices before including them in your markdown promotions. For an extensive list of pricing recommendations, see the <b>Growth</b> tab in Seller Hub.</p> <p>There are two ways to add items to markdown promotions:</p> <ul><li><b>Key-based promotions</b> select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the <b>inventoryReferenceId</b> and the associated <b>inventoryReferenceType</b> of the item(s) you want to include the promotion.</li>  <li><b>Rule-based promotions</b> select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions.</li></ul>  <p>New promotions must be created in either a <code>DRAFT</code> or a <code>SCHEDULED</code> state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it's correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the <b>Location</b> response header. Use this ID to reference the promotion in subsequent requests (such as to schedule a promotion that's in a DRAFT state).</p>  <p class=\"tablenote\"><b>Tip:</b> Refer to <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a> in the <i>Selling Integration Guide</i> for details and examples showing how to create and manage seller promotions.</p>  <p>Markdown promotions are available on all eBay marketplaces. For more information, see <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager requirements and restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_item_price_markdown_promotion_with_http_info(content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param ItemPriceMarkdown body: This type defines the fields that describe an item price markdown promotion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_item_price_markdown_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `create_item_price_markdown_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_price_markdown', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_item_price_markdown_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """delete_item_price_markdown_promotion  # noqa: E501

        This method deletes the item price markdown promotion specified by the <b>promotion_id</b> path parameter. Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  <br><br>You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running promotion, call <a href=\"/api-docs/sell/marketing/resources/item_price_markdown/methods/updateItemPriceMarkdownPromotion\">updateItemPriceMarkdownPromotion</a> and adjust the <b>endDate</b> field as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_price_markdown_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_item_price_markdown_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_item_price_markdown_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def delete_item_price_markdown_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """delete_item_price_markdown_promotion  # noqa: E501

        This method deletes the item price markdown promotion specified by the <b>promotion_id</b> path parameter. Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  <br><br>You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running promotion, call <a href=\"/api-docs/sell/marketing/resources/item_price_markdown/methods/updateItemPriceMarkdownPromotion\">updateItemPriceMarkdownPromotion</a> and adjust the <b>endDate</b> field as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_price_markdown_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_price_markdown_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `delete_item_price_markdown_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_price_markdown/{promotion_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_price_markdown_promotion(self, promotion_id, **kwargs):  # noqa: E501
        """get_item_price_markdown_promotion  # noqa: E501

        This method returns the complete details of the item price markdown promotion that's indicated by the <b>promotion_id</b> path parameter. <br><br>Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_price_markdown_promotion(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :return: ItemPriceMarkdown
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_price_markdown_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_price_markdown_promotion_with_http_info(promotion_id, **kwargs)  # noqa: E501
            return data

    def get_item_price_markdown_promotion_with_http_info(self, promotion_id, **kwargs):  # noqa: E501
        """get_item_price_markdown_promotion  # noqa: E501

        This method returns the complete details of the item price markdown promotion that's indicated by the <b>promotion_id</b> path parameter. <br><br>Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_price_markdown_promotion_with_http_info(promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :return: ItemPriceMarkdown
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['promotion_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_price_markdown_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `get_item_price_markdown_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_price_markdown/{promotion_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ItemPriceMarkdown',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_item_price_markdown_promotion(self, content_type, promotion_id, **kwargs):  # noqa: E501
        """update_item_price_markdown_promotion  # noqa: E501

        This method updates the specified item price markdown promotion with the new configuration that you supply in the payload of the request. Specify the promotion you want to update using the <b>promotion_id</b> path parameter. Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  <br><br>When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don't pass a field that currently has a value, the update request fails.  <br><br>The parameters you are allowed to update with this request depend on the status of the promotion you're updating:  <ul><li>DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the <b>discountRules</b>.</li> <li>RUNNING promotions: You can change the <b>endDate</b> and the item's inventory but you cannot change the promotional discount or the promotion's start date.</li> <li>ENDED promotions: Nothing can be changed.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_item_price_markdown_promotion(content_type, promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :param ItemPriceMarkdown body: This type defines the fields that describe an item price markdown promotion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_item_price_markdown_promotion_with_http_info(content_type, promotion_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_item_price_markdown_promotion_with_http_info(content_type, promotion_id, **kwargs)  # noqa: E501
            return data

    def update_item_price_markdown_promotion_with_http_info(self, content_type, promotion_id, **kwargs):  # noqa: E501
        """update_item_price_markdown_promotion  # noqa: E501

        This method updates the specified item price markdown promotion with the new configuration that you supply in the payload of the request. Specify the promotion you want to update using the <b>promotion_id</b> path parameter. Call <a href=\"/api-docs/sell/marketing/resources/promotion/methods/getPromotions\">getPromotions</a> to retrieve the IDs of a seller's promotions.  <br><br>When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don't pass a field that currently has a value, the update request fails.  <br><br>The parameters you are allowed to update with this request depend on the status of the promotion you're updating:  <ul><li>DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the <b>discountRules</b>.</li> <li>RUNNING promotions: You can change the <b>endDate</b> and the item's inventory but you cannot change the promotional discount or the promotion's start date.</li> <li>ENDED promotions: Nothing can be changed.</li></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_item_price_markdown_promotion_with_http_info(content_type, promotion_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href=\"/api-docs/static/rest-request-components.html#HTTP\" target=\"_blank \">HTTP request headers</a>. (required)
        :param str promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code> (required)
        :param ItemPriceMarkdown body: This type defines the fields that describe an item price markdown promotion.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'promotion_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_item_price_markdown_promotion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `update_item_price_markdown_promotion`")  # noqa: E501
        # verify the required parameter 'promotion_id' is set
        if ('promotion_id' not in params or
                params['promotion_id'] is None):
            raise ValueError("Missing the required parameter `promotion_id` when calling `update_item_price_markdown_promotion`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'promotion_id' in params:
            path_params['promotion_id'] = params['promotion_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item_price_markdown/{promotion_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
