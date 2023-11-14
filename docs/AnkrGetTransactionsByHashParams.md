# AnkrGetTransactionsByHashParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **list[str]** | Name of the blockchain or list of blockchain names. Single: eth. Multiple: [arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai]. All chains: empty value. | [optional] 
**decode_logs** | **bool** | Decode logs (true) or not (false). | [optional] 
**decode_tx_data** | **bool** | Decode transaction data (true) or not (false). | [optional] 
**include_logs** | **bool** | Include logs (true) or exclude them (false). | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**transaction_hash** | **str** | Hash of the transaction. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

