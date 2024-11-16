package main

func romanToInt(s string) int {
    romans := map[string]int{
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,}
    i := 0 
    result := 0
    len_str := len([]rune(s))

    for i < len_str{
        value := romans[string(s[i])] 
        if i + 1 < len_str{
            nextVal := romans[string(s[i + 1])]
            if value < nextVal{
                result += nextVal - value
                i += 2
            }else{
                result += value 
                i++
            }
        } else{
            result += value
            i++
        }
    }

    return result
}