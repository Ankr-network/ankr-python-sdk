# AnkrGetTokenPriceHistoryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai. | 
**contract_address** | **str** | Address of the token contract. | [optional] 
**from_timestamp** | **int** | Beginning of a time period. UNIX timestamp. | [optional] 
**interval** | **int** | Time interval for updating the token price. UNIX timestamp. | [optional] 
**limit** | **int** | Amount of records to be returned. | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**to_timestamp** | **object** | End of a time period. UNIX timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

