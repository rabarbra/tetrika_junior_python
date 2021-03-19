#-*- encoding: utf-8 -*-

def intersect_interval_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i + 1 < len(arr1) and j + 1 < len(arr2):
        if arr2[j] >= arr1[i + 1]:
            i += 2
        elif arr1[i] >= arr2[j + 1]:
            j += 2
        else:
            if arr1[i] < arr2[j]:
                result.append(arr2[j])
            else:
                result.append(arr1[i])
            if arr1[i + 1] < arr2[j + 1]:
                result.append(arr1[i + 1])
                i += 2
            else:
                result.append(arr2[j + 1])
                j += 2
    return(result)


def appearance(intervals):
    intersection = intersect_interval_arrays(intervals["lesson"], intersect_interval_arrays(intervals["pupil"], intervals["tutor"]))
    i = 0
    secs = 0
    while i < len(intersection):
        secs += intersection[i + 1] - intersection[i]
        i += 2
    return(secs)
