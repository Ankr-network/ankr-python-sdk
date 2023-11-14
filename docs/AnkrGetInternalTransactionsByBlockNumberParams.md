# AnkrGetInternalTransactionsByBlockNumberParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_number** | **int** | Number of the block that contains the transaction. | [optional] 
**blockchain** | **str** | Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai. | 
**only_with_value** | **bool** | Filtering. Only responses containing the value parameter (true) or all responses (false). | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

