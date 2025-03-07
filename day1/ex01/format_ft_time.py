import  time
import  datetime

t_time = time.time()
t_date = datetime.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {t_time:.4f} or {t_time:.2e}  in scientific notation")
print(t_date)