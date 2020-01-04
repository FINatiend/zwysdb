# 使用位逻辑运算实现位向量就是用一串类似0100011的二进制数
# 与要改变的向量进行位运算
# 与运算常常用mask技术的关闭开关，针对某一位置0
# 异或运算与全1串可以将所有位反转

a=30
b=5
# 实现与操作
c=a&b
print(bin(a),'\n',bin(b),'\n','与操作为：',bin(c))
#实现或操作
c=a|b
print(bin(a),'\n',bin(b),'\n','或操作为：',bin(c))
#实现异或操作
c=a^b
print(bin(a),'\n',bin(b),'\n','异或操作为：',bin(c))
#实现非操作
c=~a
print(bin(a),'\n',bin(b),'\n','非操作为：',bin(c))
#实现左移操作，高位丢弃，地位补零
c=a<<2
print(bin(a),'\n',bin(b),'\n','左移操作为：',bin(c))
#实现右移操作，地位丢弃，高位补零
c=a>>2
print(bin(a),'\n',bin(b),'\n','右移操作为：',bin(c))