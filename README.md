🍄 Mushroom Edibility Predictor

A simple web app that uses machine learning to predict if a mushroom is edible or poisonous from its physical traits.





✨ Features
Predicts edible or poisonous from 22 mushroom traits
Easy dropdown inputs, grouped into Cap, Gill, Stalk, and Other details
Helpful tips under each input that explain the codes (for example, b = bell, c = conical)
Visual guide images to help you understand mushroom parts
Clear result: green for edible, red for poisonous


🛠️ Tech Stack
Language	Python
Data handling	Pandas, NumPy
Machine learning	Scikit-learn (Random Forest, PCA, LabelEncoder)
Saving models	Joblib
Web app	Streamlit
Version control	Git & GitHub

📁 Project Folder Structure
Mushroom-Classification/
│
├── app.py                       # Streamlit web app (frontend)
├── mushroom_classification.py   # Model training code
├── Mushroom_prediction.pkl      # Saved Random Forest model
├── encoders.pkl                 # Saved encoders (text to numbers)
├── pca_model.pkl                # Saved PCA model
├── requirements.txt             # Python libraries needed
├── structure.png                # Guide image: mushroom parts
├── cap_shape.png                # Guide images used in the app
├── ...                          # (other guide images)
└── README.md                    # Project documentation

📊 Dataset and Model Details
Dataset
Name: Mushroom dataset (mushrooms.csv)
Records: about 8,000 mushrooms
Features: 22 physical traits (cap, gill, stalk, ring, spore print, habitat, and more)
Target: class → edible (e) or poisonous (p)

How the model was built
Clean the data: check for missing values.
Encode: change text categories into numbers using LabelEncoder.
Reduce features: use PCA to shrink 22 features to 7 main components.
Split the data: 80% for training, 20% for testing.
Compare models: Logistic Regression, KNN, SVC, Decision Tree, Random Forest, and Gradient Boosting.
Save the final model: Random Forest, saved with Joblib.

Performance
Model	Accuracy
Logistic Regression	add your result
KNN	add your result
SVC	add your result
Decision Tree	add your result
Random Forest	add your result
Gradient Boosting	add your result

👤 Author-Dilunis
   GitHub- @Dilunis
