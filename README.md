# Neuroscience Wikipedia Replicate

This repository contains a Streamlit application that replicates a Wikipedia-style article on Neuroscience. The application provides an interactive and educational reading experience with custom styling, a functional search bar, and hover-to-reveal tooltips for key terminology.

## Features

*   **Wikipedia-style Interface**: Custom CSS is used to mimic the look and feel of a Wikipedia article for a familiar user experience.
*   **Interactive Tooltips**: Hover over key neuroscience terms like `prefrontal cortex`, `neuron`, or `fMRI` to get a concise definition without leaving the page.
*   **Content Search**: A search bar at the top allows users to quickly find sections containing specific keywords.
*   **Table of Contents**: A sidebar provides a clickable table of contents for easy navigation between sections.
*   **Responsive Design**: The layout adjusts for a clean reading experience on both desktop and mobile devices.

## Link to View

https://neurowikireplica.streamlit.app/

## How to Run Locally

Follow these steps to run the application on your local machine.

### Prerequisites

*   Python 3.8+
*   pip

### Installation and Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/rohitmalavathu/NeuroscienceWikipediaReplicate.git
    cd NeuroscienceWikipediaReplicate
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the App

Once the dependencies are installed, run the Streamlit application with the following command:

```sh
streamlit run neuroscience_wiki_app.py
```

Your web browser will automatically open a new tab with the running application.

## Technologies Used

*   **Python**: The core programming language for the application logic.
*   **Streamlit**: The framework used to build and serve the interactive web application.
*   **HTML/CSS**: Custom styles are injected to create the Wikipedia-like theme and interactive tooltips.
