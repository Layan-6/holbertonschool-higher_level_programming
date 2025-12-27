# Python Serialization

This directory contains exercises and files related to serialization and deserialization concepts in Python.

## 📁 Directory Contents

### 0. Basic Serialization
- **File:** `task_00_basic_serialization.py`
- **Description:** Basic serialization and deserialization module using JSON
- **Functions:**
  - `serialize_and_save_to_file(data, filename)`: Serialize a Python dictionary and save it to a JSON file
  - `load_and_deserialize(filename)`: Load and deserialize a JSON file to a Python dictionary

## 🚀 How to Use

### Running Exercise 0:
```bash
# First: Create a test file
cat > test_serialization.py << 'EOF'
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Test data
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize and save
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# Load and deserialize
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
EOF

# Second: Run the test
python3 test_serialization.py
