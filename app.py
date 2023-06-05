from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'Kuala Lumpur, Malaysia',
    'salary': 'RM 8,000'
  },
  {
    'id': 4,
    'title': 'Frontend Developer',
    'location': 'New York, America',
    # 'salary': ''
  }
]


@app.route("/")
def hello():
  # return "Hello, Hanz"
  return render_template('home.html', jobs=JOBS, company_name='Hanz')


@app.route("/api/jobs")
def list_jobs():
  # return "Hello, Hanz"
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
