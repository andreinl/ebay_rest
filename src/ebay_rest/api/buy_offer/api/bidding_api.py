# coding: utf-8

"""
    Buy Offer API

    The Buy Offer API enables Partners to place proxy bids for a buyer and retrieve the auctions where the buyer is bidding.  By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction. </p>   # noqa: E501

    OpenAPI spec version: v1_beta.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from buy_offer.api_client import ApiClient


class BiddingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_bidding(self, item_id, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_bidding  # noqa: E501

        This method retrieves the bidding details that are specific to the buyer of the specified auction. This must be an auction where the buyer has already placed a bid. To retrieve the bidding information you use a user access token and pass in the item ID of the auction. You can also retrieve general bidding details about the auction, such as minimum bid price and the count of unique bidders, using the Browse API getItem method. URLs for this method Production URL: https://api.ebay.com/buy/offer/v1_beta/bidding/ Sandbox URL: https://api.sandbox.ebay.com/buy/offer/v1_beta/bidding/ Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bidding(item_id, x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str item_id: The eBay RESTful identifier of an item that you want the buyer's bidding information. This ID is returned by the Browse and Feed API methods. RESTful Item ID example: v1|2**********2|0 For more information about item ID for RESTful APIs, see the Legacy API compatibility section of the Buy APIs Overview. Restriction: The buyer must have placed a bid for this item. (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the buyer is based. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :return: Bidding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bidding_with_http_info(item_id, x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bidding_with_http_info(item_id, x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_bidding_with_http_info(self, item_id, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_bidding  # noqa: E501

        This method retrieves the bidding details that are specific to the buyer of the specified auction. This must be an auction where the buyer has already placed a bid. To retrieve the bidding information you use a user access token and pass in the item ID of the auction. You can also retrieve general bidding details about the auction, such as minimum bid price and the count of unique bidders, using the Browse API getItem method. URLs for this method Production URL: https://api.ebay.com/buy/offer/v1_beta/bidding/ Sandbox URL: https://api.sandbox.ebay.com/buy/offer/v1_beta/bidding/ Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bidding_with_http_info(item_id, x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str item_id: The eBay RESTful identifier of an item that you want the buyer's bidding information. This ID is returned by the Browse and Feed API methods. RESTful Item ID example: v1|2**********2|0 For more information about item ID for RESTful APIs, see the Legacy API compatibility section of the Buy APIs Overview. Restriction: The buyer must have placed a bid for this item. (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the buyer is based. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :return: Bidding
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'x_ebay_c_marketplace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bidding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `get_bidding`")  # noqa: E501
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_bidding`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/bidding/{item_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bidding',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def place_proxy_bid(self, x_ebay_c_marketplace_id, item_id, **kwargs):  # noqa: E501
        """place_proxy_bid  # noqa: E501

        This method uses a user access token to place a proxy bid for the buyer on a specific auction item. The item must offer AUCTION as one of the buyingOptions. To place a bid, you pass in the item ID of the auction as a URI parameter and the buyer's maximum bid amount (maxAmount ) in the payload. By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction. After this bid is placed, if someone else outbids the buyer a bid, eBay automatically bids again for the buyer up to the amount of their maximum bid. When the bid exceeds the buyer's maximum bid, eBay will notify them that they have been outbid. To find auctions, you can use the Browse API to search for items and use a filter to return only auction items. For example: /buy/browse/v1/item_summary/search?q=iphone&amp;filter=buyingOptions:{AUCTION} URLs for this method Production URL: https://api.ebay.com/buy/offer/v1_beta/bidding/ Sandbox URL: https://api.sandbox.ebay.com/buy/offer/v1_beta/bidding/ Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_proxy_bid(x_ebay_c_marketplace_id, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the buyer is based. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :param str item_id: The eBay RESTful identifier of an item you want to bid on. This ID is returned by the Browse and Feed API methods. RESTful Item ID Example: v1|2**********2|0 For more information about item ID for RESTful APIs, see the Legacy API compatibility section of the Buy APIs Overview. (required)
        :param PlaceProxyBidRequest body:
        :return: PlaceProxyBidResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.place_proxy_bid_with_http_info(x_ebay_c_marketplace_id, item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.place_proxy_bid_with_http_info(x_ebay_c_marketplace_id, item_id, **kwargs)  # noqa: E501
            return data

    def place_proxy_bid_with_http_info(self, x_ebay_c_marketplace_id, item_id, **kwargs):  # noqa: E501
        """place_proxy_bid  # noqa: E501

        This method uses a user access token to place a proxy bid for the buyer on a specific auction item. The item must offer AUCTION as one of the buyingOptions. To place a bid, you pass in the item ID of the auction as a URI parameter and the buyer's maximum bid amount (maxAmount ) in the payload. By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction. After this bid is placed, if someone else outbids the buyer a bid, eBay automatically bids again for the buyer up to the amount of their maximum bid. When the bid exceeds the buyer's maximum bid, eBay will notify them that they have been outbid. To find auctions, you can use the Browse API to search for items and use a filter to return only auction items. For example: /buy/browse/v1/item_summary/search?q=iphone&amp;filter=buyingOptions:{AUCTION} URLs for this method Production URL: https://api.ebay.com/buy/offer/v1_beta/bidding/ Sandbox URL: https://api.sandbox.ebay.com/buy/offer/v1_beta/bidding/ Restrictions For a list of supported sites and other restrictions, see API Restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.place_proxy_bid_with_http_info(x_ebay_c_marketplace_id, item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the buyer is based. Note: This value is case sensitive. For example: &nbsp;&nbsp;X-EBAY-C-MARKETPLACE-ID = EBAY_US For a list of supported sites see, API Restrictions. (required)
        :param str item_id: The eBay RESTful identifier of an item you want to bid on. This ID is returned by the Browse and Feed API methods. RESTful Item ID Example: v1|2**********2|0 For more information about item ID for RESTful APIs, see the Legacy API compatibility section of the Buy APIs Overview. (required)
        :param PlaceProxyBidRequest body:
        :return: PlaceProxyBidResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_ebay_c_marketplace_id', 'item_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_proxy_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `place_proxy_bid`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `place_proxy_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']  # noqa: E501

        query_params = []

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/bidding/{item_id}/place_proxy_bid', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlaceProxyBidResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
