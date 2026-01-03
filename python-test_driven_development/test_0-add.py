import sys
sys.path.insert(0, '.')

# Use importlib to import module with special name
import importlib.util
spec = importlib.util.spec_from_file_location("add_integer_module", "0-add_integer.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test the function
print(module.add_integer(1, 2))
print(module.add_integer(100, -2))
print(module.add_integer(2))
