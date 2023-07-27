# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TvSeriesInfo(object):
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
        'year_end': 'str',
        'creators': 'str',
        'creator_list': 'list[StarShort]',
        'seasons': 'list[str]'
    }

    attribute_map = {
        'year_end': 'yearEnd',
        'creators': 'creators',
        'creator_list': 'creatorList',
        'seasons': 'seasons'
    }

    def __init__(self, year_end=None, creators=None, creator_list=None, seasons=None):  # noqa: E501
        """TvSeriesInfo - a model defined in Swagger"""  # noqa: E501
        self._year_end = None
        self._creators = None
        self._creator_list = None
        self._seasons = None
        self.discriminator = None
        if year_end is not None:
            self.year_end = year_end
        if creators is not None:
            self.creators = creators
        if creator_list is not None:
            self.creator_list = creator_list
        if seasons is not None:
            self.seasons = seasons

    @property
    def year_end(self):
        """Gets the year_end of this TvSeriesInfo.  # noqa: E501


        :return: The year_end of this TvSeriesInfo.  # noqa: E501
        :rtype: str
        """
        return self._year_end

    @year_end.setter
    def year_end(self, year_end):
        """Sets the year_end of this TvSeriesInfo.


        :param year_end: The year_end of this TvSeriesInfo.  # noqa: E501
        :type: str
        """

        self._year_end = year_end

    @property
    def creators(self):
        """Gets the creators of this TvSeriesInfo.  # noqa: E501


        :return: The creators of this TvSeriesInfo.  # noqa: E501
        :rtype: str
        """
        return self._creators

    @creators.setter
    def creators(self, creators):
        """Sets the creators of this TvSeriesInfo.


        :param creators: The creators of this TvSeriesInfo.  # noqa: E501
        :type: str
        """

        self._creators = creators

    @property
    def creator_list(self):
        """Gets the creator_list of this TvSeriesInfo.  # noqa: E501


        :return: The creator_list of this TvSeriesInfo.  # noqa: E501
        :rtype: list[StarShort]
        """
        return self._creator_list

    @creator_list.setter
    def creator_list(self, creator_list):
        """Sets the creator_list of this TvSeriesInfo.


        :param creator_list: The creator_list of this TvSeriesInfo.  # noqa: E501
        :type: list[StarShort]
        """

        self._creator_list = creator_list

    @property
    def seasons(self):
        """Gets the seasons of this TvSeriesInfo.  # noqa: E501


        :return: The seasons of this TvSeriesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this TvSeriesInfo.


        :param seasons: The seasons of this TvSeriesInfo.  # noqa: E501
        :type: list[str]
        """

        self._seasons = seasons

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
        if issubclass(TvSeriesInfo, dict):
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
        if not isinstance(other, TvSeriesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
