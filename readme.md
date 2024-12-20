# Simplreg Documentation

Simplreg is a simple machine learning pipeline designed for beginners to quickly perform forecasting and classification tasks on supervised datasets. This package abstracts the complexities of preprocessing, model training, evaluation, and visualization into a user-friendly interface.

---

## Installation

To install Simplreg, use pip:

```bash
pip install simplreg
```

---

## Features

- **Preprocessing:** Automatically splits the dataset into training and testing sets and handles basic preprocessing tasks.
- **Model Training:** Supports both classification and regression tasks with pre-configured models.
- **Evaluation:** Provides performance metrics for both classification and regression tasks.
- **Visualization:** Displays feature importance for classification models.

---

## Getting Started

### 1. Import the Package

```python
from simplreg import simplereg_pipeline
```

### 2. Prepare Your Dataset

Ensure your dataset is in the form of a Pandas DataFrame. The target column should be specified for predictions.

Example:

```python
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
```

### 3. Run the Pipeline

```python
# Run the pipeline
simplereg_pipeline(df, target_column='target', task_type='classification')
```

---

## API Reference

### `simplereg_pipeline`

**Definition:**

```python
def simplereg_pipeline(df, target_column, task_type):
    """Simple ML pipeline: Preprocess, train, evaluate, visualize."""
```

**Parameters:**

- `df` (*DataFrame*): Input dataset.
- `target_column` (*str*): Name of the column containing the target variable.
- `task_type` (*str*): Type of task, either `classification` or `regression`.

**Returns:**
None (Outputs results to the console and visualizes feature importance).

---

## Under the Hood

### Modules

1. **Preprocessing**

   - Splits the dataset into training and testing sets.
   - Handles missing values and scaling (if necessary).

2. **Model Training**

   - Uses Logistic Regression for classification tasks.
   - Uses Linear Regression for regression tasks.

3. **Evaluation**

   - **Classification:** Outputs accuracy, precision, recall, and F1 score.
   - **Regression:** Outputs mean absolute error, mean squared error, and R-squared value.

4. **Visualization**

   - Displays feature importance for classification tasks using bar plots.

---

## Example Usage

### Classification Example

```python
from simplreg import simplereg_pipeline
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Run pipeline
simplereg_pipeline(df, target_column='target', task_type='classification')
```

### Regression Example

```python
from simplreg import simplereg_pipeline
import pandas as pd
import numpy as np

# Generate synthetic regression data
data = {
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'target': np.random.rand(100) * 10
}
df = pd.DataFrame(data)

# Run pipeline
simplereg_pipeline(df, target_column='target', task_type='regression')
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/yourusername/simplreg) or contact the maintainer at [your-email@example.com](mailto\:your-email@example.com).

---

## Acknowledgments

- **Scikit-learn:** For providing robust machine learning utilities.
- **Matplotlib:** For visualization capabilities.
- **Pandas:** For data manipulation and analysis.

Thank you for using Simplreg! Happy learning!
