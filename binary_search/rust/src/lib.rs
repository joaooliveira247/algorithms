pub fn binary_search(vec: &Vec<i32>, item: i32) -> Option<i32> {
    let mut low = 0;
    let mut high = vec.len() - 1;

    while low <= high {
        let mid = (low + high) / 2;
        let guess = vec[mid];
        if guess == item {
            return Some(mid as i32);
        }
        if guess > item {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use crate::binary_search;

    #[test]
    fn binary_search_value() {
        let vec = vec![2, 4, 6, 8, 10, 13, 19, 32];
        let result = binary_search(&vec, 13);
        assert_eq!(result, Some(5))
    }

    #[test]
    fn binary_search_none() {
        let vec = vec![2, 4, 6, 8, 10, 13, 19, 32];
        let result = binary_search(&vec, 666);
        assert_eq!(result, None)
    }
}
