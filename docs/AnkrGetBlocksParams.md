# AnkrGetBlocksParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai. | 
**decode_logs** | **bool** | Decode logs (true) or not (false). | [optional] 
**decode_tx_data** | **bool** | Decode transaction data (true) or not (false). | [optional] 
**desc_order** | **bool** | Sorting order. Descending (true) or ascending (false). | [optional] 
**from_block** | **int** | Number of the first block in a range. Integer or string (hex value or earliest). Max range — 30 blocks. | [optional] 
**include_logs** | **bool** | Include logs (true) or exclude them (false). Logs are stored inside transactions, so includeTxs also has to be true when IncludeLogs is true. | [optional] 
**include_txs** | **bool** | Include transactions (true) or exclude them (false). IncludeTxs has to be true if IncludeLogs is true. | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**to_block** | **object** | Number of the last block in a range. Integer or string (hex value or latest). Max range — 30 blocks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

