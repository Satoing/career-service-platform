> 这是小组合作项目，我负责的是Flask后端部分和前端版式的代码。爬虫的数据以csv的格式传入，echarts图表的javascript代码已集成到html里面。

# 项目使用说明
---

1. 数据库的创建：执行function目录下的models.py(建表)和insert.py(插值)即可。


> 注意：需要事先建好数据库，数据库的名字设置为jobs。也可以在models.py中修改：

![image-20220714162431019](/static/images/image-20220714162431019.png)

> 如果你的数据库密码不是123，或者用户名不是root，也需要在models.py中修改：

![image-20220714162559084](/static/images/image-20220714162559084.png)


2. 执行项目根目录下的main.py：`python main.py`，进入首页：

   ![image-20220714162651883](/static/images/image-20220714162651883.png)

3. 点击导航栏的学生专区，进入学生专区首页。首页以表格+文字的形式展示数据。但是可能因为屏幕尺寸的原因出现错位。导航栏有查看职业信息与职业分析与推荐两个部分，后者需要登录。

   ![image-20220714162747816](/static/images/image-20220714162747816.png)

4. 职业信息界面以卡片的方式展示了各种职业的信息。点击上面右边的文字可以进行筛选，点击左边的城市、分类、薪资可以进入相应的可视化界面。

   ![image-20220714163122698](/static/images/image-20220714163122698.png)

   ![image-20220714163307476](/static/images/image-20220714163307476.png)

   ![image-20220714163329198](/static/images/image-20220714163329198.png)

   ![image-20220714163353925](/static/images/image-20220714163353925.png)

5. 进行职业分析前需要先登录和注册，填写表单即可。

6. 职业分析界面，填写表单即可。需要注意不能留空，不然会打回来重填。填写完提交即可，生成推荐职业。

   ![image-20220714163614818](/static/images/image-20220714163614818.png)

   ![image-20220714164149840](/static/images/image-20220714164149840.png)

7. 学校专区的界面就比较简单了，首页展示各学校的就业网网址，就业政策展示教育部的就业政策：

   ![image-20220714164257851](/static/images/image-20220714164257851.png)

   ![image-20220714164327027](/static/images/image-20220714164327027.png)
   
---
> 让一个不怎么会前端的负责前端可真是折磨。
