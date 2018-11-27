def sotogawa(num: int) -> int:

    def uchigawa(comp: int) -> int:

        return num * comp

    return uchigawa


so1 = sotogawa(1)
so3 = sotogawa(3)

print(so1(2))
print(so1(4))
print(so3(2))
print(so3(4))

print(so1)
