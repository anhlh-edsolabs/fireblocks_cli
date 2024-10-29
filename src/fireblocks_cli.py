#!/usr/bin/env python3# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:45:00 2024

@author: Le Hoang Anh
"""
import os
from fireblocks_sdk import FireblocksSDK, TransferPeerPath, DestinationTransferPeerPath


def main():
    "Main function to create a Fireblocks transaction"
    print("\n=====*===== Fireblocks Transaction Tool =====*=====\n")
    vault_id = input("Enter Vault account ID: ").strip()
    external_wallet = input("Enter External wallet ID: ").strip()
    call_data = input("Enter Contract call data: ").strip()
    eth_amount = input("Enter ETH amount (default 0): ").strip()
    max_fee = input("Enter Max gas fee (default 10): ").strip()
    tx_note = input("Enter Transaction note: ").strip()

    # Use default value for eth_amount if not provided
    if not eth_amount:
        eth_amount = "0"

    # Use default value for max_fee if not provided
    if not max_fee:
        max_fee = "10"

    # Print transaction details for confirmation
    print("\nTransaction Details:")
    print(f"Vault Account ID: {vault_id}")
    print(f"External Wallet ID: {external_wallet}")
    print(f"Contract Call Data: {call_data}")
    print(f"ETH Amount: {eth_amount}")
    print(f"Max Gas Fee: {max_fee}")
    print(f"Transaction Note: {tx_note}")

    confirmation = input(
        "\nDo you want to proceed with the transaction? (y/n): ").strip()
    if confirmation.lower() not in ['yes', 'y']:
        print("Transaction cancelled.")
        return

    # Determine the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        with open(os.path.join(script_dir, "quantum_main.key"), "r", encoding="utf-8") as secret_file:
            api_secret = secret_file.read().strip()
        with open(os.path.join(script_dir, "api_key.txt"), "r", encoding="utf-8") as key_file:
            api_key = key_file.read().strip()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    fireblocks = FireblocksSDK(api_secret, api_key)

    try:
        tx_result = fireblocks.create_transaction(
            asset_id="ETH",
            amount=eth_amount,
            source=TransferPeerPath("VAULT_ACCOUNT", vault_id),
            destination=DestinationTransferPeerPath(
                "EXTERNAL_WALLET", external_wallet),
            tx_type="CONTRACT_CALL",
            note=tx_note,
            max_fee=max_fee,
            extra_parameters={"contractCallData": call_data}
        )
        print("Transaction Result:", tx_result)
    except Exception as e:
        print(f"Transaction failed: {e}")


if __name__ == "__main__":
    main()
