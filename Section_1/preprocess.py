import pandas as pd
import argparse
import re
import datetime

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--fpath', type=str, required=True, help='file path to dataset.csv')
    parser.add_argument('--spath', type=str, required=True, help='save path to processed dataset.csv')

    return parser.parse_args()

def clean_names(names):
    '''
    Clean the names column of the dataframe by removing salutations and titles from the start and end of the name
    This is done by passing 2 regex patterns, and for any matches the salutations/titles is replaced with empty string
    Args:
        names (List): list of names to be filtered
    Returns:
        filtered_names (List): List of filtered names that only contains <First Name> <Last Name>
    '''
    start_pattern = re.compile(r"^(\.|Mr|Mrs|Ms|Miss|Mdm|Madam|Dr|Jr)\.?\s")
    eos_pattern = re.compile(r"(Jr|I+V*|V+I*|X+I*V*|DDS|DVM|MD|PhD)\.?$")
    
    filtered_names = names.copy()
    for idx in range(len(filtered_names)):
        original_name = filtered_names[idx]
        r1 = re.search(start_pattern, filtered_names[idx])
        if r1:
            filtered_names[idx] = filtered_names[idx].replace(r1.group(), "").strip()
        r2 = re.search(eos_pattern, filtered_names[idx])
        if r2:
            filtered_names[idx] = filtered_names[idx].replace(r2.group(), "").strip()
        assert len(filtered_names[idx].split()) == 2, print(f"[{str(datetime.datetime.now())}] Names not filtered correctly. {original_name} -> {filtered_names[idx]}")

    return filtered_names

def main():
    args = parse_arguments()
    df = pd.read_csv(args.fpath)
    # Step 1: Converting price to numeric to remove prepended zeros
    df['price'] = pd.to_numeric(df['price'])

    # Step 2: Remove rows where the names are missing
    df = df.dropna(subset=['name'])

    # Step 3: Converting names column into first name and last name column
    names = list(df.name)
    names = clean_names(names)
    # Assigning list of first names to fnames and list of last names to lnames
    fnames = [name.split()[0] for name in names]
    lnames = [name.split()[1] for name in names]
    # Adding the fnames and lnames as columns to dataframe
    df['first_name'] = fnames
    df['last_name'] = lnames
    # dropping original name column
    df = df.drop('name', 1)

    # Step 4: Create a new field named `above_100`, which is `true` if the price is strictly greater than 100
    df['above_100'] = df['price'] > 100

    # Save the dataframe back to the original csv file
    df.to_csv(args.spath, index=False)


if __name__ == '__main__':
    main()