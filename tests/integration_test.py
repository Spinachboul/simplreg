from sklearn.datasets import load_iris
import pandas as pd
from simplreg import simplereg_pipeline

def test_iris_dataset():
    # Load Iris dataset
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['target'] = iris.target

    # Display basic information
    print("Dataset Head:")
    print(data.head())

    print("\nDataset Information:")
    print(data.info())

    # Define pipeline parameters
    target_column = 'target'
    task_type = 'classification'  # Since Iris is a classification dataset

    print("\nStarting pipeline...")
    try:
        # Run the machine learning pipeline
        simplereg_pipeline(data, target_column=target_column, task_type=task_type)
        print("Pipeline executed successfully!")
    except Exception as e:
        print(f"Pipeline failed with exception: {e}")

if __name__ == "__main__":
    test_iris_dataset()
