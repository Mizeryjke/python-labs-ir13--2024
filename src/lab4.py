class Lamp:
    def __init__(self, type="LED", power=0, led_count=0, fabricator="Unknown"):
        self.__type = type
        self.__power = power
        self.__led_count = led_count
        self.__fabricator = fabricator
        self.warranty_period = 1
        self.color = "White"

    def get_type(self):
        return self.__type

    def get_power(self):
        return self.__power

    def get_led_count(self):
        return self.__led_count

    def get_fabricator(self):
        return self.__fabricator

    def __str__(self):
        return (
            f"Lamp(type={self.__type}, power={self.__power}W, led_count={self.__led_count}, "
            f"fabricator={self.__fabricator}, warranty_period={self.warranty_period}, color={self.color})"
        )

    def __repr__(self):
        return (
            f"Lamp(type='{self.__type}', power={self.__power}, led_count={self.__led_count}, "
            f"fabricator='{self.__fabricator}', warranty_period={self.warranty_period}, color='{self.color}')"
        )

    def __del__(self):
        print(
            f"Lamp object with type '{self.__type}' and fabricator '{self.__fabricator}' is being deleted"
        )


def main():
    lamp1 = Lamp("LED", 60, 10, "Philips")
    lamp2 = Lamp("Halogen", 100, 5, "Osram")
    lamp3 = Lamp("Fluorescent", 40, 8, "GE")

    print(lamp1)
    print(lamp2)
    print(lamp3)


if __name__ == "__main__":
    main()
