# Spring AOP 的实现方式

## 1. 为什么用？

在面向对象编程的过程中，我们经常会遇到代码水平扩散分布在各个对象的问题，这样有时候会造成大量的重复代码，如果需求变化，有一处代码要更改，那么就需要悲剧地修改很多地方的重复代码。而面向切面的编程（AOP）就是为了解决这种情况而产生的。

“将应用程序的商业逻辑同对其提供通用支持的服务进行分离。”

## 2. 如何实现？

实现AOP的技术，主要分为两大类：

一是采用动态代理技术，利用截取消息的方式，对该消息进行装饰，以取代原有对象行为的执行；spring.

二是采用静态织入的方式，引入特定的语法创建“方面”，从而使得编译器可以在编译期间织入有关“方面”的代码。

### 2.1 Java 代理模式



## 3. 试着实现 spring aop 的动态代理

AOP实现中，可以看到三个主要的步骤，一个是代理对象的生成，然后是拦截器的作用，然后是Aspect编织的实现。






##参考文章
1. [Spring AOP 实现原理与 CGLIB 应用](https://www.ibm.com/developerworks/cn/java/j-lo-springaopcglib/)
2. [Spring AOP 实现原理](http://blog.csdn.net/moreevan/article/details/11977115)
3. [Spring技术内幕——深入解析Spring架构与设计原理（二）AOP](http://java.02ta.com/blog/spring/494620)