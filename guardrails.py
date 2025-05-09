def is_safe_response(response: str) -> (bool, list):
    unsafe_keywords = ["guaranteed", "get rich quick", "no risk"]
    found = [word for word in unsafe_keywords if word in response.lower()]
    return len(found) == 0, found