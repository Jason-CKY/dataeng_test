# DSAID Data Engineering Technical Test

## Section 1: Data Pipelines
The objective of this section is to design and implement a solution to process a data file on a regular interval (e.g. daily). Given the test data file `dataset.csv`, design a solution to process the file, along with the scheduling component. The expected output of the processing task is a CSV file including a header containing the field names.

You can use common scheduling solutions such as `cron` or `airflow` to implement the scheduling component. You may assume that the data file will be available at 1am everyday. Please provide documentation (a markdown file will help) to explain your solution.

Processing tasks:
- Split the `name` field into `first_name`, and `last_name`
- Remove any zeros prepended to the `price` field
- Delete any rows which do not have a `name`
- Create a new field named `above_100`, which is `true` if the price is strictly greater than 100

*Note: please submit the processed dataset too.*


## Examining dataset.csv

The csv file is read using the pandas read_csv function.

A cursory view through the dataset.csv reveals certain problematic name structure such as Salutations at the start of the name like `Mr.`, `Mrs.` and `Miss`, as well as titles or acronyms at the end of the name like `MD`, `DDS`, and `III`.

## Step 1: Removing Prepended zeros to the `price` field

Prepended zeros are captured by the dataframe if the `price` column is read as an object containing strings.

The prepended zeros can be easily ignored by converting the dtype of the `price` column of the dataframe into float. 

This is done by converting the df['price'] dtype using the `pd.to_numeric` function.

## Step 2: Delete any rows which do not have a `name`
Rows with no name will show up as a `NaN` in the pandas dataframe.
These rows can be removed using `pd.dropna(subset=['name'])`.
The subset argument is passed as name, so only rows with missing name will be removed,
but not rows with missing price.

## Step 3: Split the `name` field into `first_name`, and `last_name`
There are 2 kinds of titles in the name column:
1. Titles at the start of the name (`Mr.`, `Mrs.`, `etc`)
2. Titles at the end of the name (`PhD`, `III`, `DVM`, `etc`)

I made 2 regex patterns to match the 2 kinds of titles.

Start of String pattern: 

`re.compile(r"^(\.|Mr|Mrs|Ms|Miss|Dr|Jr)\.?\s")`

This pattern matches at the start of the string, any Mr, Mrs, Ms, Miss, Dr, Jr character sets with an optional period (`.`) at the end, followed by a space.


End of String pattern: 

`re.compile(r"(Jr|I+V*|V+I*|X+I*V*|DDS|DVM|MD|PhD)\.?$")`

This pattern matches at the end of the string, any Jr, Roman Numerals that start with I, V, and X respectively, DDS, DVM, MD, and PhD character sets with an optional period (`.`) at the end.

Each name in the names column is passed through the regex pattern match, and every match discovered, the pattern in the name is replaced with an empty string to remove the pattern.

After removing all titles and salutations from the name, we ensure that each name now only has 2 words, the first name and last name with an assert statement. 

After that, we create 2 separate list from this edited names list, containing the first name and last name respectively, and add them into the dataframe. 

Finally, we remove the original names column from the dataframe.



