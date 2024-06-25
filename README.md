# Recipe Generator App using OpenAI API

This Streamlit application generates recipes based on user-provided ingredients and preferences using the OpenAI API. It also generates an image related to the generated recipe description.

## Features

- **Recipe Generation**: Select a recipe type (e.g., Breakfast, Salad, Dessert) and specify main ingredients to generate a recipe.
- **Image Generation**: An image related to the generated recipe is generated using the DALL-E model from OpenAI.
- **Error Handling**: Handles API key validation and error messages gracefully.

## Setup

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**

   Ensure you have Python 3.7+ installed. Install required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=<your_openai_api_key>
   ```

4. **Run the Application**

   Execute the following command to run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   This command starts a local server, typically on `http://localhost:8501`.

5. **Use the Application**

   - Select a recipe type from the dropdown menu.
   - Enter main ingredients (comma-separated) into the input box.
   - Optionally, exclude certain ingredients.
   - Click on the "Generate Recipe" button to see the generated recipe and related image.
