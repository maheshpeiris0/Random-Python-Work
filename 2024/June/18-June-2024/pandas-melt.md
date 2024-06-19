The `pandas.melt` function is used to transform or reshape a DataFrame from wide format to long format. This function is especially useful when you have a DataFrame where multiple columns represent different variables, and you want to consolidate them into a single column with corresponding values.

Here is a detailed example and explanation of how to use `pandas.melt`.

### Example DataFrame

Let's create an example DataFrame in wide format:

```python
import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 95],
    'Science': [88, 92, 98],
    'English': [87, 89, 94]
}

df = pd.DataFrame(data)
print(df)
```

This will produce the following DataFrame:

```
   ID     Name  Math  Science  English
0   1    Alice    85       88       87
1   2      Bob    90       92       89
2   3  Charlie    95       98       94
```

### Using `pd.melt`

To transform this DataFrame into long format, where each subject's score is a row, we use `pd.melt`:

```python
df_melted = pd.melt(df, id_vars=['ID', 'Name'], value_vars=['Math', 'Science', 'English'], var_name='Subject', value_name='Score')
print(df_melted)
```

This will produce the following long-format DataFrame:

```
   ID     Name  Subject  Score
0   1    Alice     Math     85
1   2      Bob     Math     90
2   3  Charlie     Math     95
3   1    Alice  Science     88
4   2      Bob  Science     92
5   3  Charlie  Science     98
6   1    Alice  English     87
7   2      Bob  English     89
8   3  Charlie  English     94
```

### Explanation

- **`id_vars`**: These are the columns that you do not want to melt. They will remain as identifier variables in the resulting DataFrame. In this example, `['ID', 'Name']` are identifier variables.
- **`value_vars`**: These are the columns that you want to melt. They will be unpivoted to the row axis. In this example, `['Math', 'Science', 'English']` are the variables that are melted.
- **`var_name`**: The name to use for the variable column. In this example, it's `Subject`.
- **`value_name`**: The name to use for the value column. In this example, it's `Score`.

The resulting DataFrame now has each subject's score in a single column, making it easier to analyze or visualize the data in a long-format style.

Feel free to ask if you have any more questions or need further examples!
