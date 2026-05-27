from pinger import ping

def prepare_data(data):
    return f"[NOTIFY] {data.strip().upper()}"

def notify(data):
    ping()
    print(f"Sending notification: '{data}'")
    with open("notifications.txt", "a") as f:
        f.write(f"{data}\n")
    print("Notification saved -> notifications.txt")

def dummy():
    ping() # good ping
    print("This is a dummy function in notifier.py")
