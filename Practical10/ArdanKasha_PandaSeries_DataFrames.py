import pandas as pd

# Part 1: Create a Pandas Series with 5 numbers and custom index labels.
numberData = [229, 154, 345, 78, 98]
index = ['a', 'b', 'c', 'd', 'e']
numberSeries = pd.Series(data=numberData, index=index)

# Print the sum, mean, and maximum value of the series.
print("\nPrint the sum, mean, and maximum value of the series")
print("\nSum:", numberSeries.sum())
print("Mean:", numberSeries.mean())
print("Maximum value:", numberSeries.max())
print()

##########################################################################################################

# Part 2: Create a DataFrame with 4 columns: student, age, grade, marks.
studentData = {
    "Student": ['Ardan', 'Ryder', 'Josh', 'Carter', 'Brodey'],
    "Age": [23, 18, 17, 28, 34],
    "Grade": ['A', 'C', 'C', 'A', 'B'],
    "Marks": [85, 62, 70, 81, 71]
}
df = pd.DataFrame(studentData)

# Print the first 3 rows of the DataFrame.
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

# Select only the Student and Marks columns.
print("\nStudent and Marks columns:")
print(df[['Student', 'Marks']])

# Display students who scored above 80 in Marks.
print("\nStudents who scored above 80:")
print(df[df['Marks'] > 80])

# Sort students based on Marks in descending order.
print("\nStudents sorted by marks in descending order:")
print(df.sort_values(by='Marks', ascending=False))
print()

##########################################################################################################

# Part 3: Modified DataFrame from part 2, with missing values.
studentDataMissing = {
    "Student": ['Ardan', 'Ryder', 'Josh', 'Carter', 'Brodey'],
    "Age": [23, 18, 17, 28, None],
    "Grade": ['A', 'C', 'C', 'A', 'B'],
    "Marks": [85, 62, None, 81, 71]
}

missingData_df = pd.DataFrame(studentDataMissing)

# Replace missing values in Age with the mean age.
missingData_df.fillna({'Age': missingData_df['Age'].mean()}, inplace=True)

print("\nDataFrame with 'Brodey' age as an average:")
print(missingData_df)
print()

# Remove any rows where Marks is missing.
missingData_df.dropna(subset=['Marks'], inplace=True)

print("\nDataFrame with 'Brodey' age as an average, and the 'Josh' row deleted:")
print(missingData_df)
print()

##########################################################################################################

# Part 4: Save the cleaned DataFrame.
missingData_df.to_csv("Practical10/students_cleaned.csv", index=False)

# Load the CSV into a new DataFrame.
fromCSV_df = pd.read_csv("Practical10/students_cleaned.csv")

# Display the first 5 rows from the CSV DataFrame.
print("\nDataFrame from CSV:")
print()
print(fromCSV_df.head())
print()