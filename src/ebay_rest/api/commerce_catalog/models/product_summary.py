# coding: utf-8

"""
    Catalog API

    The Catalog API allows users to search for and locate an eBay catalog product that is a direct match for the product that they wish to sell. Listing against an eBay catalog product helps insure that all listings (based off of that catalog product) have complete and accurate information. In addition to helping to create high-quality listings, another benefit to the seller of using catalog information to create listings is that much of the details of the listing will be prefilled, including the listing title, the listing description, the item specifics, and a stock image for the product (if available). Sellers will not have to enter item specifics themselves, and the overall listing process is a lot faster and easier.  # noqa: E501

    OpenAPI spec version: v1_beta.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductSummary(object):
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
        'additional_images': 'list[Image]',
        'aspects': 'list[Aspect]',
        'brand': 'str',
        'ean': 'list[str]',
        'epid': 'str',
        'gtin': 'list[str]',
        'image': 'Image',
        'isbn': 'list[str]',
        'mpn': 'list[str]',
        'product_href': 'str',
        'product_web_url': 'str',
        'title': 'str',
        'upc': 'list[str]'
    }

    attribute_map = {
        'additional_images': 'additionalImages',
        'aspects': 'aspects',
        'brand': 'brand',
        'ean': 'ean',
        'epid': 'epid',
        'gtin': 'gtin',
        'image': 'image',
        'isbn': 'isbn',
        'mpn': 'mpn',
        'product_href': 'productHref',
        'product_web_url': 'productWebUrl',
        'title': 'title',
        'upc': 'upc'
    }

    def __init__(self, additional_images=None, aspects=None, brand=None, ean=None, epid=None, gtin=None, image=None, isbn=None, mpn=None, product_href=None, product_web_url=None, title=None, upc=None):  # noqa: E501
        """ProductSummary - a model defined in Swagger"""  # noqa: E501
        self._additional_images = None
        self._aspects = None
        self._brand = None
        self._ean = None
        self._epid = None
        self._gtin = None
        self._image = None
        self._isbn = None
        self._mpn = None
        self._product_href = None
        self._product_web_url = None
        self._title = None
        self._upc = None
        self.discriminator = None
        if additional_images is not None:
            self.additional_images = additional_images
        if aspects is not None:
            self.aspects = aspects
        if brand is not None:
            self.brand = brand
        if ean is not None:
            self.ean = ean
        if epid is not None:
            self.epid = epid
        if gtin is not None:
            self.gtin = gtin
        if image is not None:
            self.image = image
        if isbn is not None:
            self.isbn = isbn
        if mpn is not None:
            self.mpn = mpn
        if product_href is not None:
            self.product_href = product_href
        if product_web_url is not None:
            self.product_web_url = product_web_url
        if title is not None:
            self.title = title
        if upc is not None:
            self.upc = upc

    @property
    def additional_images(self):
        """Gets the additional_images of this ProductSummary.  # noqa: E501

        Contains information about additional images associated with this product. For the primary image, see the <b>image</b> container.  # noqa: E501

        :return: The additional_images of this ProductSummary.  # noqa: E501
        :rtype: list[Image]
        """
        return self._additional_images

    @additional_images.setter
    def additional_images(self, additional_images):
        """Sets the additional_images of this ProductSummary.

        Contains information about additional images associated with this product. For the primary image, see the <b>image</b> container.  # noqa: E501

        :param additional_images: The additional_images of this ProductSummary.  # noqa: E501
        :type: list[Image]
        """

        self._additional_images = additional_images

    @property
    def aspects(self):
        """Gets the aspects of this ProductSummary.  # noqa: E501

        Contains an array of the category aspects and their values that are associated with this product.  # noqa: E501

        :return: The aspects of this ProductSummary.  # noqa: E501
        :rtype: list[Aspect]
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """Sets the aspects of this ProductSummary.

        Contains an array of the category aspects and their values that are associated with this product.  # noqa: E501

        :param aspects: The aspects of this ProductSummary.  # noqa: E501
        :type: list[Aspect]
        """

        self._aspects = aspects

    @property
    def brand(self):
        """Gets the brand of this ProductSummary.  # noqa: E501

        The manufacturer's brand name for this product.  # noqa: E501

        :return: The brand of this ProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this ProductSummary.

        The manufacturer's brand name for this product.  # noqa: E501

        :param brand: The brand of this ProductSummary.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def ean(self):
        """Gets the ean of this ProductSummary.  # noqa: E501

        A list of all European Article Numbers (EANs) that identify this product.  # noqa: E501

        :return: The ean of this ProductSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this ProductSummary.

        A list of all European Article Numbers (EANs) that identify this product.  # noqa: E501

        :param ean: The ean of this ProductSummary.  # noqa: E501
        :type: list[str]
        """

        self._ean = ean

    @property
    def epid(self):
        """Gets the epid of this ProductSummary.  # noqa: E501

        The eBay product ID of this product.  # noqa: E501

        :return: The epid of this ProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._epid

    @epid.setter
    def epid(self, epid):
        """Sets the epid of this ProductSummary.

        The eBay product ID of this product.  # noqa: E501

        :param epid: The epid of this ProductSummary.  # noqa: E501
        :type: str
        """

        self._epid = epid

    @property
    def gtin(self):
        """Gets the gtin of this ProductSummary.  # noqa: E501

        A list of all GTINs that identify this product. This includes all of the values returned in the <b>ean</b>, <b>isbn</b>, and <b>upc</b> fields.  # noqa: E501

        :return: The gtin of this ProductSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this ProductSummary.

        A list of all GTINs that identify this product. This includes all of the values returned in the <b>ean</b>, <b>isbn</b>, and <b>upc</b> fields.  # noqa: E501

        :param gtin: The gtin of this ProductSummary.  # noqa: E501
        :type: list[str]
        """

        self._gtin = gtin

    @property
    def image(self):
        """Gets the image of this ProductSummary.  # noqa: E501


        :return: The image of this ProductSummary.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ProductSummary.


        :param image: The image of this ProductSummary.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def isbn(self):
        """Gets the isbn of this ProductSummary.  # noqa: E501

        A list of all International Standard Book Numbers (ISBNs) that identify this product.  # noqa: E501

        :return: The isbn of this ProductSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this ProductSummary.

        A list of all International Standard Book Numbers (ISBNs) that identify this product.  # noqa: E501

        :param isbn: The isbn of this ProductSummary.  # noqa: E501
        :type: list[str]
        """

        self._isbn = isbn

    @property
    def mpn(self):
        """Gets the mpn of this ProductSummary.  # noqa: E501

        A list of all Manufacturer Product Number (MPN) values that the manufacturer uses to identify this product.  # noqa: E501

        :return: The mpn of this ProductSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._mpn

    @mpn.setter
    def mpn(self, mpn):
        """Sets the mpn of this ProductSummary.

        A list of all Manufacturer Product Number (MPN) values that the manufacturer uses to identify this product.  # noqa: E501

        :param mpn: The mpn of this ProductSummary.  # noqa: E501
        :type: list[str]
        """

        self._mpn = mpn

    @property
    def product_href(self):
        """Gets the product_href of this ProductSummary.  # noqa: E501

        The URI of the <b>getProduct</b> call request that retrieves this product's details.  # noqa: E501

        :return: The product_href of this ProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._product_href

    @product_href.setter
    def product_href(self, product_href):
        """Sets the product_href of this ProductSummary.

        The URI of the <b>getProduct</b> call request that retrieves this product's details.  # noqa: E501

        :param product_href: The product_href of this ProductSummary.  # noqa: E501
        :type: str
        """

        self._product_href = product_href

    @property
    def product_web_url(self):
        """Gets the product_web_url of this ProductSummary.  # noqa: E501

        The URL for this product's eBay product page.  # noqa: E501

        :return: The product_web_url of this ProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._product_web_url

    @product_web_url.setter
    def product_web_url(self, product_web_url):
        """Sets the product_web_url of this ProductSummary.

        The URL for this product's eBay product page.  # noqa: E501

        :param product_web_url: The product_web_url of this ProductSummary.  # noqa: E501
        :type: str
        """

        self._product_web_url = product_web_url

    @property
    def title(self):
        """Gets the title of this ProductSummary.  # noqa: E501

        The title of this product on eBay.  # noqa: E501

        :return: The title of this ProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProductSummary.

        The title of this product on eBay.  # noqa: E501

        :param title: The title of this ProductSummary.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def upc(self):
        """Gets the upc of this ProductSummary.  # noqa: E501

        A list of Universal Product Codes (UPCs) that identify this product.  # noqa: E501

        :return: The upc of this ProductSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this ProductSummary.

        A list of Universal Product Codes (UPCs) that identify this product.  # noqa: E501

        :param upc: The upc of this ProductSummary.  # noqa: E501
        :type: list[str]
        """

        self._upc = upc

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
        if issubclass(ProductSummary, dict):
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
        if not isinstance(other, ProductSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
