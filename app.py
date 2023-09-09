# app.py
from flask import Flask, render_template, request, redirect, url_for
from crontab import CronTab

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_job():
    job_command = request.form['command']
    cron_schedule = request.form['schedule']

    # Create a CronTab object
    cron = CronTab(user='your_username')

    # Create a new cron job
    job = cron.new(command=job_command)

    # Set the job schedule
    job.setall(cron_schedule)

    # Write the job to the user's crontab
    job.set_comment("Scheduled Job")
    cron.write()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
