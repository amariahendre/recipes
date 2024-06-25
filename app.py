import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")

# Retrieve API key from config
api_key = config.get("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key= api_key)

    def generate_recipe(ingredients, excluded_ingredients, recipe_type):
        # Prepare the prompt for the OpenAI API for text generation
        prompt = f"Create a {recipe_type} recipe using the following main ingredients: {ingredients}."
        if excluded_ingredients:
            prompt += f" Avoid using these ingredients: {excluded_ingredients}."
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            recipe_text = response.choices[0].message.content
            return recipe_text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_image(description):
        # Prepare the prompt for the OpenAI API for image generation
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=description,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            # Assuming the image is the first in the list
            image_url = response.data[0].url
            return image_url
        except Exception as e:
            return f"Error generating image: {str(e)}"

    # Streamlit user interface
    st.title('Recipe Generator')
    # st.write('Select the type of recipe, and specify the main ingredients to generate a recipe.')

    # Recipe type selection
    recipe_type = st.selectbox('Select a recipe type:', ['Breakfast', 'Smoothie', 'Salad', 'Soup', 'Snack', 'Entree', 'Main', 'Side', 'Dessert', 'Sauce'])

    # Ingredients input
    ingredients = st.text_input('Enter main ingredients (comma-separated):')
    
    # Excluded ingredients input
    excluded_ingredients = st.text_input('Exclude ingredients (comma-separated):')

    # Button to generate recipe
    if st.button('Generate Recipe'):
        if not ingredients:
            st.write('Please enter at least one ingredient.')
        else:
            recipe_text = generate_recipe(ingredients, excluded_ingredients, recipe_type)
            if 'An error occurred' not in recipe_text:
                # st.write('### Generated Recipe:')
                # st.write(recipe_text)
                
                # Generate and display image
                image_description = recipe_text
                image_url = generate_image(image_description)
                if 'Error generating image' not in image_url:
                    st.image(image_url, caption='Generated Image', use_column_width=True)
                    st.write(recipe_text)
                else:
                    st.write(image_url)
                    st.write(recipe_text)
            else:
                st.write(recipe_text)
else:
    st.write('API key not found. Please set the OPENAI_API_KEY environment variable.')

