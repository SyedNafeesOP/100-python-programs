# what is use of groupby ()function in pandas

# The groupby() is one of the most frequently
#  used Pandas functions in data analysis.
#   It is used for grouping the data points (i.e. rows)
#  based on the distinct values in the given column or columns. 
# exp
import pandas as pd

# Creating a sample DataFrame
data = {
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Math', 'English', 'English', 'Math', 'English'],
    'Score': [80, 90, 75, 85, 88, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Grouping by 'Student'
grouped_df = df.groupby('Student')

# Calculating the mean score for each student
average_scores = grouped_df['Score'].mean()

print("\nAverage Scores:")
print(average_scores)

