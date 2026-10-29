from MyPackage import arithmetic, geometry


def main():
    sum_result = arithmetic.add(10, 5)
    diff_result = arithmetic.subtract(10, 5)
    area = geometry.area_of_circle(7)
    perimeter = geometry.perimeter_of_circle(7)

    print("Sum:", sum_result)
    print("Difference:", diff_result)
    print(f"Area of Circle: {area:.2f}")
    print(f"Perimeter of Circle: {perimeter:.2f}")


if __name__ == "__main__":
    main()
