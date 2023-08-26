import requests
import base64


def get_block_transactions(block_height):
    url = f"http://akash-rpc.w3coins.io/block?height={block_height}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        txs = data.get("result", {}).get("block", {}).get("data", {}).get("txs", [])

        if txs:
            for encoded_tx in txs:
                try:
                    decoded_data = base64.b64decode(encoded_tx)
                    print(decoded_data.hex())
                except Exception as e:
                    print("Error decoding:", e)
        else:
            print("No transactions found in the block.")
    else:
        print("Error:", response.status_code)


get_block_transactions(11260637)
