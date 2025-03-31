import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Configuration
TESTNET_MIRROR_URL = "https://testnet.mirrornode.hedera.com/api/v1"
YOUR_ACCOUNT_ID = os.getenv('OPERATOR_ID')
YOUR_TOKEN_ID = token_id = os.getenv('Token_ID')

def get_token_balance_for_account(account_id, token_id):
    """Get balance of a specific token for a given account"""
    url = f"{TESTNET_MIRROR_URL}/accounts/{account_id}/tokens"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        tokens = response.json().get('tokens', [])
        
        for token in tokens:
            if token['token_id'] == token_id:
                return int(token['balance'])
        return 0  # Token not found
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching balance: {e}")
        return None

def get_token_info(token_id):
    """Get token metadata including total supply"""
    url = f"{TESTNET_MIRROR_URL}/tokens/{token_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'name': data.get('name'),
            'symbol': data.get('symbol'),
            'total_supply': int(data.get('total_supply', 0)),
            'decimals': data.get('decimals', 0)
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token info: {e}")
        return None

def get_all_token_holders(token_id, limit=100):
    """Get all accounts holding the specified token"""
    url = f"{TESTNET_MIRROR_URL}/tokens/{token_id}/balances"
    params = {'limit': limit}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return [
            {
                'account': entry['account'],
                'balance': int(entry['balance'])
            } for entry in response.json().get('balances', [])
        ]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching holders: {e}")
        return None