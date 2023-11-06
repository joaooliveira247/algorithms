#[allow(dead_code)]
fn find_smallest(arr: &Vec<i32>) -> usize {
    let mut smallest_index = 0;
    let mut smallest = arr[smallest_index];

    for (i, _) in arr.iter().enumerate() {
        if arr[i] < smallest {
            smallest = arr[i];
            smallest_index = i;
        }
    }
    smallest_index
}

#[allow(dead_code)]
fn selection_sort(arr: &mut Vec<i32>) -> Vec<i32> {
    let mut new_arr = Vec::new();
    while !arr.is_empty() {
        let smallest = find_smallest(arr);
        new_arr.push(arr.remove(smallest));
    }
    new_arr
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_smallest() {
        let result = find_smallest(&vec![32, 55, 26, 8, 19, 3]);
        assert_eq!(result, 5);
    }

    #[test]
    fn test_selection_sort() {
        let result = selection_sort(&mut vec![32, 55, 26, 8, 19, 3]);
        assert_eq!(result, vec![3, 8, 19, 26, 32, 55])
    }
}
