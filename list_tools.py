def count_items(items):
    return len(items)

def unique_items(items):
    return list(set(items))

if __name__ == "__main__":
    sample = ["apple", "banana", "apple", "orange"]
    print("Count:", count_items(sample))
    print("Unique:", unique_items(sample))
