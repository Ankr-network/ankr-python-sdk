# ankr.QueryAPIApi

All URIs are relative to *https://rpc.ankr.com/multichain*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ankr_get_blockchain_stats_post**](QueryAPIApi.md#ankr_get_blockchain_stats_post) | **POST** /?ankr_getBlockchainStats | ankr_getBlockchainStats
[**ankr_get_blocks_post**](QueryAPIApi.md#ankr_get_blocks_post) | **POST** /?ankr_getBlocks | ankr_getBlocks
[**ankr_get_interactions_post**](QueryAPIApi.md#ankr_get_interactions_post) | **POST** /?ankr_getInteractions | ankr_getInteractions
[**ankr_get_logs_post**](QueryAPIApi.md#ankr_get_logs_post) | **POST** /?ankr_getLogs | ankr_getLogs
[**ankr_get_token_transfers_post**](QueryAPIApi.md#ankr_get_token_transfers_post) | **POST** /?ankr_getTokenTransfers | ankr_getTokenTransfers
[**ankr_get_transactions_by_address_post**](QueryAPIApi.md#ankr_get_transactions_by_address_post) | **POST** /?ankr_getTransactionsByAddress | ankr_getTransactionsByAddress
[**ankr_get_transactions_by_hash_post**](QueryAPIApi.md#ankr_get_transactions_by_hash_post) | **POST** /?ankr_getTransactionsByHash | ankr_getTransactionsByHash

# **ankr_get_blockchain_stats_post**
> InlineResponse2003 ankr_get_blockchain_stats_post(body=body)

ankr_getBlockchainStats

Retrieves blockchain statistics.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetBlockchainStatsBody() # AnkrGetBlockchainStatsBody |  (optional)

try:
    # ankr_getBlockchainStats
    api_response = api_instance.ankr_get_blockchain_stats_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_blockchain_stats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetBlockchainStatsBody**](AnkrGetBlockchainStatsBody.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_blocks_post**
> InlineResponse2004 ankr_get_blocks_post(body=body)

ankr_getBlocks

Retrieves details of the specified range of blocks.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetBlocksBody() # AnkrGetBlocksBody |  (optional)

try:
    # ankr_getBlocks
    api_response = api_instance.ankr_get_blocks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_blocks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetBlocksBody**](AnkrGetBlocksBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_interactions_post**
> InlineResponse2006 ankr_get_interactions_post(body=body)

ankr_getInteractions

Retrieves a list of blockchains on which interactions (tokens, NFTs, transactions) were registered for the specified address.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetInteractionsBody() # AnkrGetInteractionsBody |  (optional)

try:
    # ankr_getInteractions
    api_response = api_instance.ankr_get_interactions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_interactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetInteractionsBody**](AnkrGetInteractionsBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_logs_post**
> InlineResponse2008 ankr_get_logs_post(body=body)

ankr_getLogs

Retrieves historical data for the specified range of blocks.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetLogsBody() # AnkrGetLogsBody |  (optional)

try:
    # ankr_getLogs
    api_response = api_instance.ankr_get_logs_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_logs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetLogsBody**](AnkrGetLogsBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_token_transfers_post**
> InlineResponse20017 ankr_get_token_transfers_post(body=body)

ankr_getTokenTransfers

Retrieves the details of token transfers for the specified wallet address.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetTokenTransfersBody() # AnkrGetTokenTransfersBody |  (optional)

try:
    # ankr_getTokenTransfers
    api_response = api_instance.ankr_get_token_transfers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_token_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTokenTransfersBody**](AnkrGetTokenTransfersBody.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_transactions_by_address_post**
> InlineResponse20018 ankr_get_transactions_by_address_post(body=body)

ankr_getTransactionsByAddress

Retrieves the details of transactions for the specified address.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetTransactionsByAddressBody() # AnkrGetTransactionsByAddressBody |  (optional)

try:
    # ankr_getTransactionsByAddress
    api_response = api_instance.ankr_get_transactions_by_address_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_transactions_by_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTransactionsByAddressBody**](AnkrGetTransactionsByAddressBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_transactions_by_hash_post**
> InlineResponse20019 ankr_get_transactions_by_hash_post(body=body)

ankr_getTransactionsByHash

Retrieves details of the transaction specified by its hash.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.QueryAPIApi()
body = ankr.AnkrGetTransactionsByHashBody() # AnkrGetTransactionsByHashBody |  (optional)

try:
    # ankr_getTransactionsByHash
    api_response = api_instance.ankr_get_transactions_by_hash_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryAPIApi->ankr_get_transactions_by_hash_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetTransactionsByHashBody**](AnkrGetTransactionsByHashBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

