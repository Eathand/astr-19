import math

def main():
    num_points = 1000
    x_start = 0.0
    x_end = 2.0

    step = (x_end - x_start) / (num_points - 1)

    print("x\t\tsin(x)")
    print("------------------------")

    for i in range(num_points):
        x = x_start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t{y:.6f}")


if __name__ == "__main__":
    main()