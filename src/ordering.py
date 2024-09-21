def ordering_bubble(folders) -> bool:
    limit = len(folders)
    for i in range(limit - 1):
        for j in range(limit - 1 - i):
            if folders[j] > folders[j + 1]:
                folders[j], folders[j + 1] = folders[j + 1], folders[j]
    return True


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
