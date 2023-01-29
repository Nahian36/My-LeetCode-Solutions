def hammingWeight(n: int):
    # return bin(n).count("1")
    return str(n).count("1")

print(hammingWeight("00000000000000000000000000001011"))
print(hammingWeight("00000000000000000000000010000000"))
print(hammingWeight("11111111111111111111111111111101"))