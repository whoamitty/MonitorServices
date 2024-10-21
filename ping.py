import os

def ping_ipurl(address):
    response = os.popen(f"ping {address} -c1 -w2").read()
    if "packets transmitted, 1 received" in response:
        print(f"{address} is Up")
        return True
    else:
        print(f"{address} is Down")
        return False

# Example usage
# ping_ipurl('google.com')               # Ping an IP address
