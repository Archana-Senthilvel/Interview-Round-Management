# Interview Round Management System

## Overview
The **Interview Round Management System** is a streamlined web application designed to help HR teams manage and assign interview rounds efficiently. Built using **Streamlit**, the application provides functionality to create and organize interview rounds, assign types of interviews, and send email notifications to interviewers with round-specific details.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Interview-Round-Management
2. Set Up Virtual Environment:

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

pip install streamlit python-dotenv

4. Configure Environment Variables: Create a .env file in the project directory with the following contents:

YOUR_EMAIL=your_email_address@gmail.com

YOUR_PASSWORD=your_email_password

Replace your_email_address@gmail.com and your_email_password with valid SMTP credentials.

5. Run the Application:

streamlit run app.py

6. Access the Application: Open your browser and navigate to http://localhost:8501.

## Usage

1. Add Interview Rounds:

Click the Add Round button to create a new round.
Assign a type to each round (HR, Communication, Technical, Aptitude) using the provided buttons.

2. Send Email Notifications:

Click the Send Email button for a specific round to open the email input field.
Enter the interviewer's email address and click Submit to send an assignment email.

3. Monitor Round Structure:

View the dynamic list of rounds and their assigned types on the Final Round Structure section.
