from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    skills = request.form['skills']
    education = request.form['education']
    experience = request.form['experience']
    projects = request.form['projects']
    achievements = request.form['achievements']

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Resume", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"Skills: {skills}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Education: {education}")
    pdf.multi_cell(0, 10, txt=f"Experience: {experience}")
    pdf.multi_cell(0, 10, txt=f"Projects: {projects}")
    pdf.multi_cell(0, 10, txt=f"Achievements: {achievements}")

    file_path = "generated_resume.pdf"
    pdf.output(file_path)

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

