# coding: utf-8

"""
    Ankr Advanced API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnkrGetInternalTransactionsByBlockNumberBody(object):
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
        'id': 'int',
        'jsonrpc': 'str',
        'method': 'str',
        'params': 'AnkrGetInternalTransactionsByBlockNumberParams'
    }

    attribute_map = {
        'id': 'id',
        'jsonrpc': 'jsonrpc',
        'method': 'method',
        'params': 'params'
    }

    def __init__(self, id=None, jsonrpc=None, method=None, params=None):  # noqa: E501
        """AnkrGetInternalTransactionsByBlockNumberBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._jsonrpc = None
        self._method = None
        self._params = None
        self.discriminator = None
        self.id = id
        self.jsonrpc = jsonrpc
        self.method = method
        self.params = params

    @property
    def id(self):
        """Gets the id of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501


        :return: The id of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnkrGetInternalTransactionsByBlockNumberBody.


        :param id: The id of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def jsonrpc(self):
        """Gets the jsonrpc of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501


        :return: The jsonrpc of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._jsonrpc

    @jsonrpc.setter
    def jsonrpc(self, jsonrpc):
        """Sets the jsonrpc of this AnkrGetInternalTransactionsByBlockNumberBody.


        :param jsonrpc: The jsonrpc of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :type: str
        """
        if jsonrpc is None:
            raise ValueError("Invalid value for `jsonrpc`, must not be `None`")  # noqa: E501
        allowed_values = ["2.0"]  # noqa: E501
        if jsonrpc not in allowed_values:
            raise ValueError(
                "Invalid value for `jsonrpc` ({0}), must be one of {1}"  # noqa: E501
                .format(jsonrpc, allowed_values)
            )

        self._jsonrpc = jsonrpc

    @property
    def method(self):
        """Gets the method of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501


        :return: The method of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AnkrGetInternalTransactionsByBlockNumberBody.


        :param method: The method of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["ankr_getInternalTransactionsByBlockNumber"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def params(self):
        """Gets the params of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501


        :return: The params of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :rtype: AnkrGetInternalTransactionsByBlockNumberParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this AnkrGetInternalTransactionsByBlockNumberBody.


        :param params: The params of this AnkrGetInternalTransactionsByBlockNumberBody.  # noqa: E501
        :type: AnkrGetInternalTransactionsByBlockNumberParams
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

        self._params = params

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
        if issubclass(AnkrGetInternalTransactionsByBlockNumberBody, dict):
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
        if not isinstance(other, AnkrGetInternalTransactionsByBlockNumberBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
