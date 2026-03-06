from supabase import create_client
import json
import os
import requests
import sys
account_id = sys.argv[1]

SUPABASE_URL = "https://pdvpmvfeovzhtxdodtjh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBkdnBtdmZlb3Z6aHR4ZG9kdGpoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI3ODgzNjMsImV4cCI6MjA4ODM2NDM2M30.r4FbGPBhv3yY12ArEb0I0FWoG1mdinLNhooZ4dKf5QI"

def store_account(account_id, version):

    memo_path = f"outputs/accounts/{account_id}/{version}/memo.json"
    agent_path = f"outputs/accounts/{account_id}/{version}/agent_spec.json"

    with open(memo_path) as f:
        memo = json.load(f)

    with open(agent_path) as f:
        agent = json.load(f)

    payload = {
        "account_id": account_id,
        "version": version,
        "memo": memo,
        "agent_spec": agent
    }

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    url = f"{SUPABASE_URL}/rest/v1/accounts"

    response = requests.post(url, headers=headers, json=payload)

    print("Supabase response:", response.status_code)


if __name__ == "__main__":
    account = sys.argv[1]
    version = sys.argv[2]

    store_account(account, version)