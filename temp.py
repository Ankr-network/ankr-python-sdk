import time

import ankr
from ankr import types
from ankr.types import Blockchain

if __name__ == "__main__":
    # ankr_w3= ankr.AnkrWeb3(api_key="31000350a6f93afcfdf56edef0b7169e1d87c3ac72d747f74ee4acfa3a3b1c42")
    ankr_w3 = ankr.AnkrWeb3(api_key="31000350a6f93afcfdf56edef0b7169e1d87c3ac72d747f74ee4acfa3a3b1c42")

    # result = ankr_w3.query.get_logs(
    #     request=types.GetLogsRequest(
    #         blockchain=[Blockchain.Eth],
    #         fromBlock=1181739,
    #         toBlock=1181739,
    #         address=["0x3589d05a1ec4af9f65b0e5554e645707775ee43c"],
    #         topics=[
    #             [],
    #             ["0x000000000000000000000000feb92d30bf01ff9a1901666c5573532bfa07eeec"],
    #         ],
    #         decodeLogs=True,
    #     ),
    #     limit=10
    # )
    # result = ankr_w3.query.get_logs_raw(
    #     request=types_gen.GetLogsRequest(
    #         blockchain= types_gen.Blockchain.Eth,
    #         fromBlock=1181739,
    #         toBlock=1181739,
    #         address=["0x3589d05a1ec4af9f65b0e5554e645707775ee43c"],
    #         topics=[
    #             [],
    #             ["0x000000000000000000000000feb92d30bf01ff9a1901666c5573532bfa07eeec"],
    #         ],
    #         decodeLogs= True,
    #         pageSize=1,
    #         pageToken="7hWsYQQwY43r58nqZa7ygmKMnmYueRk2JFvH6o5c5cKv2Z2jFYhsgtsgJhHDih8ukNNue4ZYvDYzoT"
    #     ),
    # )
    #
    # pairs = ankr_w3.token.explain_token_price_raw(
    #     request=types.ExplainTokenPriceRequest(
    #         blockchain=Blockchain.Eth,
    #         tokenAddress='0x8290333cef9e6d528dd5618fb97a76f268f3edd4',
    #         blockHeight=17463534,
    #     )
    # )
    #
    # print(pairs.pairs)

    #
    # result = ankr_w3.query.get_blocks(
    #     request=types_gen.GetBlocksRequest(
    #         blockchain="eth",
    #         from_block=14500001,
    #         to_block=14500004,
    #         desc_order=True,
    #         include_logs=True,
    #         include_txs=True,
    #         decode_logs=True,
    #     )
    # )

    # result = ankr_w3.token.get_token_holders(
    #     blockchain="eth",
    #     contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7")

    # result = ankr_w3.nft.get_nft_holders(
    #     blockchain="arbitrum",
    #     contract_address="0xc36442b4a4522e871399cd717abdd847ab11fe88",
    #     limit=1000
    # )

    # result = ankr_w3.token.get_token_holders_count_history(
    #     blockchain="eth",
    #     contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7")

    result = ankr_w3.token.get_token_transfers_raw(
        request=types.GetTransfersRequest(
            blockchain=Blockchain.Eth,
            address=['0xf16e9b0d03470827a95cdfd0cb8a8a3b46969b91'],
            fromTimestamp=1674441035,
            toTimestamp=1674441035,
            descOrder=True,
        )
    )

    # for balance in result:
    #     print(balance)
    print(result.transfers)
    # result = ankr_w3.nft.get_nfts_raw(
    #     request=types_gen.GetNFTsByOwnerRequest(
    #         blockchain=Blockchain.Eth,
    #         walletAddress="0x0E11A192d574b342C51be9e306694C41547185DD"
    #     )
    # )
    #
    # result = ankr_w3.nft.get_nft_holders(
    #     blockchain="eth",
    #     contract_address="0xc36442b4a4522e871399cd717abdd847ab11fe88",
    #     limit=1000
    # )

    # result = ankr_w3.query.get_transaction(
    #     transaction_hash="0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f",
    #     decode_tx_data=True
    # )

    # result = ankr_w3.token.get_token_holders_count(
    #     blockchain="eth",
    #     contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7")

    # result = ankr_w3.token.get_token_price(
    #     blockchain="eth",
    #     contract_address="")
    #
    # result = ankr_w3.nft.get_nft_metadata(
    #     blockchain="eth",
    #     contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
    #     token_id="1500",
    #     force_fetch=False
    # )

    # Call the function
    # print(len(list(result)))
    # print(result)
    # print(result.logs)
    # print(result.nextPageToken)
    # print(result.logs)
    # result
    # for log in result:
    #     print(log)
    # print()