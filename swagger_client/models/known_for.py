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

class KnownFor(object):
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
        'id': 'str',
        'title': 'str',
        'full_title': 'str',
        'year': 'str',
        'role': 'str',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'full_title': 'fullTitle',
        'year': 'year',
        'role': 'role',
        'image': 'image'
    }

    def __init__(self, id=None, title=None, full_title=None, year=None, role=None, image=None):  # noqa: E501
        """KnownFor - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._full_title = None
        self._year = None
        self._role = None
        self._image = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if full_title is not None:
            self.full_title = full_title
        if year is not None:
            self.year = year
        if role is not None:
            self.role = role
        if image is not None:
            self.image = image

    @property
    def id(self):
        """Gets the id of this KnownFor.  # noqa: E501


        :return: The id of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KnownFor.


        :param id: The id of this KnownFor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this KnownFor.  # noqa: E501


        :return: The title of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this KnownFor.


        :param title: The title of this KnownFor.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_title(self):
        """Gets the full_title of this KnownFor.  # noqa: E501


        :return: The full_title of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this KnownFor.


        :param full_title: The full_title of this KnownFor.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def year(self):
        """Gets the year of this KnownFor.  # noqa: E501


        :return: The year of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this KnownFor.


        :param year: The year of this KnownFor.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def role(self):
        """Gets the role of this KnownFor.  # noqa: E501


        :return: The role of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this KnownFor.


        :param role: The role of this KnownFor.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def image(self):
        """Gets the image of this KnownFor.  # noqa: E501


        :return: The image of this KnownFor.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this KnownFor.


        :param image: The image of this KnownFor.  # noqa: E501
        :type: str
        """

        self._image = image

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
        if issubclass(KnownFor, dict):
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
        if not isinstance(other, KnownFor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
