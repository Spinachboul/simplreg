from setuptools import setup, find_packages

setup(
    name="simplreg",
    version="0.1",
    author="Mridul",
    author_email="jain.mridul.20@gmail.com",
    description="A simple machine learning package for forecasting and classification",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url
    packages=find_packages(),
    install_requires = [
        "pandas",
        "numpy",
        "scikit-learn",
        "tabulate",
        "matplotlib",
        "seaborn"
    ],
    pytest_requires=">=3.6",
)