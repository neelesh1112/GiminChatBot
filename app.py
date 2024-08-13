# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
# import time

# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":robot_face:",  # Favicon emoji
#     layout="wide",  # Set layout to wide to accommodate sidebar
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     return "assistant" if user_role == "model" else user_role

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Custom CSS to change GUI colors
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f0f0f0;
#         color: #333;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#     }
#     .stTextInput>div>div>input {
#         background-color: #f9f9f9;
#         border: 1px solid #ccc;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Sidebar for displaying chat history
# with st.sidebar:
#     st.header("Chat History")
#     # Display the chat history in the sidebar
#     for message in st.session_state.chat_session.history:
#         st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# # Main area for chatbot interaction
# st.title("🤖 Gemini Pro - ChatBot")

# # Display the chat history in the main area
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro... 💬")
# if user_prompt:
#     # Add user's message to chat and display it with an emoji
#     st.chat_message("user").markdown(f"👨‍💻 {user_prompt}")

#     # Display loading effect with emojis
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = "🤖 Thinking"
#         for _ in range(5):  # Simulate a loading effect
#             full_response += "."
#             message_placeholder.markdown(full_response)
#             time.sleep(0.2)

#     try:
#         # Send user's message to Gemini-Pro and get the response
#         gemini_response = st.session_state.chat_session.send_message(user_prompt)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#     else:
#         # Display Gemini-Pro's response with an emoji
#         with st.chat_message("assistant"):
#             st.markdown(f"🤖 {gemini_response.text}")
        
#         # Update the chat history in the sidebar
#         with st.sidebar:
#             st.header("Chat History")
#             for message in st.session_state.chat_session.history:
#                 st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")





# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
# import time

# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":robot_face:",  # Favicon emoji
#     layout="wide",  # Set layout to wide to accommodate sidebar
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     return "assistant" if user_role == "model" else user_role

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Custom CSS to change GUI colors
# st.markdown(
#     """
#     <style>
#     /* Background color for the whole page */
#     body {
#         background-color: #e3f2fd; /* Light blue */
#         color: #333; /* Dark text color */
#     }
#     /* Sidebar background color */
#     .css-1v0mbdj {
#         background-color: #b3e5fc; /* Light blue */
#         color: #000000; /* Dark text color */
#     }
#     /* Sidebar header styling */
#     .css-1v0mbdj .css-1v0mbdj {
#         color: #000000; /* Dark text color */
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #03a9f4; /* Light blue */
#         color: white;
#         border: none;
#     }
#     .stButton>button:hover {
#         background-color: #0288d1; /* Darker blue on hover */
#     }
#     /* Text input field styling */
#     .stTextInput>div>div>input {
#         background-color: #ffffff; /* White background */
#         border: 1px solid #03a9f4; /* Light blue border */
#     }
#     /* Chat message styling */
#     .css-1v0mbdj .stMarkdown {
#         color: #0277bd; /* Darker blue for chat messages */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Sidebar for displaying chat history
# with st.sidebar:
#     st.header("Chat History")
#     # Display the chat history in the sidebar
#     for message in st.session_state.chat_session.history:
#         st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# # Main area for chatbot interaction
# st.title("🤖 Gemini Pro - ChatBot")

# # Display the chat history in the main area
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro... 💬")
# if user_prompt:
#     # Add user's message to chat and display it with an emoji
#     st.chat_message("user").markdown(f"👨‍💻 {user_prompt}")

#     # Display loading effect with emojis
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = "🤖 Thinking"
#         for _ in range(5):  # Simulate a loading effect
#             full_response += "."
#             message_placeholder.markdown(full_response)
#             time.sleep(0.2)

#     try:
#         # Send user's message to Gemini-Pro and get the response
#         gemini_response = st.session_state.chat_session.send_message(user_prompt)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#     else:
#         # Display Gemini-Pro's response with an emoji
#         with st.chat_message("assistant"):
#             st.markdown(f"🤖 {gemini_response.text}")
        
#         # Update the chat history in the sidebar
#         with st.sidebar:
#             st.header("Chat History")
#             for message in st.session_state.chat_session.history:
#                 st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")


# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
# import time

# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":robot_face:",  # Favicon emoji
#     layout="wide",  # Set layout to wide to accommodate sidebar
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     return "assistant" if user_role == "model" else user_role

# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# # Function to clear chat history
# def clear_chat_history():
#     st.session_state.chat_session.history = []
#     st.session_state.chat_session = model.start_chat(history=[])
#     st.sidebar.write("Chat history cleared.")

# # Custom CSS to change GUI colors
# st.markdown(
#     """
#     <style>
#     /* Background color for the whole page */
#     body {
#         background-color: #e3f2fd; /* Light blue */
#         color: #333; /* Dark text color */
#     }
#     /* Sidebar background color */
#     .css-1v0mbdj {
#         background-color: #b3e5fc; /* Light blue */
#         color: #000000; /* Dark text color */
#     }
#     /* Sidebar header styling */
#     .css-1v0mbdj .css-1v0mbdj {
#         color: #000000; /* Dark text color */
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #03a9f4; /* Light blue */
#         color: white;
#         border: none;
#     }
#     .stButton>button:hover {
#         background-color: #0288d1; /* Darker blue on hover */
#     }
#     /* Text input field styling */
#     .stTextInput>div>div>input {
#         background-color: #ffffff; /* White background */
#         border: 1px solid #03a9f4; /* Light blue border */
#     }
#     /* Chat message styling */
#     .css-1v0mbdj .stMarkdown {
#         color: #0277bd; /* Darker blue for chat messages */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Sidebar for clearing chat history
# with st.sidebar:
#     st.header("Chat History")
#     # Button to clear chat history with a unique key
#     if st.button("Clear History", key="clear_history_sidebar"):
#         clear_chat_history()
#     # Display user inputs in the sidebar
#     if st.session_state.chat_session.history:
#         for message in st.session_state.chat_session.history:
#             if message.role == 'user':
#                 st.markdown(f"👨‍💻 {message.parts[0].text}")
#     else:
#         st.write("No chat history to display.")

# # Main area for chatbot interaction
# st.title("🤖 Hi There, How may I assist you ?")

# # Display the chat history in the main area
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# # Input field for user's message
# user_prompt = st.chat_input("Ask to me I'm here to help you! 💬")
# if user_prompt:
#     # Add user's message to chat and display it with an emoji
#     st.chat_message("user").markdown(f"👨‍💻 {user_prompt}")

#     # Display loading effect with a typing simulation
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         simulated_typing = "🤖 Cooking your response..."
#         for i in range(3):  # Simulate a typing effect
#             message_placeholder.markdown(f"{simulated_typing}{'.' * (i + 1)}")
#             time.sleep(0.5)

#         try:
#             # Send user's message to Gemini-Pro and get the response
#             gemini_response = st.session_state.chat_session.send_message(user_prompt)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#         else:
#             # Display Gemini-Pro's response with a faster typing effect
#             response_text = ""
#             for char in gemini_response.text:
#                 response_text += char
#                 message_placeholder.markdown(f"🤖 {response_text}")
#                 time.sleep(0.01)  # Faster typing effect








import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import time

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":robot_face:",  # Favicon emoji
    layout="wide",  # Set layout to wide to accommodate sidebar
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Function to clear chat history
def clear_chat_history():
    st.session_state.chat_session.history = []
    st.session_state.chat_session = model.start_chat(history=[])
    st.sidebar.write("Chat history cleared.")

# Custom CSS to change GUI colors and fix the copyright disclaimer at the bottom
st.markdown(
    """
    <style>
    /* Background color for the whole page */
    body {
        background-color: #e3f2fd; /* Light blue */
        color: #333; /* Dark text color */
    }
    /* Sidebar background color */
    .css-1v0mbdj {
        background-color: #b3e5fc; /* Light blue */
        color: #000000; /* Dark text color */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    /* Sidebar header styling */
    .css-1v0mbdj .css-1v0mbdj {
        color: #000000; /* Dark text color */
    }
    /* Button styling */
    .stButton>button {
        background-color: #03a9f4; /* Light blue */
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0288d1; /* Darker blue on hover */
    }
    /* Text input field styling */
    .stTextInput>div>div>input {
        background-color: #ffffff; /* White background */
        border: 1px solid #03a9f4; /* Light blue border */
    }
    /* Chat message styling */
    .css-1v0mbdj .stMarkdown {
        color: #0277bd; /* Darker blue for chat messages */
    }
    /* Position the copyright disclaimer at the bottom of the sidebar */
    .copyright-disclaimer {
        text-align: center;
        display: table-cell;
        vertical-align: bottom;
        padding: 10px 0;
        font-size: 12px;
        color: 	#A8A8A8; /* white text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for clearing chat history
with st.sidebar:
    st.header("Chat History")
    # Button to clear chat history with a unique key
    if st.button("Clear History", key="clear_history_sidebar"):
        clear_chat_history()
    # Display user inputs in the sidebar
    if st.session_state.chat_session.history:
        for message in st.session_state.chat_session.history:
            if message.role == 'user':
                st.markdown(f"👨‍💻 {message.parts[0].text}")
    else:
        st.write("No chat history to display.")

# Main area for chatbot interaction
st.title("🤖 Hi There, How may I assist you ?")

# Display the chat history in the main area
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(f"{'👨‍💻' if message.role == 'user' else '🤖'} {message.parts[0].text}")

# Input field for user's message
user_prompt = st.chat_input("Ask to me, I'm here to help you... 💬")
if user_prompt:
    # Add user's message to chat and display it with an emoji
    st.chat_message("user").markdown(f"👨‍💻 {user_prompt}")

    # Display loading effect with a typing simulation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        emoji_sequence = ["🍳", "🏗️", "🚗", "💻", "🎯", "🚀", "🎨", "📚", "🎶", "📊"]  # Randomized emojis
        for i in range(20):  # Simulate a typing effect
            message_placeholder.markdown(f"{emoji_sequence[i % len(emoji_sequence)]} Preparing your response...")
            time.sleep(0.2)

        try:
            # Send user's message to Gemini-Pro and get the response
            gemini_response = st.session_state.chat_session.send_message(user_prompt)
        except Exception as e:
            st.error(f"An error occurred: {e}")
        else:
            # Display Gemini-Pro's response with a faster typing effect
            response_text = ""
            for char in gemini_response.text:
                response_text += char
                message_placeholder.markdown(f"🤖 {response_text}")
                time.sleep(0.01)  # Faster typing effect

# Add a copyright disclaimer with your name at the bottom of the sidebar
st.sidebar.markdown('<div class="copyright-disclaimer" >© 2024 Neelesh. All rights reserved.</div>', unsafe_allow_html=True)
