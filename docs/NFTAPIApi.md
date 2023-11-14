# ankr.NFTAPIApi

All URIs are relative to *https://rpc.ankr.com/multichain*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ankr_get_nft_holders_post**](NFTAPIApi.md#ankr_get_nft_holders_post) | **POST** /?ankr_getNFTHolders | ankr_getNFTHolders
[**ankr_get_nft_metadata_post**](NFTAPIApi.md#ankr_get_nft_metadata_post) | **POST** /?ankr_getNFTMetadata | ankr_getNFTMetadata
[**ankr_get_nft_transfers_post**](NFTAPIApi.md#ankr_get_nft_transfers_post) | **POST** /?ankr_getNftTransfers | ankr_getNftTransfers
[**ankr_get_nfts_by_owner_post**](NFTAPIApi.md#ankr_get_nfts_by_owner_post) | **POST** /?ankr_getNFTsByOwner | ankr_getNFTsByOwner

# **ankr_get_nft_holders_post**
> InlineResponse2009 ankr_get_nft_holders_post(body=body)

ankr_getNFTHolders

Retrieves a list of holders (wallet addresses) of the specified NFT.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.NFTAPIApi()
body = ankr.AnkrGetNFTHoldersBody() # AnkrGetNFTHoldersBody |  (optional)

try:
    # ankr_getNFTHolders
    api_response = api_instance.ankr_get_nft_holders_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTAPIApi->ankr_get_nft_holders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetNFTHoldersBody**](AnkrGetNFTHoldersBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_nft_metadata_post**
> InlineResponse20010 ankr_get_nft_metadata_post(body=body)

ankr_getNFTMetadata

Retrieves the metadata of to the specified NFT (ERC721/ERC1155/ENS/POAP).

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.NFTAPIApi()
body = ankr.AnkrGetNFTMetadataBody() # AnkrGetNFTMetadataBody |  (optional)

try:
    # ankr_getNFTMetadata
    api_response = api_instance.ankr_get_nft_metadata_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTAPIApi->ankr_get_nft_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetNFTMetadataBody**](AnkrGetNFTMetadataBody.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_nft_transfers_post**
> InlineResponse20012 ankr_get_nft_transfers_post(body=body)

ankr_getNftTransfers

Retrieves the details of NFT transfers for the specified address.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.NFTAPIApi()
body = ankr.AnkrGetNftTransfersBody() # AnkrGetNftTransfersBody |  (optional)

try:
    # ankr_getNftTransfers
    api_response = api_instance.ankr_get_nft_transfers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTAPIApi->ankr_get_nft_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetNftTransfersBody**](AnkrGetNftTransfersBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ankr_get_nfts_by_owner_post**
> InlineResponse20011 ankr_get_nfts_by_owner_post(body=body)

ankr_getNFTsByOwner

Retrieves a list of NFTs (ERC721/ERC1155/ENS/POAP) that belong to the specified account.

### Example
```python
from __future__ import print_function
import time
import ankr
from ankr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ankr.NFTAPIApi()
body = ankr.AnkrGetNFTsByOwnerBody() # AnkrGetNFTsByOwnerBody |  (optional)

try:
    # ankr_getNFTsByOwner
    api_response = api_instance.ankr_get_nfts_by_owner_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTAPIApi->ankr_get_nfts_by_owner_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnkrGetNFTsByOwnerBody**](AnkrGetNFTsByOwnerBody.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

