# AnkrGetNFTHoldersParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai. | 
**contract_address** | **str** | Contract address of the NFT collection. Supports ENS. | 
**page_size** | **int** | Number of entries per page. int32. Max value — 10000, default value — 1000. | [optional] 
**page_token** | **str** | Current page token for pagination. | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

