# Sesame-Production
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4db1cb9e961d4516b4c65b086d18a8c6)](https://app.codacy.com/gh/ahmed14-cell/sesame-production?utm_source=github.com&utm_medium=referral&utm_content=ahmed14-cell/sesame-production&utm_campaign=Badge_Grade)

## Introduction

The data used in this workflow has been obtained from the **United Nations Food and Agriculture Organisation**
public data repository.

The objective of this ML Workflow is to accurately predict the **Production quantity** of
sesame seeds provided the **Area harvested** and the **Yield Expected**.

### The steps of this workflow consist of

*   Extracting the data from a remote storage.

*   Feature extraction, preprocessing and transformation.

*   A machine learning algorithm is applied to the transformed data and saved in a serialized format.

*   Finally the last step of our pipeline is model evaluation.

--------
### The metrics used for this project are
*   Coefficent of Determination **(r²)**

*   Root Mean Squared Error **(rmse)**

--------

## How to build this workflow
*   First you need to clone this repository using:
>   ```git clone https://github.com/ahmed-gaal/sesame-production.git```
*   Then you need to create a virtual environment using:
>   ```python3 -m venv env```
*   Activate your virtual environment using:
>   ```source env/bin/activate```
*   After activate your virtual environment, install the project dependencies using:
>   ```pip install -r requirements.txt```
*   Add the original data to your environment variables:
>   ```export DATA='https://drive.google.com/uc?id=1pC5Md6KKJYCkSb32BV3xV-SkEDg2icff'```
*   Finally, create necessary changes in either train script or feature extraction script and reproduce the workflow using the following command:
>   ```dvc repro```

To launch the interactive web application, click ⇢ [here](https://sesame-prediction.herokuapp.com/)

--------