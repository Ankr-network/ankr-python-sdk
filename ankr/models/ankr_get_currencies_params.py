# coding: utf-8

"""
    Ankr Advanced API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnkrGetCurrenciesParams(object):
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
        'blockchain': 'str',
        'sync_check': 'bool'
    }

    attribute_map = {
        'blockchain': 'blockchain',
        'sync_check': 'syncCheck'
    }

    def __init__(self, blockchain=None, sync_check=None):  # noqa: E501
        """AnkrGetCurrenciesParams - a model defined in Swagger"""  # noqa: E501
        self._blockchain = None
        self._sync_check = None
        self.discriminator = None
        self.blockchain = blockchain
        if sync_check is not None:
            self.sync_check = sync_check

    @property
    def blockchain(self):
        """Gets the blockchain of this AnkrGetCurrenciesParams.  # noqa: E501

        Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai.  # noqa: E501

        :return: The blockchain of this AnkrGetCurrenciesParams.  # noqa: E501
        :rtype: str
        """
        return self._blockchain

    @blockchain.setter
    def blockchain(self, blockchain):
        """Sets the blockchain of this AnkrGetCurrenciesParams.

        Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai.  # noqa: E501

        :param blockchain: The blockchain of this AnkrGetCurrenciesParams.  # noqa: E501
        :type: str
        """
        if blockchain is None:
            raise ValueError("Invalid value for `blockchain`, must not be `None`")  # noqa: E501
        allowed_values = ["arbitrum", "avalanche", "avalanche_fuji", "base", "bsc", "eth", "eth_goerli", "fantom", "flare", "gnosis", "linea", "optimism", "optimism_testnet", "polygon", "polygon_mumbai", "polygon_zkevm", "rollux", "scroll", "syscoin"]  # noqa: E501
        if blockchain not in allowed_values:
            raise ValueError(
                "Invalid value for `blockchain` ({0}), must be one of {1}"  # noqa: E501
                .format(blockchain, allowed_values)
            )

        self._blockchain = blockchain

    @property
    def sync_check(self):
        """Gets the sync_check of this AnkrGetCurrenciesParams.  # noqa: E501

        If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive.  # noqa: E501

        :return: The sync_check of this AnkrGetCurrenciesParams.  # noqa: E501
        :rtype: bool
        """
        return self._sync_check

    @sync_check.setter
    def sync_check(self, sync_check):
        """Sets the sync_check of this AnkrGetCurrenciesParams.

        If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive.  # noqa: E501

        :param sync_check: The sync_check of this AnkrGetCurrenciesParams.  # noqa: E501
        :type: bool
        """

        self._sync_check = sync_check

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
        if issubclass(AnkrGetCurrenciesParams, dict):
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
        if not isinstance(other, AnkrGetCurrenciesParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
