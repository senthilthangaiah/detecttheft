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

  git clone https://github.com/senthilthangaiah/detecttheft.git
  cd theftdetect
```
## Install the required Python packages:
```bash
    pip install -r requirements.txt
```
### Run the Streamlit app:
```bash
streamlit run app.py
```
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
Now your project is ready and can be accessed by others through your GitHub repository!
