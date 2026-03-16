from wxauto import WeChat

# 初始化微信实例
wx = WeChat()

# 发送消息给"马锋"（已注释）
# wx.SendMsg("你咋现在才到家啊？？？晕！！！", who="马锋")

# 打开与马锋的聊天窗口（已注释）
# wx.ChatWith("马锋")

# 获取聊天记录（已注释）
# msgs = wx.GetAllMessage()
# print(f"获取到 {len(msgs)} 条消息：\n")
# for msg in msgs:
#     print(f"发送者: {msg.sender}")
#     print(f"内容: {msg.content}")
#     print(f"类型: {msg.type}")
#     print("-" * 50)

# 获取最新消息（已注释）
# print("开始监听最新消息...\n")
# wx.ChatWith("马锋")
# msgs = wx.GetAllMessage()
# latest_msgs = msgs[-5:] if len(msgs) >= 5 else msgs
# print(f"最新的 {len(latest_msgs)} 条消息：\n")
# for msg in latest_msgs:
#     print(f"发送者: {msg.sender}")
#     print(f"内容: {msg.content}")
#     print(f"类型: {msg.type}")
#     print("-" * 50)

# 监听马锋的消息，有新消息时自动触发
import time

print("开始监听马锋的消息，等待新消息...\n")

# 添加监听对象
wx.AddListenChat(who="练瓜", savepic=False, savefile=False, savevoice=False)

# 持续监听新消息
try:
    while True:
        # 获取监听对象的新消息
        msgs = wx.GetListenMessage(who="练瓜")
        
        if msgs:
            print(f"\n收到新消息！")
            for msg in msgs:
                print(f"发送者: {msg.sender}")
                print(f"内容: {msg.content}")
                print(f"类型: {msg.type}")
                print("-" * 50)
        
        # 每隔1秒检查一次
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\n停止监听")
    wx.RemoveListenChat(who="马锋")
