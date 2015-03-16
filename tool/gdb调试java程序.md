#用GDB 调试Java程序
## 背景
想要使用GDB调试程序，就需要用GNU的编译器编译程序。如：用GCC编译的C/C++的程序，才能用GDB调试。对于Java程序也是一样的，如果想要用GDB调试，那么就需要用GNU的Java编译器——GCJ来编译Java程序。

## 用GCJ编译Java程序
用GCJ编译Java程序很简单，关于编译成.o和执成文件，如下所示：
```
gcj -c -g -O MyJavaProg.java
gcj -g --main=MyJavaProg -o MyJavaProg MyJavaProg.o
```
很明显，基本上就是gcc的语法。当然，你也可以一步编译出可执行文件：
```
gcj -g --main=MyJavaProg -o MyJavaProg MyJavaProg.java
```
>其中，使用-g参数表示加入调试信息，这对于调试时相当重要。不然，无法看到实际的源码和函数。而关于--main参数，意思是指定main函数所在的Java类。

## 使用GDB调试Java程序
###1. 进入GDB环境
```
gdb ./MyJavaProg
```
###2. 查看源代码
>Workaround的解决方案如下：
>1）先List类的构造函数，这样可以找到源文件。
>2）使用源文件的行号进行break。
```
l(ist) MyJavaProg::main
或者
l MyJavaProg.main
```
###3. 设置断点
```
break line-number
或
break MyJavaProg.main
或
break MyJavaProg::main
或
break line-number if variable==50 <--条件断点
```
###4. 打印变量
1. print方法 `print vaiable_name`	可以单次查看
2. display方法 `display variable_name` 每次断点都会输出variable_name
###5. 设置和查看args变量
`set args`
    Specify the arguments to be used the next time your program is run. If set args has no arguments, run executes your program with no arguments. Once you have run your program with arguments, using set args before the next run is the only way to run it again without arguments.

`show args`
    Show the arguments to give your program when it is started. 
###6. 其他常用操作
1. 打出函数栈 `bt`
2. 下一步 `n` 或者 `next`
3. 退出函数 `finish`
4. 产看信息`info`
5. 帮助`help subject`
6. 退出`quit`
###9. 其它注意事项
当你使用GDB调试被GCJ编译的程序时，你需要让GDB忽略SIGPWR和SIGCPU这两个信号。这两个信号被垃圾回收器使用，为了让调试工作进行的更顺利，我们需要使用GDB的命令来忽略这两个信号：
```
(gdb) handle SIGPWR nostop noprint
Signal        Stop      Print   Pass to program Description
SIGPWR        No        No      Yes             Power fail/restart
```
```
(gdb) handle SIGXCPU nostop noprint
Signal        Stop      Print   Pass to program Description
SIGXCPU       No        No      Yes             CPU time limit exceeded
```
当然，你并不用每次都需要设置这两个命令，你可以设置$HOME目录下的.gdbinit文件来把这两个命令作为GDB的初始化选项。
###8. 未解决的问题
1. 如何答应String
