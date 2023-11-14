# ankr.TokenAPIApi

All URIs are relative to *https://rpc.ankr.com/multichain*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ankr_explain_token_price_post**](TokenAPIApi.md#ankr_explain_token_price_post) | **POST** /?ankr_explainTokenPrice | ankr_explainTokenPrice
[**ankr_get_account_balance_post**](TokenAPIApi.md#ankr_get_account_balance_post) | **POST** /?ankr_getAccountBalance | ankr_getAccountBalance
[**ankr_get_currencies_post**](TokenAPIApi.md#ankr_get_currencies_post) | **POST** /?ankr_getCurrencies | ankr_getCurrencies
[**ankr_get_token_holders_count_post**](TokenAPIApi.md#ankr_get_token_holders_count_post) | **POST** /?ankr_getTokenHoldersCount | ankr_getTokenHoldersCount
[**ankr_get_token_holders_post**](TokenAPIApi.md#ankr_get_token_holders_post) | **POST** /?ankr_getTokenHolders | ankr_getTokenHolders
[**ankr_get_token_price_post**](TokenAPIApi.md#ankr_get_token_price_post) | **POST** /?ankr_getTokenPrice | ankr_getTokenPrice

# **ankr_explain_token_price_post**
> InlineResponse200 ankr_explain_token_price_post(body=body)

ankr_explainTokenPrice

Offers a breakdown of the specified token's price, detailing the contributing token pairs, their liquidity pools, and intermediate prices.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrExplainTokenPriceBody() # AnkrExplainTokenPriceBody |  (optional)

try:
    # ankr_explainTokenPrice
    api_response = api_instance.ankr_explain_token_price_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_explain_token_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrExplainTokenPriceBody**](AnkrExplainTokenPriceBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_account_balance_post**
> InlineResponse2001 ankr_get_account_balance_post(body=body)

ankr_getAccountBalance

Retrieves the balance of the specified account.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrGetAccountBalanceBody() # AnkrGetAccountBalanceBody |  (optional)

try:
    # ankr_getAccountBalance
    api_response = api_instance.ankr_get_account_balance_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_get_account_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetAccountBalanceBody**](AnkrGetAccountBalanceBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_currencies_post**
> InlineResponse2005 ankr_get_currencies_post(body=body)

ankr_getCurrencies

Retrieves a list of all currencies used on the specified blockchain.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrGetCurrenciesBody() # AnkrGetCurrenciesBody |  (optional)

try:
    # ankr_getCurrencies
    api_response = api_instance.ankr_get_currencies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_get_currencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetCurrenciesBody**](AnkrGetCurrenciesBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_token_holders_count_post**
> InlineResponse20014 ankr_get_token_holders_count_post(body=body)

ankr_getTokenHoldersCount

Retrieves the number of holders of the specified token.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrGetTokenHoldersCountBody() # AnkrGetTokenHoldersCountBody |  (optional)

try:
    # ankr_getTokenHoldersCount
    api_response = api_instance.ankr_get_token_holders_count_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_get_token_holders_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTokenHoldersCountBody**](AnkrGetTokenHoldersCountBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_token_holders_post**
> InlineResponse20013 ankr_get_token_holders_post(body=body)

ankr_getTokenHolders

Retrieves the metadata and a list of holders (wallet addresses) of the specified token.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrGetTokenHoldersBody() # AnkrGetTokenHoldersBody |  (optional)

try:
    # ankr_getTokenHolders
    api_response = api_instance.ankr_get_token_holders_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_get_token_holders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTokenHoldersBody**](AnkrGetTokenHoldersBody.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_token_price_post**
> InlineResponse20015 ankr_get_token_price_post(body=body)

ankr_getTokenPrice

Retrieves the USD price of the specified token.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.TokenAPIApi()
body = ankr.AnkrGetTokenPriceBody() # AnkrGetTokenPriceBody |  (optional)

try:
    # ankr_getTokenPrice
    api_response = api_instance.ankr_get_token_price_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenAPIApi->ankr_get_token_price_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTokenPriceBody**](AnkrGetTokenPriceBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

