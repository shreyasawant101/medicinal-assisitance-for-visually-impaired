**# AI Driven Customer Support System**

This project implements an intelligent customer support system leveraging Streamlit and a fine-tuned Llama large language model (LLM) from  Hugging Face. It empowers users to interact with the system through text input, speech recognition, and tailored responses based on the chosen assistance type (Agriculture, Healthcare, Education).

**Key Features:**

- **Seamless User Interaction:**
    - Text input for clear queries.
    - Speech recognition for hands-free convenience.
    - Response word limit selection for concise or detailed answers.
    - Radio button selection for focused assistance type.
- **Enhanced Response Generation:**
    - Pre-trained Llama model fine-tuned on a relevant dataset ([https://huggingface.co/datasets/PRAKALP-PANDE/PSP-agricultureQnA-1k-unique](https://huggingface.co/datasets/PRAKALP-PANDE/PSP-agricultureQnA-1k-unique)).
    - Caching mechanism for efficient retrieval of existing responses.
- **Accessibility:**
    - Text-to-speech functionality for reading responses aloud.

**Getting Started:**

1. **Prerequisites:**
   - Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
   - Git version control system ([https://git-scm.com/](https://git-scm.com/))
   - Anaconda package manager ([https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution))

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/PRAKALP-PANDE/AI-Driven-Customer_Support_System.git
   ```

3. **Set Up a Conda Environment (Optional but Recommended):**
   - Create a virtual environment to isolate project dependencies and avoid conflicts with other projects:
     ```bash
     cd AI-Driven-Customer-Support-System
     conda create -n dcss_env python=3.8  # Adjust Python version as needed
     conda activate dcss_env
     ```

4. **Install Required Libraries:**
   - The `requirements.txt` file specifies all necessary dependencies:
     ```bash
     pip install -r requirements.txt
     ```

**Project Structure:**

```
AI-Driven-Customer-Support-System/
├── app.py                     # Main application script
├── models/                     # Folder to store the downloaded LLM model
│   └── PSP-AI-DCSS-finetune.bin  # (Download from https://huggingface.co/PRAKALP-PANDE/PSP-AI-DCSS-finetune)
├── ReadMe.md                   # This file (project documentation)
├── requirements.txt            # List of required Python libraries
└── .gitignore                   # Specifies files to exclude from version control
```

**Model Download and Usage:**

1. **Download the Pre-trained Model:**
   - Access the LLM model from the provided link ([https://huggingface.co/PRAKALP-PANDE/PSP-AI-DCSS-finetune](https://huggingface.co/PRAKALP-PANDE/PSP-AI-DCSS-finetune)).
   - Download the model file (e.g., `PSP-AI-DCSS-finetune.bin`).
2. **Move the Model File:**
   - Place the downloaded model file inside the `models` folder within the project directory.

**Running the Application:**

1. **Activate the Conda Environment (if you created one):**
   ```bash
   conda activate dcss_env
   ```
2. **Start the Streamlit Development Server:**
   ```bash
   streamlit run app.py
   ```

3. **Access the Application:**
   - Open http://localhost:8501 in your web browser.

**Usage:**

1. **Interact with the System:**
   - Type your query in the text input field or use speech recognition.
   - Select the desired word limit for the response.
   - Choose the type of customer assistance you need (Agriculture, Healthcare, Education).
   - Click "Generate" to receive a response from the model.
2. **Response Generation:**
   - The system will leverage the fine-tuned LLM to generate a tailored response based on your input and chosen assistance type.
   - Caching is implemented to retrieve existing responses efficiently.
3. **Text-to-Speech (Optional):**
   - Click "Listen to the Response" to have the system read the response aloud using text-to-speech.

**Built With:**

- Streamlit (web framework)
- langchain (LLM interaction)
- PyMongo (optional, for database integration)
- SpeechRecognition (speech-to-text)
- pyttsx3 (text-to-