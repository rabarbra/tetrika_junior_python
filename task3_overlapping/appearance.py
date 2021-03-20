#-*- encoding: utf-8 -*-

def merge_intervals(arr):
    res = []
    for beg, end in arr:
        if res and res[-1][1] >= beg:
            res[-1] = (res[-1][0], max(res[-1][1], end))
        else:
            res.append((beg, end))
    return(res)

def intersect_interval_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i][1] <= arr2[j][0]:
            i += 1
        elif arr2[j][1] <= arr1[i][0]:
            j += 1
        else:
            result.append((max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])))
            if arr1[i][1] < arr2[j][1]:
                i += 1
            else:
                j += 1
    return(result)


def appearance(intervals):
    lesson = merge_intervals(sorted(zip(intervals["lesson"][::2], intervals["lesson"][1::2])))
    pupil = merge_intervals(sorted(zip(intervals["pupil"][::2], intervals["pupil"][1::2])))
    tutor = merge_intervals(sorted(zip(intervals["tutor"][::2], intervals["tutor"][1::2])))
    intersection = intersect_interval_arrays(lesson, 
            intersect_interval_arrays(pupil, tutor))
    secs = 0
    for interval in intersection:
        secs += interval[1] - interval[0]
    return(secs)
