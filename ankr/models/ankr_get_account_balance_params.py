# coding: utf-8

"""
    Ankr Advanced API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnkrGetAccountBalanceParams(object):
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
        'blockchain': 'list[str]',
        'native_first': 'bool',
        'only_whitelisted': 'bool',
        'page_size': 'int',
        'page_token': 'str',
        'sync_check': 'bool',
        'wallet_address': 'str'
    }

    attribute_map = {
        'blockchain': 'blockchain',
        'native_first': 'nativeFirst',
        'only_whitelisted': 'onlyWhitelisted',
        'page_size': 'pageSize',
        'page_token': 'pageToken',
        'sync_check': 'syncCheck',
        'wallet_address': 'walletAddress'
    }

    def __init__(self, blockchain=None, native_first=None, only_whitelisted=None, page_size=None, page_token=None, sync_check=None, wallet_address=None):  # noqa: E501
        """AnkrGetAccountBalanceParams - a model defined in Swagger"""  # noqa: E501
        self._blockchain = None
        self._native_first = None
        self._only_whitelisted = None
        self._page_size = None
        self._page_token = None
        self._sync_check = None
        self._wallet_address = None
        self.discriminator = None
        if blockchain is not None:
            self.blockchain = blockchain
        if native_first is not None:
            self.native_first = native_first
        if only_whitelisted is not None:
            self.only_whitelisted = only_whitelisted
        if page_size is not None:
            self.page_size = page_size
        if page_token is not None:
            self.page_token = page_token
        if sync_check is not None:
            self.sync_check = sync_check
        self.wallet_address = wallet_address

    @property
    def blockchain(self):
        """Gets the blockchain of this AnkrGetAccountBalanceParams.  # noqa: E501

        Name of the blockchain or list of blockchain names. Single: eth. Multiple: [arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai.]. All chains: empty value.  # noqa: E501

        :return: The blockchain of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._blockchain

    @blockchain.setter
    def blockchain(self, blockchain):
        """Sets the blockchain of this AnkrGetAccountBalanceParams.

        Name of the blockchain or list of blockchain names. Single: eth. Multiple: [arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai.]. All chains: empty value.  # noqa: E501

        :param blockchain: The blockchain of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: list[str]
        """

        self._blockchain = blockchain

    @property
    def native_first(self):
        """Gets the native_first of this AnkrGetAccountBalanceParams.  # noqa: E501

        Sorting order. Native network token first (true) or not (false).  # noqa: E501

        :return: The native_first of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: bool
        """
        return self._native_first

    @native_first.setter
    def native_first(self, native_first):
        """Sets the native_first of this AnkrGetAccountBalanceParams.

        Sorting order. Native network token first (true) or not (false).  # noqa: E501

        :param native_first: The native_first of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: bool
        """

        self._native_first = native_first

    @property
    def only_whitelisted(self):
        """Gets the only_whitelisted of this AnkrGetAccountBalanceParams.  # noqa: E501

        Filtering. Only show tokens listed on CoinGekko (true) or all the tokens (false). Default — true.  # noqa: E501

        :return: The only_whitelisted of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: bool
        """
        return self._only_whitelisted

    @only_whitelisted.setter
    def only_whitelisted(self, only_whitelisted):
        """Sets the only_whitelisted of this AnkrGetAccountBalanceParams.

        Filtering. Only show tokens listed on CoinGekko (true) or all the tokens (false). Default — true.  # noqa: E501

        :param only_whitelisted: The only_whitelisted of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: bool
        """

        self._only_whitelisted = only_whitelisted

    @property
    def page_size(self):
        """Gets the page_size of this AnkrGetAccountBalanceParams.  # noqa: E501

        Number of entries per page. int32. Max value — all, default value — all.  # noqa: E501

        :return: The page_size of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AnkrGetAccountBalanceParams.

        Number of entries per page. int32. Max value — all, default value — all.  # noqa: E501

        :param page_size: The page_size of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_token(self):
        """Gets the page_token of this AnkrGetAccountBalanceParams.  # noqa: E501

        Current page token for pagination.  # noqa: E501

        :return: The page_token of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: str
        """
        return self._page_token

    @page_token.setter
    def page_token(self, page_token):
        """Sets the page_token of this AnkrGetAccountBalanceParams.

        Current page token for pagination.  # noqa: E501

        :param page_token: The page_token of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: str
        """

        self._page_token = page_token

    @property
    def sync_check(self):
        """Gets the sync_check of this AnkrGetAccountBalanceParams.  # noqa: E501

        If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive.  # noqa: E501

        :return: The sync_check of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: bool
        """
        return self._sync_check

    @sync_check.setter
    def sync_check(self, sync_check):
        """Sets the sync_check of this AnkrGetAccountBalanceParams.

        If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive.  # noqa: E501

        :param sync_check: The sync_check of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: bool
        """

        self._sync_check = sync_check

    @property
    def wallet_address(self):
        """Gets the wallet_address of this AnkrGetAccountBalanceParams.  # noqa: E501

        Address to get the balance of.  # noqa: E501

        :return: The wallet_address of this AnkrGetAccountBalanceParams.  # noqa: E501
        :rtype: str
        """
        return self._wallet_address

    @wallet_address.setter
    def wallet_address(self, wallet_address):
        """Sets the wallet_address of this AnkrGetAccountBalanceParams.

        Address to get the balance of.  # noqa: E501

        :param wallet_address: The wallet_address of this AnkrGetAccountBalanceParams.  # noqa: E501
        :type: str
        """
        if wallet_address is None:
            raise ValueError("Invalid value for `wallet_address`, must not be `None`")  # noqa: E501

        self._wallet_address = wallet_address

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
        if issubclass(AnkrGetAccountBalanceParams, dict):
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
        if not isinstance(other, AnkrGetAccountBalanceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
