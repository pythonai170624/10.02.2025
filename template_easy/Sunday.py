from template_easy.DailyRoutine import DailyRoutine


class Sunday(DailyRoutine):

    def follow_routine(self):
        """Template method defining the structure of the day."""
        self.wake_up()
        self.shower()
        self.go_to_work()
        self.eat()
        self.have_fun()
        self.sleep()

    """Sunday routine: Relax and enjoy the weekend."""
    def eat(self):
        print("Eating stakes with fries")

    def wake_up(self):
        super().wake_up()
        print('sunday morning ! fun day ...')

    def go_to_work(self):
        print("No work today! Staying in pajamas all day. 🛌😎")

    def have_fun(self):
        print("Having a beer and watching Netflix! 🍺📺")

class Sunday4weeks(Sunday):

    def have_fun(self):
        print("Going for a nature view trip ...")

class Monday(DailyRoutine):
    """Monday routine: Start the work week."""

    def eat(self):
        print("Eating Sushi with Eliya ")

    def go_to_work(self):
        print("Going to work... Ugh, it's Monday. ☕😩")

    def have_fun(self):
        print("Too tired to have fun. Just scrolling through social media. 📱💀")
