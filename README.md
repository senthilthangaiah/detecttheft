# Illegal Activity Detection in Images using LLava Model

This Streamlit application allows users to upload an image and detect illegal activities present in the image using the LLava model. The model analyzes the image based on a predefined query to determine if any illegal activities are visible.

This application has several potential use cases across different domains:

1. **Security Monitoring**: 
   - The app can be integrated into security systems to automatically analyze images from surveillance cameras. It can help in detecting illegal activities such as trespassing, vandalism, or other suspicious behaviors.

2. **Content Moderation**:
   - Online platforms can use this tool to analyze user-uploaded images for illegal content, ensuring compliance with legal standards and community guidelines.

3. **Law Enforcement**:
   - Law enforcement agencies could employ this app to scan images from various sources for illegal activities, aiding in investigations and evidence collection.

4. **Forensic Analysis**:
   - Forensic teams can utilize the app to analyze images from crime scenes, identifying potential illegal activities or objects that could be relevant to a case.

5. **Custom Compliance Checks**:
   - Businesses that need to adhere to specific regulations (e.g., anti-piracy, anti-counterfeiting) can use the app to verify that images do not contain illegal or unauthorized content.

6. **Educational Purposes**:
   - The app can serve as a teaching tool in cybersecurity and AI courses, demonstrating how image analysis and machine learning models like LLava can be applied to real-world scenarios.
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
# 1. Installation
   Clone this repository:
```bash
   git clone https://github.com/senthilthangaiah/detecttheft.git
   cd detecttheft
```
 Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Install and Configure LLava:13B Model:

You need to install the llava:13b model to analyze images. Follow these steps to set up the model:

Install Ollama CLI: If you haven't installed the Ollama CLI yet, you can do so by following the instructions on the Ollama website.

### Download the LLava:13B Model:

```bash

ollama pull llava:13b
```
This command will download and set up the LLava:13B model on your local machine.

# 2. Usage
After running the app, open your web browser and navigate to the provided local URL.
Upload an image and click "Analyze Image" to get the analysis results.
# 3. License
This project is licensed under the MIT License - see the LICENSE file for details.

# 4. Acknowledgments
Streamlit - For the easy-to-use app framework.
LLava Model - For the powerful image analysis model.

### Snapshot
![screenshot](https://github.com/senthilthangaiah/detecttheft/blob/master/snatch.png)

