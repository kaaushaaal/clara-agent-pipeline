import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python run_pipeline.py <account_id>")
    sys.exit(1)

account = sys.argv[1]

print("Running pipeline for:", account)

subprocess.run([sys.executable, "scripts/generate_memo_v1.py", account])
subprocess.run([sys.executable, "scripts/generate_agent_v1.py", account])

subprocess.run([sys.executable, "scripts/update_memo_v2.py", account])
subprocess.run([sys.executable, "scripts/generate_agent_v2.py", account])

subprocess.run([sys.executable, "scripts/generate_changelog.py", account])

subprocess.run([sys.executable, "scripts/store_account_supabase.py", account, "v1"])
subprocess.run([sys.executable, "scripts/store_account_supabase.py", account, "v2"])