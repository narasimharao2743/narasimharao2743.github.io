"""
Generates NARASIMHARAO_RESUME_GENAI.pdf directly (no LaTeX needed).
Mirrors NARASIMHARAO_RESUME_GENAI.tex content. Requires fpdf2.
Run: python generate_genai_resume.py
"""

from fpdf import FPDF

NAVY = (31, 58, 95)
DARK = (40, 40, 40)
GRAY = (95, 95, 95)
RULE = (150, 162, 178)

LEFT = 14
RIGHT = 14
TOP = 12
PAGE_W = 210
CONTENT_W = PAGE_W - LEFT - RIGHT
RIGHT_X = PAGE_W - RIGHT

FONT_DIR = "C:/Windows/Fonts/"

pdf = FPDF(format="A4", unit="mm")
pdf.set_auto_page_break(False)
pdf.set_margins(LEFT, TOP, RIGHT)
pdf.add_font("Calibri", "", FONT_DIR + "calibri.ttf")
pdf.add_font("Calibri", "B", FONT_DIR + "calibrib.ttf")
pdf.add_font("Calibri", "I", FONT_DIR + "calibrii.ttf")
pdf.add_page()

BULLET = chr(0x2022)
DASH = chr(0x2013)


def heading(title):
    pdf.ln(2.2)
    pdf.set_xy(LEFT, pdf.get_y())
    pdf.set_font("Calibri", "B", 11.5)
    pdf.set_text_color(*NAVY)
    pdf.cell(CONTENT_W, 5.2, title.upper())
    pdf.ln(5.5)
    y = pdf.get_y()
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.3)
    pdf.line(LEFT, y, RIGHT_X, y)
    pdf.ln(1.5)


def body_paragraph(text):
    pdf.set_xy(LEFT, pdf.get_y())
    pdf.set_font("Calibri", "", 9.4)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(CONTENT_W, 4.3, text, align="J")


def skill_line(label, items):
    y0 = pdf.get_y()
    pdf.set_xy(LEFT, y0)
    pdf.set_font("Calibri", "B", 9.4)
    pdf.set_text_color(*NAVY)
    lt = label + ":  "
    lw = pdf.get_string_width(lt)
    pdf.cell(lw, 4.6, lt)
    pdf.set_font("Calibri", "", 9.4)
    pdf.set_text_color(*DARK)
    pdf.set_xy(LEFT + lw, y0)
    pdf.multi_cell(CONTENT_W - lw, 4.6, items)


def exp_header(role, dates, company):
    y0 = pdf.get_y()
    pdf.set_xy(LEFT, y0)
    pdf.set_font("Calibri", "B", 10.5)
    pdf.set_text_color(*DARK)
    pdf.cell(CONTENT_W / 2, 5, role, align="L")
    pdf.set_xy(LEFT + CONTENT_W / 2, y0)
    pdf.set_font("Calibri", "I", 9.3)
    pdf.set_text_color(*GRAY)
    pdf.cell(CONTENT_W / 2, 5, dates, align="R")
    pdf.ln(5)
    pdf.set_xy(LEFT, pdf.get_y())
    pdf.set_font("Calibri", "B", 9.7)
    pdf.set_text_color(*NAVY)
    pdf.cell(CONTENT_W, 4.6, company)
    pdf.ln(4.9)


def bullet(text):
    indent = 4.0
    y0 = pdf.get_y()
    pdf.set_xy(LEFT, y0)
    pdf.set_font("Calibri", "", 9.3)
    pdf.set_text_color(*NAVY)
    pdf.cell(indent, 4.2, BULLET)
    pdf.set_xy(LEFT + indent, y0)
    pdf.set_text_color(*DARK)
    pdf.multi_cell(CONTENT_W - indent, 4.2, text, align="J")


def edu_line(degree, place, dates, cgpa):
    y0 = pdf.get_y()
    pdf.set_xy(LEFT, y0)
    pdf.set_font("Calibri", "B", 9.5)
    pdf.set_text_color(*DARK)
    deg = degree + "  " + BULLET + "  "
    dw = pdf.get_string_width(deg)
    pdf.cell(dw, 4.7, deg)
    pdf.set_font("Calibri", "", 9.3)
    pdf.cell(0, 4.7, place)
    pdf.set_xy(LEFT, y0)
    pdf.set_font("Calibri", "I", 9.0)
    pdf.set_text_color(*GRAY)
    pdf.cell(CONTENT_W, 4.7, dates + "    " + cgpa, align="R")
    pdf.ln(4.9)


# ============================ HEADER ============================
pdf.set_xy(LEFT, TOP)
pdf.set_font("Calibri", "B", 23)
pdf.set_text_color(*NAVY)
pdf.cell(CONTENT_W, 10, "Narasimharao Bhavirisetty", align="C")
pdf.ln(10)

pdf.set_xy(LEFT, pdf.get_y())
pdf.set_font("Calibri", "", 11)
pdf.set_text_color(*DARK)
pdf.cell(CONTENT_W, 5,
         "Software Engineer  " + BULLET +
         "  Backend, Data Engineering & GenAI", align="C")
pdf.ln(5.6)

pdf.set_xy(LEFT, pdf.get_y())
pdf.set_font("Calibri", "", 9.3)
pdf.set_text_color(*GRAY)
pdf.cell(CONTENT_W, 4.5,
         "+91 63032 27485  " + BULLET +
         "  narasimharao2743@gmail.com  " + BULLET +
         "  linkedin.com/in/narasimharao-bhavirisetty-0526891b0", align="C")
pdf.ln(5.4)

y = pdf.get_y()
pdf.set_draw_color(*NAVY)
pdf.set_line_width(0.5)
pdf.line(LEFT, y, RIGHT_X, y)

# ====================== PROFESSIONAL SUMMARY ======================
heading("Professional Summary")
body_paragraph(
    "Software Engineer with 1.7 years of experience in event-driven backend "
    "systems and real-time data pipelines " + DASH + " processing 50K+ trade "
    "events daily through Kafka, ClickHouse, and Redis with millisecond-level "
    "latency, with a proven 40% improvement in data extraction accuracy at "
    "Algonox. Hands-on GenAI expertise in RAG pipelines, vector search, model "
    "inferencing, and prompt engineering " + DASH + " built to contribute "
    "across enterprise data infrastructure and AI-driven application layers."
)

# ======================= TECHNICAL SKILLS ========================
heading("Technical Skills")
skill_line("GenAI", "RAG, Vector Search, Model Inferencing, Prompt Engineering, "
                    "LangChain, HuggingFace, Groq, Ollama")
skill_line("Languages", "Python, Java")
skill_line("Databases", "MySQL, MSSQL, PostgreSQL, ClickHouse, Redis, ChromaDB")
skill_line("Stream Processing", "Apache Kafka, Redpanda, PyFlink")
skill_line("Frameworks & Tools", "Flask, Docker, Kubernetes, Git, Postman, Linux")
skill_line("Concepts", "REST APIs, Microservices, Distributed Systems, "
                       "Event-Driven Architecture, OOP, Agile, SDLC")

# ===================== PROFESSIONAL EXPERIENCE ====================
heading("Professional Experience")
exp_header("Software Engineer", "December 2025 " + DASH + " May 2026",
           "Spizen Technologies (CLR3 Ventures), Bangalore, India")
bullet("Designed and built a real-time data pipeline processing 50K+ trade "
       "events per day through Kafka, PyFlink, ClickHouse, and Redis, "
       "enabling live tracking and analytics on trading activity.")
bullet("Built reliable stream processing jobs that automatically detect and "
       "remove duplicate records with 95% accuracy, ensuring clean data for "
       "all downstream analytics.")
bullet("Developed an automated classification system to identify suspicious "
       "trading patterns and bot activity, improving the quality of "
       "investment signals on the platform.")
bullet("Built a real-time scoring system that evaluates every trade event "
       "and generates live investment signals within milliseconds using "
       "multiple quality metrics.")
pdf.ln(1.4)
exp_header("Software Engineer", "September 2024 " + DASH + " December 2025",
           "Algonox Technologies Pvt Ltd, Hyderabad, India")
bullet("Boosted document data extraction accuracy by 40% by implementing "
       "multi-layered business rule validation to clean and reconcile "
       "noisy, unstructured input data at scale.")
bullet("Built an automated email notification microservice for file queue "
       "transitions and SLA failure alerts, reducing manual monitoring "
       "overhead and improving response time.")
bullet("Developed an automated KPI reporting module tracking extraction "
       "accuracy and manual intervention rates, enabling data-driven "
       "reviews and a 20% reduction in manual QA effort.")
bullet("Built a scheduled module to automatically manage user account "
       "states based on inactivity periods, ensuring only active users "
       "retain system access and improving security compliance.")

# ====================== PERSONAL PROJECTS =========================
heading("Personal Projects")
pdf.set_xy(LEFT, pdf.get_y())
pdf.set_font("Calibri", "B", 10.2)
pdf.set_text_color(*DARK)
pdf.cell(CONTENT_W, 4.8, "RAG-based PDF Q&A System")
pdf.ln(5.0)
bullet("Built an end-to-end RAG pipeline ingesting PDFs, generating "
       "HuggingFace vector embeddings, and indexing in ChromaDB " + DASH +
       " exposed via a Flask REST API for natural language querying with "
       "source-cited answers.")
bullet("Integrated Groq Cloud LLM API (llama-3.1-8b-instant) through "
       "LangChain LCEL pipelines, delivering sub-second context-grounded "
       "answers with source citations.")

# ========================== EDUCATION ============================
heading("Education")
edu_line("B.Tech in Computer Science",
         "Tirumala Engineering College, Narasaraopet",
         "2020 " + DASH + " 2024", "CGPA: 7.86/10")
edu_line("Intermediate (MPC)",
         "Bhavana Junior College, Narasaraopet",
         "2018 " + DASH + " 2020", "CGPA: 9.46/10")
edu_line("SSC",
         "Sindhu High School, Narasaraopet",
         "2017 " + DASH + " 2018", "CGPA: 10/10")

# ======================== CERTIFICATIONS ==========================
heading("Certifications")
bullet("Microsoft " + DASH + " Azure AI Fundamentals")
bullet("AWS " + DASH + " AI and Machine Learning")

pdf.output("NARASIMHARAO_RESUME_GENAI.pdf")
print(f"Saved: NARASIMHARAO_RESUME_GENAI.pdf  |  final y = {pdf.get_y():.1f} mm "
      f"(page height 297 mm)")
