class Pig:
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.eye_count = int(eye_count)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def print_characteristics(self):
        print(f"Arm Length:    {self.arm_length:.2f} inches")
        print(f"Leg Length:    {self.leg_length:.2f} inches")
        print(f"Number of Eyes: {self.eye_count}")
        
        tail_status = "Yes" if self.has_tail else "No"
        furry_status = "Yes" if self.is_furry else "No"
        
        print(f"Has a Tail?    {tail_status}")
        print(f"Is it Furry?   {furry_status}")

def main():
    my_pig = Pig(12, 14, 2, True, False)
    my_pig.print_characteristics()

if __name__ == "__main__":
    main()
