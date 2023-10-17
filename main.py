import pandas as pd
from datetime import date
import streamlit as st
from auth import *

# Configure Streamlit
st.set_page_config(page_title="Team Skills Management", layout="wide")


# Define a session state to manage login state
if 'authorized_session' not in st.session_state:
    #st.session_state['authorized_session'] = False
    #if st.session_state['authorized_session'] is False:
    st.title("Skills assessment - Login")
    with st.form("Login credentials"):
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        if st.form_submit_button("Login"):
            st.session_state['authorized_session'], msg = display_user(username, password)
            st.write(f"{msg}")

# Load data from file
data_file = "team_skills.csv"
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Employees', 'Skills', 'Level', 'Notes', 'Date'])

# Pre-defined skills list
skills_list = [
    "SQL clean code",
    "SQL - Python - Dataset building",
    "SQL / Python - Data preparation",
    "Communication - Storytelling",
    "Communication - Presentation building",
    "Python - Pandas - data manipulation",
    "Python - ETL - data acquisition",
    "Python - Airflow - create DAGs",
    "Linux - terminal and key commands",
    "Linux - Snake2prod - administration",
    "Tableau - clean code",
    "Tableau - clean viz"
]

admin_group = ["arso"]

# If a user is logged in, allow them to perform actions
if st.session_state['authorized_session']:
    st.sidebar.title("Team Skills Management")
    action = st.sidebar.selectbox("Select action:", ["Create Employee", "Remove Employee", "Add Skill", "Remove Skill"])

    if action == "Create Employee":
        new_employee = st.sidebar.text_input("Enter employee name:")
        if st.sidebar.button("Create"):
            if new_employee.strip() != "":
                new_row = pd.DataFrame(
                    {'Employees': [new_employee], 'Skills': [None], 'Level': [None], 'Notes': [None], 'Date': [None]})
                df = pd.concat([df, new_row], ignore_index=True)

                st.sidebar.success(f"Employee '{new_employee}' created successfully!")
            else:
                st.sidebar.warning("Please enter a valid employee name.")

    if action == "Remove Employee":
        selected_employee = st.sidebar.selectbox("Select employee:", sorted(set(df['Employees'])))
        if st.sidebar.button("Remove"):
            df = df[df['Employees'] != selected_employee]
            st.sidebar.success(f"Employee '{selected_employee}' removed successfully!")

    if action == "Add Skill":
        selected_employee = st.sidebar.selectbox("Select employee:", sorted(set(df['Employees'])))
        existing_skills = df[df['Employees'] == selected_employee]['Skills'].dropna().tolist()
        available_skills = list(set(skills_list) - set(existing_skills))
        if len(available_skills) == 0:
            st.sidebar.warning("No available skills to add.")
        else:
            selected_skill = st.sidebar.selectbox("Select skill:", available_skills)
            selected_level = st.sidebar.selectbox("Select level:", ['D1', 'D2', 'D3', 'D4'])
            notes = st.sidebar.text_input("Enter notes:")
            if st.sidebar.button("Add"):
                today = date.today().strftime("%Y-%m-%d")
                new_row = pd.DataFrame(
                    {'Employees': [selected_employee], 'Skills': [selected_skill], 'Level': [selected_level],
                     'Notes': [notes], 'Date': [today]})
                df = pd.concat([df, new_row], ignore_index=True)

                st.sidebar.success(
                    f"Skill '{selected_skill}' added for employee '{selected_employee}' successfully!")

    if action == "Remove Skill":
        selected_employee = st.sidebar.selectbox("Select employee:", sorted(set(df['Employees'])))
        existing_skills = df[df['Employees'] == selected_employee]['Skills'].dropna().tolist()
        if len(existing_skills) == 0:
            st.sidebar.warning("No skills to remove.")
        else:
            selected_skill = st.sidebar.selectbox("Select skill:", existing_skills)
            if st.sidebar.button("Remove"):
                df = df[(df['Employees'] != selected_employee) | (df['Skills'] != selected_skill)]
                st.sidebar.success(f"Skill '{selected_skill}' removed for employee '{selected_employee}' successfully!")

    # Filter data based on the logged-in user
    if st.session_state['authorized_session'] in admin_group:  # Admin users can see all employees and skills
        filtered_df = df
    else:
        filtered_df = df[df['Employees'] == session_state.logged_in_user]

    if len(filtered_df) > 0:
        # Display the filtered DataFrame
        st.markdown("<h1 style='text-align: center;'>Team Skills Management</h1>", unsafe_allow_html=True)
        st.table(filtered_df)
    else:
        st.warning("No skills data to display for this user.")

    # Store the modified DataFrame back to CSV
    df.to_csv(data_file, index=False)

    # Display the image
    st.image("dev_matrix.jpeg", width=500)
else:
    st.error("Seems you are not logged in...")
