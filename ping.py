import os

def ping_address(address):
    response = os.popen(f"ping {address} -c1 -w2").read()
    print(response)
    if "packets transmitted, 1 received" in response or "paquets transmis, 1 reçus" in response :
        print(f"{address} is Up")
        return True
    else:
        print(f"{address} is Down")
        return False
    


# Example usage
# ping_address('google.com')               # Ping an IP address
