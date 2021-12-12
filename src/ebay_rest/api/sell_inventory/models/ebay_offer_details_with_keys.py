# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EbayOfferDetailsWithKeys(object):
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
        'available_quantity': 'int',
        'category_id': 'str',
        'charity': 'Charity',
        'format': 'str',
        'hide_buyer_details': 'bool',
        'include_catalog_product_details': 'bool',
        'listing_description': 'str',
        'listing_duration': 'str',
        'listing_policies': 'ListingPolicies',
        'listing_start_date': 'str',
        'lot_size': 'int',
        'marketplace_id': 'str',
        'merchant_location_key': 'str',
        'pricing_summary': 'PricingSummary',
        'quantity_limit_per_buyer': 'int',
        'secondary_category_id': 'str',
        'sku': 'str',
        'store_category_names': 'list[str]',
        'tax': 'Tax'
    }

    attribute_map = {
        'available_quantity': 'availableQuantity',
        'category_id': 'categoryId',
        'charity': 'charity',
        'format': 'format',
        'hide_buyer_details': 'hideBuyerDetails',
        'include_catalog_product_details': 'includeCatalogProductDetails',
        'listing_description': 'listingDescription',
        'listing_duration': 'listingDuration',
        'listing_policies': 'listingPolicies',
        'listing_start_date': 'listingStartDate',
        'lot_size': 'lotSize',
        'marketplace_id': 'marketplaceId',
        'merchant_location_key': 'merchantLocationKey',
        'pricing_summary': 'pricingSummary',
        'quantity_limit_per_buyer': 'quantityLimitPerBuyer',
        'secondary_category_id': 'secondaryCategoryId',
        'sku': 'sku',
        'store_category_names': 'storeCategoryNames',
        'tax': 'tax'
    }

    def __init__(self, available_quantity=None, category_id=None, charity=None, format=None, hide_buyer_details=None, include_catalog_product_details=None, listing_description=None, listing_duration=None, listing_policies=None, listing_start_date=None, lot_size=None, marketplace_id=None, merchant_location_key=None, pricing_summary=None, quantity_limit_per_buyer=None, secondary_category_id=None, sku=None, store_category_names=None, tax=None):  # noqa: E501
        """EbayOfferDetailsWithKeys - a model defined in Swagger"""  # noqa: E501
        self._available_quantity = None
        self._category_id = None
        self._charity = None
        self._format = None
        self._hide_buyer_details = None
        self._include_catalog_product_details = None
        self._listing_description = None
        self._listing_duration = None
        self._listing_policies = None
        self._listing_start_date = None
        self._lot_size = None
        self._marketplace_id = None
        self._merchant_location_key = None
        self._pricing_summary = None
        self._quantity_limit_per_buyer = None
        self._secondary_category_id = None
        self._sku = None
        self._store_category_names = None
        self._tax = None
        self.discriminator = None
        if available_quantity is not None:
            self.available_quantity = available_quantity
        if category_id is not None:
            self.category_id = category_id
        if charity is not None:
            self.charity = charity
        if format is not None:
            self.format = format
        if hide_buyer_details is not None:
            self.hide_buyer_details = hide_buyer_details
        if include_catalog_product_details is not None:
            self.include_catalog_product_details = include_catalog_product_details
        if listing_description is not None:
            self.listing_description = listing_description
        if listing_duration is not None:
            self.listing_duration = listing_duration
        if listing_policies is not None:
            self.listing_policies = listing_policies
        if listing_start_date is not None:
            self.listing_start_date = listing_start_date
        if lot_size is not None:
            self.lot_size = lot_size
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if merchant_location_key is not None:
            self.merchant_location_key = merchant_location_key
        if pricing_summary is not None:
            self.pricing_summary = pricing_summary
        if quantity_limit_per_buyer is not None:
            self.quantity_limit_per_buyer = quantity_limit_per_buyer
        if secondary_category_id is not None:
            self.secondary_category_id = secondary_category_id
        if sku is not None:
            self.sku = sku
        if store_category_names is not None:
            self.store_category_names = store_category_names
        if tax is not None:
            self.tax = tax

    @property
    def available_quantity(self):
        """Gets the available_quantity of this EbayOfferDetailsWithKeys.  # noqa: E501

        This integer value sets the quantity of the inventory item (specified by the <strong>sku</strong> value) that will be available for purchase by buyers shopping on the eBay site specified in the <strong>marketplaceId</strong> field. Quantity must be set to <code>1</code> or more in order for the inventory item to be purchasable, but this field is not necessarily required, even for published offers, if the general quantity of the inventory item has already been set in the inventory item record.<br/><br/> For auction listings, this value must be <code>1</code>.  # noqa: E501

        :return: The available_quantity of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: int
        """
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        """Sets the available_quantity of this EbayOfferDetailsWithKeys.

        This integer value sets the quantity of the inventory item (specified by the <strong>sku</strong> value) that will be available for purchase by buyers shopping on the eBay site specified in the <strong>marketplaceId</strong> field. Quantity must be set to <code>1</code> or more in order for the inventory item to be purchasable, but this field is not necessarily required, even for published offers, if the general quantity of the inventory item has already been set in the inventory item record.<br/><br/> For auction listings, this value must be <code>1</code>.  # noqa: E501

        :param available_quantity: The available_quantity of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: int
        """

        self._available_quantity = available_quantity

    @property
    def category_id(self):
        """Gets the category_id of this EbayOfferDetailsWithKeys.  # noqa: E501

        The unique identifier of the eBay category that the product will be listed under. This field is not immediately required upon creating an offer, but will be required before publishing the offer. Sellers can use the <a href=\"https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions\" target=\"_blank\">getCategorySuggestions</a> method of the Taxonomy API to retrieve suggested category ID values. The seller passes in a query string like \"<em>iPhone 6</em>\", and category ID values for suggested categories are returned in the response.  # noqa: E501

        :return: The category_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this EbayOfferDetailsWithKeys.

        The unique identifier of the eBay category that the product will be listed under. This field is not immediately required upon creating an offer, but will be required before publishing the offer. Sellers can use the <a href=\"https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions\" target=\"_blank\">getCategorySuggestions</a> method of the Taxonomy API to retrieve suggested category ID values. The seller passes in a query string like \"<em>iPhone 6</em>\", and category ID values for suggested categories are returned in the response.  # noqa: E501

        :param category_id: The category_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def charity(self):
        """Gets the charity of this EbayOfferDetailsWithKeys.  # noqa: E501


        :return: The charity of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: Charity
        """
        return self._charity

    @charity.setter
    def charity(self, charity):
        """Sets the charity of this EbayOfferDetailsWithKeys.


        :param charity: The charity of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: Charity
        """

        self._charity = charity

    @property
    def format(self):
        """Gets the format of this EbayOfferDetailsWithKeys.  # noqa: E501

        This enumerated value indicates the listing format of the offer. <br/><br/>Supported values are <code>FIXED_PRICE</code> and <code>AUCTION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The format of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this EbayOfferDetailsWithKeys.

        This enumerated value indicates the listing format of the offer. <br/><br/>Supported values are <code>FIXED_PRICE</code> and <code>AUCTION</code>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param format: The format of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def hide_buyer_details(self):
        """Gets the hide_buyer_details of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field is included and set to <code>true</code> if the seller wishes to create a private listing. <br><br> Sellers may want to use this option when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.  # noqa: E501

        :return: The hide_buyer_details of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: bool
        """
        return self._hide_buyer_details

    @hide_buyer_details.setter
    def hide_buyer_details(self, hide_buyer_details):
        """Sets the hide_buyer_details of this EbayOfferDetailsWithKeys.

        This field is included and set to <code>true</code> if the seller wishes to create a private listing. <br><br> Sellers may want to use this option when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users.  # noqa: E501

        :param hide_buyer_details: The hide_buyer_details of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: bool
        """

        self._hide_buyer_details = hide_buyer_details

    @property
    def include_catalog_product_details(self):
        """Gets the include_catalog_product_details of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field indicates whether or not eBay product catalog details are applied to a listing. A value of <code>true</code> indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in <strong>createOrReplaceInventoryItem</strong>.<br/><br/> <strong>Default:</strong> true<p><span class=\"tablenote\"><strong>Note:</strong> Though the <strong>includeCatalogProductDetails</strong> parameter is not required to be submitted in the request, the parameter defaults to <code>true</code> if omitted.</span></p>  # noqa: E501

        :return: The include_catalog_product_details of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: bool
        """
        return self._include_catalog_product_details

    @include_catalog_product_details.setter
    def include_catalog_product_details(self, include_catalog_product_details):
        """Sets the include_catalog_product_details of this EbayOfferDetailsWithKeys.

        This field indicates whether or not eBay product catalog details are applied to a listing. A value of <code>true</code> indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in <strong>createOrReplaceInventoryItem</strong>.<br/><br/> <strong>Default:</strong> true<p><span class=\"tablenote\"><strong>Note:</strong> Though the <strong>includeCatalogProductDetails</strong> parameter is not required to be submitted in the request, the parameter defaults to <code>true</code> if omitted.</span></p>  # noqa: E501

        :param include_catalog_product_details: The include_catalog_product_details of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: bool
        """

        self._include_catalog_product_details = include_catalog_product_details

    @property
    def listing_description(self):
        """Gets the listing_description of this EbayOfferDetailsWithKeys.  # noqa: E501

        The text in this field is (published offers), or will become (unpublished offers) the description of the eBay listing. This field is not immediately required for an unpublished offer, but will be required before publishing the offer. Note that if the <strong>listingDescription</strong> field was omitted in the <strong>createOffer</strong> call for the offer, the offer entity should have picked up the text provided in the <strong>product.description</strong> field of the inventory item record, or if the inventory item is part of a group, the offer entity should have picked up the text provided in the <strong>description</strong> field of the inventory item group record.<br/><br/>HTML tags and markup can be used in listing descriptions, but each character counts toward the max length limit.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's <a href=\"https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html\" target=\"_blank\">View Item description summary feature</a> when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.<br><br> Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.</span><br><br><strong>Max length</strong>: 500000 (which includes HTML markup/tags)  # noqa: E501

        :return: The listing_description of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._listing_description

    @listing_description.setter
    def listing_description(self, listing_description):
        """Sets the listing_description of this EbayOfferDetailsWithKeys.

        The text in this field is (published offers), or will become (unpublished offers) the description of the eBay listing. This field is not immediately required for an unpublished offer, but will be required before publishing the offer. Note that if the <strong>listingDescription</strong> field was omitted in the <strong>createOffer</strong> call for the offer, the offer entity should have picked up the text provided in the <strong>product.description</strong> field of the inventory item record, or if the inventory item is part of a group, the offer entity should have picked up the text provided in the <strong>description</strong> field of the inventory item group record.<br/><br/>HTML tags and markup can be used in listing descriptions, but each character counts toward the max length limit.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's <a href=\"https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html\" target=\"_blank\">View Item description summary feature</a> when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.<br><br> Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.</span><br><br><strong>Max length</strong>: 500000 (which includes HTML markup/tags)  # noqa: E501

        :param listing_description: The listing_description of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._listing_description = listing_description

    @property
    def listing_duration(self):
        """Gets the listing_duration of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field indicates the number of days that the listing will be active. For fixed-price listings, this value must be set to <code>GTC</code>, but auction listings support different listing durations.<br /><br /> The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing.<br /><br /><span class=\"tablenote\"> <strong>Note:</strong> If the listing duration expires for an auction offer without a winning bidder, the listing then becomes available as a fixed-price offer and listing duration will be <code>GTC</code>.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingDurationEnum'>eBay API documentation</a>  # noqa: E501

        :return: The listing_duration of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._listing_duration

    @listing_duration.setter
    def listing_duration(self, listing_duration):
        """Sets the listing_duration of this EbayOfferDetailsWithKeys.

        This field indicates the number of days that the listing will be active. For fixed-price listings, this value must be set to <code>GTC</code>, but auction listings support different listing durations.<br /><br /> The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing.<br /><br /><span class=\"tablenote\"> <strong>Note:</strong> If the listing duration expires for an auction offer without a winning bidder, the listing then becomes available as a fixed-price offer and listing duration will be <code>GTC</code>.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingDurationEnum'>eBay API documentation</a>  # noqa: E501

        :param listing_duration: The listing_duration of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._listing_duration = listing_duration

    @property
    def listing_policies(self):
        """Gets the listing_policies of this EbayOfferDetailsWithKeys.  # noqa: E501


        :return: The listing_policies of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: ListingPolicies
        """
        return self._listing_policies

    @listing_policies.setter
    def listing_policies(self, listing_policies):
        """Sets the listing_policies of this EbayOfferDetailsWithKeys.


        :param listing_policies: The listing_policies of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: ListingPolicies
        """

        self._listing_policies = listing_policies

    @property
    def listing_start_date(self):
        """Gets the listing_start_date of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field can be used if the seller wants to specify a time in the future that the listing will become active on eBay. The timestamp supplied in this field should be in UTC format, and it should be far enough in the future so that the seller will have enought time to publish the listing with the <strong>publishOffer</strong> method.<br><br> This field is optional. If this field is not provided, the listing starts immediately after a successful <strong>publishOffer</strong> method.  # noqa: E501

        :return: The listing_start_date of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._listing_start_date

    @listing_start_date.setter
    def listing_start_date(self, listing_start_date):
        """Sets the listing_start_date of this EbayOfferDetailsWithKeys.

        This field can be used if the seller wants to specify a time in the future that the listing will become active on eBay. The timestamp supplied in this field should be in UTC format, and it should be far enough in the future so that the seller will have enought time to publish the listing with the <strong>publishOffer</strong> method.<br><br> This field is optional. If this field is not provided, the listing starts immediately after a successful <strong>publishOffer</strong> method.  # noqa: E501

        :param listing_start_date: The listing_start_date of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._listing_start_date = listing_start_date

    @property
    def lot_size(self):
        """Gets the lot_size of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field is only applicable if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same item, such as four identical tires being sold as a single offer, or it can be a mixed lot of similar items, such as used clothing items or an assortment of baseball cards. Whether the lot listing involved identical items or a mixed lot, the integer value passed into this field is the total number of items in the lot. Lots can be used for auction and fixed-price listings.  # noqa: E501

        :return: The lot_size of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this EbayOfferDetailsWithKeys.

        This field is only applicable if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same item, such as four identical tires being sold as a single offer, or it can be a mixed lot of similar items, such as used clothing items or an assortment of baseball cards. Whether the lot listing involved identical items or a mixed lot, the integer value passed into this field is the total number of items in the lot. Lots can be used for auction and fixed-price listings.  # noqa: E501

        :param lot_size: The lot_size of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this EbayOfferDetailsWithKeys.  # noqa: E501

        This enumeration value is the unique identifier of the eBay site for which the offer will be made available. See <strong>MarketplaceEnum</strong> for the list of supported enumeration values. This field is required. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this EbayOfferDetailsWithKeys.

        This enumeration value is the unique identifier of the eBay site for which the offer will be made available. See <strong>MarketplaceEnum</strong> for the list of supported enumeration values. This field is required. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def merchant_location_key(self):
        """Gets the merchant_location_key of this EbayOfferDetailsWithKeys.  # noqa: E501

        The unique identifier of a merchant's inventory location (where the inventory item in the offer is located). A <strong>merchantLocationKey</strong> value is established when the merchant creates an inventory location using the <strong>createInventoryLocation</strong> call. To get more information about inventory locations, the <strong>getInventoryLocation</strong> call can be used.<br/><br/>This field is not initially required upon first creating an offer, but will become required before an offer can be published.<br/><br/><b>Max length</b>: 36  # noqa: E501

        :return: The merchant_location_key of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._merchant_location_key

    @merchant_location_key.setter
    def merchant_location_key(self, merchant_location_key):
        """Sets the merchant_location_key of this EbayOfferDetailsWithKeys.

        The unique identifier of a merchant's inventory location (where the inventory item in the offer is located). A <strong>merchantLocationKey</strong> value is established when the merchant creates an inventory location using the <strong>createInventoryLocation</strong> call. To get more information about inventory locations, the <strong>getInventoryLocation</strong> call can be used.<br/><br/>This field is not initially required upon first creating an offer, but will become required before an offer can be published.<br/><br/><b>Max length</b>: 36  # noqa: E501

        :param merchant_location_key: The merchant_location_key of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._merchant_location_key = merchant_location_key

    @property
    def pricing_summary(self):
        """Gets the pricing_summary of this EbayOfferDetailsWithKeys.  # noqa: E501


        :return: The pricing_summary of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: PricingSummary
        """
        return self._pricing_summary

    @pricing_summary.setter
    def pricing_summary(self, pricing_summary):
        """Sets the pricing_summary of this EbayOfferDetailsWithKeys.


        :param pricing_summary: The pricing_summary of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: PricingSummary
        """

        self._pricing_summary = pricing_summary

    @property
    def quantity_limit_per_buyer(self):
        """Gets the quantity_limit_per_buyer of this EbayOfferDetailsWithKeys.  # noqa: E501

        This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity specified for this field. So, if this field's value is <code>5</code>, each buyer may purchase between one to five of these products, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase. <br/>  # noqa: E501

        :return: The quantity_limit_per_buyer of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: int
        """
        return self._quantity_limit_per_buyer

    @quantity_limit_per_buyer.setter
    def quantity_limit_per_buyer(self, quantity_limit_per_buyer):
        """Sets the quantity_limit_per_buyer of this EbayOfferDetailsWithKeys.

        This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity specified for this field. So, if this field's value is <code>5</code>, each buyer may purchase between one to five of these products, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase. <br/>  # noqa: E501

        :param quantity_limit_per_buyer: The quantity_limit_per_buyer of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: int
        """

        self._quantity_limit_per_buyer = quantity_limit_per_buyer

    @property
    def secondary_category_id(self):
        """Gets the secondary_category_id of this EbayOfferDetailsWithKeys.  # noqa: E501

        The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions\" target=\"_blank\">getCategorySuggestions</a> method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing. <br/><br/><span class=\"tablenote\"><strong>Note:</strong> You cannot list <strong>US eBay Motors</strong> vehicles in two categories. However, you can list <strong>Parts & Accessories</strong> in two categories.</span>  # noqa: E501

        :return: The secondary_category_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._secondary_category_id

    @secondary_category_id.setter
    def secondary_category_id(self, secondary_category_id):
        """Sets the secondary_category_id of this EbayOfferDetailsWithKeys.

        The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the <a href=\"/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions\" target=\"_blank\">getCategorySuggestions</a> method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing. <br/><br/><span class=\"tablenote\"><strong>Note:</strong> You cannot list <strong>US eBay Motors</strong> vehicles in two categories. However, you can list <strong>Parts & Accessories</strong> in two categories.</span>  # noqa: E501

        :param secondary_category_id: The secondary_category_id of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._secondary_category_id = secondary_category_id

    @property
    def sku(self):
        """Gets the sku of this EbayOfferDetailsWithKeys.  # noqa: E501

        This is the seller-defined SKU value of the product that will be listed on the eBay site (specified in the <strong>marketplaceId</strong> field). Only one offer (in unpublished or published state) may exist for each <strong>sku</strong>/<strong>marketplaceId</strong>/<strong>format</strong> combination. This field is required.<br/><br/><strong>Max Length</strong>: 50<br/>  # noqa: E501

        :return: The sku of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this EbayOfferDetailsWithKeys.

        This is the seller-defined SKU value of the product that will be listed on the eBay site (specified in the <strong>marketplaceId</strong> field). Only one offer (in unpublished or published state) may exist for each <strong>sku</strong>/<strong>marketplaceId</strong>/<strong>format</strong> combination. This field is required.<br/><br/><strong>Max Length</strong>: 50<br/>  # noqa: E501

        :param sku: The sku of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def store_category_names(self):
        """Gets the store_category_names of this EbayOfferDetailsWithKeys.  # noqa: E501

        This container is used if the seller would like to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) passed in to this container will be the full path(s) to the eBay store categories, as shown below:<br> <pre><code>\"storeCategoryNames\": [<br/> \"/Fashion/Men/Shirts\", <br/> \"/Fashion/Men/Accessories\" ], </pre></code>  # noqa: E501

        :return: The store_category_names of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: list[str]
        """
        return self._store_category_names

    @store_category_names.setter
    def store_category_names(self, store_category_names):
        """Sets the store_category_names of this EbayOfferDetailsWithKeys.

        This container is used if the seller would like to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) passed in to this container will be the full path(s) to the eBay store categories, as shown below:<br> <pre><code>\"storeCategoryNames\": [<br/> \"/Fashion/Men/Shirts\", <br/> \"/Fashion/Men/Accessories\" ], </pre></code>  # noqa: E501

        :param store_category_names: The store_category_names of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: list[str]
        """

        self._store_category_names = store_category_names

    @property
    def tax(self):
        """Gets the tax of this EbayOfferDetailsWithKeys.  # noqa: E501


        :return: The tax of this EbayOfferDetailsWithKeys.  # noqa: E501
        :rtype: Tax
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this EbayOfferDetailsWithKeys.


        :param tax: The tax of this EbayOfferDetailsWithKeys.  # noqa: E501
        :type: Tax
        """

        self._tax = tax

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
        if issubclass(EbayOfferDetailsWithKeys, dict):
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
        if not isinstance(other, EbayOfferDetailsWithKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
