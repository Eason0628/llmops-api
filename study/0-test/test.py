from langchain_openai import OpenAI


def completion(self):
    print("completion is called")

    # 2.创建openai客户端，并发起请求
    client = OpenAI(
        api_key="sk-PpijgqOl3UEEUqXyr9UmbiiM3pHfjA3QzgjfwTV075vcoexj",
        base_url="https://poloapi.top",
    )
    resp = client.responses.create(
        model="gpt-3.5-turbo",
        input=[
            {"role": "system", "content": "你是OPENAI开发的聊天机器人，请根据用户的输入回复对应的信息"},
            {"role": "user", "content": "你好，你是谁？"},
        ],
    )
    # 3.得到请求结果，然后将openai的结果返回给前端
    print(resp)
    # return jsonify({"answer": resp.output_text})
