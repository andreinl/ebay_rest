# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_browse.api_client import ApiClient


class ShoppingCartApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_item(self, **kwargs):  # noqa: E501
        """add_item  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b> value is greater than the number of available, the <b> quantity</b> value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to 15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, whether it has just been added to the cart or has been in the cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>       <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a> method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay members.</li>  <li>You can add only items with a FIXED_PRICE that accept PayPal as a payment.  </li> </ul> <p>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_item(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_item_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_item_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_item_with_http_info(self, **kwargs):  # noqa: E501
        """add_item  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b> value is greater than the number of available, the <b> quantity</b> value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to 15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, whether it has just been added to the cart or has been in the cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>       <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a> method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay members.</li>  <li>You can add only items with a FIXED_PRICE that accept PayPal as a payment.  </li> </ul> <p>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_item_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_item" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/shopping_cart/add_item', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemoteShopcartResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shopping_cart(self, **kwargs):  # noqa: E501
        """get_shopping_cart  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>    <p>This method retrieves all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. There are no URI parameters or request payload.  <br /><br />The response returns the summary details of all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If the cart is empty, the response is HTTP 204. </p>   <br /><br /> The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.                         <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shopping_cart(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shopping_cart_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_shopping_cart_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_shopping_cart_with_http_info(self, **kwargs):  # noqa: E501
        """get_shopping_cart  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>    <p>This method retrieves all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. There are no URI parameters or request payload.  <br /><br />The response returns the summary details of all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If the cart is empty, the response is HTTP 204. </p>   <br /><br /> The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.                         <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shopping_cart_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shopping_cart" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/shopping_cart/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemoteShopcartResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_item(self, **kwargs):  # noqa: E501
        """remove_item  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method removes a specific item from the eBay member's cart. You specify the ID of the item in the cart (<b>cartItemId</b>) that you want to remove.   <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If you remove the last item in the cart, the response is HTTP 204.<br /><br />  The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note: </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the identifier of a specific item <i>in</i> the cart and is generated when the item was added to the cart.</span></p>               <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/remove_item</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/remove_item</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_item(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RemoveCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_item_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.remove_item_with_http_info(**kwargs)  # noqa: E501
            return data

    def remove_item_with_http_info(self, **kwargs):  # noqa: E501
        """remove_item  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method removes a specific item from the eBay member's cart. You specify the ID of the item in the cart (<b>cartItemId</b>) that you want to remove.   <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If you remove the last item in the cart, the response is HTTP 204.<br /><br />  The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note: </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the identifier of a specific item <i>in</i> the cart and is generated when the item was added to the cart.</span></p>               <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/remove_item</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/remove_item</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_item_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RemoveCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_item" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/shopping_cart/remove_item', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemoteShopcartResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_quantity(self, **kwargs):  # noqa: E501
        """update_quantity  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the quantity. If the <b> quantity</b> value is greater than the number of available, the <b> quantity</b> value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note: </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the identifier of a specific item <i>in</i> the cart and is generated when the item was added to the cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quantity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_quantity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_quantity_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_quantity_with_http_info(self, **kwargs):  # noqa: E501
        """update_quantity  # noqa: E501

        <span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the quantity. If the <b> quantity</b> value is greater than the number of available, the <b> quantity</b> value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and state of an item changes often. If the item becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note: </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the identifier of a specific item <i>in</i> the cart and is generated when the item was added to the cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b> Production URL: </b> <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>            <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>         <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quantity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCartItemInput body:
        :return: RemoteShopcartResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_quantity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/shopping_cart/update_quantity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemoteShopcartResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
