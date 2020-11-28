# Sesame-Production
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4db1cb9e961d4516b4c65b086d18a8c6)](https://app.codacy.com/gh/ahmed14-cell/sesame-production?utm_source=github.com&utm_medium=referral&utm_content=ahmed14-cell/sesame-production&utm_campaign=Badge_Grade)
The data used in this workflow has been obtained from the United Nations
Food and Agriculture Organisations' public data portal. The objective of
this ML Workflow is to accurately predict the Production Quantity of
Sesame seeds provided the Area harvested.
This is a Machine Learning Pipeline that consists of extracting the data from
a remote storage. From the data obtained, feature extraction, preprocessing and
transformation occurs. After which a machine learning algorithm is applied to
the transformed data and saved in a serialized format. Finally the last step of
our pipeline is model evaluation. Here the accuracy of the model is evaluated
with robust regression metrics and the results is produced in a JSON file.
