from aophelper.baseAdvice import BaseAdvice
import time


class LoggingAdvice(BaseAdvice):
    """기본 로깅 어드바이스"""

    def before(self, func, *args, **kwargs):
        print(f"[BEFORE] {func.__name__} 실행됨. 인자: {args}, {kwargs}")

    def after(self, func, result, *args, **kwargs):
        print(f"[AFTER] {func.__name__} 실행 완료. 결과: {result}")

    def around(self, func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[AROUND] {func.__name__} 실행 시간: {end - start:.4f}초")
        return result

    def on_exception(self, func, exception, *args, **kwargs):
        print(f"[EXCEPTION] {func.__name__}에서 예외 발생: {exception}")