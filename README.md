# image_theme_generator_using_KMeans_Clustering

A Machine Learning project to generate theme from image using K-Means Clustering. As we see in windows taskbar theme from wallpaper, youtube ambient mode from thumbnail.

## Features
- Preprocessing of image into matrix
- create potential clusters of dominant colors from image
- Visualization of most dominant color palatte
- Interactive Streamlit app for testing the model

## Installation

### Clone the Repository
```bash
git clone https://github.com/prashant-shinde98/image_theme_generator_using_KMeans_Clustering.git
cd image_theme_generator_using_KMeans_Clustering
```

### Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Steps Followed in the Project
1. **Upload Image:** 
2. **Data Preprocessing:**
   - Cleaned and vectorize image.
   - convert in (n,3) [RBG]
3. **Model Training:**
   - Trained a K-means Clustering on the preprocessed data.
   - Generate a color palatte from most dominant clusters.
4. **Building the App:**
   - Developed an interactive Streamlit app to test the new inputs.
5. **Deployment:** Prepared the app for local usage with simple setup steps.

## Usage

### Running the Streamlit App
To launch the Streamlit app:
```bash
streamlit run app.py
```

## Project Structure
```
image_theme_generator_using_KMeans_Clustering/
├── app.py                   # Streamlit app for the classifier
├── them_generator.ipynb # Script for training and saving the model
├── 
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation
```

### Description of Each File
- **`app.py`:** Contains the Streamlit code to create an interactive web application for testing the spam classifier.
- **`them_generator.ipynb`:** Includes code for K-Means Clustering.
- **`requirements.txt`:** Lists all Python dependencies required to run the project.
- **`README.md`:** Documentation for the project, including setup and usage instructions.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
[Prashant Shinde](https://github.com/prashant-shinde98)
