import geometry_utils


def run_calculator():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    operation = input("Enter the operation you want to perform: ").strip().lower()

    functions = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    try:
        if operation == "circle_area" or operation == "circle_perimeter":
            r = float(input("Enter radius: "))
            result = functions[operation](r)

        elif operation == "rectangle_area" or operation == "rectangle_perimeter":
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = functions[operation](w, h)

        elif operation == "triangle_area":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = functions[operation](b, h)

        else:
            print("Invalid operation!")
            return

        print(f"Result: {result:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except KeyError:
        print("Error: The operation you entered is not available.")


if __name__ == "__main__":
    run_calculator()