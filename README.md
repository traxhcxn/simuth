# simuth

A simple Python package built while bored.
Currently contains only basic sorts, will do more as I progress more :D

---

## Installation

You can install from PyPI:

```bash
pip install simuth
```

## Usage
After installing, import the `Sorting` class and call any method.

```python
from simuth import Sorting

arr = [5, 3, 8, 4, 2]

print(Sorting.bubble_sort(arr))
print(Sorting.quick_sort_lomuto(arr))

# Special Dutch National Flag (only for 0s, 1s and 2s)
colors = [2, 0, 1, 2, 0, 0]
print(Sorting.dutch_national_flag(colors)) 
```

## Currently available algorithms
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort (Lomuto and Hoare)
6. Dutch National Flag Algorithm
7. An Easter Egg

## License
This project is licensed under the [MIT License](LICENSE)