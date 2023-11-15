import ankr

if __name__ == "__main__":
    # Example usage when running the script

    # Assuming you have instantiated AnkrGetNFTsByOwnerParams
    params = ankr.AnkrGetNFTsByOwnerParams(
        blockchain="eth",
        wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
        filter=[
            {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
            {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
        ],
    )

    # Assuming you have instantiated AnkrGetNFTsByOwnerBody and set its attributes
    body = ankr.AnkrGetNFTsByOwnerBody(
        id=1,
        jsonrpc="2.0",
        method="ankr_getNFTsByOwner",
        params=params
    )

    configuration = ankr.Configuration()
    configuration.api_key = "API_KEY"

    nftAPI = ankr.api.NFTAPIApi(api_client=ankr.ApiClient(configuration=configuration))

    # Call the function
    print(nftAPI.ankr_get_nfts_by_owner_post(body=body))


