
import datetime
import webbrowser

def greet_user():
    """Greet the user based on the time."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")
    print("I am your  AI Assistant. How can I help you today?")

def respond(command):
    """Respond to user commands."""
    if 'hello' in command:
        print("Hello! How are you?")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(f"The time is {time}")
    elif 'open google' in command:
        webbrowser.open('https://www.google.com')
        print("Opening Google...")
    elif 'bye' in command:
        print("Goodbye! Have a great day.")
        exit()
    else:
        print("Sorry, I didn't understand that.")

# Main loop
greet_user()
while True:
    command = input("You: ").lower()
    respond(command)
