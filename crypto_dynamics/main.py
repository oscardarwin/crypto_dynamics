from bitcoinrpc import BitcoinRPC

if __name__ == "__main__":
    rpc = BitcoinRPC

    BitcoinRPC.from_config("http://localhost:18443", ("rpc_user", "rpc_passwd"))


