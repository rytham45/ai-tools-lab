# ai-tools-lab
# AI Tools Lab

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

A beginner-friendly Python project that brings together classic **sorting algorithms** and handy **utility functions**. The code is kept simple and well documented, making it a good place to learn, experiment, and contribute.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Sorting algorithms:** simple implementations such as Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort.
- **Utility functions:** small, reusable helpers for everyday tasks.
- **Beginner-friendly code:** plain Python with no external dependencies and clear docstrings on every function.

### Utility functions

| Function | Description |
|----------|-------------|
| `is_palindrome(s)` | Returns `True` if a string reads the same forwards and backwards (ignores spaces, punctuation, and case). |
| `count_words(text)` | Returns the number of words in a piece of text. |
| `celsius_to_fahrenheit(c)` | Converts a temperature from Celsius to Fahrenheit. |

## Project Structure

```
ai-tools-lab/
├── sorting.py      # Sorting algorithms
├── utils.py        # Utility functions
├── README.md
└── LICENSE
```

## Installation

**Requirements:** Python 3.8 or newer. No third-party packages are needed.

1. **Clone the repository**

   ```bash
   git clone https://github.com/rytham45/ai-tools-lab.git
   ```

2. **Move into the project folder**

   ```bash
   cd ai-tools-lab
   ```

3. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

4. **Verify your setup**

   ```bash
   python utils.py
   ```

## Usage

### Utility functions

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

# Check for palindromes
print(is_palindrome("Race car"))          # True
print(is_palindrome("Hello"))             # False

# Count words
print(count_words("Python is fun"))       # 3
print(count_words(""))                    # 0

# Convert temperatures
print(celsius_to_fahrenheit(0))           # 32.0
print(celsius_to_fahrenheit(100))         # 212.0
```

### Sorting algorithms

```python
from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort

numbers = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(numbers))       # [11, 12, 22, 25, 34, 64, 90]
print(selection_sort(numbers))    # [11, 12, 22, 25, 34, 64, 90]
print(insertion_sort(numbers))    # [11, 12, 22, 25, 34, 64, 90]
print(merge_sort(numbers))        # [11, 12, 22, 25, 34, 64, 90]
```

### Time complexity at a glance

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes, keeping the code simple and adding docstrings.
4. Commit your work: `git commit -m "Add your feature"`
5. Push to your branch: `git push origin feature/your-feature-name`
6. Open a Pull Request describing your changes.

## Contributors

Thanks to everyone who has contributed to this project!

| Name | GitHub | Role |
|------|--------|------|
| Rytham | [@rytham45](https://github.com/rytham45) | Creator & Maintainer |

Want to see your name here? Check out the [Contributing](#contributing) section.

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Rytham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
