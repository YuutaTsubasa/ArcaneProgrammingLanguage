from enum import Enum
from llvmlite import ir

class TypeDefinition(str, Enum):
    Int8 = "Int8"
    Int16 = "Int16"
    Int32 = "Int32"
    Int64 = "Int64"
    Uint8 = "Uint8"
    Uint16 = "Uint16"
    Uint32 = "Uint32"
    Uint64 = "Uint64"
    Float32 = "Float32"
    Float64 = "Float64"
    Bool = "Bool"
    Char = "Char"

    def get_llvm_type(self):
        type_mapping = {
            TypeDefinition.Int8: ir.IntType(8),
            TypeDefinition.Int16: ir.IntType(16),
            TypeDefinition.Int32: ir.IntType(32),
            TypeDefinition.Int64: ir.IntType(64),
            TypeDefinition.Float32: ir.FloatType(),
            TypeDefinition.Float64: ir.DoubleType(),
            TypeDefinition.Bool: ir.IntType(1),
            TypeDefinition.Char: ir.IntType(8)
        }

        return type_mapping.get(self, None)
    
    def is_integer(self):
        return (self is TypeDefinition.Int8 or
            self is TypeDefinition.Int16 or
            self is TypeDefinition.Int32 or 
            self is TypeDefinition.Int64)
    
    def is_float(self):
        return (self is TypeDefinition.Float32 or
            self is TypeDefinition.Float64)

    def get_convertible_type(type_a, type_b):
        if type_a == type_b:
            return type_a
        
        weight_table = {
            TypeDefinition.Int8: 0,
            TypeDefinition.Int16: 1,
            TypeDefinition.Int32: 2,
            TypeDefinition.Int64: 3,
            TypeDefinition.Float32: 4,
            TypeDefinition.Float64: 5,
        }

        if type_a not in weight_table:
            raise Exception(f"{type_a} is not a convertible type.")
        
        if type_b not in weight_table:
            raise Exception(f"{type_b} is not a convertible type.")
        
        weight_a = weight_table[type_a]
        weight_b = weight_table[type_b]

        max_weight = max(weight_a, weight_b)
        weight_to_type_table = {v: k for k, v in weight_table.items()}
        return weight_to_type_table[max_weight]