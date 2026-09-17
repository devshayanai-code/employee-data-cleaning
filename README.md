# employee-data-cleaning
"Data cleaning pipeline for employee records using pandas"
# Employee Data Cleaning

This is my first data cleaning project using Python, Pandas, and NumPy.

I worked with an employee dataset that contained different types of messy and missing data. The purpose of this project was to inspect the dataset, identify problems, and clean the data so that it could be used more reliably for further analysis.

## What I worked on

I started by loading the dataset with Pandas and inspecting it using functions such as `info()`, `describe()`, and `isnull().sum()`.

This helped me understand the structure of the data, the data types of different columns, the basic statistics, and where missing values existed.

### Employee ID

I checked the `EmployeeID` column for missing values. Records without an Employee ID were removed because the ID is important for identifying an employee.

### Employee Name

Some names had unnecessary spaces or inconsistent capitalization. I used Pandas string methods to remove extra spaces and convert the names into title case.

For example, a name such as:

`  john smith  `

was converted into:

`John Smith`

Missing names were replaced with `"Unknown"`.

### Email

I cleaned the email column by removing unnecessary spaces and converting the emails to lowercase.

For example:

`  JOHN@EMAIL.COM  `

was converted into:

`john@email.com`

Missing email values were replaced with `"no_email"`.

### Salary

I checked the salary column for invalid values.

Salaries less than or equal to zero were considered invalid, and salaries greater than 200,000 were also treated as invalid values.

These invalid values were converted to `NaN` and then replaced using the mean salary of the dataset.

### Joining Date

The `JoinDate` column contained dates that needed to be converted into a proper datetime format.

I used Pandas `to_datetime()` to convert the values and handled missing dates by filling them with the most common date in the dataset.

### Phone Number

The phone numbers had inconsistent formatting, such as spaces and hyphens.

I removed these characters to make the phone numbers more consistent.

For example:

`0300-123 4567`

was cleaned to:

`03001234567`

Missing phone numbers were replaced with `"unknown"`.

## What I learned

Through this project, I practiced some of the fundamental techniques used in data cleaning with Python.

I learned how to inspect a dataset, identify missing and invalid values, clean strings, work with dates, apply conditions to data, replace problematic values, and use Pandas and NumPy to prepare data for further analysis.

This project is a starting point for me, and I plan to build on these skills with more advanced data analysis and machine learning projects.

