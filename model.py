import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API Key


genai.configure(api_key="AIzaSyD4T5_tMAIF_UUgBCY68tPkzj_ZlhXylws")


# Load the Gemini mode
model = genai.GenerativeModel('gemini-1.5-flash')

# Set up the Streamlit app
def main():
    # App title and description
    st.title("WAT/GD Preparation Helper")
    st.subheader("Prepare effectively for your Written Ability Test (WAT) or Group Discussion (GD) on any topic of your choice.")

    # Input topic
    topic = st.text_input("Enter a topic for preparation:", placeholder="e.g., Climate Change, Artificial Intelligence")

    if topic:
        st.write(f"You have entered: **{topic}**")

        # Buttons for WAT and GD
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Prepare for WAT"):
                prepare_for_wat(topic)
        with col2:
            if st.button("Prepare for GD"):
                prepare_for_gd(topic)

# Function to fetch WAT content
def prepare_for_wat(topic):
    st.subheader("WAT Preparation")
    st.write("Fetching content for WAT preparation...")

    # Generate content using Gemini API
    response = generate_content(f"Write a detailed article for a Written Ability Test (WAT) on the topic: {topic}.")
    if response:
        st.write(response)
    else:
        st.error("Failed to fetch content. Please try again.")

# Function to fetch GD content
def prepare_for_gd(topic):
    st.subheader("GD Preparation")
    st.write("Fetching content for GD preparation...")

    # Generate content using Gemini API
    response = generate_content(f"Generate a simulated Group Discussion among five participants (P1, P2, P3, P4, P5) on the topic: {topic}.")
    if response:
        st.write(response)
    else:
        st.error("Failed to fetch content. Please try again.")

# Function to call Gemini API
def generate_content(prompt):
    try:
        # Use the Gemini model to generate content
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    main()



