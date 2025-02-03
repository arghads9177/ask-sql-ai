import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Reset the value in session_state
def reset_ta_schema():
    st.session_state.ta_schema = "" 
    st.session_state.qno = 1

# Create text area
if 'ta_schema' not in st.session_state:
    st.session_state.ta_schema = ""

if 'qno' not in st.session_state:
    st.session_state.qno = 1

def reset_ta_query():
    st.session_state.ta_query = ""

if "ta_query" not in st.session_state:
    st.session_state.ta_query = ""
    
# Initialize session state for schema persistence and Q&A history
if "schema" not in st.session_state:
    st.session_state.schema = None
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI
st.title("🧠 AskSQL AI - SQL Query Builder")

st.write("Provide a database schema and ask SQL-related questions to generate queries. The app will remember your schema and questions during this session.")

# Schema input section
schema_input = st.text_area("📌 Enter Database Schema", value= st.session_state.ta_schema, placeholder="e.g., Customers (CustomerID, Name, Age, City)")

# Update schema in session state
if st.button("Set Schema"):
    if schema_input.strip():
        st.session_state.schema = schema_input.strip()
        st.success("Schema updated successfully!")
        st.subheader("📋 Current Schema:")
        st.text(st.session_state.schema)
        st.session_state.history.append({"schema": st.session_state.schema})
        reset_ta_schema()
    else:
        st.warning("Please enter a valid database schema.")

# User query input
user_query = st.text_area("📝 Enter your SQL question", value= st.session_state.ta_query, placeholder="e.g., Get the names of all customers above 25 years old.")

# Generate SQL button
if st.button("Generate SQL"):
    if not user_query.strip():
        st.warning("Please enter a valid SQL question.")
    else:
        with st.spinner("Building SQL. Please be patient..."):
            llm = ChatOpenAI(model="gpt-4o", temperature=0)

            # Define prompt
            prompt_template = PromptTemplate(
                input_variables=["schema", "query"],
                template="""
                You are an expert SQL assistant. Based on the given database schema, generate an appropriate optimized SQL query.
                If the user question is unrelated to the schema, provide a general answer but mention that a proper schema is needed for an accurate SQL query.
                
                Schema: {schema}
                User Query: {query}
                
                SQL Query:
                """
            )

            # Use stored schema if provided, else notify no schema
            schema_text = st.session_state.schema if st.session_state.schema else "No schema provided."

            # Create chain
            chain = prompt_template | llm
            
            # Generate SQL query
            response = chain.invoke({
                "schema": schema_text,
                "query": user_query
            })
            reset_ta_query()
            sql_query = response.content.strip()
            if sql_query.startswith("```sql") and sql_query.endswith("```"):
                sql_query = sql_query[6:-3].strip()  # Remove ```sql and ```
            elif "```sql" in sql_query:
                start = sql_query.index("```sql")
                end = sql_query.index("```", start + 1)
                sql_query = sql_query[start + 6:end].strip()  # Remove ```sql and ```

            # Store question and answer in session state
            st.session_state.history.append({"qno": st.session_state.qno, "question": user_query, "answer": sql_query})
            st.session_state.qno= st.session_state.qno + 1

            # Display latest SQL result
            st.subheader("🔍 Generated SQL Query:")
            st.code(sql_query, language="sql")

# Display session history
if st.session_state.history:
    st.subheader("🗂️ Session Q&A History:")
    # for idx, qa in enumerate(st.session_state.history, 1):
    for qa in st.session_state.history:
        if "schema" not in qa:
            st.markdown(f"**Q{qa["qno"]}:** {qa['question']}")
            st.code(qa['answer'], language="sql")
            st.markdown("---")
        else:
            st.markdown("📋 **Schema:**")
            st.text(qa["schema"])
            st.markdown(qa["schema"])
            st.markdown("---")