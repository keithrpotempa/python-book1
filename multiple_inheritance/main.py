from flowers import Rose
from flowers import Daisy
from flowers import Alstroemeria
from arrangements import ValentinesDay
from arrangements import MothersDay

if __name__ == "__main__":
  for_beth = ValentinesDay()
  red_rose = Rose("red")
  daisy = Daisy("yellow")
  al = Alstroemeria("rainberws")
  for_beth.enhance(red_rose)
  for_beth.enhance(daisy)
  for_beth.enhance(al)
  for_beth.describe()
  