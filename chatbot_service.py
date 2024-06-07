# chatbot_service.py
import win32serviceutil
import win32service
import win32event
from chatbot import get_response, conversation_history

class ChatbotService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ChatbotService"
    _svc_display_name_ = "Chatbot Background Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import time
        while True:
            # Example of periodic task
            time.sleep(5)
            user_input = "hello"  # This should be replaced by actual input method
            response, conversation_history = get_response(user_input, conversation_history)
            print(response)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ChatbotService)
