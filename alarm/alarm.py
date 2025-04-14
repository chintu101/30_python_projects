from flask import Flask, render_template, request
import time
import threading

app = Flask(__name__)

alarm_set = False
alarm_time = ""

def alarm_check():
    global alarm_set, alarm_time
    while True:
        if alarm_set and time.strftime("%H:%M") == alarm_time:
            alarm_set = False  # reset after triggering
            print("Time to wake up!")  # could be extended to play sound, etc.
        time.sleep(1)

@app.route("/", methods=["GET", "POST"])
def index():
    global alarm_set, alarm_time
    message = ""
    if request.method == "POST":
        alarm_time = request.form["alarm_time"]
        alarm_set = True
        message = f"Alarm set for {alarm_time}"
    return render_template("alarm.html", message=message)

if __name__ == "__main__":
    threading.Thread(target=alarm_check, daemon=True).start()
    app.run(debug=True)
