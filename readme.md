## 2-1

python 创建虚拟环境命令:
优点:相互隔离，每个项目之间有自己的环境，和其它项目不相互干扰    
缺点:占用空间大，每次使用时必须激活才能使用
python -m venv env(环境名) --创建虚拟环境依赖的文件，以env命名
激活虚拟环境命令：
env\Scripts\activate
退出虚拟环境命令：
env\Scripts\deactivate.bat
安装 * 包
pip install openai

全局配置腾讯云镜像源
pip config set global.index.url https://mirrors.cloud.tencent.com/pypi/simple
pip config list --检查配置
Python+Flask技术栈开发的优缺点：
优点：
Langchain简化了开发流程，屏蔽了很多细节将所有的大语言模型封装成标准接口、还统一了向量数据库，嵌入模型等接口，避免自己封装轮子对接大语言模型、向量数据库等；
langchain+python简化开发流程、提升开发效率，少写50-60%代码。

## 2-2

Py依赖管理
python安装injector依赖
pip install injector

py项目开发时要记录代码里面使用了哪些包，给使用项目的人一键安装相应的依赖；
pip freeze 这个命令的作用是显示当前环境中安装的所有包及其版本号。
这个命令的作用是将当前环境中安装的所有包及其版本号输出到 requirements.txt 文件中。
pip freeze > requirements.txt

当更多时候使用的是pipreqs,安装pipreqs依赖
pip install --no-deps pipreqs
pip install yarg==0.1.9 docopt==0.6.2

pipreqs . --ignore env --force --encoding=utf-8 这个命令的作用是生成当前项目 的依赖文件 requirements.txt，
--ignore env 表示忽略 env 目录下的文件，--force 表示强制覆盖已有的 requirements.txt 文件。
根据项目的依赖文件 requirements.txt 安装依赖
pip install -r requirements.txt

在postgresql数据库中创建数据库llmops,启动/关闭数据库服务
pg_ctl.exe start/stop -D "D:\2025\D_Coding\llmops\llmops-api\env\pgdata"

python安装openai依赖
pip install openai

安装python-dotenv依赖
pip install python-dotenv

安装Flask-WTF依赖，用于表单验证
pip install -U Flask-WTF

安装pytest依赖
pip install pytest
测试文件以 test_ 开头或 _test 结尾；
测试类以 Test 开头，并且不能带有 init 方法；
测试函数以 test_ 开头；
断言使用基本的 assert 即可；

安装 Flask-SQLAlchemy和postgresql数据库驱动
pip install flask-sqlalchemy psycopg2

## 2-3

LangChain
pip install langchain==0.2.1 langchain-community==0.2.1



