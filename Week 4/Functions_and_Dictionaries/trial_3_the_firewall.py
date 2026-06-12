# ==========================================
# TRIAL 3: THE FIREWALL
# ==========================================
# We have a dictionary of banned IP addresses and their threat levels.
banned_ips = {
    "192.168.1.50": "High",
    "10.0.0.99": "Critical",
    "172.16.254.1": "Low"
}

# TODO: Build the firewall scanner.
# 1. Create a function called 'scan_ip' that takes one argument: 'ip_address'.
# 2. IF the ip_address is IN the banned_ips dictionary, RETURN its threat level.
# 3. ELSE, RETURN "Safe".

# --- Write your function below ---



# --- Do not change the code below ---
incoming_request = input("Enter IP to scan: ")
result = scan_ip(incoming_request)
print(f"Scan Result: {result}")