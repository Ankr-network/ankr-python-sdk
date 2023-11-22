import time

import ankr

if __name__ == "__main__":
    ankr_w3= ankr.AnkrWeb3(api_key="31000350a6f93afcfdf56edef0b7169e1d87c3ac72d747f74ee4acfa3a3b1c42")
    ankr_w3= ankr.AnkrWeb3(api_key="31000350a6f93afcfdf56edef0b7169e1d87c3ac72d747f74ee4acfa3a3b1c42")
    # result = ankr_w3.query.get_logs(
    #     blockchain="eth",
    #     from_block="0xdaf6b1",
    #     to_block=14350010,
    #     address=["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    #     topics=[
    #         [],
    #         ["0x000000000000000000000000def1c0ded9bec7f1a1670819833240f027b25eff"],
    #     ],
    #     decode_logs=True,
    #     limit=10
    # )
    #
    # result = ankr_w3.query.get_blocks(
    #     blockchain="eth",
    #     from_block=14500001,
    #     to_block=14500004,
    #     desc_order=True,
    #     include_logs=True,
    #     include_txs=True,
    #     decode_logs=True,)

    # result = ankr_w3.token.get_token_holders(
    #     blockchain="eth",
    #     contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7")

    result = ankr_w3.nft.get_nft_holders(
        blockchain="arbitrum",
        contract_address="0xc36442b4a4522e871399cd717abdd847ab11fe88",
        limit=1000
    )

    # result = ankr_w3.token.get_token_holders_count_history(
    #     blockchain="eth",
    #     contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7")

    # result = ankr_w3.token.get_account_balance(
    #     blockchain="eth",
    #     wallet_address="vitalik.eth"
    # )
    #
    # result = ankr_w3.nft.get_nfts(
    #     blockchain="eth",
    #     wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD"
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
    for log in result:
        print(log)




