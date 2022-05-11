# 蔚蓝天空开发日志
作者：张厚泽
时间：2022-02-14
地点：普罗旺斯埃克斯
公司：LMSM

# 专业术语

IHM
tab

# 项目wiki

# 设计文档
设计文档的编写结构是按照业务逻辑展开的，设计文档的章节按照IHM以及IHM的tab划分

## Management

### User Allocation
#### insect
? 问题在于怎么让insect的administrator修改权限？
？qt5无法隐藏table，除非创建一个新的window
**当我将insect选项设置为Non，将user table和权限配置模块隐藏，同时，将ItemsIHM的onglet抹去
**将Test Execution 中Insect name Add Possible insect in Environment删除
**将WT中的Insect name和Quantity删除

## ListOfTestMeans

### 关于sensor的表结构修改
替换sensor表结构：type换成ref，并且删除order
calibration添加date字段
param sensor用idsensor而不是sensortype做外键

? 关于param的validate字段，如何实现param的增删改查
删除这两个validate字段

? 用户是否有权利在本IHM下创建新的sensor type
可以创建number de sensor

? 用户是否有权利在本IHM下创建新的tank
可以创建number de tank

### Aircraft/Wind tunnel组件

##### ParamModel

##### search模块

##### validate模块

##### delete模块
如何判断用户是否拥有删除某一test_mean的param对象：
token<=4 && validate is False

###### 实现思路：
绑定double_click方法，在controller层中实现权限的核验，在model层update表type_param_test_mean

### Sensor组件
? 能给我sensor的配置文件吗
没有sensor的配置文件，需要手动输入

? 为什么sensor界面不能导入param的配置文件
自主添加param的search按钮

? calibration按钮允许实验人员导入calibration数据
OK

#### sensor type和sensor ref
table sensor type && table sensor
type_sensor.ref 填充sensor type
sensor.type 填充reference
sensor.number 填充sensor number

###### 实现思路
见SensorModel类

#### order，configuration和sensor number表格
order设置为二选一模式，working || Out of order
config设置为二选一模式，in store || in configuration

### Tank组件
? 能给我tank position的配置文件吗
CIO CATIA extract按钮能够导入数据

#### Sensor-coating-type下拉框实现
分别调用sensor type和coating type，拼装两表

### Ejector&&Camera组件
? 有权利删除ejector和camera吗

# commit日志

## 常规-2022-04-20

### 关于manager页面清零的bug

## 常规-2022-04-13-

###
挺离谱的，Python会在第二次运行函数的时候将之前的函数定义覆盖

## 常规-2022-04-12-

### 待改进
create新position

双击删除attri
单击填充attri
create 新attri

db_transfer上传数据
db_transfer弹窗

### 实现action_configue_by_type_number函数
用一个函数来基本实现该GUI的大部分逻辑，包括validate判定，chara和unity两个combobox的填充，实现按钮的虚化

### 补充right Graph权限图的注释
略

### 修改数据库初始化脚本
删除attribute-coating表格的validate字段

### 用户创建和赋权测试
创建用户随后赋予用户权限不会影响用户权限图的健壮性，测试成功

### 实现action_get_coating_position接口


## 常规-2022-04-11-a8e85a5

### Manager界面版本控制调整
创建新的分支，localdev，思路是希望明确自己的版本控制流程，main选择用来发布而不是测试
localdev分支用于开发
test分支用于测试部署

新建分支 git checkout -b new-branch

强制切换新分支能够让我在不提交现有修改的前提下，直接切换到其他分支上
强制切换分支 git checkout -f old-branch

将新建的分支推送到远程服务器
git push origin new-branch-name:new-branch-name

### PyQt5的组件透明度

使用QtWidgers.QGraphicsOpacityEffect()创建透明度参数
它不能一次创建多次使用，原因未知
op_05 = QtWidgers.QGraphicsOpacityEffect()
op_05.setOpacity(0.5)

研究了Items界面的业务逻辑，纠正了表结构的错误，
对

### 数据库更新

删除表attribute_coating和attribute_detergent中的validate字段

### 开发items界面

新的界面涉及登录用户的权限调取，是只读的，所以我第一版程序选择使用之前开发好的RightGraph接口进行后续开发
在开发的过程中发现问题漏洞：在update数据的时候，仅仅更新有权限的普通用户，管理员级别的用户，如root，内建的manager们，以及没有任何权限的新用户都将被排除在外，因为manager，root和新用户都有权限可以访问items界面勾选coating_type，所以必须重新修改update方法，仅仅添加一个if块即可实现

基本实现type_coating combobox，待测试

### 待改进

需要回归测试新的图数据结构，给新用户赋予权限可能不会把用户在user_right中初始的记录删除，有数据异常的风险
