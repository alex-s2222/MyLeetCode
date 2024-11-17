package main

func isValid(s string) bool {
    brackets := map[string]string{
        "}":"{",
        ")":"(",
        "]":"[",
    }
    stack := []rune{}

    for _, element := range(s){
        str_element := string(element)
        if str_element == "(" || str_element == "{" || str_element == "["{
            stack = append(stack, element)
        }else if len(stack) == 0 || string(stack[len(stack) - 1]) != brackets[str_element]{
            return false
        }else{
            stack = stack[:len(stack) - 1]
        }
    }
    return len(stack) == 0
}