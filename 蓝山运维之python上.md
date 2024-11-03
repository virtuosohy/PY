# 蓝山运维之python上

## 前言：

可能有的同学正在学或者没有学过python，或者有的学过C语言而有的一门编程语言都没有学过，不过都没关系，对于python来说，变量以及运算符号都是差不多的。所以大家不用担心，网上也有很多关于python的教程。大家可以根据自己的实际情况去看视频或者查阅相关文档。

## Python简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。(Python 的解释器会逐行读取代码，解析并执行每一行)。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
- **Python 是初学者的语言：**Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

**python的版本：**

  现在python默认的都是python3了。因为**官方宣布，2020 年 1 月 1 日， 停止 Python 2 的更新。**这意味着 Python 2 不再接受官方的维护更新或安全补丁。Python 3 是当前的主要版本，它包括许多新特性和改进，同时解决了 Python 2 中的一些问题。

查看版本

```
python3 --version
```

## python基础教程

### 运行第一个Python程序

**交互式编程**

交互式编程不需要创建脚本文件，是通过 Python 解释器的交互模式进来编写代码。

在终端直接输入python3命令即可启动交互式编程

![image-20240819150808956](https://gitee.com/vkermt/blogimage/raw/master/images/image-20240819150808956.png)

**脚本式编程**

通过脚本参数调用解释器开始执行脚本，直到脚本执行完毕。当脚本执行完成后，解释器不再有效。

所有 Python 文件将以 **.py** 为扩展名。

```shell
echo "hello world" > app.py
python3 app.py
```

### python语法规范

####  标识符

在编程中，**标识符**是用于标识变量、函数、类、模块和其他对象的名称。标识符是程序员定义的名字，帮助我们引用特定的对象。不同编程语言可能对标识符的定义有所不同，但 Python 中标识符的基本规则如下：

1. **由字母、数字和下划线组成**：标识符必须以字母（a-z、A-Z）或下划线（_）开头，后面可以跟字母、数字（0-9）或下划线。例如，`my_var` 和 `variable1` 是有效的标识符。
2. **不可以以数字开头**：标识符不能以数字开头。例如，`1variable` 是无效的标识符。
3. **区分大小写**：Python 中的标识符是区分大小写的，即 `Variable` 和 `variable` 是两个不同的标识符。
4. **不能是保留字**：标识符不能是 Python 的关键字（如 `if`、`else`、`for` 等），因为这些关键字在语言中有特殊的意义。



如何查看该版本有哪些关键字呢？

```python
import keyword
keyword.kwlist
```



5. **符合命名规则**：虽然 Python 对标识符的字符集比较宽松，但通常推荐使用有意义的名字，并遵循命名规范。例如，使用小写字母和下划线来分隔单词的形式（如 `my_variable`）以提高代码的可读性。

#### 行和缩进

学习 Python 与其他语言最大的区别就是，Python 的代码块，函数以及其他逻辑判断不使用大括号 **{}** 来控制类。python 最具特色的就是用缩进来写模块。

```c
#include<stdio.h>
int main(void)
{
    print("hello world");
    return 0;
}
```

```python
print("hello world")
```

缩进相同的一组语句构成一个代码块，我们称之代码组。

缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

```python
if True:
    print ("True")
else:
    print ("False")
```

#### python引号

Python 可以使用引号( **'** )、双引号( **"** )、三引号( **'''** 或 **"""** ) 来表示字符串，引号的开始与结束必须是相同类型的。

其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

#### Python注释



python中单行注释采用<font color='red'> **#**</font> 开头。

多行注释：“”“”“”

```python
# 这是一行注释

"""
这是
多行
注释
"""
```





### python变量类型

#### python中的变量

Python 中的变量赋值不需要类型声明。

每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。

每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

等号 **=** 用来给变量赋值。

等号 **=** 运算符左边是一个变量名，右边是存储在变量中的值。

**标准数据类型**

在内存中存储的数据可以有多种类型。

例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。

Python 定义了一些标准类型，用于存储各种类型的数据。

标准数据类型：

- **数字(Numbers)**：114514，3.14
- 布尔类(bool)：True，False
- **字符串(String)**：”Hello World”，’string’，’114514’
- **列表(List)**：列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表
- 元组(Tuple)：与列表类似，不同之处在于元组的元素不能修改
- 集合(Set)：是一种无序可变的数据类型，用于储存唯一元素
- 字典(Dictionary)：是一个无序，可变和有索引的集合

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。





#### 数字

Python支持三种不同的数字类型：

- **整型(int)** - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
- **浮点型(float)** - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 10^2^ = 250）
- **复数( (complex))** - 复数由实数部分和虚数部分构成，可以用a + bi,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

数字类型的转换：

有时候，我们需要对数据的类型进行转换，显式的来说，python提供了使用int,float等内置函数使其可以直接相互转换。

- **int(x)**   将x转换为一个整数。
- **float(x)**   将x转换到一个浮点数。
- **complex(x, y)**   将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

```python
# 定义一个复数1 + 2i
print(complex(1,2))
```

隐式数据类型的转换：

```python
a = 5
b = 3.1415
new_var = a + b
print(f"int + float 的类型为：{type(new_var)}")
```

显式转换：

```python
num_int = 1
num_flo = 3.14
a = float(num_int)
b = int(num_flo)
print(type(a))
print(type(b))
```







#### 字符串（字符容器）

字符串是 Python 中最常用的数据类型。我们可以使用引号( **'** 或 **"**或者**“”“** )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。例如：

```python
var1 = "我在蓝山学python"
var2 = '我在蓝山学python'
var3 = """我在蓝山学python"""
```

Python 访问字符串，可以使用方括号 **[]** 来截取字符串，字符串的截取的语法格式如下：

```
变量[头下标:尾下标]
```

索引值以 **0** 为开始值，**-1** 为从末尾的开始位置。

![img](https://static.jyshare.com/wp-content/uploads/123456-20200923-1.svg)



```python
var1[0]
```









**转义字符**

在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。

```
\n
print("\\n")
```





**字符串格式化**

==使用百分号 `%` 格式化（老方法）==：

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

```python
name = "Alice"
age = 30
greeting = "My name is %s and I am %d years old." % (name, age)
print(greeting)

```



==使用 f-strings（格式化字符串，Python 3.6 及以上）==

f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。

```python
name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

```



==使用 str.format()方法==

可以使用 `str.format()` 方法，通过 `{}` 占位符来插入变量。

```python
name = "Alice"
age = 30
greeting = "My name is {} and I am {} years old.".format(name, age)
print(greeting)

```



**字符串常用内建函数**

* len()

**方法**：

* count()
* replace()
* index()
* strip()

字符串规整操作：去掉前后指定字符串(默认去除前后的空格)

* find()

find与index的区别：find不会抛出异常,index会抛出异常

* split()

```python
# 将一个字符串根据指定字符，分割为对各字符串存入一个list中，并返回
my_str = "this is a str"
my_list = my_str.split(" ")
print(my_list)
```



#### 列表

列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表可以进行的操作包括索引，切片，加，乘，检查成员。此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

```python
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```

**访问列表**

与字符串的索引一样，列表索引从 **0** 开始，第二个索引是 **1**，依此类推。

通过索引列表可以进行截取、组合等操作。

索引也可以从尾部开始，最后一个元素的索引为 **-1**，往前一位为 **-2**，以此类推。

你也可以使用方括号 **[]** 的形式截取字符。

```python
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])
//输出10,20,30,40

```

**更新列表**

你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项，如下所示：

```python
list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
```

**删除列表**

```python
list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)

a = list.pop[0]
print(f"删除的元素为：{a}")
print(list)
```

del为python中的关键字，它用于删除对象引用或者从容器中移除项。

也可以用pop方法：将指定下标元素取出返回

或者用remove方法

**嵌套列表**

使用嵌套列表即在列表里创建其它列表，

**列表常用函数和方法**

| 序号 | 函数                                                         |
| :--- | :----------------------------------------------------------- |
| 1    | [len(list)](https://www.runoob.com/python3/python3-att-list-len.html) 列表元素个数 |
| 2    | [max(list)](https://www.runoob.com/python3/python3-att-list-max.html) 返回列表元素最大值 |
| 3    | [min(list)](https://www.runoob.com/python3/python3-att-list-min.html) 返回列表元素最小值 |
| 4    | [list(seq)](https://www.runoob.com/python3/python3-att-list-list.html) |

Python包含以下方法:

| 序号 | 方法                                                         |
| :--- | :----------------------------------------------------------- |
| 1    | [list.append(obj)](https://www.runoob.com/python3/python3-att-list-append.html) 在列表末尾添加新的对象 |
| 2    | [list.count(obj)](https://www.runoob.com/python3/python3-att-list-count.html) 统计某个元素在列表中出现的次数 |
| 3    | [list.extend(seq)](https://www.runoob.com/python3/python3-att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4    | [list.index(obj)](https://www.runoob.com/python3/python3-att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
| 5    | [list.insert(index, obj)](https://www.runoob.com/python3/python3-att-list-insert.html) 将对象插入列表 |
| 6    | [list.pop([index=-1\])](https://www.runoob.com/python3/python3-att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | [list.remove(obj)](https://www.runoob.com/python3/python3-att-list-remove.html) 移除列表中某个值的第一个匹配项 |
| 8    | [list.reverse()](https://www.runoob.com/python3/python3-att-list-reverse.html) 反向列表中元素 |
| 9    | [list.sort( key=None, reverse=False)](https://www.runoob.com/python3/python3-att-list-sort.html) 对原列表进行排序 |
| 10   | [list.clear()](https://www.runoob.com/python3/python3-att-list-clear.html) 清空列表 |
| 11   | [list.copy()](https://www.runoob.com/python3/python3-att-list-copy.html) 复制列表 |

#### 元组

元组与列表相似，不同的是元组不能被修改。

元组使用小括号 **( )**，列表使用方括号 **[ ]**。

如何定义一个元素的元组呢？	

Python元组包含了以下内置函数

| 序号 | 方法及描述                               | 实例                                                         |
| :--- | :--------------------------------------- | :----------------------------------------------------------- |
| 1    | len(tuple) 计算元组元素个数。            | `>>> tuple1 = ('Google', 'Runoob', 'Taobao') >>> len(tuple1) 3 >>> ` |
| 2    | max(tuple) 返回元组中元素最大值。        | `>>> tuple2 = ('5', '4', '8') >>> max(tuple2) '8' >>> `      |
| 3    | min(tuple) 返回元组中元素最小值。        | `>>> tuple2 = ('5', '4', '8') >>> min(tuple2) '4' >>> `      |
| 4    | tuple(iterable) 将可迭代系列转换为元组。 | `>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu'] >>> tuple1=tuple(list1) >>> tuple1 ('Google', 'Taobao', 'Runoob', 'Baidu')` |

元组常用方法：index  , count

```python
mytup = ("这","一", "个", "元", "组")
mytup.index(1)
mytup.count("一")
```



#### 集合

以上三个数据容器基本已经可以满足我们大多数的使用场景。但有一个局限性就是他们都支持重复元素，如果需要对内容进行去重复操作，就比较不方便了。

这时集合就登场了，集合不支持重复元素，并且内容为无序。

集合（set）是一个无序的不重复元素序列。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

可以使用大括号 **{ }** 创建集合，元素之间用逗号 **,** 分隔， 或者也可以使用 **set()** 函数创建集合。

集合内置方法完整列表

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [add()](https://www.runoob.com/python3/ref-set-add.html)     | 为集合添加元素                                               |
| [clear()](https://www.runoob.com/python3/ref-set-clear.html) | 移除集合中的所有元素                                         |
| [copy()](https://www.runoob.com/python3/ref-set-copy.html)   | 拷贝一个集合                                                 |
| [difference()](https://www.runoob.com/python3/ref-set-difference.html) | 返回多个集合的差集                                           |
| [difference_update()](https://www.runoob.com/python3/ref-set-difference_update.html) | 移除集合中的元素，该元素在指定的集合也存在。                 |
| [discard()](https://www.runoob.com/python3/ref-set-discard.html) | 删除集合中指定的元素                                         |
| [intersection()](https://www.runoob.com/python3/ref-set-intersection.html) | 返回集合的交集                                               |
| [intersection_update()](https://www.runoob.com/python3/ref-set-intersection_update.html) | 返回集合的交集。                                             |
| [isdisjoint()](https://www.runoob.com/python3/ref-set-isdisjoint.html) | 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。 |
| [issubset()](https://www.runoob.com/python3/ref-set-issubset.html) | 判断指定集合是否为该方法参数集合的子集。                     |
| [issuperset()](https://www.runoob.com/python3/ref-set-issuperset.html) | 判断该方法的参数集合是否为指定集合的子集                     |
| [pop()](https://www.runoob.com/python3/ref-set-pop.html)     | 随机移除元素                                                 |
| [remove()](https://www.runoob.com/python3/ref-set-remove.html) | 移除指定元素                                                 |
| [symmetric_difference()](https://www.runoob.com/python3/ref-set-symmetric_difference.html) | 返回两个集合中不重复的元素集合。                             |
| [symmetric_difference_update()](https://www.runoob.com/python3/ref-set-symmetric_difference_update.html) | 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 |
| [union()](https://www.runoob.com/python3/ref-set-union.html) | 返回两个集合的并集                                           |
| [update()](https://www.runoob.com/python3/ref-set-update.html) | 给集合添加元素                                               |
| [len()](https://www.runoob.com/python3/python3-string-len.html) | 计算集合元素个数                                             |

#### 字典

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 **key=>value** 对用冒号 **:** 分割，每对之间用逗号(**,**)分割，整个字典包括在花括号 **{}** 中 ,格式如下所示：

```python
d = {key1 : value1, key2 : value2, key3 : value3 }
```

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变类型的，如字符串，数字。

**字典的常用方法**

向字典添加新内容的方法是增加新的键/值对

```python
mydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
mydict['Age'] = 8               # 更新 Age
mydict['School'] = "蓝山python教程"  # 添加信息

 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])
```

删除可用del关键字，或者pop方法

```pytohn
element = site.pop('key')
```

**遍历字典**

```python
my_dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 遍历字典的键
for key in my_dict:
    print("-----这是字典的keys---------")
    print(key)

# 遍历字典的值
for value in my_dict.values():
    print("-----这是字典的values---------")
    print(value)

# 遍历字典的键值对
for key, value in my_dict.items():
    print("-----这是键值对---------")
    print(f"{key}: {value}")
```







#### 序列

什么是序列？

序列是 Python 中最基本的数据结构;是内容连续有序支持下表索引的一类容器。（列表，元组，字符串，范围range）。

序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。

Python 有 多 个序列的内置类型，但最常见的是列表和字符串。



**序列切片**：

python中所有序列类型的数据结构都支持切片操作。

![image-20240821235103356](https://gitee.com/vkermt/blogimage/raw/master/images/image-20240821235103356.png)



#### Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将<font color='each'>数据类型</font>作为<font color='red'>函数名</font>即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [int(x [,base\])](https://www.runoob.com/python/python-func-int.html) | 将x转换为一个整数                                   |
| [long(x [,base\] )](https://www.runoob.com/python/python-func-long.html) | 将x转换为一个长整数                                 |
| [float(x)](https://www.runoob.com/python/python-func-float.html) | 将x转换到一个浮点数                                 |
| [complex(real [,imag\])](https://www.runoob.com/python/python-func-complex.html) | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python/att-tuple-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python/att-list-list.html)  | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python/python-func-dict.html) | 创建一个字典。d 必须是一个序列 (key,value)元组。    |
| [frozenset(s)](https://www.runoob.com/python/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [unichr(x)](https://www.runoob.com/python/python-func-unichr.html) | 将一个整数转换为Unicode字符                         |
| [ord(x)](https://www.runoob.com/python/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |



### python运算符

#### Python 运算符

Python语言支持以下类型的运算符:

- [算术运算符](https://www.runoob.com/python/python-operators.html#ysf1)
- [比较（关系）运算符](https://www.runoob.com/python/python-operators.html#ysf2)
- [赋值运算符](https://www.runoob.com/python/python-operators.html#ysf3)
- [逻辑运算符](https://www.runoob.com/python/python-operators.html#ysf4)
- [位运算符](https://www.runoob.com/python/python-operators.html#ysf5)
- [成员运算符](https://www.runoob.com/python/python-operators.html#ysf6)
- [身份运算符](https://www.runoob.com/python/python-operators.html#ysf7)
- [运算符优先级](https://www.runoob.com/python/python-operators.html#ysf8)

#### 算数运算符

以下假设变量： **a=10，b=20**：

| 运算符 | 描述                                            | 实例                                               |
| :----- | :---------------------------------------------- | :------------------------------------------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 30                                  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -10                                 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200                                 |
| /      | 除 - x除以y                                     | b / a 输出结果 2.0                                 |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 0                                   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的20次方， 输出结果 100000000000000000000 |
| //     | 取整除 - 返回商的整数部分（**向下取整**）       | `>>> 9//2 4 >>> -9//2 -5`                          |

```python
import math
a = 10
b = 20
print(a + b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```







#### 比较运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述                                                         | 实例                                     |
| :----- | :----------------------------------------------------------- | :--------------------------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。                    |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 True。                     |
| <>     | 不等于 - 比较两个对象是否不相等。**python3 已废弃。**        | (a <> b) 返回 True。这个运算符类似 != 。 |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。                     |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量 True 和 False 等价。 | (a < b) 返回 True。                      |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。                    |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 True。                     |

#### Python赋值运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述             | 实例                                  |
| :----- | :--------------- | :------------------------------------ |
| =      | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| +=     | 加法赋值运算符   | c += a 等效于 c = c + a               |
| -=     | 减法赋值运算符   | c -= a 等效于 c = c - a               |
| *=     | 乘法赋值运算符   | c *= a 等效于 c = c * a               |
| /=     | 除法赋值运算符   | c /= a 等效于 c = c / a               |
| %=     | 取模赋值运算符   | c %= a 等效于 c = c % a               |
| **=    | 幂赋值运算符     | `c **= a `等效于` c = c ** a`         |
| //=    | 取整除赋值运算符 | c //= a 等效于 c = c // a             |

以下实例演示了Python所有赋值运算符的操作：

#### 逻辑运算符

Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                    |
| :----- | :--------- | :----------------------------------------------------------- | :---------------------- |
| and    | x and y    | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 | (a and b) 返回 20。     |
| or     | x or y     | 布尔"或" - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值。 | (a or b) 返回 10。      |
| not    | not x      | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

### Python 条件控制

Python条件语句是通过一条或多条语句的执行结果（<font color='red'>True或者False</font>）来决定执行的代码块。

可以通过下图来简单了解条件语句的执行过程:

![img](https://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg)

```python
a = int(input("输入一个number"))
b = int(input("输入一个number"))
if a > b:
    print("a>b")
elif a == b:
    print("a=b")
else:
    print("a<b")
```





Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

Python 编程中 if 语句用于控制程序的执行，基本形式为：

```python
if 判断条件：
    执行语句……
elif 判断条件：
    执行语句……
else：
    执行语句……
```

其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。

<font color='red'>else 为可选语句</font>，当需要在条件不成立时执行内容则可以执行相关语句。



### Python 循环语句

编程语言提供了各种控制结构，允许更复杂的执行路径。

循环语句允许我们执行一个语句或语句组多次，下面是在大多数编程语言中的循环语句的一般形式：

![img](https://www.runoob.com/wp-content/uploads/2015/12/loop.png)

Python 提供了 for 循环和 while 循环（在 Python 中没有 do..while 循环）:

#### while循环

Python 中 while 语句的一般形式：

```python
while 判断条件(condition)：
    执行语句(statements)……
```

例子：

```python
count = 1
var = "我做梦都想进蓝山"
while count < 100:
    print(var,end = "\n")
    count += 1
```



#### for循环

python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

for循环的一般格式如下：

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```





#### 循环控制语句



循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：

**break** 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

**continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

**pass**语句是空语句，只是为了保持程序结构的完整性。

```python
# 猜数字小游戏
import random
num = random.randint(1, 10)
count = 1
mynum = int(input(f"第{count}次猜数字，输入您要猜的数字：\n"))
while True:
    if count == num:
        print("您猜对了")
        break
    else:
        count += 1
        mynum = int(input(f"第{count}次猜数字，输入您要猜的数字：\n"))
print(f"您总共猜了{count}次")
print("gameover.....")

```









### 函数基础



函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。



#### 自定义函数

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号 **:** 起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

![img](https://www.runoob.com/wp-content/uploads/2014/05/py-tup-10-26-1.png)

```python
def 函数名（参数列表）:
    函数体
```

#### 函数的调用

定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过函数名调用执行。



#### 传参

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

```python
        def change(a):
            print(id(a))   # 指向的是同一个对象
            a=10
            print(id(a))   # 一个新对象

        a=1
        print(id(a))
        change(a)
```

#### 参数

以下是调用函数时可使用的正式参数类型：

**必需参数**

必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

```python
def printme(a):
    print(a)
a = "hello world"
printme()
```



**关键字参数**

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

```python
def printme(a, b):
    print(a + b)
a = "hello"
b = " world"
printme(b=b,a=a)
```



**默认参数(缺省参数)**

调用函数时，如果没有传递参数，则会使用默认参数。默认参数在函数定义时，必须定义在必须参数的后面。

```python
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="chen" )
print ("------------------------")
printinfo( name="chen" )
```

**不定长参数**

主要分为位置不定长、关键字不定长：

位置不定长：

```python
def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(result = sum_numbers(1, 2, 3, 4, 5))

```

关键字不定长：

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")

```





#### return返回值

**return [表达式]** 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。



### 文件操作

#### 1. 打开文件

使用 `open()` 函数可以打开一个文件。该函数接受两个主要参数：文件名和模式。

**文件打开模式**

- `'r'`：只读模式（默认）。如果文件不存在，会引发错误。
- `'w'`：写入模式。如果文件存在，则会覆盖文件；如果文件不存在，则会创建新文件。
- `'a'`：追加模式。数据会被添加到文件末尾。
- `'b'`：二进制模式。通常与其他模式结合使用，例如 `'rb'` 或 `'wb'`。
- `'t'`：文本模式（默认）。通常不需要指定。

示例：

```
# 打开一个文本文件
file = open('test.txt', 'r')
```

#### 2. 读取文件

可以使用几种方法从文件中读取内容：

 `read(size)`

读取文件的全部或指定字节数。

```
print(file.read())  # 读取整个文件内容
```

`readline()`

读取文件的一行。

```
print(file.readline())  # 读取文件的第一行
```

`readlines()`

读取文件的所有行，并返回一个列表。

```
print(file.readlines())  # 返回文件的所有行
```

#### 3. 写入文件

在文件中写入数据时，可以使用 `write()` 或 `writelines()` 方法。

 `write()`

写入字符串到文件中。

```
file = open('example.txt', 'w')  # 打开文件以写入
file.write("Hello, World!\n")  # 写入字符串
```

 `writelines()`

写入一个字符串列表。

```
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)  # 写入多行
```

#### 4. 关闭文件

完成文件操作后，使用 `close()` 方法关闭文件，以释放系统资源。

```
pythonfile.close()  # 关闭文件
```

#### 5. 使用 `with` 语句

为了更安全和方便地处理文件，推荐使用 `with` 语句。它会自动管理文件的打开和关闭，避免文件未关闭的问题。

示例：

```
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # 读取并打印内容
# 文件会在离开 `with` 块时自动关闭
```



#### 7. 文件检查和操作

- **检查文件是否存在**：可以使用 `os.path` 模块。

```
import os

if os.path.exists('example.txt'):
    print("文件存在")
else:
    print("文件不存在")
```

- **删除文件**：使用 `os.remove()`。

```
import os

os.remove('example.txt')  # 删除文件
```

**file对象常用方法**

| 序号 | 方法及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [file.close()](https://www.runoob.com/python3/python3-file-close.html)关闭文件。关闭后文件不能再进行读写操作。 |
| 2    | [file.flush()](https://www.runoob.com/python3/python3-file-flush.html)刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| 3    | [file.fileno()](https://www.runoob.com/python3/python3-file-fileno.html)返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
| 4    | [file.isatty()](https://www.runoob.com/python3/python3-file-isatty.html)如果文件连接到一个终端设备返回 True，否则返回 False。 |
| 5    | [file.next()](https://www.runoob.com/python3/python3-file-next.html)**Python 3 中的 File 对象不支持 next() 方法。**返回文件下一行。 |
| 6    | [file.read([size\])]从文件读取指定的字节数，如果未给定或为负则读取所有。 |
| 7    | [file.readline([size\])]读取整行，包括 "\n" 字符。一次读一行 |
| 8    | [file.readlines([sizeint\])]读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。 |
| 9    | [file.seek(offset[, whence\])](https://www.runoob.com/python3/python3-file-seek.html)移动文件读取指针到指定位置 |
| 10   | [file.tell()](https://www.runoob.com/python3/python3-file-tell.html)返回文件当前位置。 |
| 11   | [file.truncate([size\])](https://www.runoob.com/python3/python3-file-truncate.html)从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。 |
| 12   | [file.write(str)](https://www.runoob.com/python3/python3-file-write.html)将字符串写入文件，返回的是写入的字符长度。 |
| 13   | [file.writelines(sequence)](https://www.runoob.com/python3/python3-file-writelines.html)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |











### 捕获异常

即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

语法：

![img](https://www.runoob.com/wp-content/uploads/2019/07/try_except_else_finally.png)

```
try:
	代码块
except Exception as e:
	代码块
[esle:]
[finaly:]
```

```python
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
    print(f"结果是: {result}")
except ValueError as e:
    print(f"输入错误: {e}")
except ZeroDivisionError as e:
    print(f"除以零错误: {e}")

```

**`else` 和 `finally` 块**

- **`else` 块**：在 `try` 块没有引发异常时执行。
- **`finally` 块**：无论是否发生异常，都会执行的代码，通常用于清理资源。

```python
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ValueError as e:
    print(f"输入错误: {e}")
except ZeroDivisionError as e:
    print(f"除以零错误: {e}")
else:
    print(f"结果是: {result}")
finally:
    print("清理资源，程序结束。")

```



### Python模块

Python 模块是包含 Python 代码的文件，用于组织和重用代码。模块可以包含函数、类和变量，也可以包含可执行的代码。你可以通过 `import` 语句导入模块，从而在其他脚本中使用模块中的功能。模块文件的扩展名通常是 `.py`。Python 标准库提供了许多内置模块，例如 `math`、`sys` 和 `os`，用户也可以创建自定义模块来封装自己的代码。模块化编程有助于提高代码的可维护性和复用性。

#### 导入模块

常用的四种导入方式:

```python
import 模块名

import 模块名 as 别名

from 模块名 import 函数/类/变量/* 

from 模块名 import 函数/类/变量/* as 别名
```

#### 内置模块和自定义模块

**内置模块** 是 Python 标准库的一部分，提供了多种功能，如数学运算、文件操作和系统管理等。这些模块在 Python 安装时自带，无需额外安装。常见的内置模块包括 `math`、`datetime` 和 `os`。

**自定义模块** 是由用户创建的 Python 文件，通常用于组织和重用自己的代码。你可以定义函数、类和变量，然后通过 `import` 语句在其他脚本中使用这些模块。自定义模块的文件名以 `.py` 结尾，放在 Python 的搜索路径中即可被导入。

例子...

**`__main__`**变量:

`__main__` 是 Python 的一个特殊变量，用于确定一个脚本是否是直接运行的主程序。当你运行一个 Python 脚本时，解释器会将 `__name__` 设置为 `'__main__'`。如果这个脚本被作为模块导入，`__name__` 将被设置为模块的名称。

作用：使用 `__main__` 变量可以让你在脚本中区分直接执行和作为模块导入的情况。

```python
# example.py
def main():
    print("Script is running directly")

if __name__ == "__main__":
    main()
```

`__all__`变量：

`__all__` 是一个特殊的变量，用于定义 `from module import *` 语句时，模块中哪些名称会被导入。它是一个列表，包含了模块中希望公开的属性和方法的名称。如果 `__all__` 被定义了，那么只有列表中的名称会被导入，其他名称则会被忽略。

```python
# mymodule.py
__all__ = ['foo', 'bar']

def foo():
    pass

def bar():
    pass

def baz():
    pass
```

```python
from mymodule import *

# 只有 foo 和 bar 会被导入，baz 不会被导入
```







### python包

Python 包是用于组织和管理 Python 模块的目录结构。它们通过目录和文件的方式提供了一种层次化的代码组织方法，使得大型项目可以更容易地进行管理和维护。下面是关于 Python 包的一些重要概念和特点：

#### 包的基本结构

一个 Python 包通常是一个包含 `__init__.py` 文件的目录。

- **`__init__.py` 文件**：这是一个特殊的文件，用于初始化包。可以是空文件，但它的存在标志着该目录是一个 Python 包。`__init__.py` 文件可以包含包初始化代码或者设置 `__all__` 列表，以控制哪些模块可以被导入。

#### 导入包的模块

要使用包中的模块，可以使用点（`.`）符号进行导入。例如：

```python
# 导入 my_package 包中的 module1 模块
import my_package.module1

# 导入 my_package 包中的 module2 模块中的特定功能
from my_package.module2 import some_function

# 导入 my_package.sub_package 包中的 sub_module1 模块
import my_package.sub_package.sub_module1
```

#### `__all__`列表

在包的 `__init__.py` 文件中定义 `__all__` 列表，可以指定哪些模块或对象可以被 `from package import *` 语句导入。这有助于控制包的公开接口。例如：

```python
# my_package/__init__.py
__all__ = ['module1', 'module2']
```

#### 包的用途

- **组织代码**：通过将相关模块放在同一个包中，可以使代码更有结构、更易于理解和维护。
- **避免命名冲突**：将功能模块组织在不同的包中可以避免命名冲突，例如，两个不同的包可以有同名的模块。
- **分层设计**：支持分层和嵌套的模块化设计，有助于将复杂的项目拆分成更小、更管理的部分。

#### 安装第三方包

安装第三方包通常使用 Python 的包管理工具 pip。

```shell
# install安装包。
pip install package_name

#--upgrade: 升级到最新版本。
pip install --upgrade package_name

#uninstall: 卸载包。
pip uninstall package_name

#list: 列出已安装的包。
pip list

#freeze: 输出所有已安装包及其版本（用于生成 requirements.txt 文件）
pip freeze

#show: 显示包的详细信息。
pip show package_name

#search: 查找包（某些 pip 版本可能不再支持）
pip search package_name
```

如何导出项目的所有依赖项写入 `requirements.txt` 文件中呢？

**生成 `requirements.txt` 文件**：

```shell
pip freeze > requirements.txt
```

**从 `requirements.txt` 安装依赖**：

```shell
pip install -r requirements.txt
```

**`tips`使用国内源安装**

常用国内源

```shell
#清华大学源：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
#阿里云源：
pip install -i https://mirrors.aliyun.com/pypi/simple package_name
#中国科技大学源：
pip install -i https://pypi.mirrors.ustc.edu.cn/simple package_name
#华为云源：
pip install -i https://repo.huaweicloud.com/repository/pypi/simple package_name
#使用这些镜像源可以提高安装速度和成功率，特别是在网络条件较差的情况下。
```



# 作业:smiley_cat:

##### level0:

安装好python相关编译器，并打印输出'hello world'

##### level1:

判断101-200之间有多少个素数，并输出所有素数。

##### level2:

打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

##### level3:

输入五个数字，并判断是否能作为分数（0<=n<=100）,若能作为分数再判断是哪个等级

将满分为100的整数型考试分数，转化为ABCDE五个等级
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E

将等级为A的数字存入A.txt

##### level4:

使用python写一个监控CPU，I/O，内存使用情况，网络流量的监控平台，做到每天更新一次数据，并将监控到的数据存入到log.txt文件中。

