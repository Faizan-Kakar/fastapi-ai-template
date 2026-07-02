class AppException(Exception):
    def __init__(self, message: str, status_code: int, detail: str | None = None):
        self.message = message
        self.status_code = status_code
        self.detail = detail
        super().__init__(message)
        

class AgentExecutionError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Agent execution failed",
            status_code=500,
            detail=detail)