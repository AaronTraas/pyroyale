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


class WarParticipant(object):
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
        'tag': 'str',
        'name': 'str',
        'cards_earned': 'int',
        'battles_played': 'int',
        'collection_day_battles_played': 'int',
        'wins': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'cards_earned': 'cardsEarned',
        'battles_played': 'battlesPlayed',
        'collection_day_battles_played': 'collectionDayBattlesPlayed',
        'wins': 'wins'
    }

    def __init__(self, tag=None, name=None, cards_earned=None, battles_played=None, collection_day_battles_played=None, wins=None):  # noqa: E501
        """WarParticipant - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._cards_earned = None
        self._battles_played = None
        self._collection_day_battles_played = None
        self._wins = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if cards_earned is not None:
            self.cards_earned = cards_earned
        if battles_played is not None:
            self.battles_played = battles_played
        if collection_day_battles_played is not None:
            self.collection_day_battles_played = collection_day_battles_played
        if wins is not None:
            self.wins = wins

    @property
    def tag(self):
        """Gets the tag of this WarParticipant.  # noqa: E501


        :return: The tag of this WarParticipant.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this WarParticipant.


        :param tag: The tag of this WarParticipant.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this WarParticipant.  # noqa: E501


        :return: The name of this WarParticipant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WarParticipant.


        :param name: The name of this WarParticipant.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cards_earned(self):
        """Gets the cards_earned of this WarParticipant.  # noqa: E501


        :return: The cards_earned of this WarParticipant.  # noqa: E501
        :rtype: int
        """
        return self._cards_earned

    @cards_earned.setter
    def cards_earned(self, cards_earned):
        """Sets the cards_earned of this WarParticipant.


        :param cards_earned: The cards_earned of this WarParticipant.  # noqa: E501
        :type: int
        """

        self._cards_earned = cards_earned

    @property
    def battles_played(self):
        """Gets the battles_played of this WarParticipant.  # noqa: E501


        :return: The battles_played of this WarParticipant.  # noqa: E501
        :rtype: int
        """
        return self._battles_played

    @battles_played.setter
    def battles_played(self, battles_played):
        """Sets the battles_played of this WarParticipant.


        :param battles_played: The battles_played of this WarParticipant.  # noqa: E501
        :type: int
        """

        self._battles_played = battles_played

    @property
    def collection_day_battles_played(self):
        """Gets the collection_day_battles_played of this WarParticipant.  # noqa: E501


        :return: The collection_day_battles_played of this WarParticipant.  # noqa: E501
        :rtype: int
        """
        return self._collection_day_battles_played

    @collection_day_battles_played.setter
    def collection_day_battles_played(self, collection_day_battles_played):
        """Sets the collection_day_battles_played of this WarParticipant.


        :param collection_day_battles_played: The collection_day_battles_played of this WarParticipant.  # noqa: E501
        :type: int
        """

        self._collection_day_battles_played = collection_day_battles_played

    @property
    def wins(self):
        """Gets the wins of this WarParticipant.  # noqa: E501


        :return: The wins of this WarParticipant.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this WarParticipant.


        :param wins: The wins of this WarParticipant.  # noqa: E501
        :type: int
        """

        self._wins = wins

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
        if issubclass(WarParticipant, dict):
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
        if not isinstance(other, WarParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
