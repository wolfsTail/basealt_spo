## Package Comparison Tool

This CLI application compares binary packages between two specified branches and saves the results in a JSON file.

### Prerequisites

- Python 3.11 or later installed on your system.
- Internet access if the tool needs to fetch package data from an online API.

### Getting Started

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/wolfsTail/basealt_spo.git
cd basealt_spo
```

Install requerments:
```bash
pip install -r requerments.txt
```

Before running the script, you need to make it executable. This can be done using the chmod command:

```bash
chmod +x main.py
```

### Usage

Run the tool by specifying two branches to compare. You can also specify an optional output file name (without extension).

```bash
main.py <branch1> <branch2> [-o <output_filename_without_extension>]
```

### Arguments
- branch1: The name of the first branch for comparison.
- branch2: The name of the second branch for comparison.
- -o, --output (optional): The base name for the output file (without extension) where the results will be saved. Defaults to result, creating a file named result.json in the current directory.

### Example

To compare packages between p10 and sisyphus branches and save the results in comparison_results.json:

```bash
main.py p10 sisyphus -o comparison_results
```

### Output

The results are saved in a JSON file in the current directory.