from fpdf import FPDF


def generate_pdf(form_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt="Resume", ln=True, align="C")
    pdf.ln(10)

    # Personal Info
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {form_data['name']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {form_data['email']}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {form_data['phone']}", ln=True)
    pdf.ln(5)

    # Education
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=form_data['education'])
    pdf.ln(5)

    # Skills
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=form_data['skills'])
    pdf.ln(5)

    # Projects
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Projects", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=form_data['projects'])
    pdf.ln(5)

    # Achievements
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Achievements", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=form_data['achievements'])

    return pdf
