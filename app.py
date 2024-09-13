import random

from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
from datetime import datetime


app = Flask(__name__)


# Route for landing page - upload or create new JSON
@app.route('/')
def index():
    return render_template('index.html')


# Route for uploading a JSON file
@app.route('/upload', methods=['POST'])
def upload_json():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.json'):
        data = json.load(file)
        return redirect(url_for('dashboard', data=data))

    return "Invalid file format. Please upload a JSON file."


# Route for creating a new JSON file
@app.route('/create_new', methods=['POST'])
def create_new_json():
    # Create a new JSON structure
    data = {
        "Jobs": []
    }
    # Save the file locally
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    return redirect(url_for('dashboard'))


# Route to display the dashboard with jobs in a table






@app.route('/dashboard')
def dashboard():
    if not os.path.exists('data.json'):
        # If the file doesn't exist, create an empty JSON structure with 'Jobs'
        data = {"Jobs": []}
        with open('data.json', 'w') as f:
            json.dump(data, f)
    else:
        # Load existing data from JSON file
        with open('data.json') as f:
            data = json.load(f)

    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('dashboard.html', jobs=data['Jobs'], current_date=current_date)


# Route for adding a new job
def generate_unique_job_id(existing_ids):
    while True:
        job_id = random.randint(1, 10000)  # Adjust range if necessary
        if job_id not in existing_ids:
            return job_id

# Route for adding a new job
@app.route('/add_job', methods=['POST'])
def add_job():
    # Retrieve the form data
    job_position = request.form['job_position']
    company_name = request.form['company_name']
    date_of_application = request.form['date_of_application'] or datetime.now().strftime('%Y-%m-%d')
    req_id = request.form.get('req_id', '')
    location = request.form.get('location', '')
    salary = request.form.get('salary', '')
    related = request.form.get('related', 0)

    # Load existing jobs data
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    # Get existing job IDs
    existing_ids = {job['job_id'] for job in data['Jobs']}

    # Generate a unique job ID
    job_id = generate_unique_job_id(existing_ids)

    # Create a new job entry
    new_job = {
        'job_id': job_id,
        'job_position': job_position,
        'company_name': company_name,
        'date_of_application': date_of_application,
        'req_id': req_id,
        'location': location,
        'salary': salary,
        'related': related,
        'status': 'In Progress'  # Set default status for new jobs
    }

    # Add new job to the list and save it
    data['Jobs'].append(new_job)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    return redirect(url_for('dashboard'))


@app.route('/update_status', methods=['POST'])
def update_status():
    job_id = request.form['job_id']
    new_status = request.form['status']

    # Load existing jobs data
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    # Find and update the job with the given job_id
    for job in data['Jobs']:
        if str(job['job_id']) == str(job_id):
            job['status'] = new_status
            break

    # Save the updated data back to the JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    return jsonify({'success': True})

def delete_job_from_database(job_id):
    # Load existing jobs data
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    # Filter out the job with the given job_id
    initial_count = len(data['Jobs'])
    data['Jobs'] = [job for job in data['Jobs'] if str(job['job_id']) != str(job_id)]

    if len(data['Jobs']) < initial_count:  # Check if a job was actually removed
        # Save the updated list back to the JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
        return True  # Job was successfully deleted
    return False  # Job not found
@app.route('/delete_job/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    # Logic to delete the job from the database
    # Return a JSON response indicating success or failure
    success = delete_job_from_database(job_id)  # Implement the actual deletion logic
    return jsonify({'success': success})


@app.route('/company_suggestions', methods=['GET'])
def company_suggestions():
    query = request.args.get('query', '').lower()
    jobs = load_jobs_data()  # Load jobs from the JSON file
    company_names = set(job['company_name'] for job in jobs['Jobs'])
    # company_names = list({job['company_name'] for job in jobs['Jobs']})
    # Filter company names based on the user's input query
    suggestions = [name for name in company_names if query in name.lower()]

    print(suggestions)

    return jsonify(suggestions)

def load_jobs_data():
    with open('data.json', 'r') as f:
        return json.load(f)


@app.route('/analysis')
def analysis():
    # Path to the data.json file
    data_file_path = 'data.json'

    # Ensure the file exists
    if not os.path.isfile(data_file_path):
        return "Data file not found.", 404

    # Read data from the JSON file
    with open(data_file_path, 'r') as file:
        data = json.load(file)

    # Extract jobs from data
    jobs = data.get('Jobs', [])

    # Pass jobs data to the analysis.html template
    return render_template('analysis.html', jobs=jobs)

def load_jobs():
    with open('data.json') as f:
        data = json.load(f)
    return data['Jobs']


# Route to edit a job by job_id
@app.route('/editjob/<int:job_id>', methods=['GET', 'POST'])
def editjob(job_id):
    jobs = load_jobs()  # Load all jobs from data.json

    job_details = next((job for job in jobs if job['job_id'] == job_id), None)

    if request.method == 'POST':
        # Update job details with form data
        job_details['job_position'] = request.form.get('job_position')
        job_details['company_name'] = request.form.get('company_name')
        job_details['date_of_application'] = request.form.get('date_of_application')
        job_details['location'] = request.form.get('location')
        job_details['salary'] = request.form.get('salary')
        job_details['related'] = request.form.get('related')
        job_details['status'] = request.form.get('status')

        # Save updated jobs back to the file
        with open('data.json', 'w') as f:
            json.dump({"Jobs": jobs}, f, indent=4)

        return jsonify({"success": True})

    return render_template('EditJob.html', job=job_details)

if __name__ == '__main__':
    app.run(debug=True)
