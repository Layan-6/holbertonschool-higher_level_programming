import pickle
import json

# For pickle serialization
def save_data(data, filename):
    """Save data using pickle serialization"""
    try:
        with open(filename, 'wb') as f:  # 'wb' for binary writing
            pickle.dump(data, f)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_data(filename):
    """Load data using pickle deserialization"""
    try:
        with open(filename, 'rb') as f:  # 'rb' for binary reading
            data = pickle.load(f)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# For JSON serialization (for simpler data types)
def save_json(data, filename):
    """Save data using JSON serialization"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:  # 'w' for text writing
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False 
