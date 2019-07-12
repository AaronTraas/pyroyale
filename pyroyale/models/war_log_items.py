# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from pyroyale.models.war_participant import WarParticipant  # noqa: F401,E501
from pyroyale.models.war_standing import WarStanding  # noqa: F401,E501


class WarLogItems(object):
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
        'season_id': 'int',
        'created_date': 'str',
        'participants': 'list[WarParticipant]',
        'standings': 'list[WarStanding]'
    }

    attribute_map = {
        'season_id': 'seasonId',
        'created_date': 'createdDate',
        'participants': 'participants',
        'standings': 'standings'
    }

    def __init__(self, season_id=None, created_date=None, participants=None, standings=None):  # noqa: E501
        """WarLogItems - a model defined in Swagger"""  # noqa: E501
        self._season_id = None
        self._created_date = None
        self._participants = None
        self._standings = None
        self.discriminator = None
        if season_id is not None:
            self.season_id = season_id
        if created_date is not None:
            self.created_date = created_date
        if participants is not None:
            self.participants = participants
        if standings is not None:
            self.standings = standings

    @property
    def season_id(self):
        """Gets the season_id of this WarLogItems.  # noqa: E501


        :return: The season_id of this WarLogItems.  # noqa: E501
        :rtype: int
        """
        return self._season_id

    @season_id.setter
    def season_id(self, season_id):
        """Sets the season_id of this WarLogItems.


        :param season_id: The season_id of this WarLogItems.  # noqa: E501
        :type: int
        """

        self._season_id = season_id

    @property
    def created_date(self):
        """Gets the created_date of this WarLogItems.  # noqa: E501


        :return: The created_date of this WarLogItems.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this WarLogItems.


        :param created_date: The created_date of this WarLogItems.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def participants(self):
        """Gets the participants of this WarLogItems.  # noqa: E501


        :return: The participants of this WarLogItems.  # noqa: E501
        :rtype: list[WarParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this WarLogItems.


        :param participants: The participants of this WarLogItems.  # noqa: E501
        :type: list[WarParticipant]
        """

        self._participants = participants

    @property
    def standings(self):
        """Gets the standings of this WarLogItems.  # noqa: E501


        :return: The standings of this WarLogItems.  # noqa: E501
        :rtype: list[WarStanding]
        """
        return self._standings

    @standings.setter
    def standings(self, standings):
        """Sets the standings of this WarLogItems.


        :param standings: The standings of this WarLogItems.  # noqa: E501
        :type: list[WarStanding]
        """

        self._standings = standings

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
        if issubclass(WarLogItems, dict):
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
        if not isinstance(other, WarLogItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
