# AnkrGetNFTMetadataParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Name of the blockchain. Acceptable values: arbitrum, avalanche, base, bsc, eth, fantom, flare, gnosis, optimism, polygon, polygon_zkevm, rollux, syscoin, zksync_era, avalanche_fuji, eth_goerli, optimism_testnet, polygon_mumbai. | [optional] 
**contract_address** | **str** | Address of the NFT contract the metadata belongs to. Supports ENS. | 
**force_fetch** | **bool** | Get NFT metadata from the contract (true) or database (false). | [optional] 
**sync_check** | **bool** | If false, the data is returned regardless of indexer health, if true, the data is returned only when the indexer health check is positive. | [optional] 
**token_id** | **str** | Token ID of the NFT the metadata belongs to. Created by the contract when minting the NFT. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

