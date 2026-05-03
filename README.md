# # AI Text Summarizer (Offline)

![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

A powerful, offline text summarization tool built with **Streamlit** and **Sumy**. This application allows you to condense long articles, documents, or any text into a concise summary without sending your data to any external APIs.

## Features

- **100% Offline**: No API keys required. Your data stays on your machine.
- - **Real-time Summarization**: Uses LSA (Latent Semantic Analysis) for high-quality summaries.
  - - **Adjustable Length**: Choose exactly how many sentences you want in your summary.
    - - **Clean UI**: Modern and intuitive interface powered by Streamlit.
      - - **Python-powered**: Built using industry-standard NLP libraries.
       
        - ## Getting Started
       
        - ### Prerequisites
       
        - - Python 3.8 or higher installed on your system.
         
          - ### Installation
         
          - 1. Clone this repository:
            2.    ```bash
                     git clone https://github.com/Aniket12-coder07/ai-text-summarizer.git
                     cd ai-text-summarizer
                     ```

                  2. Install the required dependencies:
                  3.    ```bash
                           pip install -r requirements.txt
                           ```

                        3. (Optional) Download the necessary NLTK data if prompted:
                        4.    ```python
                                 import nltk
                                 nltk.download('punkt')
                                 ```

                              ### Running the App

                          Start the Streamlit application:
                    ```bash
                    streamlit run main.py
                    ```

                    ## Built With

              - [Streamlit](https://streamlit.io/) - The web framework for Machine Learning and Data Science.
              - - [Sumy](https://github.com/miso-belica/sumy) - Module for automatic summarization of text documents and HTML pages.
               
                - ## License
               
                - This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
                - 
