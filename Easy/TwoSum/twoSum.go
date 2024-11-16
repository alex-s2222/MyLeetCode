package main

func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)

    for i, num := range nums {
        if j, ok := hashMap[target-num]; ok {
            return []int{i,j}
        }
        hashMap[num] = i
    }
    return []int{-1,-1}
}

