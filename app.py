import io
import sys
import streamlit as st
from agent import multi_agent_framework


# Define the multi agent framework
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
agent = multi_agent_framework(model_id)

# Function to log agent actions
def log_agent_action(prompt, activity, result):
    st.write(f"### Agent Activity")
    st.write("**Prompt Sent to Agent:**")
    st.code(prompt, language="text")
    st.write("**Agent Activity:**")
    st.code(activity, language="text")
    st.write("**Agent Output:**")
    st.code(result, language="text")

# Streamlit app title
st.title("Multi Agent GPT")

# App description
st.write("Generate creative content, search the web and generate images enriched with the power of MultiAgent framework")

# Input blog topic or prompt
user_prompt = st.text_area("How may I help you?:", placeholder="E.g., Generate me a picture of cute puppy")

# Button to generate content
if st.button("Generate"):
    if user_prompt:
        with st.spinner("Generating content with our Multi agents"):
            try:
                # Run the agent with the given prompt
                buffer = io.StringIO()
                sys.stdout = buffer
                result = agent.run(user_prompt)
                # Display the generated content
                st.subheader("Generated Content:")
                st.write(result)

                # Log backend activity
                sys.stdout = sys.__stdout__
                activity = buffer.getvalue()
                log_agent_action(user_prompt, activity, result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt to proceed.")

# Footer
st.markdown("---")
st.caption("Powered by SmolAgents, DuckDuckGo, black-forest-labs and Streamlit")