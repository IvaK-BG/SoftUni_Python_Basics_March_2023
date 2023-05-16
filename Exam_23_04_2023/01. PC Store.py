cpu_usd = float(input())
gpu_usd = float(input())
ram_usd = float(input())
count_ram = int(input())
discount = float(input())

cpu_bgn = cpu_usd * 1.57
gpu_bgn = gpu_usd * 1.57
ram_bgn = ram_usd * 1.57
cpu_bgn_total = cpu_bgn - (cpu_bgn * discount)
gpu_bgn_total = gpu_bgn - (gpu_bgn * discount)
ram_total = ram_bgn * count_ram
total_price = cpu_bgn_total + gpu_bgn_total + ram_total


print(f"Money needed - {total_price:.2f} leva.")
