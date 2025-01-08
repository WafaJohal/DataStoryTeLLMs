# DataStoryTeLLMs
LLMs swarm that tells you stories about your data

# DataStoryTeLLMs

**DataStoryTeLLMs** is an interactive tool that uses large language model (LLM) agents from the Swarm framework to craft compelling and insightful stories about your data. The app leverages Streamlit for its user interface, allowing users to upload their datasets or select from preloaded sklearn datasets. Through a series of intelligent agents, the tool transforms raw data into engaging narratives, offering both analytical insights and human-centric storytelling.

## Features

- **Dataset Input Options**:
  - Upload your dataset in CSV or Excel format.
  - Choose from popular sklearn datasets, such as Iris, Diabetes, Wine, and more.

- **Swarm Agents**:
  - **Data Analyst Agent**: Analyzes the dataset to uncover patterns, trends, and anomalies.
  - **Character Agent**: Creates a dynamic, relatable character inspired by the dataset.
  - **Storyteller Agent**: Crafts a narrative based on data insights, anchored by the character agent.

- **Interactive Stories**:
  - Stories are presented in a first-person narration style.
  - Designed to be engaging and relatable for non-technical and technical audiences alike.

## How It Works

1. **Choose Your Dataset**: Upload a custom dataset or select one from sklearn.
2. **Preview the Data**: View a preview of the dataset, including the first few rows.
3. **Generate Stories**: Let the Swarm agents analyze the data and produce a compelling story.
4. **Engage with the Story**: The generated story integrates insights, human-like characters, and interactive storytelling elements.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DataStoryTeLLMs.git
   cd DataStoryTeLLMs


2. Install the dependencies:
    ```bash 
    pip install -r requirements.txt

3. Run the Streamlit app:
    ```bash
    streamlit run app.py


## Dependencies

The following dependencies are required:

- Streamlit for the interactive web interface.
- pandas for data manipulation.
- scikit-learn for preloaded datasets.
- Swarm Framework for LLM agents.

Refer to the requirements.txt for the complete list.

## Usage

1. Launch the app using the installation steps above.
2. Follow the UI prompts to upload a dataset or select a sklearn dataset.
3. Click on "Generate Story" to create a narrative based on the data.
4. Enjoy and interact with the story crafted by the Swarm agents.


Example:

Dataset: Iris
Output Preview:

- Main Trends: The Iris dataset reveals clusters of data based on species with clear separations in petal and sepal dimensions.
- Character: Meet Dr. Flora Petalis, a botanist fascinated by the delicate balance of flower morphology.
Story:
- Once upon a time, I, Dr. Flora Petalis, stumbled upon a peculiar garden divided into three vibrant sections...
Contribution


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- OpenAI Swarm for the multi-agent framework.
- Streamlit for the intuitive web app framework.
- Sklearn for providing accessible datasets for prototyping and learning.