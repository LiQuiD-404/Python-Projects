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
            app_icon="<location of the icon.ico file>", timeout=12)

        time.sleep(60*60)  # Reminds the user after every one hour
