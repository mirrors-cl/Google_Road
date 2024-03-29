## you don't know about the javascript

#### 什么是作用域
作用域是一套规则，用于确定在何处以及如何查找变量（标识符）。如果查找的目的是对变量进行赋值，那么就会使用LHS查询，如果目的是获取变量的值，就会使用RHS查询

***RHS：***查询查询与简单的查找某个变量的值别无二致，（可以理解成取到它的原值，这意味着得到某某的值）

***LHS：***查询则是试图找到变量的容器本身，从而可以对其进行赋值


> 区分LHS和RHS还有一件非常重要的事情，用RHS进行查询时如果在所有嵌套的作用域中遍寻不到所需的变量，引擎就会抛出一个ReferenceError异常。（ReferenceEroor）是非常重要的异常类型。

>当引擎执行LHS查询时，如果在顶层（全局作用域）中也无法找到目标变量，全局作用域中就会创建一个具有该名称的变量，并将其返回给引擎，（前提是程序运行在非“严格模式”下）


#### 小结
>作用域是一套规则，用于确定在何处以及如何查找变量(标识符)。如果查找的目的是对
变量进行赋值，那么就会使用 LHS 查询;如果目的是获取变量的值，就会使用 RHS 查询。
赋值操作符会导致 LHS 查询。=操作符或调用函数时传入参数的操作都会导致关联作用域 的赋值操作。
JavaScript引擎首先会在代码执行前对其进行编译，在这个过程中，像var a = 2这样的声 明会被分解成两个独立的步骤:
1. 首先，var a 在其作用域中声明新变量。这会在最开始的阶段，也就是代码执行前进行。 2. 接下来，a = 2 会查询(LHS 查询)变量 a 并对其进行赋值。
LHS 和 RHS 查询都会在当前执行作用域中开始，如果有需要(也就是说它们没有找到所 需的标识符)，就会向上级作用域继续查找目标标识符，这样每次上升一级作用域(一层 楼)，最后抵达全局作用域(顶层)，无论找到或没找到都将停止。
不成功的 RHS 引用会导致抛出 ReferenceError 异常。不成功的 LHS 引用会导致自动隐式 地创建一个全局变量(非严格模式下)，该变量使用 LHS 引用的目标作为标识符，或者抛 出 ReferenceError 异常(严格模式下)。
