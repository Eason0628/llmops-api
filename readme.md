Flask
Handler->Controller
Ruoter->ControllerPath

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

文本嵌入模型：将传入的文本/文档转换成向量,维度越大，能记录的数据特征就越多，检索效果就越好，但是也会增加计算成本，空间占用也会增加。
对于复杂场景我们需要记录更多维度特征，我们就可以使用更高维度的文本嵌入模型生成的向量，检索效果会更好。

RAG搜索添加对应的知识库关联也就是说获取人类传递的数据，然后去检索到对应的文档，接下来再将文档转换成文字，嵌入到prompt中。
app_handler构建的链应用每一次去提问的时候，它都会去后台去检索出对应的历史，然后去知识库中按照我们的输入去检索出对应的信息，
接下来将检索到的文档拼接成字符串，跟着记忆一起，还有我们人类输入一起发给大语言模型,完成大语言模型根据特定的文本去生成内容的流程，这就是一个最基础的RAG应用。

AI机器人去总结整个视频内容实现思路：加载视频站的URL去提取出文本字幕，通过加载器去加载整个视频的字幕展示出整个视频内容，然后去写一段Prompt，让大模型去总结字幕的内容。

Document文档加载器
以TextLoader为例，扩展到 LangChain 封装的其他文档加载器，使用技巧都是一模一样的，在实例化加载器的时候，传入对应的信息（文件路径、网址、目录等），然后调用加载器的
load() 方法即可一键加载文档。

7-1
内置插件动态加载逻辑
1.core->tools->builtin_tools->providers->providers.yaml中定义有哪些服务商，服务商信息包括服务商名称、服务商标签、icon等
2.对应的服务商文件夹google中的positions.yaml存放对应的服务商包含的工具名称，例如googole服务商有googole_serper、googole_weaviate等工具
3.创建对应的py脚本，提供对应的服务商的Langchain工具实现，例如googole_serper.py、googole_weaviate.py等
4.在对应的文件夹内给googole_serper.py、googole_weaviate.py添加对应的google_serper.yaml、googole_weaviate.yaml保存服务商工具信息
5.internal->lib->helper.py中添加dynamic_import函数，用于动态导入特定模块下的特定功能

Q:
lib中add_attribute装饰器的用法python?
@add_attribute("args_schema", Dalle3ArgsSchema) 因为Delle3内置工具有调用函数，那为什么要绑定一下？
def dalle3(**kwargs) -> BaseTool:










