import streamlit as st


def display_profile():
    st.markdown(
        """
        <h1 style='text-align: center;'>Justin Borneo</h1>
        <p style='text-align: center;'>Queens, NY 11413 | justinfborneo@gmail.com | (718)-810-5036 | <a href="https://www.linkedin.com/in/justin-borneo-035ba1120/" target="_blank">LinkedIn</a></p>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style='text-align: center;'>
            <p>Aspiring Quantitative Analyst pursuing a degree in Data Science. Excels at quantitative analysis, quantitative development, and data analysis.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("TECHNICAL SKILLS")
    st.write("Programming Languages: Python, SQL, N1QL")
    st.write("Database Management: PostgreSQL, MySQL, Couchbase Server, Docker Desktop, Kafka, MinsDB, AI databases")
    st.write("Data Visualization Tools: Microsoft Excel")
    st.write("Libraries: Pandas, Matplotlib, NumPy, Plotly, QuantStats, yfinance, Zipline, Blueshift, RESTful APIs")
    st.write("Machine Learning Algorithms: Scikit-Learn, SciPy, Sklearn, TensorFlow")
    st.write("Certifications: Executive Programme in Algorithmic Trading (EPAT) QuantInsti (December 2023)")

    st.title("PROJECTS / VIRTUAL WORK SIMULATION")
    st.write("**Tata Consultancy Services (TCS), Data Visualization: Empowering Business with Effective Insights, The Forage | December 2023**")
    st.write("- Collaborated in a team of 4 to perform EDA on Sales data to anticipate the needs of C-level executives using Python.")
    st.write("- Generated dashboards using Python and Tableau; helping C-level executives to reduce costs and increase profitability.")
    st.write("- Created and delivered a presentation to TCS data analytics member and made recommendations based on my findings.")

    st.write("**Trading With Stats: Using the GARCH Model to trade META**")
    st.write("- Used the GARCH model to predict volatility in the S&P 500 and trade META based on predictions")

    st.write("**Risk Analysis: META**")
    st.write("- Looks at Historical VaR and CVAR, and Monte Carlo Simulated VaR and CVaR risk measures of META stock price.")

    st.title("PROFESSIONAL EXPERIENCE")
    st.write("**Reverse Mortgage Funding LLC, Melville, NY | Intake Coordinator/Pipeline Manager | Sept 2019 – Nov 2022**")
    st.write("- Conducted rigorous data analysis of credit, income, assets, and disclosures for loan applications, resulting in an increase in accurate risk assessments and informed decisions on loan approvals.")
    st.write("- Enhanced communication and streamlined applications by sending personalized emails highlighting application issues, reducing processing time.")

    st.write("**Sharestates, Great Neck, NY | Loan Processor | April 2019 – September 2019**")
    st.write("- Implemented consistent borrower communication, reducing document retrieval time and streamlining the loan application process for enhanced customer satisfaction.")
    st.write("- Analyzed 100+ complex loan transactions each month, reviewing and uploading loan documentation for accuracy and compliance.")


    
    

def display_project():
    st.title("PROJECT: Trading With Stats")
    st.write("Using the GARCH Model to trade META")

    