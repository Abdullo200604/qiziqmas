"""1. Funksiyani bajarilish vaqtini o‘lchash"""
import time


def decorator(func):
    def birnima(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksiya {end_time - start_time:.5f} sekundda bajarildi")
        return result

    return wrapper


@time_decorator
def uzun_hisoblash(n):
    total = 0
    for i in range(n):
        total += i
    return total


print(uzun_hisoblash(1000000))
#
# """2. Kiruvchi ma'lumotlarni tekshirish"""
#
#
# def check_positive(func):
#     def wrapper(a, b):
#         if a < 0 or b < 0:
#             raise ValueError("Sonlar musbat bo‘lishi kerak!")
#         return func(a, b)
#
#     return wrapper
#
#
# @check_positive
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(3, 4))
# # print(multiply(-1, 5))  # ValueError chiqadi
#
# """3. Funksiyani faqat bir marta bajarish"""
#
#
# def only_once(func):
#     called = False
#
#     def wrapper(*args, **kwargs):
#         nonlocal called
#         if called:
#             print("Bu funksiya allaqachon bajarilgan!")
#             return None
#         called = True
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @only_once
# def hello():
#     print("Salom!")
#
#
# hello()
# hello()
#
# """4. Kiruvchi argumentlarni log qilish"""
#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Funksiya chaqirildi: {func.__name__}({args}, {kwargs})")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @logger
# def add(a, b):
#     return a + b
#
#
# print(add(5, 10))
# """5. Funksiya natijasini keshlash (caching)"""
#
#
# def cache(func):
#     saved_results = {}
#
#     def wrapper(*args):
#         if args in saved_results:
#             print("Natija keshdan olindi")
#             return saved_results[args]
#         result = func(*args)
#         saved_results[args] = result
#         return result
#
#     return wrapper
#
#
# @cache
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))
# print(factorial(5))  # Keshdan olinadi
