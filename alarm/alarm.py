from flask import Flask, render_template, request, jsonify
import time
import threading

app = Flask(__name__)

alarm_set = False
alarm_time = ""
alarm_triggered = False

def alarm_check():
    global alarm_set, alarm_time, alarm_triggered
    while True:
        if alarm_set and time.strftime("%H:%M") == alarm_time:
            alarm_triggered = True
            alarm_set = False
        time.sleep(1)

@app.route("/", methods=["GET", "POST"])
def index():
    global alarm_set, alarm_time, alarm_triggered
    if request.method == "POST":
        alarm_time = request.form["alarm_time"]
        alarm_set = True
        alarm_triggered = False
    return render_template("alarm.html")

@app.route("/status")
def status():
    return jsonify(triggered=alarm_triggered)

if __name__ == "__main__":
    threading.Thread(target=alarm_check, daemon=True).start()
    app.run(debug=True)
