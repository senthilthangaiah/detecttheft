# Illegal Activity Detection in Images using LLava Model

This Streamlit application allows users to upload an image and detect illegal activities present in the image using the LLava model. The model analyzes the image based on a predefined query to determine if any illegal activities are visible.

## Features

- Upload an image in PNG, JPG, or JPEG format.
- Automatically analyze the image to detect illegal activities.
- Display the results of the analysis on the web interface.

## Getting Started

### Prerequisites

Make sure you have Python installed. You can check your installation by running:

```bash
python --version
```
## Installation
   Clone this repository:
```bash
   git clone https://github.com/your-username/image-illegal-activity-detection.git
   cd image-illegal-activity-detection
   Install the required Python packages:
```

```bash
pip install -r requirements.txt
```
## Install and Configure LLava:13B Model:

You need to install the llava:13b model to analyze images. Follow these steps to set up the model:

Install Ollama CLI: If you haven't installed the Ollama CLI yet, you can do so by following the instructions on the Ollama website.

### Download the LLava:13B Model:

```bash
Copy code
ollama pull llava:13b
```
This command will download and set up the LLava:13B model on your local machine.

## Usage
After running the app, open your web browser and navigate to the provided local URL.
Upload an image and click "Analyze Image" to get the analysis results.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Streamlit - For the easy-to-use app framework.
LLava Model - For the powerful image analysis model.

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
```
## Environment
```bash 
.env
.venv
env/
venv/
```
# 6. Pushing to GitHub

Initialize Git:

Run git init in your project directory.
Add all files: git add .
Commit your changes: git commit -m "Initial commit"
Create a GitHub Repository:

Go to GitHub and create a new repository.
Follow the instructions to add the remote and push your code:
```bash
git remote add origin https://github.com/your-username/image-illegal-activity-detection.git
git branch -M main
git push -u origin main
```

### Snapshot
`![App Screenshot](/app.png)
Now your project is ready and can be accessed by others through your GitHub repository!
