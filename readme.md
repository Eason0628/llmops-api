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

安装pip install flask-cors处理跨域请求

安装langchain-community依赖，使用FileChatMessageHistory,PostgresChatMessageHistory
pip install langchain langchain-community

什么是RAG:
而且在实际代码中，无论多么复杂的 RAG，无论如何进行优化， 本质上都是执行外部搜索，然后将外部搜索的内容和用户原始提问合并成prompt，
再向大语言模型发起提问，最终得到对应的内容。
关于RAG的优化有几个部分:
第一部分就是提问的内容，我们需不需要去优化？如果用户传递的问题是一大长串，传递给检索器，那么一般检索效果是不好，
第二部分是检索部分优化：大语言模型有注意力机制，对越靠近的部分那么它注意力会越大，所以检索到的内容如果有多条，可以考虑到进行排序。重要的排在前面，大语言模型对前面的数据它的关注度会更高，对后面它可能忽略了。
第三部分存储知识这部分是不是也可以去考虑如何去操作，比如文档的块大小有多大？一个文档要多少字比较合适？然后文档和文档之间要有什么关联？文档和文档之间要怎么切割？然后我们该如何去搜索？这些是不是都可以优化？
所以本质上学习RAG应用开发就是学习RAG优化的一个过程
对于一个最基础的RAG运行流程，虽然可以运行，但是对于一些复杂场合，或者说数据库比较特殊情况下，运行效果是比较差的，
所以后续做RAG优化的时候，就会从几个方面，一个是用户提问，然后是生成输出内容，接下来存储这些知识库的数据是不是也可以优化。然后原始数据我们该怎么切割、存储都可以优化。

向量检索基于不同维度的语义相近的搜索：
向量数据库的最常使用场景：人脸识别、图像搜索、音频识别、智能推荐系统等。
而在 RAG 中，我们将对应的知识文档按照特定的规则拆分成合适的大小，再转换成向量存储到向量数据库中，当人类提问时，将人类提问
query 转换成向量并进行搜索，找到在特征上更接近的文本块，这些文本块就可以看成和 query 具有强关联或者说有因果关系。
这样就可以将这些文本块作为这次提问的额外补充知识，让 LLM 基于补充知识 + 提问生成对应的内容，从而实现知识库问答。





