from typing import List

class Sorting:   
    @staticmethod 
    def bubble_sort(arr: List[int]) -> List[int]:
        temp = arr[:]
        N = len(temp)
        for i in range(N):
            swapped = False
            for j in range(0, N-i-1):
                if temp[j] > temp[j+1]:
                    temp[j], temp[j+1] = temp[j+1], temp[j]
                    swapped = True
            if not swapped:
                break
        return temp

    @staticmethod
    def selection_sort(arr: List[int]) -> List[int]:
        temp = arr[:]
        N = len(temp)
        for i in range(N):
            for j in range(i+1, N):
                if temp[i] > temp[j]:
                    temp[i], temp[j] = temp[j], temp[i]
        return temp
    
    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        temp = arr[:]
        N = len(temp)
        for i in range(1, N):
            key = temp[i]
            j = i - 1
            while j >= 0 and temp[j] > key:
                temp[j+1] = temp[j]
                j -= 1
            temp[j+1] = key
        return temp
    
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        temp = arr[:]
        N = len(temp)
        if N <= 1: return temp
        mid = N // 2
        left = Sorting.merge_sort(temp[:mid])
        right = Sorting.merge_sort(temp[mid:])
        return Sorting._merge(left, right)
    
    @staticmethod
    def quick_sort_lomuto(arr: List[int]) -> List[int]:
        temp = arr[:]
        
        def partition(low, high):
            pivot = temp[high]
            i = low - 1
            for j in range(low, high):
                if temp[j] <= pivot:
                    i += 1
                    temp[i], temp[j] = temp[j], temp[i]
            temp[i+1], temp[high] = temp[high], temp[i+1]
            return i + 1

        def quicksort(low,high):
            if low < high:
                pi = partition(low, high)
                quicksort(low, pi - 1)
                quicksort(pi + 1, high)

        quicksort(0, len(temp) - 1)
        return temp
    
    @staticmethod
    def quick_sort_hoare(arr: List[int]) -> List[int]:
        temp = arr[:]

        def partition(low, high):
            pivot = temp[(low + high) // 2]
            i, j = low, high
            while True:
                while temp[i] < pivot:
                    i += 1
                while temp[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                temp[i], temp[j] = temp[j], temp[i]
                i += 1
                j -= 1

        def quicksort(low, high):
            if low < high:
                pi = partition(low, high)
                quicksort(low, pi)
                quicksort(pi + 1, high)

        quicksort(0, len(temp) - 1)
        return temp

    @staticmethod
    def dutch_national_flag(arr: List[int]) -> List[int]:
        temp = arr[:]
        low, mid, high = 0, 0, len(temp) - 1

        while mid <= high:
            if temp[mid] == 0:
                temp[low], temp[mid] = temp[mid], temp[low]
                low += 1
                mid += 1
            elif temp[mid] == 1:
                mid += 1
            else:
                temp[mid], temp[high] = temp[high], temp[mid]
                high -= 1
        return temp
    
    def _merge(left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    @staticmethod
    def get_muruganed() -> str:
        return "You got Muruganed!"