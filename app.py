import streamlit as st
import ollama
from PIL import Image

def get_image_description(image, query):
    response = ollama.chat(
        model='llava:13b',
        messages=[
            {
                'role': 'user',
                'content': query,
                'images': [image],
            },
        ],
    )
    return response['message']['content']

def main():
    st.title("Illegal Activity Detection with LLava Model")
    
    # Upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Default query to detect illegal activities
    query = "Are there any illegal activities visible in the image? If yes then reply Yes else No "

    if st.button("Analyze Image"):
        if uploaded_image is not None:
            image_bytes = uploaded_image.read()
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            description = get_image_description(image_bytes, query)
            st.write("Analysis Result:", description)
        else:
            st.write("Please upload an image.")

if __name__ == "__main__":
    main()

