import dis

# The dis module supports the analysis of CPython bytecode by disassembling it


def hello():
    print("Hello World")


hello()
print("~~~~~ Bytecode ~~~~~")

dis.dis(hello)
