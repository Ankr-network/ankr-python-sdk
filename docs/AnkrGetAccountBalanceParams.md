# AnkrGetAccountBalanceParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **list[str]** | Name of the blockchain or list of blockchain names. Single: eth. Multiple: [arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai.]. All chains: empty value. | [optional] 
**native_first** | **bool** | Sorting order. Native network token first (true) or not (false). | [optional] 
**only_whitelisted** | **bool** | Filtering. Only show tokens listed on CoinGekko (true) or all the tokens (false). Default — true. | [optional] 
**page_size** | **int** | Number of entries per page. int32. Max value — all, default value — all. | [optional] 
**page_token** | **str** | Current page token for pagination. | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**wallet_address** | **str** | Address to get the balance of. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

