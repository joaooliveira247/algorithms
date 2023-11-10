#[allow(dead_code)]
fn sum_natural_numbers(n: u32) -> u32 {
    if n < 1 {
        return n;
    }
    n + sum_natural_numbers(n - 1)
}

#[allow(dead_code)]
fn sum_array_elements(arr: &mut Vec<u32>) -> u32 {
    if arr.len() <= 0 {
        return 0;
    }
    arr.remove(0) + sum_array_elements(arr)
}

#[allow(dead_code)]
fn factorial(n: u32) -> u32 {
    if n <= 1 {
        return 1;
    }
    n * factorial(n - 1)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum_natural_numbers() {
        let result = sum_natural_numbers(3);
        assert_eq!(result, 6);
    }

    #[test]
    fn test_sum_array_elements() {
        let mut arr: Vec<u32> = vec![1, 2, 3, 4, 5, 6];
        let result = sum_array_elements(&mut arr);
        assert_eq!(result, 21);
    }

    #[test]
    fn test_factorial() {
        let result = factorial(6);
        assert_eq!(result, 720);
    }
}
