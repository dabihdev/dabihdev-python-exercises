# this file can stay empty; however it is often used to make imports easier
# kind of a Setup Code
from .converter import decimal_to_binary, binary_to_decimal

print("Initializing package....")

__all__ = ["decimal_to_binary", "binary_to_decimal"]

print("Ready to use!")