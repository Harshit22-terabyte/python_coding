"""
Convert hex to binary and take first 2 digit values as system id and others as severity
"""
def severity_sys_id(hexa_value):
    # Calculate the dynamic bit count based on the length of the hexadecimal value
    required_bit_length = len(hexa_value) * 4  # Each hex digit maps to 4 binary bits

    # Convert hexadecimal to binary
    binary_value = bin(int(hexa_value, 16)).replace('0b', "").zfill(required_bit_length)
    print("Binary representation: {}".format(binary_value))

    # Extract System ID (first 2 bits) and Severity (remaining bits)
    system_id = binary_value[0:2]
    severity = binary_value[2:]

    # Convert Severity to an integer for proper comparisons
    integer_severity = int(severity, 2)

    # Map Severity Levels
    if integer_severity >= int('110', 2):  # High severity
        severity_factor = "High"
    elif int('010', 2) <= integer_severity <= int('101', 2):  # Medium severity
        severity_factor = "Medium"
    else:  # Low severity
        severity_factor = "Low"

    # Convert System ID to decimal
    decimal_system_id = int(system_id, 2)

    # Print Results
    print(
        "Node with System ID (binary: {}) and (decimal: {}) has a severity of {}.".format(
            system_id, decimal_system_id, severity_factor
        )
    )


# Test Cases
severity_sys_id(hexa_value='1F')  # 2 hex digits → 8 bits
severity_sys_id(hexa_value='01')
severity_sys_id(hexa_value='05')
severity_sys_id(hexa_value='ABC')  # 3 hex digits → 12 bits
severity_sys_id(hexa_value='FACE')  # 4 hex digits → 16 bits
