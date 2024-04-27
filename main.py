import streamlit as st
import pandas as pd

# Function to manage challan
def manage_challan():
    st.subheader("Manage Challan")

    # Add form to input challan details
    challan_number = st.text_input("Challan Number")
    customer_name = st.text_input("Customer Name")
    product_name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=1)
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Add Challan"):
        # Save challan details to a dataframe or database
        st.write("Challan Added Successfully!")

# Function to manage invoice
def manage_invoice():
    st.subheader("Manage Invoice")

    # Add form to input invoice details
    invoice_number = st.text_input("Invoice Number")
    customer_name = st.text_input("Customer Name")
    product_name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=1)
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Generate Invoice"):
        # Save invoice details to a dataframe or database
        st.write("Invoice Generated Successfully!")

# Function to manage site work
def manage_site_work():
    st.subheader("Manage Site Work")

    # Add form to input site work details
    project_name = st.text_input("Project Name")
    work_description = st.text_area("Work Description")
    work_hours = st.number_input("Work Hours", min_value=0)
    date = st.date_input("Date")

    if st.button("Add Site Work"):
        # Save site work details to a dataframe or database
        st.write("Site Work Added Successfully!")

# Function to manage expenses
def manage_expenses():
    st.subheader("Manage Expenses")

    # Add form to input expense details
    expense_type = st.selectbox("Expense Type", ["Material", "Equipment", "Labor", "Other"])
    amount = st.number_input("Amount", min_value=0.0)
    date = st.date_input("Date")
    description = st.text_area("Description")

    if st.button("Add Expense"):
        # Save expense details to a dataframe or database
        st.write("Expense Added Successfully!")

# Function to generate monthly finance summary
def generate_monthly_summary(data):
    st.subheader("Monthly Finance Summary")

    # Group data by month
    data['Month'] = pd.to_datetime(data['Date']).dt.to_period('M')
    monthly_summary = data.groupby('Month').agg({'Income': 'sum', 'Expenses': 'sum'}).reset_index()
    monthly_summary['Profit'] = monthly_summary['Income'] - monthly_summary['Expenses']

    st.write(monthly_summary)

# Function to generate yearly finance summary
def generate_yearly_summary(data):
    st.subheader("Yearly Finance Summary")

    # Group data by year
    data['Year'] = pd.to_datetime(data['Date']).dt.to_period('Y')
    yearly_summary = data.groupby('Year').agg({'Income': 'sum', 'Expenses': 'sum'}).reset_index()
    yearly_summary['Profit'] = yearly_summary['Income'] - yearly_summary['Expenses']

    st.write(yearly_summary)

# Function to calculate salary
def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

# Function to manage attendance
def manage_attendance():
    st.subheader("Attendance Management")

    # Add form to input attendance details
    employee_name = st.text_input("Employee Name")
    date = st.date_input("Date")
    hours_worked = st.number_input("Hours Worked", min_value=0)
    hourly_rate = st.number_input("Hourly Rate", min_value=0.0)

    if st.button("Add Attendance"):
        # Save attendance details to a dataframe or database
        st.write("Attendance Recorded Successfully!")

# Function to manage work reminders
def manage_work_reminders():
    st.subheader("Work Reminders")

    # Add form to input work reminder details
    reminder_name = st.text_input("Reminder Name")
    reminder_date = st.date_input("Reminder Date")
    reminder_description = st.text_area("Description")

    if st.button("Add Work Reminder"):
        # Save work reminder details to a dataframe or database
        st.write("Work Reminder Added Successfully!")

# Function to manage payment reminders
def manage_payment_reminders():
    st.subheader("Payment Reminders")

    # Add form to input payment reminder details
    reminder_name = st.text_input("Reminder Name")
    reminder_date = st.date_input("Reminder Date")
    reminder_description = st.text_area("Description")

    if st.button("Add Payment Reminder"):
        # Save payment reminder details to a dataframe or database
        st.write("Payment Reminder Added Successfully!")

# Main function to run the web app
def main():
    st.title("Online Software for Business Management")

    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Challan & Invoice", "Site Work & Expenses", "Finance Summary", "Salary & Attendance", "Reminders"))

    if page == "Home":
        st.subheader("Welcome to Online Software for Business Management")
        st.subheader("This project is under devlopment")
        st.subheader("Hosted for Client viewing purposes")
        st.subheader("Some features may not work")
        st.write("This software helps you manage various aspects of your business, including challan, invoice, site work, expenses, finance, salary, attendance, and reminders.")
   
    elif page == "Challan & Invoice":
        st.subheader("Challan & Invoice")
        option = st.selectbox("Select Option", ("Manage Challan", "Manage Invoice"))

        if option == "Manage Challan":
            manage_challan()
        elif option == "Manage Invoice":
            manage_invoice()

    elif page == "Site Work & Expenses":
        st.subheader("Site Work & Expenses")
        option = st.selectbox("Select Option", ("Site Work", "Expenses"))

        if option == "Site Work":
            manage_site_work()
        elif option == "Expenses":
            manage_expenses()
 
    elif page == "Finance Summary":
        st.subheader("Finance Summary")
        option = st.selectbox("Select Option", ("Monthly Summary", "Yearly Summary"))

        if option == "Monthly Summary":
            # Load finance data (sample data for demonstration)
            finance_data = pd.DataFrame({
                'Date': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15'],
                'Income': [1500, 2000, 1800, 2200],
                'Expenses': [500, 800, 700, 1000]
            })
            generate_monthly_summary(finance_data)

        elif option == "Yearly Summary":
            # Load finance data (sample data for demonstration)
            finance_data = pd.DataFrame({
                'Date': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15'],
                'Income': [1500, 2000, 1800, 2200],
                'Expenses': [500, 800, 700, 1000]
            })
            generate_yearly_summary(finance_data)

    elif page == "Salary & Attendance":
        st.subheader("Salary & Attendance")
        option = st.selectbox("Select Option", ("Calculate Salary", "Manage Attendance"))

        if option == "Calculate Salary":
            st.subheader("Automatic Salary Calculation")

            # Add form to input salary details
            hours_worked = st.number_input("Hours Worked", min_value=0)
            hourly_rate = st.number_input("Hourly Rate", min_value=0.0)

            if st.button("Calculate Salary"):
                salary = calculate_salary(hours_worked, hourly_rate)
                st.write(f"Salary for {hours_worked} hours worked at ${hourly_rate}/hour is ${salary}")

        elif option == "Manage Attendance":
            manage_attendance()

    elif page == "Reminders":
        st.subheader("Reminders")
        option = st.selectbox("Select Option", ("Work Reminders", "Payment Reminders"))

        if option == "Work Reminders":
            manage_work_reminders()
        elif option == "Payment Reminders":
            manage_payment_reminders()

    # Add other sections and their functionalities as per your requirements

if __name__ == "__main__":
    main()
