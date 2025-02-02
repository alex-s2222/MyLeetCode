package main

func strStr(haystack string, needle string) int {
    end := 0
    len_needle := len(needle)

    for start := 0; start + len_needle <= len(haystack); start ++{
        end = len_needle + start
        if haystack[start:end] == needle{
            return start
        }
    }
    return -1
}