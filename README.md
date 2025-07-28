# Modular Multi-Agent E-Commerce System

This project demonstrates a modular, intelligent, and scalable multi-agent system for managing e-commerce tasks using the CrewAI framework. It features four specialized AI agents that collaborate to handle product listing, pricing, logistics, and reporting, all powered by a local language model to ensure free and private operation.

## Features

- **Modular Agent Architecture**: Easily extend or modify agent capabilities.
- **Local LLM Integration**: Uses Ollama with the `llama3` model to avoid API keys and costs.
- **Sequential Workflow**: Agents work in a logical sequence: Listing -> Pricing -> Logistics -> Reporting.
- **Inter-Agent Communication**: Task outputs are passed as context to subsequent agents, enabling seamless collaboration.
- **Stateful Memory**: The crew maintains memory to ensure context is preserved throughout the workflow.

### The Agents

1.  **Senior Product Lister**: Creates engaging, SEO-optimized product listings.
2.  **Chief Pricing Analyst**: Determines competitive and profitable prices based on market data.
3.  **Logistics Manager**: Handles inventory checks and calculates shipping details.
4.  **Chief Reporting Officer**: Aggregates the outputs from all other agents into a final, comprehensive report.

## Technology Stack

- [CrewAI](https://www.crewai.com/) for multi-agent orchestration.
- [Ollama](https://ollama.com/) for running local language models.
- Python

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Ollama](https://ollama.com/download)

After installing Ollama, you must pull the `llama3` model by running:
```bash
ollama pull llama3
```

## Installation & Setup

Follow these steps to get the project running on your local machine.

1.  **Clone the Repository**

    Open your terminal and clone the repository:
    ```bash
    git clone https://github.com/stabbler53/multi-AgentSystem.git
    cd multi-AgentSystem
    ```

2.  **Create a Virtual Environment (Recommended)**

    It's best practice to create a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3.  **Install Dependencies**

    Install all the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

With Ollama running and the setup complete, you can now run the multi-agent system.

1.  **Ensure Ollama is Running**

    Make sure the Ollama application is running in the background.

2.  **Execute the Script**

    Run the main script from the project's root directory:
    ```bash
    python main.py
    ```

You will see the output in your terminal as each agent performs its task in sequence, starting with the Product Lister and ending with the Reporting Officer.
