from brownie.network.web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import GZToken
from web3 import Web3

initial_supply = Web3.toWei(100000000, "ether")


def deploy_token():
    acccout = get_account()
    gz_token = GZToken.deploy(initial_supply, {"from": acccout})
    print(gz_token.name())


def main():
    deploy_token()
