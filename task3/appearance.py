#-*- encoding: utf-8 -*-

def sort_by_begin(arr):
    decorated = [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]
    decorated.sort()
    return(decorated)

def intersect_interval_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []
    arr1 = sort_by_begin(arr1)
    arr2 = sort_by_begin(arr2)
    while i < len(arr1) and j < len(arr2):
        if arr2[j][0] >= arr1[i][1]:
            i += 1
        elif arr1[i][0] >= arr2[j][1]:
            j += 1
        else:
            if arr1[i][0] < arr2[j][0]:
                result.append(arr2[j][0])
            else:
                result.append(arr1[i][0])
            if arr1[i][1] < arr2[j][1]:
                result.append(arr1[i][1])
                i += 1
            else:
                result.append(arr2[j][1])
                j += 1
    return(result)


def appearance(intervals):
    intersection = intersect_interval_arrays(intervals["lesson"], intersect_interval_arrays(intervals["pupil"], intervals["tutor"]))
    i = 0
    secs = 0
    while i < len(intersection):
        secs += intersection[i + 1] - intersection[i]
        i += 2
    return(secs)
