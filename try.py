try:
	result = 10/0
except ZeroDivisionError:
	print("Cannot divided by Zero")
except Exception as e:
	print(f"error:{e}")
finally:
	print("Executation Complete")
