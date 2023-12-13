---
title: java
date: 2022-07-06
tags:
- language
- java
---

## Java 基础

### == equals, hasCode，instance

== 两个对象的引用完全相同（即同一对象），hashCode()以C++实现，返回对象的内存地址

### 正则表达式[https://jquery.cuishifeng.cn/regexp.html](https://jquery.cuishifeng.cn/regexp.html)
String类中的各种方法（matches()、replaceAll()、replaceFirst()、split()）和Pattern对象
```java
Pattern p = Pattern.compile(``".*?(?=\\()"``);   
```
## 接口和抽象类区别
接口=规范（属性：public static final;方法：抽象方法）；抽象类=规范+实现

接口和抽象类均可多态（父类定义，子类实现），但抽象类只能单继承，接口可以多个实现；抽象类可实例化对象，接口无构造函数，不能实例化；抽象类可以不包含抽象方法，但接口只能有抽象方法。

### 内部类
要想访问内部类中的内容，必须通过外部类对象来实例化内部类。能够访问外部类所有的属性和方法，原理就是在通过外部类对象实例化内部类对象时，外部类对象把自己的引用传进了内部类，使内部类可以用通过Outer.this去调用外部类的属性和方法，一般都是隐式调用了，但是当内部类中有属性或者方法名和外部类中的属性或方法名相同的时候，就需要通过显式调用Outer.this了。

局部内部类是在一个方法内部声明的一个类。局部内部类中可以访问外部类的成员变量及方法。局部内部类中如果要访问该内部类所在方法中的局部变量,那么这个局部变量就必须是final修饰的

###  IO流（NIO，BIO，）
- 分类
    - 阻塞：读写数据时客户端会发生阻塞
    - 非阻塞
    - 多路复用：Selector的线程不断轮询多个Socket的状态，只有在Socket有读写事件时，才会通知用户线程进行I/O读写操作。
    - 信号驱动：户线程发起一个I/O请求操作时，系统会为该请求对应的Socket注册一个信号函数，然后用户线程可以继续执行其他业务逻辑；在内核数据就绪时，系统会发送一个信号到用户线程，用户线程在接收到该信号后，会在信号函数中调用对应的I/O读写操作完成实际的I/O请求操作
    - 异步：**类似信号驱动**，但用户线程不需要关心整个I/O操作是如何进行的，只需发起一个请求，在接收到内核返回的成功或失败信号时说明I/O操作已经完成，直接使用数据即可。
- 示例
    - 阻塞IO（BIO）:A拿着一支鱼竿在河边钓鱼，并且一直在鱼竿前等，在等的时候不做其他的事情，十分专心。只有鱼上钩的时，才结束掉等的动作，把鱼钓上来。
    - 非阻塞IO(NIO):B也在河边钓鱼，但是B不想将自己的所有时间都花费在钓鱼上，在等鱼上钩这个时间段中，B也在做其他的事情（一会看看书，一会读读报纸，一会又去看其他人的钓鱼等），但B在做这些事情的时候，每隔一个固定的时间检查鱼是否上钩。一旦检查到有鱼上钩，就停下手中的事情，把鱼钓上来。 B在检查鱼竿是否有鱼，是一个轮询的过程。
    - 异步IO(AIO):C也想钓鱼，但C有事情，于是他雇来了D、E、F，让他们帮他等待鱼上钩，一旦有鱼上钩，就把鱼钓上来，然后打电话给C
    - 多路复用IO：H同样也在河边钓鱼，但是H生活水平比较好，H拿了很多的鱼竿，一次性有很多鱼竿在等，H不断的查看每个鱼竿是否有鱼上钩。增加了效率，减少了等待的时间。
    - 信号驱动IO：G也在河边钓鱼，但与A、B、C不同的是，G比较聪明，他给鱼竿上挂一个铃铛，当有鱼上钩的时候，这个铃铛就会被碰响，G就会将鱼钓上来
- **NIO(非阻塞IO)**
    1. Buffer为所有的原始类型提供 (Buffer)缓存支持。
    2. Charset字符集编码解码解决方案
    3. Channel一个新的原始 I/O抽象，用于读写Buffer类型，通道可以认为是一种连接，可以是到特定设备，程序或者是网络的连接。

### 集合
- Collection对集合进行排序，查找，复制等功能。（二分查找，乱序）总继承
- List 有序集合
	- ArrayList：数组形式存储，默认长度为0，添加数据默认长度为10，长度不足时可以扩容但有最大长度限制。
	- LinkedList：双向链表，含有长度，头结点，尾节点三个属性，在迭代中可以添加删除数据
	- Vector: 线程安全的ArrayList，即当线程A使用Synchronized标记方法时，其他线程阻塞。但一般不使用，原因1. 线程并不安全，产生fail-fase错误；2. 在业务中有加锁需求，重复加锁浪费资源。
		- 在迭代中修改数据会产生fail-fast错误。但java.util.concurrent包下的相同情况会产生fail-safe错误，其原因是对数据修改时是对原数据的副本进行修改，不影响原数据；当修改完成后将原数据指向副本。
- Set 无序集合
- Map 键值对
	- HashMap: 数组+（链表 or 红黑树）
		- keySet():String：获取map.key的set集合
		- entrySet():Set<Map>：获取map关系的set集合
        
### util
- StringUtil common.lang[https://www.jianshu.com/p/1886903ed14c](https://www.jianshu.com/p/1886903ed14c)
- BigDecimal 浮点数精确计算
	- setScale(scale, BigDecimal.ROUND_HALF_UP)：四舍五入，scale=小数后几位？
	- add/subtract 加减法
	- mutiply() 乘法
	- divide()	除法

### 异常
多个catch：先小后大，按顺序匹配，当某一个catch匹配，跳过之后的catch，进入后续步骤。
任何执行try 或者catch中的return语句之前，都会先执行finally语句，如果finally存在的话。如果finally中有return语句，那么程序就return了，所以finally中的return是一定会被return的，编译器把finally中的return实现为一个warning。
**如果都有return 优先级为 final > try = catch > return**

## 反射，注解
- 反射：实例化对象，通过Class.forName()获取对象
- 注解：@Target注解目标，@Retention注解生存周期，@Documented注解文档
- 加密算法：AES(对称加密)，RES(非对称加密，公钥加密，私钥解密)
动态加载类，jvm中需要另一个类的方法实现时，动态加入相应类

#### Lambda 

规定接口中只能有一个需要被实现的方法，不是规定接口中只能有一个方法,常与@FuncitonalInterface注解一同使用[原文链接](https://www.cnblogs.com/haixiang/p/11029639.html)

```java
@FunctionalInterface
public interface NoReturnMultiParam {
    void method(int a, int b);
}
public static void main(String[] args){
	NoReturnNoParam noReturnNoParam = () -> {
            System.out.println("NoReturnNoParam");
        };
        noReturnNoParam.method();
}
```

###  native方法

非Java实现的java方法。以其他语言实现的Java方法即为native方法。

## jvm
- 堆：对象，数组
- 方法区（永久代）：类信息，常量，静态变量
- 程序计数器：当前线程执行 的字节码行号指示器
- 虚拟机栈：多个栈帧（局部变量表，操作数栈，动态链接表，方法出口）：java方法的执行即为栈帧的入栈，出栈
- 本地方法栈：类似虚拟机栈，对native方法执行出入栈操作
###  垃圾回收机制
- 识别
    - 可达性分析算法：判断对象的引用链是否可达
    - 引用计数算法：判断对象的引用数量，数量为零回收
- 回收
    - 标记清除算法：该算法首先从根集合进行扫描，对存活的对象对象标记，标记完毕后，再扫描整个空间中未被标记的对象并进行回收
    - 复制算法：将可用内存按容量划分为大小相等的两块，每次只使用其中的一块。当这一块的内存用完了，就将还存活着的对象复制到另外一块上面，然后再把已使用过的内存空间一次清理掉。
    - 标记整理算法：标记过程类似**标记清除算法**，但后续步骤不是直接对可回收对象进行清理，而是让所有存活的对象都向一端移动，然后直接清理掉端边界以外的内存，类似于磁盘整理的过程，该垃圾回收算法适用于对象存活率高的场景（老年代）
    - 分段收集算法：不同的对象的生命周期(存活情况)是不一样的，而不同生命周期的对象位于堆中不同的区域，因此对堆内存不同区域采用不同的策略进行回收可以提高 JVM 的执行效率。**新生代（标记复制），老年代（标记整理，清除）**
- 内存
    - 新生代的目标就是尽可能快速的收集掉那些生命周期短的对象，一般情况下，所有新生成的对象首先都是放在新生代的
    - 老年代存放的都是一些生命周期较长的对象，就像上面所叙述的那样，在新生代中经历了N次垃圾回收后仍然存活的对象就会被放到老年代中。
    - 永久代主要用于存放静态文件，如Java类、方法等。
- 回收器
    - Serial收集器（复制算法): 新生代单线程收集器，标记和清理都是单线程，优点是简单高效；
    - Serial Old收集器 (标记-整理算法): 老年代单线程收集器，Serial收集器的老年代版本；
    - ParNew收集器 (复制算法): 新生代收并行集器，实际上是Serial收集器的多线程版本，在多核CPU环境下有着比Serial更好的表现；
    - Parallel Scavenge收集器 (复制算法): 新生代并行收集器，追求高吞吐量，高效利用 CPU。吞吐量 = 用户线程时间/(用户线程时间+GC线程时间)，高吞吐量可以高效率的利用CPU时间，尽快完成程序的运算任务，适合后台应用等对交互相应要求不高的场景；
    - Parallel Old收集器 (标记-整理算法)： 老年代并行收集器，吞吐量优先，Parallel Scavenge收集器的老年代版本；
    - CMS(Concurrent Mark Sweep)收集器（标记-清除算法）： 老年代并行收集器，以获取最短回收停顿时间为目标的收集器，具有高并发、低停顿的特点，追求最短GC回收停顿时间。
    - G1(Garbage First)收集器 (标记-整理算法)： Java堆并行收集器，G1收集器是JDK1.7提供的一个新收集器，G1收集器基于“标记-整理”算法实现，也就是说不会产生内存碎片。此外，G1收集器不同于之前的收集器的一个重要特点是：G1回收的范围是整个Java堆(包括新生代，老年代)，而前六种收集器回收的范围仅限于新生代或老年代。
    - [原文链接](https://blog.csdn.net/justloveyou_/article/details/71216049)
### 类加载（加载，链接【验证，准备，解析】，初始化，使用，卸载）
- 类加载器：启动类lib，扩展类jre/lib/ext，应用程序类classpath，自定义类
- 双亲委派：当一个类收到了类加载请求，他首先不会尝试自己去加载这个类，而是把这个请求委派给父
类去完成。只有当父类加载器反馈自己无法完成这个请求的时候（在它的加载路径下没有找到所需加载的
Class），子类加载器才会尝试自己去加载。【使用不同的类加载
器最终得到的都是同样一个 Object 对象】

## 多线程
    [原文链接](https://blog.csdn.net/tanmomo/article/details/99671622)
1. 创建线程有哪几种方式？
    - 继承Thread类（真正意义上的线程类），是Runnable接口的实现。
    - 实现Runnable接口，并重写里面的run方法。
    - 使用Executor框架创建线程池。Executor框架是juc里提供的线程池的实现。
2. synchronized 和 volatile 的区别是什么？
    - volatile 是变量修饰符；synchronized 是修饰类、方法、代码段。
    - volatile 仅能实现变量的修改可见性，不能保证原子性；而 synchronized 则可以保证变量的修改可见性和原子性。
    - volatile 不会造成线程的阻塞；synchronized 可能会造成线程的阻塞。
3. 线程共享：堆，方法区（元数据）; 线程私有：程序计数器，虚拟机栈，本地方法栈
4. 状态： 新建(New)、就绪（Runnable）start()、运行（Running）run()、阻塞(Blocked)和死亡(Dead)
    
## 数据结构
#### Array ,ArrayList

Array和ArrayList的不同点：
Array可以包含基本类型和对象类型，ArrayList只能包含对象类型。
Array大小是固定的，ArrayList的大小是动态变化的。
ArrayList提供了更多的方法和特性，比如：addAll()，removeAll()，iterator()等等。
对于基本类型数据，集合使用自动装箱来减少编码工作量。但是，当处理固定大小的基本数据类型的时候，这种方式相对比较慢

#### hashMap原理

   2. 哈希冲突
### 二叉树
   1. **红黑树**

``` java
/** 以下是力扣刷题总结内容 */
/** 双指针
*	快慢指针
*	头尾指针
*/
/** 二分法 —— 按条件快速查找 */
	int left = 0;
	int right = increase.length - 1;
	while (left < right) {
		int mid = left + (right - left) / 2;
		if (increase[mid] < target) {	//不符合条件
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;	// 符合条件元素下标
	
/** 分治法 —— 将复杂问题分为简单问题求解，将结果合并 */
/** 动态规划 —— 最少，最短 */ 
/** DFS —— 递归 */ 
	// 广度优先遍历
	Queue<Integer> queue = new LinkedList<Integer>();
	queue.offer(0);
	while (!queue.isEmpty()) {
		int size = queue.size();
		for (int i = 0; i < size; i++) {	// 获取当前队列中元素
			int index = queue.poll();	
			List<Integer> list = edges.get(index);
			for (int nextIndex : list) {	// 添加下一层遍历得到的元素
				queue.offer(nextIndex);
			}
		}
	}
	// 深度优先遍历
	public void dfs(int index) {
		List<Integer> list = edges.get(index);	//获取当前元素对应的下层元素
        for (int nextIndex : list) {			// 对每个下层元素递归获取内容
            dfs(nextIndex);
        }
	}


/** 摩尔投票法
* 候选人(cand_num)初始化为nums[0]，票数count初始化为1。
* 当遇到与cand_num相同的数，则票数count = count + 1，否则票数count = count - 1。
* 当票数count为0时，更换候选人，并将票数count重置为1。
* 遍历完数组后，cand_num即为最终答案。*/
    public int majorityElement(int[] nums) {
        int cand_num = nums[0], count = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (cand_num == nums[i])
                ++count;
            else if (--count == 0) {
                cand_num = nums[i];
                count = 1;
            }
        }
        return cand_num;
    }
/** 树 */
	/** 中序遍历 */
	public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        while(cur != null || !stack.isEmpty()){
            if(cur != null){
                stack.push(cur);
                cur = cur.left;
            }else{
                cur = stack.pop();
                list.add(cur.val);
                cur = cur.right;
            }
        }
        return list;
    }
	/** 前缀树
	* 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
	* 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
	* 每个节点的所有子节点包含的字符都不相同。
	* */
		class Trie {
			private Trie[] children;
			private boolean isEnd;

			public Trie() {
				children = new Trie[26];
				isEnd = false;
			}
			
			public void insert(String word) {
				Trie node = this;
				for (int i = 0; i < word.length(); i++) {
					char ch = word.charAt(i);
					int index = ch - 'a';
					if (node.children[index] == null) {
						node.children[index] = new Trie();
					}
					node = node.children[index];
				}
				node.isEnd = true;
			}

			public Trie[] getChildren() {
				return children;
			}

			public boolean isEnd() {
				return isEnd;
			}
		}

/**以下是程序员小灰学习资料自我总结内容*/  
class ListNode{    //链表
    int val;
    ListNode next;
    ListNode(int x){ this.val = x;}
}
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
}
class Grammer{
    //冒泡排序 n*n
    public void bubbleSort(int[] arr, int n){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n-i-1; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    //插入排序 n*n
    public void insertSort(int[] arr){
        for(int i = 1; i < arr.length; i++){
            //要插入元素及下标
            int insertVal = arr[i];    
            int index = i-1;
            while(index >= 0 && insertVal < arr[index]){
                arr[index+1] = arr[index];    //原来数据后移
                index--;
            }
            arr[index+1] = insertVal;
        }
    }
    //希尔排序 分段插入排序 略优于n*n，不足nlogn
	public void shellSort(int[] arr){
        int dk = arr.length/2;
        while(dk >= 1){
            shellInsert(arr, dk);
            dk = dk/2;
        }
    }
    private void shellInsert(int[] arr, int dk){
        //类似插入，将1改为dk
        for(int i = dk; i < arr.length; i++){
            if(arr[i] < a[i-dk]){
                int x = a[i];
                a[i] = a[i-dk];
                for(int j = i-dk; j >= 0 && x < a[j]; j = j -dk){
                    a[j+dk] = a[j];
                }
                a[j+dk] = x;
            }
        }
    }
    //快速排序 递归 nlogn
    public void quickSort(int[] arr, int low, int high){
        int start = low, end = high, key = arr[low];
        while(end > start){
            while(end > start && arr[end] >= key)    //从后往前找比key小的值
                end--;
            if(arr[end] <= key){
                int temp = arr[end];
                arr[end] = arr[start];
                arr[start] = temp;
            }
            while(end > start && arr[start] <= key)    //从前往后找比key大的值
                start++;
            if(arr[start] >= key){
                int temp = arr[start];
                arr[start] = a[end];
                arr[end] = temp;
            }
        }
        //左右两侧数据递归排序
        if(start > low)    quickSort(arr, low, start-1);
            if(end < high)    quickSort(arr, end+1, high);
    }
    
    //归并排序 nlogn jdk底层排序
    public mergerSort(int[] arr, int left, int right){    //初始值 0，length-1 
        if(left >= right)    return;
        int center(left+right)/2;
        //左右两侧递归排序
        sort(arr,left, center);
        sort(arrm center+1, right);
        //合并
        int[] tmpArr = new int[arr.length];
        int mid = center+1, third = left, tmp = left;//右数组第一元素索引,临时数组索引，左数组第一元素索引
        while(left <= center && mid <= right){
            if(arr[left] <= arr[mid]){
                tmpArr[third++] = arr[left++];
            }else{
                tmpArr[third++] = arr[mid++];
            }
        }
        //剩余合并
        while(mid <= right){
            tmpArr[third++] = arr[mid++];
        }
        while(left <= center){
            tmpArr[third++] = arr[left++];
        }
        //原 left-right 范围的内容被复制回原数组
        while(tmp <= right){
            arr[tmp] = tmpArr[tmp++];
        }
    }
     
    //非递归前序遍历
    public void preOrderTraveralWithStack(TreeNode root){
        Stack<TreeNode> stack = new Stack();
        TreeNode treeNode = root;
        while(treeNode != null || !stack.isEmpty()){
            //访问左侧子节点，并入栈
            while(treeNode != null){
            System.out.println(treeNode.val);
                stack.push(treeNode);
                treeNode = treeNode.left;
            }
            //如果没有左侧子节点，弹出栈顶节点，访问右侧子节点
            if(!stack.isEmpty()){
                treeNode = stack.pop();
                treeNode = treeNode.right;
            }
        }
    }
    //层序遍历
    public void levelOrderTraversal(TreeNode root){
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            System.out.println(node.val);
            if(node.left != null){
                queue.offer(node.left);
            }
            if(node.right != null){
                queue.offer(node.right);
            }
        }
    }
     
    //上浮
    public void upAdjust(int[] array){
        int childIndex = array.length-1;
        int parentIndex = (childIndex-1)/2;
        int temp = array[childIndex];
        while(childIndex > 0 && temp < array[parentIndex]){
            array[childIndex] = array[parentIndex];
            childIndex = parentIndex;
            parentIndex = (parentIndex-1)/2;
        }
        array[childIndex] = temp;
    }
    //下沉,要下沉的父节点，堆的有效大小
    public void downAdjust(int[] array, int parentIndex, int length){
        int temp = array[parentIndex];
        int childIndex = 2*parentIndex+1;
        while(childIndex < length){
            //如果有右孩子，且右孩子小于左孩子，则定位到右孩子
            if(childIndex+1 < length && array[childIndex+1] <array[childIndex]){
                childIndex++;
            }
           //如果父节点小于任何子节点 跳出循环
            if(temp <= array[childIndex]){
                break;
            }
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2*childIndex+1;
        }
    }
    //构建二叉堆
    public void buildHeap(int[] array){
        //从最后一个非叶子节点开始下沉
        for(inti = (array.length-2)/2; i >= 0; i--){
            downAdjust(array, i, array.length);
       }
   }
    
    //堆排序 nlogn 255
    public void downAdjusts(int[] array, int parentIndex, int length){
        int temp = array[parentIndex];
        int childIndex = 2* parentIndex+1;
        while(childIndex < length){
            if(childIndex+1 < length && array[childIndex+1] < array[childIndex]){
                childIndex++;
            }
            if(temp >= array[childIndex])
                break;
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2*childIndex+1;
        }
        array[parentIndex] = temp;
    }
    public void heapSort(int[] array){
        for(int i = (array.length-2)/2; i >= 0; i--){
            downAdjusts(array, i, array.length);
        }
        //循环删除堆顶，调整产生新的堆顶
        for(int i = array.length-1; i > 0; i--){
            //首尾元素交换
            int temp = array[i];
            array[i] = array[0];
            array[0] = temp;
            downAdjusts(array, 0, i);    //下沉调整最大堆
        }
    }
    //计数排序 数据在小范围内，统计个数排序 n
    public int[] countSort(int[] array){
        int max = array[0], min = array[0];                //获取最大值，最小值
        for(int i = 1; i < array.length; i++){
            if(array[i] > max){
                max = array[i];
            }
            if(array[i] < min){
                min = array[i];
            }
        }                            
        int[] countArray = new int[max-min+1];    //计数
        for(int i = 0; i < array.length; i++){
            countArray[array[i]-min]++;
        }
        for(int i = 1; i < countArray.length; i++){    //统计变形
            countArray[i] += countArray[i-1];
        }
        int[] sortedArray = new int[array.length];//排序
        for(int i = array.length-1; i >= 0; i--){
            sortedArray[countArray[array[i]-min]-1] = array[i];
            countArray[array[i]-min]--;
        }
        return sortedArray;
    }
    //桶排序 浮点数的计数排序 n
    public double[] bucketSort(double[] array){
        double max = array[0], min = array[0];
        for(int i = 1; i < array.length; i++){
            if(array[i] > max){
                max = array[i];
            }if(array[i] < min){
                min = array[i];
            }
        }
        ArrayList<LinkedList<Double>> bucketList = new ArrayList<LinkedList<Double>>(array.length);
        for(int i = 0; i < array.length; i++){
            bucketList.add(new LinkedList<Double>());
        }
        for(int i = 0; i < array.length; i++){
            int num = (int)((array[i] - min) * (array.length-1)/(max-min));
            bucketList.get(num).add(array[i]);
        }
        for(int i = 0; i < bucketList.size(); i++){
            Collections.sort(bucketList.get(i));
        }
        double[] sortedArray = new double[array.length];
        int index = 0;
        for(LinkedList<Double> list: bucketList){
            for(double element : list){
                sortedArray[index++] = element;
            }
        }
        return sortedArray;
    }
  

  
    //二分查找
    public int biSearch(int[] array, int a){
        int left = 0, right = array.length-1;
        int mid = 0;
        while(left <= right){
            mid = (left+right)/2;
            if(array[mid] == a){    //找到元素
                return mid+1;
            }else if(array[mid] < a){ //向右查找
                left = mid+1;
            }else{                    //向左查找
                right = mid-1;
            }
        }
        return -1;                    //未找到元素
    }
    //判断链表有环
    public boolean isCycle(ListNode head){
        ListNode fast = head, slow = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(fast == slow){    
            //首次相遇后，计算步数，当再次相遇时获得环长
            //首次相遇后，slow指向头结点，再次相遇节点为入环节点
                return true;
            }
        }
        return false;
    }
    //最小栈实现
    class MinStack{
        private Stack<Integer> stack = new Stack();
        private Stack<Integer> minStack = new Stack();
        public void push(int element){
            stack.push(element);
            if(minStack.isEmpty() || element <= minStack.peek()){
                minStack.push(element);
            }
        }
        public Integer pop(){
            if(stack.peek().equals(minStack.peek())){
                minStack.pop();
            }
            return stack.pop();
        }
        public int getMin() throw Exception{
            if(stack.isEmpty()){
                throw new Exception("stack is empty");
            }
            return minStack.peek();
        }
    }
    //最大公约数 辗转相除法，欧几里得
    public int getGreatestCommonDivisor(int a, int b){
        if(a == b)    return a;
        if((a&1) == 0 && (b&1) == 0)
            return getGreatestCommonDivisor(a>>1, b>>1);
        else if((a&1) == 0 && (b&1) != 0)
            return getGreatestCommonDivisor(a>>1, b);
        else if((a&1) != 0 && (b&1) == 0)
            return getGreatestCommonDivisor(a, b>>1);
        else{
            int big = a>b ? a:b;
            int small = a<b ? a:b;
            return getGreatestCommonDivisor(big-small, small);
        }
    }
    //判定数为二次幂
    public boolean isPowOf2(int num){
        return (num & num-1) == 0;
    }
    //无序数组排序后的最大相邻差    桶排序
    private class Bucket{
        Integer max;
        Integer min;
    }
    public int gerMaxSort(int[] array){
        int max = array[0];
        int min = array[0];
        for(int i = 1; i < array.length; i++){
            if(array[i] > max){
                max =array[i];
            if(array[i] < min)
                min = array[i];
            }
        }
        if(max-min == 0)
            return 0;
        Bucket[] buckets = new Bucket[array.length];
        for(int i = 0; i < array.length; i++){
            buckets[i] = new Bucket();
            int index = ((array[i]-min)*(array.length-1)/(max=min));
            if(buckets[index].min == null || buckets[index].min > array[i])
                buckets[index],min = array[i];
            if(buckets[index].max == null || buckets[index].max < array[i])
                buckets[index].max = array[i];
        }
        int leftMax= buckets[0].max, maxDistance = 0;
        for(int i = 1; i < buckets.length; i++){
            if(buckets[i].min == null)
                continue;
            if(buckets[i].min-leftMax > maxDistance)
                maxDistance = buckets[i].min-leftMax;
            leftMax = buckets[i].max;
        }
        return maxDistance;
    }
    //队列实现栈
    private Stack<Integer> stackA = new Stack<Integer>();
    private Stack<Integer> stackB = new Stack<Integer>();
    public void enQueue(int element){
        stackA.push(element);
    }
    public Integer deQueue(){
        if(stackB.isEmpty()){
            while(!stackA.isEmpty()){
                stackB.push(stackA.pop());
            }
        }
        return stackB.pop();
    }

    //获得全排列下一个数
    public int[] findNearestNumber(int[] number){
        //从后向前查看逆序区域，获得区域前一位，数字置换边界
        int index = 0;
        for(int i = number.length-1; i >= 0; i--){
            if(number[i] > number[i-1]){
                index = i;
                break;
            }
        }
        if(index == 0)    
            return null;
        //把逆序区域前一位和逆序中刚大于它的数字交换
        int[] numberCopy = Arrays.copyOf(numberm number.length);
        int head = numberCopy[index-1];
        for(int i = numberCopy.length-1; i > 0; i--){
            if(head < numberCopy[i]){
                numberCopy[index-1] = numb[i];
                numberCopy[i] = head;
                break;
            }
        }
        //把原来的逆序区域转为顺序
        for(int i = index, j = numberCopy.length-1; i < j; i++, j--){
            int temp = numberCopy[i];
            numberCopy[i] = number[j];
            numberCopy[j] = temp;
        }
        return numberCopy;
    }
    //删去k个数字后的最小值
    public String removeDigit(String num, int k){
        int newLength = num.length()-k;
        //创建一个栈，接受所有数据
        char[] stack = new char[num.length()];
        int top = 0;
        for(int i = 0; i< num.length(); i++){
            char c = num.charAt(i);
            //当栈顶数字大于遍历到的当前数字时，栈顶数字出栈
            while(top > 0 && stack[top-1] > c && k > 0){
                top --;
                k--;
            }
            stack[top++] = c;
        }
        //找到栈中第一个非零数字的位置，构建新的整数字符串
        int offset = 0;
        while(offset < newLength && stack[offset] == '0'){
            offset++;
        }
        return offset == newLength ? "0" : new String(stack, offset, newLength-offset);
    }
    //大数相加
    public String bigBumberSum(String a, String b){
        int maxLength = a.length()>b.length()> a.length(): b.length();
        int[] array = new int[maxLength+1];
        for(int i = 0; i < array.length; i++){
            int temp = array[i];
            if(a.length()-1-i >= 0)
                temp += a.charAt(a.length()-1-i)-'0';
            if(b.length()-1-i >= 0)
                temp += b.charAt(b.length()-1-i)-'0';
            if(temp >= 10){
                temp = temp-10;
                array[i+1] = 1;
            }
            array[i] = temp;
        }
        StringBuilder ans = new StringBuilder();
        boolean findFirst = false;
        for(int i = array.length-1; i >= 0; i--){
            if(!findFirst){
                if(array[i] == 0){
                    continue;
                }
                findFirst = true;
            }
            ans.append(array[i]);
        }
        return ans.toString();
    }
    //求解金矿 背包问题 
    //工人数量，金矿开采需人工数，金矿储量
    public int getBestGoldMining(int w, int[] p, int[] g){
        int[][] result = new int[g.length+1][w+1];
        for(int i = 1; i <= g.length; i++){
            for(int j = 1; j <= w; j++){
                if(j < p[i-1])
                    result[i][j] = result[i-1][j];
                else
                    result[i][j] = Math.max(result[i-1][j], result[i-1][j-p[i-1]]+g[i-1]);
            }
        }
        return result[g.length][w];
    }
    //全排列中缺失的数据 分治
    public int[] findLostNum(int[] array){
        int[] result = new int[2];
        int xor = 0;
        for(int i = 0; i < array.length; i++){
            xor ^= array[i];
        }
        if(xor == 0)
            return null;
        int separator = 1;
        while(0 == (xor & separator)){
            separator <<= 1;
        }
        for(int i = 0; i < array.length; i++){
            if(0 == (array[i] & separator))
                result[0] ^= array[i];
            else
                result[1] ^= array[i];
        }
        return result;
    }

  
    //LRU缓存 最近最少使用
    class Node{
        Node(String key, String  value){
            this.key = key;this.value = value;
        }
        public Node pre;
        public Node next;
        public String key;
        public String value;
    }
    private Node head, end;
    private int limit;//缓存存储上限
    private HashMap<String, Node> hashMap;
    public LRUCache(int limit){
        this.limit = limit;
        hashMap = new HashMap();
    }
    public get(String key){
        Node node = hashMap.get(key);
        if(node == null)
            return null;
        refreshNode(node);
        return node.value;
    }
    public void put(String key, String value){
        Node node = hashMap.get(key);
        if(node == null){
            if(hashMap.size() >= limit){
                String oldkey =removeNode(head);
                hashMap.remove(oldkey);
            }
            node = new Node(key, value);
            addNode(node);
            hashMap.put(key, node);
        }else{
            node.value = value;
            refreshNode(node);
        }
    }
    public void remove(String key){
        Node node = hashMap.get(key);
        removeNode(node);
        hashMap.remove(key);
    }
    private void refreshNode(Node node){    //更新使用状态
        if(node == end)    return;
        removeNode(node);
        addNode(node);
    }
    private String removeNode(Node node){
        if(head == node && end == node){    //只有一个节点
            head = null; end = null;
        }else if(node == end){
            end = end.pre;
            end.next = null;
        }else if(node == head){
            head = head.next;
            head.pre = null;
        }else{
            node.pre,next = node.next;
            node.next.pre = node.pre;
        }
        return node.key;
    }
    private void addNode(Node node){    //添加数据到链表尾部
        if(end != null){
            end.next = node;
            node.pre = en;
            node.next = null;
        }
        end = node;
        if(head == null){
            head = node;
        }
    }

    
    //A星寻路算法
    public final int[][] MAZE{
        {0,0,0,0,0,0,0},
        {0,0,0,1,0,0,0},
        {0,0,0,1,0,0,0},
        {0,0,0,1,0,0,0},
        {0,0,0,0,0,0,0},
    };
    class Grid{
        public int x, y, f, g, h;
        public Grid parent;
        public Grid(int x, int y){
            this.x = x; this.y = y;
        }
        public void initGrid(Grid parent, Grid end){
            this.parent = parent;
            if(parent != null){
                this.g = parent.g+1;
            }else{
                this.g = 1;
            }
            this.h = Math.abs(this.x-end.x)+Math.abs(this.y-end.y);
            this.f = this.g+this.h;
        }
    }
    public Grid aStartSearch(Grid start, Grid end){
        ArrayList<Grid> openList = new ArrayList();    //可前进位置
        ArrayList<Grid> closeList = new ArrayList(); //已走过位置
        openList.add(start);
        while(openList.size() > 0){
            Grid currentGrid = findMinGrid(openList);
            openList.remove(currentGrid);
            closeList.add(currentGrid);
            List<Grid> neighbors = findNeighbors(currentGrid, openList,closeList);
            for(Grid grid : neighbors){
                if(!openList.contains(grid)){
                    grid.initGrid(currentGrid, end);
                    openList.add(grid);
                }
                if(grid.x == end.x && grid.y = end.y){    //如果终点在openlist 直接返回终点
                    return grid;
                }
            }
        }
        return null;
    }
    private Grid findMinGrid(ArrayList<Grid> openList){
        Grid tempGrid = openList.get(0);
        for(Grid grid: openList){
            if(grid.f < tempGrid.f)
                tempGrid = grid;
        }
        return tempGrid;
    }
    private ArrayList<Grid> findNeighbors(Grid grid, List<Grid> openList, List<Grid> closeList){
        ArrayList<Grid> gridlist = new ArrayList();
        if(isValidGrid(grid.x, grid.y-1, openList, closeList))
            gridlist.add(new Grid(grid.x, grid.y-1));
        if(isValidGrid(grid.x, grid.y+1, openList, closeList))
            gridlist.add(new Grid(grid.x, grid.y+1));
         
        if(isValidGrid(grid.x-1, grid.y, openList, closeList))
            gridlist.add(new Grid(grid.x-1, grid.y));
        if(isValidGrid(grid.x+1, grid.y, openList, closeList))
            gridlist.add(new Grid(grid.x+1, grid.y));
        return gridlist;
    }
    private boolean isValidGrid(int x,int y, List<Grid> openList, List<Grid> closeList){
        if(x < 0 || x >= MAZE.length || y < 0 || y >= MAZE[0].length)
            return false;
        if(MAZE[x][y] == 1)    //有障碍
            return false;
        if(containsGrid(openList, x, y) || containsGrid(closeList, x, y))
            return false;
        return true;
    }
    private boolean containsGrid(List<Grid> grids, int x, int y){
        for(Grid n: grids){
            if(n.x == x && n.y == y){
                return true;
            }
        }
        return false;
    }


    //红包算法
    //二倍均值法 红包=0.01——剩余金额/剩余人数*2-0.01
    public List<integer> divideRedPackage(Integer totalAmount, Integer totalPeopleNum){
        List<Integer> amountList = new ArrayList<Integer>();
        Integer restAmount = totalAmount;
        Integer restPeoPleNum = totalPeopleNum;
        Random random = new Random();
        for(int i = 0; i < totalPeopleNum-1; i++){
            int amount = random.nextInt(restAmount/restPeoPleNum*2-1)+1;
            restAmount -= amount;
            restPeoPleNum--;
            amountList.add(amount);
        }
        amountList.add(restAmount);
        return amountList;
    }
}
```

## 手撕代码
###  反转链表
    ```java
    public ListNode ReverseList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode p = null;
        ListNode q = null;
        while(head != null){
            //做循环，如果当前节点不为空的话，始终执行此循环，此循环的目的就是让当前节点从指向next到指向pre
            //如此就可以做到反转链表的效果
            //先用next保存head的下一个节点的信息，保证单链表不会因为失去head节点的原next节点而就此断裂
            q = head.next;
            //保存完next，就可以让head从指向next变成指向pre了，代码如下
            head.next = p;
            //head指向pre后，就继续依次反转下一个节点
            //让pre，head，next依次向后移动一个节点，继续下一次的指针反转
            p = head;
            head = q;
        }
        return p;
    }
    ```
###  三十个人围成一圈，数到5退出，求最后一个退出的
    ```java
    
    ```
###  矩阵蛇形遍历
    ```java
    public static void way(int n){
        int[][] arry = new int[n][n];
        for(int i = 0; i < n; i++){    //初始化
            for(int j = 0; j < n; j++){
                arry[i][j] = (i-1)*n+j+1;
            }
        }
        int i = 0, j  = 0;
        StringBuilder sb = new StringBuilder();
        sb.append(arry[0][0]+" ");    //第一个元素
        boolean isDown = false;    //判断是自上而下还是自下而上，默认自上而下
        while(i < n && j < n){
            if(i+1 == n && j+1 == n){    //结束跳出
                break;
            }
            if(i-1 < 0|| i+1 == n){        //右
                sb.append(arry[i][++j]+" ");
                isDown = false;
            }else if(j-1 < 0 || j+1 == n){        //下
                sb.append(arry[++i][j]+" ");
                isDown = true;
            }else{
                if(isDown){
                    sb.append(arry[++i][++j]+" ");
                }else{
                    sb.append(arry[--i][--j]+" ");
                }
            }
        }
        System.out.println(sb);
    }
    ```
