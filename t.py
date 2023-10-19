from web3 import Web3
import time

# RPC
rpc_url = "https://mainnet.base.org"

# 创建Web3对象
w3 = Web3(Web3.HTTPProvider(rpc_url))

# 发件人账号私钥
private_key=["test"]

t = 0
# 接收地址
recipient_address = "test"


while True:
    if t <= len(private_key):
 # 构造交易参数
        YOUR_ADDRESS = w3.eth.account.privateKeyToAccount(private_key[t]).address
        balance = w3.eth.getBalance(YOUR_ADDRESS)
        nonce = w3.eth.getTransactionCount(YOUR_ADDRESS)
        gas_price = w3.toWei("0.1", "gwei")  # 设置Gas价格
        gas_limit = 21000  # Gas上限
        gas_cost = gas_price * gas_limit
        buffer = w3.toWei(0.00007, 'ether')
        send_value = balance - gas_cost - buffer

        tx = {
            "to": recipient_address,
            "value": send_value,
            "gas": gas_limit,
            "gasPrice": gas_price,
            "nonce": nonce,
             }

        # 使用发件人私钥对交易进行签名
        signed_tx = w3.eth.account.signTransaction(tx, private_key[t])

        # 发送已签名的交易
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent with hash: {tx_hash.hex()}")

        # 增加延迟，以避免发送速度过快
        time.sleep(2)
        t+= 1

