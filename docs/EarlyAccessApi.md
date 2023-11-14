# ankr.EarlyAccessApi

All URIs are relative to *https://rpc.ankr.com/multichain*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ankr_get_account_balance_historical_post**](EarlyAccessApi.md#ankr_get_account_balance_historical_post) | **POST** /?ankr_getAccountBalanceHistorical | ankr_getAccountBalanceHistorical
[**ankr_get_internal_transactions_by_block_number_post**](EarlyAccessApi.md#ankr_get_internal_transactions_by_block_number_post) | **POST** /?ankr_getInternalTransactionsByBlockNumber | ankr_getInternalTransactionsByBlockNumber
[**ankr_get_internal_transactions_by_parent_hash_post**](EarlyAccessApi.md#ankr_get_internal_transactions_by_parent_hash_post) | **POST** /?ankr_getInternalTransactionsByParentHash | ankr_getInternalTransactionsByParentHash
[**ankr_get_token_price_history_post**](EarlyAccessApi.md#ankr_get_token_price_history_post) | **POST** /?ankr_getTokenPriceHistory | ankr_getTokenPriceHistory

# **ankr_get_account_balance_historical_post**
> InlineResponse2002 ankr_get_account_balance_historical_post(body=body)

ankr_getAccountBalanceHistorical

Retrieves the historical balance of the specified account.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.EarlyAccessApi()
body = ankr.AnkrGetAccountBalanceHistoricalBody() # AnkrGetAccountBalanceHistoricalBody |  (optional)

try:
    # ankr_getAccountBalanceHistorical
    api_response = api_instance.ankr_get_account_balance_historical_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarlyAccessApi->ankr_get_account_balance_historical_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetAccountBalanceHistoricalBody**](AnkrGetAccountBalanceHistoricalBody.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_internal_transactions_by_block_number_post**
> InlineResponse2007 ankr_get_internal_transactions_by_block_number_post(body=body)

ankr_getInternalTransactionsByBlockNumber

Retrieves the details of internal transactions for the specified block number. Internal transactions are callbacks that happen during contract-to-contract interactions.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.EarlyAccessApi()
body = ankr.AnkrGetInternalTransactionsByBlockNumberBody() # AnkrGetInternalTransactionsByBlockNumberBody |  (optional)

try:
    # ankr_getInternalTransactionsByBlockNumber
    api_response = api_instance.ankr_get_internal_transactions_by_block_number_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarlyAccessApi->ankr_get_internal_transactions_by_block_number_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetInternalTransactionsByBlockNumberBody**](AnkrGetInternalTransactionsByBlockNumberBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_internal_transactions_by_parent_hash_post**
> InlineResponse2007 ankr_get_internal_transactions_by_parent_hash_post(body=body)

ankr_getInternalTransactionsByParentHash

Retrieves the details of internal transactions for the specified parent transaction hash. Internal transactions are callbacks that happen during contract-to-contract interactions.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.EarlyAccessApi()
body = ankr.AnkrGetInternalTransactionsByParentHashBody() # AnkrGetInternalTransactionsByParentHashBody |  (optional)

try:
    # ankr_getInternalTransactionsByParentHash
    api_response = api_instance.ankr_get_internal_transactions_by_parent_hash_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarlyAccessApi->ankr_get_internal_transactions_by_parent_hash_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetInternalTransactionsByParentHashBody**](AnkrGetInternalTransactionsByParentHashBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_token_price_history_post**
> InlineResponse20016 ankr_get_token_price_history_post(body=body)

ankr_getTokenPriceHistory

Retrieves the historical price of the specified token.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.EarlyAccessApi()
body = ankr.AnkrGetTokenPriceHistoryBody() # AnkrGetTokenPriceHistoryBody |  (optional)

try:
    # ankr_getTokenPriceHistory
    api_response = api_instance.ankr_get_token_price_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarlyAccessApi->ankr_get_token_price_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTokenPriceHistoryBody**](AnkrGetTokenPriceHistoryBody.md)|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

