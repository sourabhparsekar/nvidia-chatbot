# Legal Q&A Chatbot

This project is a Flask-based Q&A chatbot designed to answer legal contract-related questions using NVIDIA's LLM. The application ingests a dataset, processes it, and provides answers based on the given context.

## Table of Contents
- [Legal Q\&A Chatbot](#legal-qa-chatbot)
  - [Table of Contents](#table-of-contents)
  - [Dependencies](#dependencies)
  - [Setup](#setup)
  - [Running the Application](#running-the-application)
  - [Testing the Application](#testing-the-application)
  - [Project Structure](#project-structure)
    - [Contributing](#contributing)
    - [Contact](#contact)
    - [License](#license)
  - [Notes](#notes)
    - [Additional Notes:](#additional-notes)

## Dependencies

This project relies on the following libraries:

```bash
flask
langchain-community[all]
langchain-nvidia-ai-endpoints
python-dotenv
```
Detailed dependency list can be found at [requirements.txt](requirements.txt)

## Setup
1. Clone the repository
```bash
git clone https://github.com/sourabhparsekar/nvidia-chatbot.git
cd legal-q-a-chatbot
```
2. Install Python Packages
```bash
pip install -r requirements.txt
```
3. Setup Environment Variables
Create a .env file in the root directory and add the following:
```bash
NVIDIA_KEY=your_api_key
```

## Running the Application
Ensure all dependencies are installed and environment variables are set.
Start the Flask server:
```bash
flask run
```

The application will be available at http://localhost:5000

## Testing the Application
You can test the application using a POST request to the /query endpoint.

Example using curl:

```bash
curl -X POST "http://localhost:5000/query" -H "Content-Type: application/json" -d '{"question":"What is the termination clause in the contract?"}'
```

## Project Structure
```
law-chatbot/
├── data_ingestor.py         # Data loading and processing script
├── execution_plan.py        # Main execution logic and chain configuration
├── main.py                  # Flask application entry point
├── memory.py                # In-memory chat history implementation
├── nvidia_embeddings.py     # NVIDIA embeddings configuration
├── nvidia_llm.py            # NVIDIA LLM configuration
├── requirements.txt         # Python dependencies
├── retrievers.py            # Retriever configuration
├── text_splitter.py         # Document splitting logic
├── vector_store.py          # Vector store implementation
└── README.md                # This file
```

### Contributing
Contributions are welcome! Please fork the repository and create a pull request.

### Contact
For any issues or questions, feel free to reach out to the maintainer.

### License
[MIT License](https://opensource.org/license/MIT)

## Notes
Make sure you have the NVIDIA API key and update the .env file accordingly.
The application uses NVIDIA's LLM models and requires an active API subscription.

### Additional Notes:

- The `requirements.txt` file should include all the necessary Python packages. You might need to create this file by running `pip freeze > requirements.txt` after installing the required packages.
- Update the repository URL (`https://github.com/sourabhparsekar/nvidia-chatbot.git`) with your actual GitHub repository URL.
- You might want to add more detailed error handling and logging to the application for production use.
- Ensure all the API keys and sensitive information are properly secured and not exposed in the codebase or commits.


*This README provides a guide for setting up, running, and testing the application, making it easier for new contributors or users to get started.*
