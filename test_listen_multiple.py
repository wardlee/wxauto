from wxauto import WeChat
import time

# 初始化微信实例
wx = WeChat()

print("开始监听所有新消息...\n")
print("按 Ctrl+C 停止监听\n")

try:
    while True:
        # 获取下一个新消息（自动检测所有有新消息的聊天窗口）
        new_messages = wx.GetNextNewMessage()
        
        if new_messages:
            chat_name = new_messages.get('chat_name', '未知')
            chat_type = new_messages.get('chat_type', '未知')
            msgs = new_messages.get('msg', [])
            
            print(f"\n{'='*60}")
            print(f"收到来自 [{chat_name}] 的新消息 (类型: {chat_type})")
            print(f"{'='*60}")
            
            for msg in msgs:
                print(f"发送者: {msg.sender}")
                print(f"内容: {msg.content}")
                print(f"类型: {msg.type}")
                print("-" * 50)
        
        # 每隔1秒检查一次
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\n\n监听已停止")
