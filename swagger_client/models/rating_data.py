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

class RatingData(object):
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
        'im_db_id': 'str',
        'title': 'str',
        'full_title': 'str',
        'type': 'str',
        'year': 'str',
        'im_db': 'str',
        'metacritic': 'str',
        'the_movie_db': 'str',
        'rotten_tomatoes': 'str',
        'film_affinity': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'im_db_id': 'imDbId',
        'title': 'title',
        'full_title': 'fullTitle',
        'type': 'type',
        'year': 'year',
        'im_db': 'imDb',
        'metacritic': 'metacritic',
        'the_movie_db': 'theMovieDb',
        'rotten_tomatoes': 'rottenTomatoes',
        'film_affinity': 'filmAffinity',
        'error_message': 'errorMessage'
    }

    def __init__(self, im_db_id=None, title=None, full_title=None, type=None, year=None, im_db=None, metacritic=None, the_movie_db=None, rotten_tomatoes=None, film_affinity=None, error_message=None):  # noqa: E501
        """RatingData - a model defined in Swagger"""  # noqa: E501
        self._im_db_id = None
        self._title = None
        self._full_title = None
        self._type = None
        self._year = None
        self._im_db = None
        self._metacritic = None
        self._the_movie_db = None
        self._rotten_tomatoes = None
        self._film_affinity = None
        self._error_message = None
        self.discriminator = None
        if im_db_id is not None:
            self.im_db_id = im_db_id
        if title is not None:
            self.title = title
        if full_title is not None:
            self.full_title = full_title
        if type is not None:
            self.type = type
        if year is not None:
            self.year = year
        if im_db is not None:
            self.im_db = im_db
        if metacritic is not None:
            self.metacritic = metacritic
        if the_movie_db is not None:
            self.the_movie_db = the_movie_db
        if rotten_tomatoes is not None:
            self.rotten_tomatoes = rotten_tomatoes
        if film_affinity is not None:
            self.film_affinity = film_affinity
        if error_message is not None:
            self.error_message = error_message

    @property
    def im_db_id(self):
        """Gets the im_db_id of this RatingData.  # noqa: E501


        :return: The im_db_id of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._im_db_id

    @im_db_id.setter
    def im_db_id(self, im_db_id):
        """Sets the im_db_id of this RatingData.


        :param im_db_id: The im_db_id of this RatingData.  # noqa: E501
        :type: str
        """

        self._im_db_id = im_db_id

    @property
    def title(self):
        """Gets the title of this RatingData.  # noqa: E501


        :return: The title of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RatingData.


        :param title: The title of this RatingData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_title(self):
        """Gets the full_title of this RatingData.  # noqa: E501


        :return: The full_title of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this RatingData.


        :param full_title: The full_title of this RatingData.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def type(self):
        """Gets the type of this RatingData.  # noqa: E501


        :return: The type of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RatingData.


        :param type: The type of this RatingData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def year(self):
        """Gets the year of this RatingData.  # noqa: E501


        :return: The year of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this RatingData.


        :param year: The year of this RatingData.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def im_db(self):
        """Gets the im_db of this RatingData.  # noqa: E501


        :return: The im_db of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._im_db

    @im_db.setter
    def im_db(self, im_db):
        """Sets the im_db of this RatingData.


        :param im_db: The im_db of this RatingData.  # noqa: E501
        :type: str
        """

        self._im_db = im_db

    @property
    def metacritic(self):
        """Gets the metacritic of this RatingData.  # noqa: E501


        :return: The metacritic of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._metacritic

    @metacritic.setter
    def metacritic(self, metacritic):
        """Sets the metacritic of this RatingData.


        :param metacritic: The metacritic of this RatingData.  # noqa: E501
        :type: str
        """

        self._metacritic = metacritic

    @property
    def the_movie_db(self):
        """Gets the the_movie_db of this RatingData.  # noqa: E501


        :return: The the_movie_db of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._the_movie_db

    @the_movie_db.setter
    def the_movie_db(self, the_movie_db):
        """Sets the the_movie_db of this RatingData.


        :param the_movie_db: The the_movie_db of this RatingData.  # noqa: E501
        :type: str
        """

        self._the_movie_db = the_movie_db

    @property
    def rotten_tomatoes(self):
        """Gets the rotten_tomatoes of this RatingData.  # noqa: E501


        :return: The rotten_tomatoes of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._rotten_tomatoes

    @rotten_tomatoes.setter
    def rotten_tomatoes(self, rotten_tomatoes):
        """Sets the rotten_tomatoes of this RatingData.


        :param rotten_tomatoes: The rotten_tomatoes of this RatingData.  # noqa: E501
        :type: str
        """

        self._rotten_tomatoes = rotten_tomatoes

    @property
    def film_affinity(self):
        """Gets the film_affinity of this RatingData.  # noqa: E501


        :return: The film_affinity of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._film_affinity

    @film_affinity.setter
    def film_affinity(self, film_affinity):
        """Sets the film_affinity of this RatingData.


        :param film_affinity: The film_affinity of this RatingData.  # noqa: E501
        :type: str
        """

        self._film_affinity = film_affinity

    @property
    def error_message(self):
        """Gets the error_message of this RatingData.  # noqa: E501


        :return: The error_message of this RatingData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this RatingData.


        :param error_message: The error_message of this RatingData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(RatingData, dict):
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
        if not isinstance(other, RatingData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other