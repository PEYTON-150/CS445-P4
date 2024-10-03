Data Cleaning
Data Source: The survey data contains 600 samples and 86 feature questions, alongside a binary label indicating whether a student is abusing alcohol (1 for yes, 0 for no).
Feature Dictionary: The original responses were graded on a 5-point scale, with specific conversions applied to simplify the dataset:
Scores 0-3 are converted to 0.
Scores 4-5 are converted to 1.
Score 99 indicates missing data and needs to be addressed.
Cleaning Strategies: You will need to implement a cleaning strategy for the dataset, addressing outlier values and missing data. Possible strategies include:
Dropping rows or columns with invalid data.
Assigning default values (0, 1) for missing data.
Using statistical methods to impute missing values.
Normalizing values to a decimal range [0, 1].
Perceptron Implementation
Model Structure: Develop a perceptron that takes 86 input parameters and outputs a binary prediction for alcohol abuse.
Parameters: Adjust the following parameters to optimize your model:
Threshold value 𝑡
Step size 𝑠 for weight updates
Initial weights on the edges of the perceptron
Number of training iterations to achieve stabilization
Data Splitting: Decide on an appropriate split between training and testing datasets to maximize model performance, considering cross-validation techniques.
Output
Generate a weights.txt file containing:
The final threshold value 𝑡
The list of 86 edge weights (one for each input feature)
The format of the weights.txt file should be as follows:
<t_value>
<weight_1>
<weight_2>
...
<weight_86>

Submission Requirements
The Python script used for cleaning the dataset.
The Python script used to implement the perceptron model and generate weights.txt.
The output file weights.txt containing the final weights and threshold value.
Evaluation Criteria
The effectiveness of the data cleaning process (accuracy of the final dataset).
The performance of the perceptron model (accuracy in predicting alcohol abuse).
The organization and clarity of the code.
Adherence to the specified output format.
