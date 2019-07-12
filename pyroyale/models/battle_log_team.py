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
from pyroyale.models.card_list import CardList  # noqa: F401,E501
from pyroyale.models.clan_base import ClanBase  # noqa: F401,E501


class BattleLogTeam(object):
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
        'starting_trophies': 'int',
        'trophy_change': 'int',
        'crowns': 'int',
        'clan': 'ClanBase',
        'cards': 'CardList'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'starting_trophies': 'startingTrophies',
        'trophy_change': 'trophyChange',
        'crowns': 'crowns',
        'clan': 'clan',
        'cards': 'cards'
    }

    def __init__(self, tag=None, name=None, starting_trophies=None, trophy_change=None, crowns=None, clan=None, cards=None):  # noqa: E501
        """BattleLogTeam - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._starting_trophies = None
        self._trophy_change = None
        self._crowns = None
        self._clan = None
        self._cards = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if starting_trophies is not None:
            self.starting_trophies = starting_trophies
        if trophy_change is not None:
            self.trophy_change = trophy_change
        if crowns is not None:
            self.crowns = crowns
        if clan is not None:
            self.clan = clan
        if cards is not None:
            self.cards = cards

    @property
    def tag(self):
        """Gets the tag of this BattleLogTeam.  # noqa: E501


        :return: The tag of this BattleLogTeam.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BattleLogTeam.


        :param tag: The tag of this BattleLogTeam.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this BattleLogTeam.  # noqa: E501


        :return: The name of this BattleLogTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BattleLogTeam.


        :param name: The name of this BattleLogTeam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def starting_trophies(self):
        """Gets the starting_trophies of this BattleLogTeam.  # noqa: E501


        :return: The starting_trophies of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._starting_trophies

    @starting_trophies.setter
    def starting_trophies(self, starting_trophies):
        """Sets the starting_trophies of this BattleLogTeam.


        :param starting_trophies: The starting_trophies of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._starting_trophies = starting_trophies

    @property
    def trophy_change(self):
        """Gets the trophy_change of this BattleLogTeam.  # noqa: E501


        :return: The trophy_change of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._trophy_change

    @trophy_change.setter
    def trophy_change(self, trophy_change):
        """Sets the trophy_change of this BattleLogTeam.


        :param trophy_change: The trophy_change of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._trophy_change = trophy_change

    @property
    def crowns(self):
        """Gets the crowns of this BattleLogTeam.  # noqa: E501


        :return: The crowns of this BattleLogTeam.  # noqa: E501
        :rtype: int
        """
        return self._crowns

    @crowns.setter
    def crowns(self, crowns):
        """Sets the crowns of this BattleLogTeam.


        :param crowns: The crowns of this BattleLogTeam.  # noqa: E501
        :type: int
        """

        self._crowns = crowns

    @property
    def clan(self):
        """Gets the clan of this BattleLogTeam.  # noqa: E501


        :return: The clan of this BattleLogTeam.  # noqa: E501
        :rtype: ClanBase
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this BattleLogTeam.


        :param clan: The clan of this BattleLogTeam.  # noqa: E501
        :type: ClanBase
        """

        self._clan = clan

    @property
    def cards(self):
        """Gets the cards of this BattleLogTeam.  # noqa: E501


        :return: The cards of this BattleLogTeam.  # noqa: E501
        :rtype: CardList
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this BattleLogTeam.


        :param cards: The cards of this BattleLogTeam.  # noqa: E501
        :type: CardList
        """

        self._cards = cards

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
        if issubclass(BattleLogTeam, dict):
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
        if not isinstance(other, BattleLogTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
