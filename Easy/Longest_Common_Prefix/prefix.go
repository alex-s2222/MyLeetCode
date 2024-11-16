package main

func longestCommonPrefix(strs []string) string {
    fl := true 
    result := ""

    for idx, letter := range strs[0]{
        for _, word := range strs[1:] {
            if len(word) >= idx + 1 {
                if string(letter) != string(word[idx]){
                    fl = false
                }
            }else{
                fl = false
            }
        }
        if fl == true {
            result += string(letter)
        }else{
            break
        }
    }
    return result
}