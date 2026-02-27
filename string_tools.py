# update

def title_case(text: str) -> str:
    """Convert text to Title Case (basic)."""
    return " ".join(w.capitalize() for w in text.split())

def snake_case(text: str) -> str:
    """Convert text to snake_case (basic)."""
    return "_".join("".join(c.lower() if c.isalnum() else " " for c in text).split())

if __name__ == "__main__":
    sample = "Hello, Infinity Developer!"
    print("Title:", title_case(sample))
    print("Snake:", snake_case(sample))
