import numpy as np
import pandas as pd
from skimage import io, feature
from skimage.measure import regionprops
from skimage.color import rgb2gray
from skimage.feature import greycomatrix, greycoprops
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_selection import SelectKBest, f_classif


# Step 1: Feature Extraction
def extract_features(image_path):
    # Load mammography image
    image = io.imread(image_path)

    # Convert to grayscale
    gray_image = rgb2gray(image)

    # Perform segmentation and get regions of interest (ROI)
    # (You can use your pre-processing and segmentation techniques here)
    # Let's assume you have a list of ROIs, each represented as a binary mask
    rois = [...]

    # Initialize empty lists to store extracted features
    shape_features = []
    texture_features = []

    for roi in rois:
        # Extract shape-based features
        region_props = regionprops(roi.astype(int))
        area = region_props[0].area
        perimeter = region_props[0].perimeter
        circularity = (4 * np.pi * area) / (perimeter**2)
        shape_features.append([area, perimeter, circularity])

        # Extract texture-based features
        glcm = greycomatrix(gray_image, [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4])
        texture_props = greycoprops(glcm, prop="dissimilarity")
        texture_features.append(texture_props)

    return np.array(shape_features), np.array(texture_features)


# Step 2: Load your dataset and extract features
# Assuming you have a CSV file 'dataset.csv' with columns 'Image_Path', 'Class', 'Type'
data = pd.read_csv("dataset.csv")

X_shape, X_texture, y_class, y_type = [], [], [], []

for index, row in data.iterrows():
    image_path = row["Image_Path"]
    class_label = row["Class"]  # Benign or Malignant
    type_label = row["Type"]  # Mass, Calcification, or Both

    shape_features, texture_features = extract_features(image_path)

    X_shape.append(shape_features)
    X_texture.append(texture_features)
    y_class.append(class_label)
    y_type.append(type_label)

# Convert lists to numpy arrays
X_shape = np.array(X_shape)
X_texture = np.array(X_texture)
y_class = np.array(y_class)
y_type = np.array(y_type)

# Step 3: Feature Selection
# Combine shape and texture features
X_combined = np.concatenate((X_shape, X_texture), axis=1)

# Perform correlation-based feature selection
num_features_to_select = 10
selector = SelectKBest(score_func=f_classif, k=num_features_to_select)
X_selected = selector.fit_transform(X_combined, y_class)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_selected, y_class, test_size=0.2, random_state=42
)

# Step 5: Classification using Random Forest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)

# Step 6: Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{classification_report}")
