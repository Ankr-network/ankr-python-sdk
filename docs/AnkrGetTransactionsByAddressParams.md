# AnkrGetTransactionsByAddressParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **list[str]** | Address to query for transactions. | 
**blockchain** | **list[str]** | Name of the blockchain or list of blockchain names. Single: eth. Multiple: [arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai]. All chains: empty value. | [optional] 
**desc_order** | **bool** | Sorting order. Descending (true) or ascending (false). | [optional] 
**from_block** | **int** | Number of the first block in a range. Integer or string (number, hex value, &#x27;earliest&#x27; or &#x27;latest&#x27;). | [optional] 
**from_timestamp** | **int** | Beginning of a time period. UNIX timestamp. | [optional] 
**include_logs** | **bool** | Include logs (true) or exclude them (false). | [optional] 
**page_size** | **int** | Number of entries per page. int32. Max value — 10000, default value — 100. | [optional] 
**page_token** | **str** | Current page token for pagination. | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**to_block** | **object** | Number of the last block in a range. Integer or string (number, hex value, &#x27;earliest&#x27; or &#x27;latest&#x27;). | [optional] 
**to_timestamp** | **object** | End of a time period. UNIX timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

