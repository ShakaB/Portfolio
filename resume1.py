from pathlib import Path

import streamlit as st
from PIL import Image


def resume():
    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "main.css"
    resume_file = current_dir / "resumejb.pdf"
    profile_pic = current_dir / "resumepic.png"

    # --- GENERAL SETTINGS ---
    
    DESCRIPTION = """
    Aspiring Quantitative Developer pursuing a degree in Data Science.
    """
    EMAIL = "justinfborneo@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/justin-borneo-035ba1120/",
    
        
    }
    PROJECTS = {
        "🏆 Tata Consultancy Services (TCS), Data Visualization: Empowering Business with Effective Insights, The Forage" : "Collaborated in a team of 4 to perform EDA on Sales data to anticipate the needs of C-level executives using Python. Generated dashboards using Python and Tableau; helping C-level executives to reduce costs and increase profitability. Created and delivered a presentation to TCS data analytics member and made recommendations based on my findings.",
        "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
        "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
        "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
    }


    # --- LOAD CSS, PDF & PROFILE PIC ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    # --- HERO SECTION ---
    st.write('Please Click Arrow on the Left To View Projects')
    st.markdown(
    """
    <h1 style='text-align: center;'>Justin Borneo</h1>
    <p style='text-align: center;'>Queens, NY 11413 | justinfborneo@gmail.com | (718)-810-5036
    """,
    unsafe_allow_html=True
)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name='justin_borneo_resume',
            mime="application/octet-stream",
        )

        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f":briefcase: [{platform}]({link})")
        st.write('justinfborneo@gmail.com')
    # --- SOCIAL LINKS ---
    
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
    """
    - ✔️ Knowledge of Algorithmic Trading Techinques and Platforms
    - ✔️ Strong hands on experience and knowledge in Python
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
)


# --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy, yfinance, Quantstats), SQL
    - 📊 Data Visulization: PowerBi, Matplotlib, Plotly
    - 📚 Modeling: Logistic regression, Linear regression, Decision trees, LSTM
    - 🗄️ Databases: PostgreSQL, MySQL, Couchbase Server, Docker Desktop, Kafka, MindsDB
    - :sports_medal:  Certifications: Executive Programme in Algorithmic Trading (EPAT) QuantInsti (December 2023)
    """
)


# --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

# --- JOB 1
    st.write("🚧", "**Pipeline Manager | Reverse Mortgage Funding LLC**")
    st.write("Sept 2019 – Nov 2022")
    st.write(
        """
    - ► Conducted rigorous data analysis of credit, income, assets, and disclosures for loan applications, resulting in an increase in accurate risk assessments and informed decisions on loan approvals.
    - ► Enhanced communication and streamlined applications by sending personalized emails highlighting application issues, reducing processing time.
    """
    )

# --- JOB 2
    st.write('\n')
    st.write("🚧", "**Loan Processor | Sharestates**")
    st.write("April 2019 – September 2019")
    st.write(
        """
    - ► Implemented consistent borrower communication, reducing document retrieval time and streamlining the loan application process for enhanced customer satisfaction.
    - ► Analyzed 100+ complex loan transactions each month, reviewing and uploading loan documentation for accuracy and compliance.
    """
    )

# --- JOB 3
    st.write('\n')
    st.subheader("Virtual Work")
    st.write("---")
    st.write("Tata Consultancy Services (TCS), Data Visualization: Empowering Business with Effective Insights, The Forage")
    st.write("December 2023")
    st.write(
        """
    - ► Collaborated in a team of 4 to perform EDA on Sales data to anticipate the needs of C-level executives using Python.
    - ► Generated dashboards using Python and Tableau; helping C-level executives to reduce costs and increase profitability.
    - ► Created and delivered a presentation to TCS data analytics member and made recommendations based on my findings
    """
    )


if __name__ == "__main__":
    resume()
