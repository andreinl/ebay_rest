# coding: utf-8

"""
    Recommendation API

    The <b>Recommendation API</b> returns information that sellers can use to optimize the configuration of their listings on eBay. <br><br>Currently, the API contains a single method, <b>findListingRecommendations</b>. This method provides information that sellers can use to configure Promoted Listings ad campaigns to maximize the visibility of their items in the eBay marketplace.  # noqa: E501

    OpenAPI spec version: v1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_recommendation.api_client import ApiClient


class ListingRecommendationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_listing_recommendations(self, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """find_listing_recommendations  # noqa: E501

        The <b>find</b> method currently returns information for a single recommendation type (<code>AD</code>) which contains information that sellers can use to configure <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\" title=\"Selling Integration Guide\">Promoted Listings</a> ad campaigns. <p>The response from this method includes an array of the seller's listing IDs, where each element in the array contains recommendations related to the associated listing ID. For details on how to use this method, see <a href=\"/api-docs/sell/static/marketing/pl-reco-api.html\" title=\"Selling Integration Guide\">Using the Recommendation API to help configure campaigns</a>.</p>  <h3>The AD recommendation type</h3>  </p>  <p>The <code>AD</code> type contains two sets of information:</p>  <ul><li><b>The promoteWithAd indicator</b> <br>The <b>promoteWithAd</b> response field indicates whether or not eBay recommends you place the associated listing in a Promoted Listings ad campaign. <p>The returned value is set to either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>, where <code>RECOMMENDED</code> identifies the listings that will benefit the most from having them included in an ad campaign.</p></li>  <li><b>The bid percentage</b> <br>Also known as the \"ad rate,\" the <b>bidPercentage</b> field provides the current trending bid percentage of similarly promoted items in the marketplace. <p>The ad rate is a user-specified value that indicates the level of promotion that eBay applies to the campaign across the marketplace. The value is also used to calculate the Promotion Listings fee, which is assessed to the seller if a Promoted Listings action results in the sale of an item.</p></li></ul>  <h3>Configuring the request</h3> <p>You can configure a request to review all of a seller's currently active listings, or just a subset of them.</p>  <ul><li><b>All active listings</b> &ndash; If you leave the request body empty, the request targets <i>all</i> the items currently listed by the seller. <p>Here, the response is filtered to contain only the items where <b>promoteWithAd</b> equals <code>RECOMMENDED</code>. In this case, eBay recommends that all the returned listings should be included in a Promoted Listings ad campaign.</p></li> <li><b>Selected listing IDs</b> &ndash; If you populate the request body with a set of <b>listingIds</b>, the response contains data for all the specified listing IDs. <p>In this scenario, the response provides you with information on listings where the <b>promoteWithAd</b> can be either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>.</li></ul>  <h3>The paginated response</h3>  <p>Because the response can contain many listing IDs, the <b>findListingRecommendations</b> method paginates the response set.</p> <p>You can control size of the returned pages, as well as an offset that dictates where to start the pagination, using query parameters in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_listing_recommendations(x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: Use this header to specify the eBay marketplace where you list the items for which you want to get recommendations. (required)
        :param FindListingRecommendationRequest body:
        :param str filter: Provide a list of key-value pairs to specify the criteria you want to use to filter the response.  <br><br>In the list, separate each filter key from its associated value with a colon (\"<code>:</code>\").  <br><br>Currently, the only supported filter value is <b>recommendationTypes</b> and it supports only the (\"<code>AD</code>\") type. Follow the <b>recommendationTypes</b> specifier with the filter type(s) enclosed in curly braces (\"<code>{ }</code>\"), and separate multiple types with commas.  <br><br><b>Example:</b> <code>filter=recommendationTypes:{AD}</code>  <br><br><b>Default:</b> <code>recommendationTypes:{AD}</code>
        :param str limit: Use this query parameter to set the maximum number of ads to return on a page from the paginated response.  <br><br><b>Default: </b>10 <br><b>Maximum:</b> 500
        :param str offset: Specifies the number of ads to skip in the result set before returning the first ad in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set.</p> <p><b>Default:</b> 0</p>
        :return: PagedListingRecommendationCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_listing_recommendations_with_http_info(x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_listing_recommendations_with_http_info(x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
            return data

    def find_listing_recommendations_with_http_info(self, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """find_listing_recommendations  # noqa: E501

        The <b>find</b> method currently returns information for a single recommendation type (<code>AD</code>) which contains information that sellers can use to configure <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\" title=\"Selling Integration Guide\">Promoted Listings</a> ad campaigns. <p>The response from this method includes an array of the seller's listing IDs, where each element in the array contains recommendations related to the associated listing ID. For details on how to use this method, see <a href=\"/api-docs/sell/static/marketing/pl-reco-api.html\" title=\"Selling Integration Guide\">Using the Recommendation API to help configure campaigns</a>.</p>  <h3>The AD recommendation type</h3>  </p>  <p>The <code>AD</code> type contains two sets of information:</p>  <ul><li><b>The promoteWithAd indicator</b> <br>The <b>promoteWithAd</b> response field indicates whether or not eBay recommends you place the associated listing in a Promoted Listings ad campaign. <p>The returned value is set to either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>, where <code>RECOMMENDED</code> identifies the listings that will benefit the most from having them included in an ad campaign.</p></li>  <li><b>The bid percentage</b> <br>Also known as the \"ad rate,\" the <b>bidPercentage</b> field provides the current trending bid percentage of similarly promoted items in the marketplace. <p>The ad rate is a user-specified value that indicates the level of promotion that eBay applies to the campaign across the marketplace. The value is also used to calculate the Promotion Listings fee, which is assessed to the seller if a Promoted Listings action results in the sale of an item.</p></li></ul>  <h3>Configuring the request</h3> <p>You can configure a request to review all of a seller's currently active listings, or just a subset of them.</p>  <ul><li><b>All active listings</b> &ndash; If you leave the request body empty, the request targets <i>all</i> the items currently listed by the seller. <p>Here, the response is filtered to contain only the items where <b>promoteWithAd</b> equals <code>RECOMMENDED</code>. In this case, eBay recommends that all the returned listings should be included in a Promoted Listings ad campaign.</p></li> <li><b>Selected listing IDs</b> &ndash; If you populate the request body with a set of <b>listingIds</b>, the response contains data for all the specified listing IDs. <p>In this scenario, the response provides you with information on listings where the <b>promoteWithAd</b> can be either <code>RECOMMENDED</code> or <code>UNDETERMINED</code>.</li></ul>  <h3>The paginated response</h3>  <p>Because the response can contain many listing IDs, the <b>findListingRecommendations</b> method paginates the response set.</p> <p>You can control size of the returned pages, as well as an offset that dictates where to start the pagination, using query parameters in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_listing_recommendations_with_http_info(x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: Use this header to specify the eBay marketplace where you list the items for which you want to get recommendations. (required)
        :param FindListingRecommendationRequest body:
        :param str filter: Provide a list of key-value pairs to specify the criteria you want to use to filter the response.  <br><br>In the list, separate each filter key from its associated value with a colon (\"<code>:</code>\").  <br><br>Currently, the only supported filter value is <b>recommendationTypes</b> and it supports only the (\"<code>AD</code>\") type. Follow the <b>recommendationTypes</b> specifier with the filter type(s) enclosed in curly braces (\"<code>{ }</code>\"), and separate multiple types with commas.  <br><br><b>Example:</b> <code>filter=recommendationTypes:{AD}</code>  <br><br><b>Default:</b> <code>recommendationTypes:{AD}</code>
        :param str limit: Use this query parameter to set the maximum number of ads to return on a page from the paginated response.  <br><br><b>Default: </b>10 <br><b>Maximum:</b> 500
        :param str offset: Specifies the number of ads to skip in the result set before returning the first ad in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the items returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set.</p> <p><b>Default:</b> 0</p>
        :return: PagedListingRecommendationCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_ebay_c_marketplace_id', 'body', 'filter', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_listing_recommendations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `find_listing_recommendations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/find', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedListingRecommendationCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
