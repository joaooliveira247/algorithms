use std::collections::HashMap;

fn main() {
    let mut book:HashMap<String, f32> = HashMap::new();
    book.insert(String::from("Avocado"), 1.49);
    book.insert(String::from("Apple"), 0.67);
    book.insert(String::from("milk"), 1.49);
    println!("{:?}", book);
}