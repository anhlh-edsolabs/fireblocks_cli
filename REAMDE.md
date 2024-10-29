# Fireblocks Transaction Tool

This project is a command-line tool for creating and managing transactions using the Fireblocks SDK.

## Project Structure

```text
.   ├── .gitignore 
    ├── package.json 
    ├── README.md
    ├── src/
        ├── api_key.txt
        ├── fireblocks_cli.py
        ├── quantum_main.key 
    ├── venv/ │ 
        ├── bin/ │ 
        ├── include/ │ 
        ├── lib/ │ 
        ├── .gitignore │ 
        ├── pyvenv.cfg
```

## Prerequisites

- Python 3.13
- Fireblocks SDK

## Setup

1. **Clone the repository:**

    ```sh
    git clone git@github.com:anhlh-edsolabs/fireblocks_cli.git
    cd fireblocks_cli
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Add your Fireblocks API key and secret:**

    - Place your API key in `src/api_key.txt`.
    - Place your API secret in `src/quantum_main.key`.

## Usage

Run the CLI tool:

```sh
python fireblocks_cli.py
```

or

```sh
python3 fireblocks_cli.py
```

Follow the prompts to enter transaction details such as Vault account ID, External wallet ID, Contract call data, ETH amount, Max gas fee, and Transaction note.

## Example

```bash
=====*===== Fireblocks Transaction Tool =====*=====

Enter Vault account ID: 1
Enter External wallet ID: a64c3824-a0af-4a9f-9daa-16d35140adc2
Enter Contract call data: 0x123456
Enter ETH amount (default 0): 0.5
Enter Max gas fee (default 10): 15
Enter Transaction note: Test transaction

Transaction Details:
Vault Account ID: 1
External Wallet ID: a64c3824-a0af-4a9f-9daa-16d35140adc2
Contract Call Data: 0x123456
ETH Amount: 0.5
Max Gas Fee: 15
Transaction Note: Test transaction

Do you want to proceed with the transaction? (y/n): y
```

## License

This project is licensed under the MIT License.
