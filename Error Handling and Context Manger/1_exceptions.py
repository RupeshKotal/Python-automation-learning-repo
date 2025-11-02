numerator = 2
denomentor = 0

try:
    result = numerator/denomentor
    print(f"Result : {result}")

except ZeroDivisionError:
    print(f"Iill handle zero division error")

except Exception as e:

    print(f"error : {e}")

else:
    print(f"I'll run once try block completed")


finally:
    print(f"I'll Run allaways")