from pinger import ping

def prepare_data(data):
    return f"[NOTIFYX] {data.strip().upper()}"

def notify(data):
    ping()
    print(f"Sending notification: '{data}'")
    with open("notifications.txt", "a") as f:
        print(f"{data}\n")
        f.write(f"{data}\n")
    print("Notification saved -> notifications.txt")

def dummy():
    ping() # good ping.... .
    print("This is a dummy function in notifier.py")
