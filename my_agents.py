import pandas as pd
import json
import streamlit as st
from swarm import Swarm, Agent
from sklearn.datasets import load_iris, load_breast_cancer, load_diabetes, load_digits, load_linnerud, load_wine

# Initialize Swarm Client
client = Swarm()


# Helper Functions
def load_sklearn_dataset(name):
    datasets = {
        "iris": load_iris,
        "diabetes": load_diabetes,
        "digits": load_digits,
        "linnerud": load_linnerud,
        "wine": load_wine,
        "breast cancer": load_breast_cancer,
    }
    dataset = datasets[name]()
    return pd.DataFrame(data=dataset.data, columns=dataset.feature_names)

def get_df_column_names(df):
    return df.columns

def get_data_analyst_instructions():
    return """ You are a data analysis expert with a deep understanding of data extraction, cleaning, transformation, and visualization. Your role involves analyzing datasets to uncover insights, patterns, and trends that help make data-driven decisions. 

    Key responsibilities:
    - Work with structured and unstructured data from various sources.
    - Clean, preprocess, and transform raw data into formats suitable for analysis.
    - Perform data analysis (EDA) to understand the data's structure and content.
    - Identify trends and uncover meaningful insights.
    - Communicate results effectively to both technical and non-technical stakeholders.

    Expectations:
    - Ask clarifying questions if the analysis goal is not fully defined.
    - Highlight any assumptions or limitations of the data or analysis methods.
    - Suggest actionable insights and potential next steps based on your findings.

    Begin by understanding the dataset, and your responsibilties and expectaions."""

def get_storyteller_instructions(): 
    return """ You are a storyteller who crafts engaging and interactive narratives based on data insights provided to you by a data analyst. You will also be given a character agent to anchor the story, making the insights relatable and impactful. Your primary goal is to transform complex data into a clear, memorable, and engaging story that resonates with the intended audience.

    Key responsibilities:
    - Use the given character agent to humanize the insights given by the data analyst and create a relatable narrative arc.
    - Develop a story with a clear structure: a beginning (context and setup) - starting with \"once upon a time\", middle - challenges related to the data insights, and end (conclusions or calls to action).
    - Ensure the story is interactive and encourages audience engagement through questions, scenarios, or decision points.
    - Make the story first-person narration. 

    Expectations:
    - Start by fully understanding the data insights and the character agent provided by the data analyst.
    - Make the story immersive and actionable, with clear takeaways for the audience.
    - Always start the story with \"once upon a time\".

    Begin by reviewing the data insights and the character agent, then create a compelling story that transforms the data into a meaningful and engaging interactive story for the audience."""

def get_character_prompt(colnames):
    return f"""
    You are tasked with creating a dynamic and relatable character for a story. This character will serve as the central agent in driving the narrative forward, helping to communicate data insights in a meaningful and engaging way. Use the column names and categorical data from the provided dataset to shape the character's traits, background, and role in the story. Use the keywords here to design the character: {colnames}

    Key details to define:
    - **Name and Background**: Create a name and backstory for the character that aligns with the themes suggested by the dataset. For example, use categorical data or feature names to inspire their profession, environment, or expertise.
    - **Personality Traits**: Develop their personality using hints from the data structure or categories (e.g., traits inspired by feature names like \"species\" or values like \"versicolor\").
    - **Role in the Story**: Define how the character interacts with the data insights. For example, they could be a botanist studying flower species or a data analyst exploring patterns in biological traits.
    - **Motivations and Goals**: Use the dataset's context to inspire their motivations. For instance, they may aim to uncover relationships between features or solve a problem related to the categorical data.
    - **Challenges and Growth**: Identify potential challenges they might encounter while analyzing the data and how they overcome them.

    Expectations:
    - Make the character relatable and grounded in the dataset's context.
    - Ensure their role and actions naturally connect to the dataset's insights and audience understanding.
    - Provide details about their appearance, voice, and mannerisms to bring them to life.

    Begin by reviewing the dataset details and crafting a character whose story reflects the dataset’s themes and categories.
    """

def get_user_input_prompt():
    return f"""
    You are tasked with in change of engaging the user in the story made by the storyteller 

    Expectations:
    - Make the story interactive
    - Allow the user to ask question about the story 
    - Provide details about their appearance, voice, and mannerisms to bring them to life.

    Begin by reviewing the dataset details and crafting a character whose story reflects the dataset’s themes and categories.
    """

def get_data_insights():
    return data_analyst_agent

def get_character():
    return character_agent

def get_story():
    return storyteller_agent




# Streamlit UI Components

st.title("Interactive Dataset Storyteller with Swarm Agents")

df = None 

# Upload or Select Dataset
dataset_source = st.radio("Choose Dataset Source:", ("Upload", "Sklearn Datasets"))

if dataset_source == "Upload":
    uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel):", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.write("Dataset Preview:", df.head())
else:
    dataset_choice = st.selectbox(
        "Select a Sklearn Dataset:",
        ("iris", "diabetes", "digits", "linnerud", "wine", "breast cancer")
    )
df = load_sklearn_dataset("iris")
st.write("Dataset Preview:", df.head())

# Pass Dataset to Agents
if df is not None:
    iris_data_json = df.to_dict(orient="records")
    print(iris_data_json)

    # Create Data Analysis Agent
    data_analyst_agent = Agent(
        name="Data Analyst",
        instructions=get_data_analyst_instructions() + f"Here is a dataset: {iris_data_json}. Please analyze this data. What are the main trends?",
    )

    # Create Character Agent
    character_agent = Agent(
        name="Main Character",
        instructions=get_character_prompt(get_df_column_names(df)),
    )

    # Create Storyteller Agent
    storyteller_agent = Agent(
        name="Storyteller",
        instructions=get_storyteller_instructions(),
        functions=[lambda: data_analyst_agent, lambda: character_agent],
    )

    # Interaction Section
    if st.button("Generate Story"):
        story = storyteller_agent.execute()
        st.markdown(story)



#### CREATE DATA ANALYSIS AGENT
data_analyst_agent = Agent(
    name="Data Analyst",
    instructions=get_data_analyst_instructions() +  f"Here is a dataset: {iris_data_json}. Please analyze this data. What are the main trends?",
)


###### CREATE CHARACTER AGENT
### Use column to create a character: Using the column names and categorical data of the dataset, create a character. 
character_agent = Agent(
    name="Main Character",
    instructions=get_character_prompt(get_df_column_names(df)),
)


##### CREATE STORYTELLER AGENT
### "Now can you generate a story narrated by the character you created,XXXX insert char name,  at the first person. The story should depict the trends of the iris dataset. "
storyteller_agent = Agent(
    name="Storyteller",
    instructions=get_storyteller_instructions(),
    functions=[get_data_insights, get_character]
)


##### CREATE USER INPUT AGENT
### "Now can you generate a story narrated by the character you created,XXXX insert char name,  at the first person. The story should depict the trends of the iris dataset. "
user_input_agent = Agent(
    name="User Input",
    instructions=get_user_input_prompt(),
    functions=[get_story]
)


