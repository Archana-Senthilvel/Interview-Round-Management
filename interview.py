import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


def send_round_assignment_email(receiver_email, round_type, round_number):
    smtp_server = "smtp.gmail.com"
    port = 587
    username = os.getenv("YOUR_EMAIL")
    password = os.getenv("YOUR_PASSWORD")


    if not username or not password:
        st.error("Email credentials are not set. Please configure environment variables.")
        return False


    subject = f"Assignment for {round_type} - Round {round_number}"
    body = f"""
    <html>
      <body>
        <p>Dear Interviewer,</p>
        <p>You have been assigned to conduct {round_type} (Round {round_number}) for the upcoming interviews.</p>
        <p>Please ensure to follow the standard evaluation criteria and provide detailed feedback after the interviews.</p>
        <p>If you need any clarification or have questions, please feel free to reach out.</p>
        <p>Best regards,<br>HR Team</p>
      </body>
    </html>
    """


    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))


    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, receiver_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")
        return False


def main():
    st.title("Interview Rounds Selection")
   
    # Initialize session state
    if 'rounds' not in st.session_state:
        st.session_state.rounds = []
    if 'round_counter' not in st.session_state:
        st.session_state.round_counter = 1
    if 'email_inputs' not in st.session_state:
        st.session_state.email_inputs = {}
    if 'show_email_input' not in st.session_state:
        st.session_state.show_email_input = {}


    # Function to add new round
    def add_round():
        st.session_state.rounds.append({
            'number': st.session_state.round_counter,
            'type': None
        })
      st.session_state.round_counter += 1


    # Add Round button
    st.button("Add Round", on_click=add_round)


    # Display rounds and selection buttons
    for idx, round_data in enumerate(st.session_state.rounds):
        st.subheader(f"Round {round_data['number']}")
        col1, col2, col3, col4 = st.columns(4)
       
        with col1:
            if st.button("HR Round", key=f"hr_{idx}"):
                round_data['type'] = "HR Round"
        with col2:
            if st.button("Communication Round", key=f"comm_{idx}"):
                round_data['type'] = "Communication Round"
        with col3:
            if st.button("Technical Round", key=f"tech_{idx}"):
                round_data['type'] = "Technical Round"
        with col4:
            if st.button("Aptitude Round", key=f"apt_{idx}"):
                round_data['type'] = "Aptitude Round"
       
        # Display selected round type
        if round_data['type']:
            st.write(f"Selected: {round_data['type']}")


    # Display final structure with email functionality
    if st.session_state.rounds:
        st.subheader("Final Round Structure")
       
        for round_data in st.session_state.rounds:
            if round_data['type']:
                col1, col2 = st.columns([3, 1])
               
                with col1:
                    st.write(f"Round {round_data['number']} - {round_data['type']}")
               
                with col2:
                    round_key = f"round_{round_data['number']}"
                   
                    # Toggle button for email input
                    if st.button("Send Email", key=f"send_email_{round_data['number']}"):
                        st.session_state.show_email_input[round_key] = True


                # Show email input field if toggle is active
                if st.session_state.show_email_input.get(round_key, False):
                    email_col1, email_col2 = st.columns([3, 1])
                   
                    with email_col1:
                        email = st.text_input(
                            "Enter email address:",
                            key=f"email_{round_data['number']}"
                        )
                   
                    with email_col2:
                        if st.button("Submit", key=f"submit_{round_data['number']}"):
                            if email:
                                if send_round_assignment_email(email, round_data['type'], round_data['number']):
                                    st.success(f"Email sent successfully for Round {round_data['number']}!")
                                    # Hide the email input after successful sending
                                    st.session_state.show_email_input[round_key] = False
                            else:
                                st.error("Please enter an email address")


if __name__ == "__main__":
    main()
