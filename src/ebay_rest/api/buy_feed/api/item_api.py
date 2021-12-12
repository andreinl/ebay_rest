# coding: utf-8

"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_feed.api_client import ApiClient


class ItemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_item_feed(self, accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, **kwargs):  # noqa: E501
        """get_item_feed  # noqa: E501

        <p>This method lets you download a TSV_GZIP (tab separated value gzip) <b> Item</b> feed file. The feed file contains all the items from <b> all</b> the child categories of the specified category.  The first line of the file is the header, which labels the columns and indicates the order of the values on each line.  Each header is described in the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed#h3-response-fields\">Response fields</a> section.  </p> <p> There are two types of item feed files generated: <ul> <li>A daily <b>Item</b> feed file containing all the newly listed items for a specific category, date, and marketplace (<b>feed_scope</b> = <code>NEWLY_LISTED</code>)</li>  <li>A weekly <b>Item Bootstrap</b> feed file containing <i> all</i> the items in a specific category and marketplace (<b>feed_scope</b> = <code>ALL_ACTIVE</code>)</li>  </ul>  </p>   <p><span class=\"tablenote\"><b>Note: </b>  Filters are applied to the feed files. For details, see <a href=\"/api-docs/buy/static/api-feed.html#feed-filters\">Feed File Filters</a>. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.</span></p>                                   <h3><b>URLs for this method</b></h3>   <p><ul>    <li><b> Production URL: </b> <code>https://api.ebay.com/buy/feed/v1_beta/item?</code></li>    <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/feed/v1_beta/item?</code></li>   </ul> </p>              <h3><b>Downloading feed files </b></h3>             <p>Item feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the <a href=\"#range-header\">Range</a> request header. The <a href=\"#content-range\">Content-range</a> response header indicates where in the full resource this partial chunk of data belongs  and the total number of bytes in the file.       For more information about using these headers, see <a href=\"/api-docs/buy/static/api-feed.html#retrv-gzip\">Retrieving a gzip feed file</a>.    </p>    <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>              <p><span class=\"tablenote\">  <b> Note:</b> A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.</span>  </p>                <h3><b>Restrictions </b></h3>                <p>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_feed(accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept: The formats that the client accepts for the response.<br /><br />A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format.<br /><br /><b>Default:</b> <code>application/json,text/tab-separated-values</code> (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. <b>Note: </b> This value is case sensitive.<br /><br />For example: <br />&nbsp;&nbsp;<code>X-EBAY-C-MARKETPLACE-ID = EBAY_US</code>  <br /><br /> For a list of supported sites see, <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>. (required)
        :param str range: <a name=\"range-header\"></a>This header specifies the range in bytes of the chunks of the gzip file being returned. <br /><br /><b> Format:</b> <code >bytes=<em>startpos</em>-<em>endpos</em></code><br /><br />  For example, the following retrieves the first 10 MBs of the feed file. <br /><br />&nbsp;&nbsp;<code>Range bytes=0-10485760</code> <br /><br />For more information about using this header, see <a href=\"/api-docs/buy/static/api-feed.html#retrv-gzip\">Retrieving a gzip feed file</a>. <br /><br /><b>Maximum:</b> 100 MB (10MB in the Sandbox) (required)
        :param str feed_scope: Specifies the type of feed file to return. <br /><br /><b>Valid Values: </b>   <ul> <li><b> NEWLY_LISTED</b> - Returns the daily <b>Item</b> feed file containing all Good 'Til Cancelled items that were listed on the day specified by the <b> date</b> parameter in the category specified by the <b> category_id</b> parameter.  <br /><br /><code>/item?feed_scope=NEWLY_LISTED&category_id=15032&date=20170925</code></li>  <li><b>ALL_ACTIVE</b> - Returns the weekly <b>Item Bootstrap</b> feed file containing all the Good 'Til Cancelled items in the category specified by the <b> category_id</b> parameter.  <br /><br /><span class=\"tablenote\"><b>Note:</b> Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The items in the file are the items that were in the specified category on Sunday.</span> <br /><br /><code>/item?feed_scope=ALL_ACTIVE&category_id=15032</code>  </ul> (required)
        :param str category_id: An eBay top-level category ID of the items to be returned in the feed file. <br /> <br />The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplace, you can use the Taxonomy API <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategoryTree\">getCategoryTree</a> method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the <b> categoryTreeNodeLevel </b> field. <br /><br /><b>For example: </b><br />&nbsp;&nbsp;<code>\"categoryTreeNodeLevel\": 1</code> <br /><br />For details see <a href=\"/api-docs/buy/buy-categories.html\">Get Categories for Buy APIs</a>. </li>  </ul> <br /><br />   <b>Restriction: </b> Must be a top-level (L1) category </b> (required)
        :param str _date: The date of the daily <b>Item</b> feed file (<b>feed_scope</b>=<code>NEWLY_LISTED</code>) you want. <p>The <b> date</b> is required only for the daily <b>Item</b> feed file. If you specify a date for the <b>Item Bootstrap</b> file (<b>feed_scope</b>=<code>ALL_ACTIVE</code>), the date is ignored and the latest file is returned. The date the <b>Item Bootstrap</b> feed file was generated is returned in the <b>Last-Modified</b> response header.</code></p>    <p>The <b> Item</b> feed files are generated every day and there are 14 daily files available.</p>  <span class=\"tablenote\"> <b>Note: </b><ul>  <li>The daily <b>Item</b> feed files are available each day after 9AM MST (US Mountain Standard Time), which is -7 hours UTC time.</li>    <li>There is a 48 hour latency when generating the <b> Item</b> feed files. This means you can download the file for July 10th on July 12 after 9AM MST. <br /><br /><b>Note: </b> For categories with a large number of items, the latency can be up to 72 hours.</li> </ul></span> <p><b> Format: </b><code>yyyyMMdd</code><br /><br /><b> Requirements: </b> <ul>  <li>Required when <b>feed_scope</b>=<code>NEWLY_LISTED</code> </li>  <li>Must be within 3-14 days in the past</li></ul>
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_item_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_item_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, **kwargs)  # noqa: E501
            return data

    def get_item_feed_with_http_info(self, accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, **kwargs):  # noqa: E501
        """get_item_feed  # noqa: E501

        <p>This method lets you download a TSV_GZIP (tab separated value gzip) <b> Item</b> feed file. The feed file contains all the items from <b> all</b> the child categories of the specified category.  The first line of the file is the header, which labels the columns and indicates the order of the values on each line.  Each header is described in the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed#h3-response-fields\">Response fields</a> section.  </p> <p> There are two types of item feed files generated: <ul> <li>A daily <b>Item</b> feed file containing all the newly listed items for a specific category, date, and marketplace (<b>feed_scope</b> = <code>NEWLY_LISTED</code>)</li>  <li>A weekly <b>Item Bootstrap</b> feed file containing <i> all</i> the items in a specific category and marketplace (<b>feed_scope</b> = <code>ALL_ACTIVE</code>)</li>  </ul>  </p>   <p><span class=\"tablenote\"><b>Note: </b>  Filters are applied to the feed files. For details, see <a href=\"/api-docs/buy/static/api-feed.html#feed-filters\">Feed File Filters</a>. When curating the items returned, be sure to code as if these filters are not applied as they can be changed or removed in the future.</span></p>                                   <h3><b>URLs for this method</b></h3>   <p><ul>    <li><b> Production URL: </b> <code>https://api.ebay.com/buy/feed/v1_beta/item?</code></li>    <li><b> Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/feed/v1_beta/item?</code></li>   </ul> </p>              <h3><b>Downloading feed files </b></h3>             <p>Item feed files are binary gzip files. If the file is larger than 100 MB, the download must be streamed in chunks. You specify the size of the chunks in bytes using the <a href=\"#range-header\">Range</a> request header. The <a href=\"#content-range\">Content-range</a> response header indicates where in the full resource this partial chunk of data belongs  and the total number of bytes in the file.       For more information about using these headers, see <a href=\"/api-docs/buy/static/api-feed.html#retrv-gzip\">Retrieving a gzip feed file</a>.    </p>    <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK\" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>              <p><span class=\"tablenote\">  <b> Note:</b> A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format. For documentation purposes, the successful call response is shown below as JSON fields so that the value returned in each column can be explained. The order of the response fields shows the order of the columns in the feed file.</span>  </p>                <h3><b>Restrictions </b></h3>                <p>For a list of supported sites and other restrictions, see <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_feed_with_http_info(accept, x_ebay_c_marketplace_id, range, feed_scope, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept: The formats that the client accepts for the response.<br /><br />A successful call will always return a TSV.GZIP file; however, unsuccessful calls generate errors that are returned in JSON format.<br /><br /><b>Default:</b> <code>application/json,text/tab-separated-values</code> (required)
        :param str x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. <b>Note: </b> This value is case sensitive.<br /><br />For example: <br />&nbsp;&nbsp;<code>X-EBAY-C-MARKETPLACE-ID = EBAY_US</code>  <br /><br /> For a list of supported sites see, <a href=\"/api-docs/buy/feed/overview.html#API\">API Restrictions</a>. (required)
        :param str range: <a name=\"range-header\"></a>This header specifies the range in bytes of the chunks of the gzip file being returned. <br /><br /><b> Format:</b> <code >bytes=<em>startpos</em>-<em>endpos</em></code><br /><br />  For example, the following retrieves the first 10 MBs of the feed file. <br /><br />&nbsp;&nbsp;<code>Range bytes=0-10485760</code> <br /><br />For more information about using this header, see <a href=\"/api-docs/buy/static/api-feed.html#retrv-gzip\">Retrieving a gzip feed file</a>. <br /><br /><b>Maximum:</b> 100 MB (10MB in the Sandbox) (required)
        :param str feed_scope: Specifies the type of feed file to return. <br /><br /><b>Valid Values: </b>   <ul> <li><b> NEWLY_LISTED</b> - Returns the daily <b>Item</b> feed file containing all Good 'Til Cancelled items that were listed on the day specified by the <b> date</b> parameter in the category specified by the <b> category_id</b> parameter.  <br /><br /><code>/item?feed_scope=NEWLY_LISTED&category_id=15032&date=20170925</code></li>  <li><b>ALL_ACTIVE</b> - Returns the weekly <b>Item Bootstrap</b> feed file containing all the Good 'Til Cancelled items in the category specified by the <b> category_id</b> parameter.  <br /><br /><span class=\"tablenote\"><b>Note:</b> Bootstrap files are generated every Tuesday and the file is available on Wednesday. However, the exact time the file is available can vary so we recommend you download the Bootstrap file on Thursday. The items in the file are the items that were in the specified category on Sunday.</span> <br /><br /><code>/item?feed_scope=ALL_ACTIVE&category_id=15032</code>  </ul> (required)
        :param str category_id: An eBay top-level category ID of the items to be returned in the feed file. <br /> <br />The list of eBay category IDs changes over time and category IDs are not the same across all the eBay marketplaces. To get a list of the top-level categories for a marketplace, you can use the Taxonomy API <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategoryTree\">getCategoryTree</a> method. This method retrieves the complete category tree for the marketplace. The top-level categories are identified by the <b> categoryTreeNodeLevel </b> field. <br /><br /><b>For example: </b><br />&nbsp;&nbsp;<code>\"categoryTreeNodeLevel\": 1</code> <br /><br />For details see <a href=\"/api-docs/buy/buy-categories.html\">Get Categories for Buy APIs</a>. </li>  </ul> <br /><br />   <b>Restriction: </b> Must be a top-level (L1) category </b> (required)
        :param str _date: The date of the daily <b>Item</b> feed file (<b>feed_scope</b>=<code>NEWLY_LISTED</code>) you want. <p>The <b> date</b> is required only for the daily <b>Item</b> feed file. If you specify a date for the <b>Item Bootstrap</b> file (<b>feed_scope</b>=<code>ALL_ACTIVE</code>), the date is ignored and the latest file is returned. The date the <b>Item Bootstrap</b> feed file was generated is returned in the <b>Last-Modified</b> response header.</code></p>    <p>The <b> Item</b> feed files are generated every day and there are 14 daily files available.</p>  <span class=\"tablenote\"> <b>Note: </b><ul>  <li>The daily <b>Item</b> feed files are available each day after 9AM MST (US Mountain Standard Time), which is -7 hours UTC time.</li>    <li>There is a 48 hour latency when generating the <b> Item</b> feed files. This means you can download the file for July 10th on July 12 after 9AM MST. <br /><br /><b>Note: </b> For categories with a large number of items, the latency can be up to 72 hours.</li> </ul></span> <p><b> Format: </b><code>yyyyMMdd</code><br /><br /><b> Requirements: </b> <ul>  <li>Required when <b>feed_scope</b>=<code>NEWLY_LISTED</code> </li>  <li>Must be within 3-14 days in the past</li></ul>
        :return: ItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accept', 'x_ebay_c_marketplace_id', 'range', 'feed_scope', 'category_id', '_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_feed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `get_item_feed`")  # noqa: E501
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_item_feed`")  # noqa: E501
        # verify the required parameter 'range' is set
        if ('range' not in params or
                params['range'] is None):
            raise ValueError("Missing the required parameter `range` when calling `get_item_feed`")  # noqa: E501
        # verify the required parameter 'feed_scope' is set
        if ('feed_scope' not in params or
                params['feed_scope'] is None):
            raise ValueError("Missing the required parameter `feed_scope` when calling `get_item_feed`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_item_feed`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feed_scope' in params:
            query_params.append(('feed_scope', params['feed_scope']))  # noqa: E501
        if 'category_id' in params:
            query_params.append(('category_id', params['category_id']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/tab-separated-values'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/item', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
