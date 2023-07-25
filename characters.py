# Website used to generate the ASCII art:
# https://ascii-generator.site/

class Bocchi:
    """Class for Bocchi ASCII art."""

    def normal(self):
        """Her normal self."""
        with open("characters raw/bocchi/normal.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def happy(self):
        """When she is happy."""
        with open("characters raw/bocchi/happy.txt", "r") as file:
            return "\n" * 8 + file.read()

class Nijika:
    """Class for Nijika ASCII art."""

    def normal(self):
        """Her normal self."""
        with open("characters raw/nijika/normal.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def happy(self):
        """When she is happy."""
        with open("characters raw/nijika/happy.txt", "r") as file:
            return "\n" * 8 + file.read()

class Ryo:
  def normal(self):
    """Her normal self."""
    with open("characters raw/ryo/normal.txt", "r") as file:
        return "\n" * 8 + file.read()

class Kita:
    def normal(self):
        """Her normal self."""
        with open("characters raw/kita/normal.txt", "r") as file:
            return "\n" * 8 + file.read()
    def happy(self):
        """When she is happy."""
        with open("characters raw/kita/happy.txt", "r") as file:
            return "\n" * 8 + file.read()


class Blank:
    """A class for the frames that are mostly blank."""

    def blank(self):
        """Returns an empty frame."""
        with open("characters raw/blank.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def inc_call(self):
        """Returns a frame with 'BRRRRIINGGG' text in the middle."""
        with open("characters raw/inc_call.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def calling(self):
        """Returns a frame with a calling symbol in the middle."""
        with open("characters raw/calling.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def exclaim(self):
        """Returns a frame with an exclamation mark in the middle."""
        with open("characters raw/exclaim.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def ty_for_playing(self):
        """Returns a wider frame of Bocchi."""
        with open("characters raw/ty_for_playing.txt", "r") as file:
            return "\n" * 8 + file.read()

class Loading:
    """The class for loading frames."""

    def one(self):
        """Returns the loading frame with one dot."""
        with open("characters raw/loading/loading1.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def two(self):
       """Returns the loading frame with two dots."""
       with open("characters raw/loading/loading2.txt", "r") as file:
            return "\n" * 8 + file.read()
       
    def three(self):
       """Returns the loading frame with three dots."""
       with open("characters raw/loading/loading3.txt", "r") as file:
            return "\n" * 8 + file.read()

class Rooms:
    """The class for the various rooms and clues."""

    def room1(self):
       """Bocchi's room's floor plan."""
       with open("characters raw/rooms/room1.txt", "r") as file:
            return "\n" * 8 + file.read()
       
    def room1_lyrics(self):
       """The lyrics that Bocchi ends up writing in middle school."""
       with open("characters raw/rooms/room1_bocchi_lyrics.txt", "r") as file:
            return "\n" * 8 + file.read()
       
    def room2(self):
       """The floor plan for the alley way."""
       with open("characters raw/rooms/room2.txt", "r") as file:
            return "\n" * 8 + file.read()

    def room2_clue1(self):
       """The 1st clue for room 2."""
       with open("characters raw/rooms/room2_clue1.txt", "r") as file:
            return "\n" * 8 + file.read()
       
    def room2_clue2(self):
        """The 2nd clue for room 2."""
        with open("characters raw/rooms/room2_clue2.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def room3(self):
        """The 'floor plan' for the 3rd room."""
        with open("characters raw/rooms/room3.txt", "r") as file:
            return "\n" * 8 + file.read()
        
    def room3_clue1(self):
        """The big sign that says 'STARRY'."""
        with open("characters raw/rooms/room3_clue1.txt", "r") as file:
            return "\n" * 8 + file.read()
    
    # Note that there isn't a room 4 here because the fourth room is less of an actual "room"
    # Bocchi is trapped inside a more of a conceptual room; she can't really play until the player helps her.