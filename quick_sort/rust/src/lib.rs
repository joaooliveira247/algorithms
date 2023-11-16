pub fn quicksort(mut arr: Vec<i32>) -> Vec<i32> {
    if arr.len() < 2 {
        return arr;
    }
    let pivot = arr.remove(0);
    let less: Vec<i32> = arr.iter().filter(|&i| *i <= pivot).cloned().collect();
    let greater: Vec<i32> = arr.into_iter().filter(|i| *i > pivot).collect();
    [quicksort(less), vec![pivot], quicksort(greater)].concat()
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_quicksort_three_elements() {
        let result = quicksort(vec![3, 2, 1]);
        assert_eq!(result, vec![1, 2, 3]);
    }

    #[test]
    fn test_quicksort_two_elements() {
        let result = quicksort(vec![27, 9]);
        assert_eq!(result, vec![9, 27]);
    }

    #[test]
    fn test_quicksort_empty() {
        let result = quicksort(vec![]);
        assert_eq!(result, vec![]);
    }
}
