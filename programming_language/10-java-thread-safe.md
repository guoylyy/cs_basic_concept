#Java线程安全和非线程安全 
##ArrayList和Vector有什么区别？
ArrayList是非线程安全的，Vector是线程安全的；
##HashMap和HashTable有什么区别？
HashMap是非线程安全的，HashTable是线程安全的；
##StringBuilder和StringBuffer有什么区别？
StringBuilder是非线程安全的，StringBuffer是线程安全的。

## 线程不安全
造成线程不安全的原因之一操作非原子性，另一个原因则是执行过程中可能被中断

## 线程不安全的原因和举个栗子
jvm运行时刻分配的内存中有一个内存区域是jvm虚拟机栈，每一个线程运行时都有一个线程栈，线程栈保存了线程运行时候变量值信息。当线程访问某一个对象时候值的时候，首先通过对象的引用找到对应在堆内存的变量的值，然后把堆内存变量的具体值load到线程本地内存中，建立一个变量副本，之后线程就不再和对象在堆内存变量值有任何关系，而是直接修改副本变量的值，在修改完之后的某一个时刻（线程退出之前），自动把线程变量副本的值回写到对象在堆中变量。这样在堆中的对象的值就产生变化了。下面一幅图描述这写交互
![jvm虚拟机栈](http://images.cnblogs.com/cnblogs_com/aigongsi/201204/201204011757235219.jpg)
其中涉及到的操作：
1. read and load 从主存复制变量到当前工作内存
2. use and assign  执行代码，改变共享变量值
3. store and write 用工作内存数据刷新主存相关内容

其中use and assign 可以多次出现

但是这一些操作并不是原子性，也就是 在read load之后，如果主内存count变量发生修改之后，线程工作内存中的值由于已经加载，不会产生对应的变化，所以计算出来的结果会和预期不一样

对于volatile修饰的变量，jvm虚拟机只是保证从主内存加载到线程工作内存的值是最新的

###栗子
>假如线程1，线程2 在进行read,load 操作中，发现主内存中count的值都是5，那么都会加载这个最新的值

1. 在线程1堆count进行修改之后，会write到主内存中，主内存中的count变量就会变为6

2. 线程2由于已经进行read,load操作，在进行运算之后，也会更新主内存count的变量值为6

导致两个线程及时用volatile关键字修改之后，还是会存在并发的情况。

##二者如何取舍

非线程安全是指多线程操作同一个对象可能会出现问题。而线程安全则是多线程操作同一个对象不会有问题。

线程安全必须要使用很多synchronized关键字来同步控制，所以必然会导致性能的降低。

所以在使用的时候，如果是多个线程操作同一个对象，那么使用线程安全的Vector；否则，就使用效率更高的ArrayList。


##非线程安全!=不安全

有人在使用过程中有一个不正确的观点：我的程序是多线程的，不能使用ArrayList要使用Vector，这样才安全。

非线程安全并不是多线程环境下就不能使用。注意我上面有说到：多线程操作同一个对象。

如果是每个线程中new一个ArrayList，而这个ArrayList只在这一个线程中使用，那么肯定是没问题的。

##线程安全的实现

线程安全是通过线程同步控制来实现的，也就是`synchronized`关键字。 通过 `synchronized `关键字来实现，所有加上`synchronized`的方法 和 块语句，在多线程访问的时候，同一时刻只能有一个线程能够用`synchronized` 修饰的方法 或者 代码块。 

##`volatile`关键字
用volatile修饰的变量，线程在每次使用变量的时候，都会读取变量修改后的最的值。但，`volatile`却并不能保证线程安全

## 参考
1. [java中volatile关键字的含义](http://www.cnblogs.com/aigongsi/archive/2012/04/01/2429166.html)
2. [Java线程安全总结](http://www.2cto.com/kf/201202/118486.html)
3. [Java线程安全和非线程安全](http://blog.csdn.net/xiao__gui/article/details/8934832)