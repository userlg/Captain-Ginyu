def quicksort(folders: list, left, right) -> None:
    if left < right:
        index_partition = partition(folders, left, right)
        quicksort(folders, left, index_partition)
        quicksort(folders, index_partition + 1, right)


def partition(folders: list, left, right) -> int:
    pivot = folders[left]
    while True:
        while folders[left] < pivot:
            left += 1

        while folders[right] > pivot:
            right -= 1

        if left >= right:
            return right
        else:
            folders[left], folders[right] = folders[right], folders[left]
            left += 1
            right -= 1
