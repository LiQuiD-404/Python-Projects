# Water Reminder - by Shubham Singh | github: LiQuiD-404
# both water_reminder.py and facts.py required for running this program

import time  # to create a delay after every reminder
from plyer import notification
import facts  # importing facts

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Take a Break! Have a glass of water",
            message=facts.fact_random(),
            app_icon="C:\\Users\\Shubham\\PycharmProjects\\python_GUI\\water reminder\\icon.ico", timeout=12)

        time.sleep(60*60)  # Reminds the user after every one hour
