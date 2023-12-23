from pathlib import Path

import streamlit as st
from PIL import Image

from pathlib import Path
import streamlit as st
from PIL import Image

def resume():
    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = "main.css"
    resume_file = "resumejb.pdf"
    profile_pic = "resumepic.png"

    # --- GENERAL SETTINGS ---
    
    DESCRIPTION = """
    Aspiring Quantitative Analyst pursuing a degree in Data Science.
    """
    EMAIL = "justinfborneo@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/justin-borneo-035ba1120/",
        
    }
    PROJECTS = {
        "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
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
    # --- SOCIAL LINKS ---
    
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
    """
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    - ✔️ Knowledge of Algorithmic Trading Techinques and Platforms
    """
)


# --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
    - 📊 Data Visulization: PowerBi, Matplotlib, Plotly
    - 📚 Modeling: Logistic regression, Linear regression, Decision trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL, MindsDB
    """
)


# --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

# --- JOB 1
    st.write("🚧", "**Pipeline Manager | Reverse Mortgage Funding LLC**")
    st.write("09/2019 - Nov 2022")
    st.write(
        """
    - ► Conducted rigorous data analysis of credit, income, assets, and disclosures for loan applications, resulting in an increase in accurate risk assessments and informed decisions on loan approvals.
    - ► Enhanced communication and streamlined applications by sending personalized emails highlighting application issues, reducing processing time.
    """
    )

# --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

# --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )


# --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

    # ... (rest of your sections)

if __name__ == "__main__":
    resume()
