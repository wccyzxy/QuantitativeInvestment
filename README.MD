# 介绍
懂得都懂

## 食用说明
运行backend.py，然后在浏览器打开web目录下的mainpage.html

## 暂时划分
计划采用前后端分离来开发，即走web那一套  
- 后端使用python，分为逻辑部分与接口部分（虽然目前有点搅合在一起）     
  ***主要采用面向对象编程。能封装为class的就封装***     
  大量数据的存储用pandas库       
- 前后端沟通的接口用python的flask库来编写      
  同时需要编写一套接口规范，便于前后端并行开发     
  请求传输的数据通常都是json，后端的flask会自动帮你转化成dict类型，前端就得手动构造object了     
- 前端用html+css+js       
  使用js发请求与后端通信
  页面html编写考虑将来使用框架，现在先凑合随便写写，给个样子
  css吔可以使用现成的
  js主要包括jQuery库（其他我还没想法   

至于为什么想到用这一套，其实是因为html+css写界面方便，且容易做的美观（     
（以后会变成什么样就再说吧）

## 目前概况
单user单账本，只能添加不能删除     
甚至还没有写读取&保存文件的逻辑，一关掉就无了      
组织架构很混乱，接口编写没有规划，随时会改变     
反正目前看看就得     
！请不要在意static和template文件夹，那是历史遗留，迟早得删

## 依赖
以下都是依赖的python库     
在CMD敲`pip install xxxx`来安装对应库（前提是已经正确配置环境变量。若提示无法识别pip，请上网搜索解决环境配置问题）
|||
|-|-|
|flask|编写接口|
|flask_cors|8太清楚|
|pandas|数据处理|
|numpy==1.9|数学计算（反正不要用最新的1.9.4版本，跑不起来）|
|scipy|科学计算|
|requests|网络请求|


# 编码风格
## ！！！
***项目刚刚起步，随着项目的推进和扩大，以后将会不可避免地面临代码重构等等    
一定要遵守编码风格，写可读性好的代码     
不然就会“写码一时爽，重构火葬场”***    
## ！！！

基本采用PEP8的规则，这里只说一些关键的     
>PEP8原文：https://www.python.org/dev/peps/pep-0008/      
>简要中文翻译版：https://www.jianshu.com/p/ffcc66bab3ce      
## 缩进
4个空格，不是tab。VSC里面默认好像就是4空格的    
不要tab跟空格混用，在python里头会出大问题

## 命名规范
### 风格
Python代码基本采用蛇形命名法，除了类名用大驼峰。
~~~python
# 变量
myfriendname = 'name'       # 不行，连着这么长一串谁看得懂啊
myFriendName = 'name'       # 不行，这是小驼峰
my_friend_name = 'name'     # 行

# 全局变量
MYFRIENDNAME = 'name'       # 不行，连着这么长一串谁看得懂啊
my_friend_name = 'name'     # 不行，这不全局变量
MY_FRIEND_NAME = 'name'     # 行
FRIEND_COUNT = 0            # 行

# 类名
class my_friend:            # 不行
class MyFriend:             # 行
class BookRecord:           # 行
~~~

### 含义
- 不要与Python内置的标识符重名
- 不要起无意义的名字
- 不要用拼音起名
- 表达相同含义时，尽量用同一个单词
~~~python
a = 0                       # 不行，谁知道这个变量代表啥啊
bian_liang = True           # 不行，变量？变亮？同音的那么多咋找，考虑改成variable
str = 'abcde'               # 不行，你让我接下来怎么用str()来强制转换类型啊
for i in range(5)           # 行，约定俗成的表示索引的循环变量
for a,b in ('Yajuu',114)    # 不行，a,b意义不明，考虑改为name,score

def give_me_money():
    cash = 114514
    return cash             # 不太好，容易搞混，如果没有特殊用意还是统一吧
~~~

## 函数定义规范
py的类型太动态了，如果不好好写好文档，容易出问题
- 定义函数时，用Annotation表明参数的类型、函数的返回值类型
- 在函数头的下方写上文档（docstring），包括：概括、参数解释（如有）、返回值解释（如有）

>标注(Annotation)参阅：https://blog.csdn.net/poblg/article/details/103583671   
>类型(typing)参阅：https://www.dazhuanlan.com/2020/02/02/5e368aafec947/       

~~~python
# 不行，前面还能猜到是数字，但color会是啥玩意？
def draw_rectangle(x, y, width, height, color):
    ...
    return rect_id

# 行，注释很清晰
def draw_rectangle(x:float, y:float, width:float, height:float, color:str) -> int:
    """
    画一个矩形，返回矩形的ID

    Params
    ---------
    x,y : 位置；
    width, heigt : 宽高，正数；
    color : 颜色，使用'#FFFFFF'的格式
    """
    ...
    return rect_id
~~~
>函数的类型标注
>>标注的目的主要是方便linter进行代码提示和自动补全    
>>python的类型无法过于精确，对于嵌套复杂的（如list里面套dict，dict里面又套list...），最多写一两层意思意思就行（如`List[dict]`）     

>>
>    

