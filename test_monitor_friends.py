from wxauto import WeChat
import time

# 初始化微信实例
wx = WeChat()

# 监控人名单
monitor_list = ["马锋", "练瓜"]

print(f"开始监控以下好友的消息：{', '.join(monitor_list)}\n")
print("按 Ctrl+C 停止监控\n")

# 为每个监控对象添加监听
for friend in monitor_list:
    wx.AddListenChat(who=friend)
    print(f"已添加监听：{friend}")

print("\n" + "="*60)
print("监控已启动，等待新消息...")
print("="*60 + "\n")

try:
    while True:
        # 获取所有监听对象的新消息
        all_msgs = wx.GetListenMessage()
        
        if all_msgs:
            for chat, msgs in all_msgs.items():
                chat_name = chat.who  # 获取聊天对象名称
                
                print(f"\n{'='*60}")
                print(f"📩 收到来自 [{chat_name}] 的新消息")
                print(f"{'='*60}")
                
                for msg in msgs:
                    print(f"👤 发送者: {msg.sender}")
                    print(f"💬 内容: {msg.content}")
                    print(f"📝 类型: {msg.type}")
                    print("-" * 50)
        
        # 每隔1秒检查一次
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\n\n停止监控...")
    # 移除所有监听
    for friend in monitor_list:
        wx.RemoveListenChat(who=friend)
        print(f"已移除监听：{friend}")
    print("\n监控已停止")
