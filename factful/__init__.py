import random

computerFacts = [
  "Per month almost 6000+ viruses are created...",
  "About 90% of the World’s Currency Only Exists on Computers",
  "The First Computer Mouse was Made of Wood",
  "About 70% of Virus Engineers Work for Organized Crime Syndicates",
  "The First Known Computer Programmer was a Woman",
  "Some of the Biggest Computer Brands Started in Garages",
  "People Blink Less When They Use Computers",
  "More Than 80% of Daily Emails in the U.S. are Spam",
  "MyDoom is the Most Expensive Computer Virus in History",
  "The Parts for the Modern Computer Were First Invented in 1833",
  "The First Gigabyte Drive Cost $40,000",
  "The Case of the First Macintosh Computer Includes 47 Signatures",
  "The Worst U.S. Security Breach of All Time Happened Because of a USB Stick",
  "A Single Computer Catches 50% of all Wikipedia Vandalism",
  "Computers Sort 95% of Mail",
  "MIT Has Computers That can Detect Fake Smiles",
  "Computers Might Soon be Able to Tell What Dogs Think",
  "Russia Engineered a Computer That Ran on Water",
  "Disney Fired John Lasseter for Pushing Computer Animation",
  "Mark Zuckerburg, Owner of Facebook once tried to make a AI in social media and things went out of hand, and Facebook shutdown their AI! Search google for more!"
]

emojiFacts = [
  "For the third year running, the `Face with Tears of Joy`` emoji reigns supreme on social media. It dominates on Twitter and on Facebook as the most-used on both social media platforms. This same symbol was even picked as the Oxford Dictionary's Word of the Year in 2015.",
  "There are now 2,666 official emoji. The Unicode Consortium, the governing body that manages the official emoji keyboard, expanded its offerings dramatically in 2017,thanks to a new array of options in skin tone, gender selection, and professions. There were just 722 as recently as 2015.",
  "The word emoji literally means picture (e) + character (moji) in Japanese.",
  "Emoji were first invented in 1999, but not commonly adopted until 2011. Japan's Shigetaka Kurita first crafted the universal language in preparation for the launch of a mobile internet system called NTT Docomo, with 176 12-pixel-by-12-pixel symbols.",
  "Now, more than 5 billion emoji are sent daily on Facebook Messenger alone. They're also wildly popular on Twitter, which regularly makes custom emoji for events and hashtags, and Instagram, where users can hashtag with emoji. Besides the 'Face with Tears of Joy,' people tend to love the red heart, the heart eyes smiley, and the kissing face smiley across platforms.",
  "Apple has a surprising secret in some of its emoji. In iOS, emoji that feature text in their icon actually use text from Apple's famous 'Think Different' ad campaign. Both the clipboard and book emoji use this text.",
  "Emoji are definitely a young-person's game. Around 86 per cent of emoji users on Twitter are 24 and younger, and 57 per cent of emoji users on Twitter are female.",
  "The Museum of Modern Art owns the original emoji collection.",
  "There is a whole Wikipedia for Emojis named EmojiPedia! You can search it from google!",
  "The most popular emoji used by everyone in the last year is cup of coffee",
  "Unfortunately, the father of emoticons isnt a fan of Emojis ;-;",
  "The Museum of Moder Art owns the original collection of Emojis!",
  "Emoji grew from nothing to this in just some few time!",
  "Per year only 5 to 10 new emojis are added to your phone!",
  "It takes one whole year to accept a emoji to keypad of your mobile! So always care for each emoji!"
]

foodFacts = [
  "Dark chocolate",
  "As sweet as nectar",
  "Raspberries are a member of the rose family",
  "Broccoli contains more protein than steak",
  "Apples give you more energy than coffee",
  "Pecans are rich with antioxidants",
  "Pistachios are actually fruits",
  "Caesar salad originated from a Mexican city",
  "Avocados are fruit",
  "SPAM",
  "Hot dogs",
  "Water",
  "Peanut butter is good for you",
  "Jelly beans",
  "The many uses of cucumbers",
  "Bananas are berries... and strawberries aren&#x27;t!",
  "The stickers on fruit are… edible!",
  "The story of the sandwich",
  "Green, yellow and red capsicums are not the same vegetable",
  "The sticker on fruits says what kind of fruit is it?",
  "Average American Cake has so much sugar which is enough for 1 ant colony to live his whole life",
  "Watermelon consists of 99% of water!",
  "More fibres means more healthy!",
  "Food is simply energy mixed with some tasters"
]

spaceFacts = [
  "Mercury & Venus are the only 2 planets in our solar system that have no moons.",
  "If a star passes too close to a black hole, it can be torn apart.",
  "Enceladus, one of Saturn’s smaller moons, reflects 90% of the Sun’s light.",
  "The Whirlpool Galaxy (M51) was the first celestial object identified as being Spiral Galaxy",
  "A light-year is the distance covered by light in a single year. The Milky Way galaxy is 105,700 light-years wide.",
  "Footprints left on the Moon won’t disappear as there is no wind.",
  "The Martian day is 24 hours 39 minutes and 35 seconds long. Almost Same to Earth.",
  "NASA’s Crater Observation and Sensing Satellite (LCROSS) found evidence of water on the Earth’s Moon.",
  "The Sun makes a full rotation once every 25 – 35 days.",
  "Earth is the only planet not named after a God.",
  "Pluto is smaller than the United States.",
  "According to mathematics, white holes are possible, although as of yet we have found none. SPOILER: White Holes Pushes things way at the speed of Light",
  "There are more volcanoes on Venus than any other planet in our solar system.",
  "Because of its unique tilt, a season on Uranus is equivalent to 21 Earth years. Well Think about Summer Leave in Uranus.",
  "There are more stars in space than there are grains of sand in the world.",
  "Neptune takes nearly 165 Earth years to make one orbit of the Sun. Don't even think about School there.",
  "Pluto’s largest moon, Charon, is half the size of Pluto.",
  "The International Space Station is the largest manned object ever sent into space.",
  "A day on Pluto is lasts for 153.6 hours long.",
  "Any free-moving liquid in outer space will form itself into a sphere.",
  "We know more about Mars and our Moon than we do about our Earth's oceans.",
  "The Black Arrow is the only British satellite to be launched using a British rocket.",
  "Only 5% of the universe is visible from Earth. Others are Dark Matter and Dark Energy which can't be seen becoz they are playing Hide and Seek with us.",
  "Light travels from the Sun to the Earth in less than 10 minutes.",
  "At any given moment, there are at least 2,000 thunderstorms happening on Earth.",
  "The Earth’s rotation is slowing slightly as time goes on.",
  "If you were driving at 75 miles per hour, it would take 258 days to drive around Saturn’s rings.",
  "The International Space Station circles Earth every 92 minutes.",
  "We always see the same side of the Moon, no matter where we stand on Earth.",
  "There are three main types of galaxies: elliptical, spiral & irregular.",
  "There are approximately 100 thousand million stars in the Milky Way.",
  "Using the naked eye, you can see 3 – 7 different galaxies from Earth.",
  "In 2016, scientists detected a radio signal from a source 5 billion light-years away.",
  "The first Supernovae observed outside of our own galaxy was in 1885.",
  "The closest galaxy to us is the Andromeda Galaxy – it’s estimated at 2.5 million light-years away.",
  "The first Supernovae observed outside of our own galaxy was in 1885.",
  "The first ever black hole photographed is 3 million times the size of Earth.",
  "The distance between the Sun & Earth is defined as an Astronomical Unit.",
  "The second man on the moon was Buzz Aldrin. “Moon” was Aldrin’s mother’s maiden name.",
  "Astronaut Buzz Aldrin’s birth name was Edwin Eugene Aldrin Jr.",
  "On Venus, it snows metal and rains sulfuric acid.",
  "The Mariner 10 was the first spacecraft that visited Mercury in 1974.",
  "Space is completely silent like a Library.",
  "Coca-Cola was the first commercial soft drink that was ever consumed in space. No need to worry about Drinks in Space.",
  "Astronauts can grow approximately two inches (5 cm) in height when in space due to low Gravity.",
  "The first woman in space was a Russian called Valentina Tereshkova.",
  "The Kuiper Belt is a region of the Solar System beyond the orbit of Neptune.",
  "If Saturn’s rings were 3 feet long, they would be 10,000 times thinner than a razorblade.",
  "The Hubble Space Telescope is one of the most productive scientific instruments ever built.",
  "The first artificial satellite in space was called “Sputnik”.",
  "Exoplanets are planets that orbit around other stars.",
  "The center of the Milky Way smells like rum & tastes like raspberries.",
  "Our moon is moving away from Earth at a rate of 1.6 inch (4 cm) per year!",
  "Pluto is named after the Roman god of the underworld, not the Disney Dog.",
  "Spacesuit helmets have a Velcro patch, to help astronauts itch.",
  "The ISS is visible to more than 90% of the Earth’s population.",
  "Saturn is the only planet that could float in water due to its low Density",
  "Asteroids are the byproducts of formations in the solar system, more than 4 billion years ago.",
  "Astronauts can’t burp in space.",
  "Uranus was originally called “George’s Star”.",
  "A sunset on Mars is blue.",
  "The Earth weighs about 81 times more than the Moon.",
  "The first living mammal to go into space was a dog named “Laika” from Russia.",
  "The word “astronaut” means “star sailor” in its origins.",
  "“NASA” stands for National Aeronautics and Space Administration.",
  "ISRO is in 4th Position in Space and Technology",
  "The Fact is I don't have a Fact",
  "Gennady Padalka has spent more time in space than anyone else.",
  "Mercury has no atmosphere, which means there is no wind or weather.",
  "In China, the Milky Way is known as the “Silver River”.",
  "Red Dwarf stars that are low in mass can burn continually for up to 10 trillion years!",
  "Scientists once believed that the same side of Mercury always faced the Sun.",
  "Jupiter’s Red Spot is shrinking.",
  "A large percentage of asteroids are pulled in by Jupiter’s gravity.",
  "A day on Mercury is equivalent to 58 Earth days.",
  "As space has no gravity, pens won’t work.",
  "Buzz Lightyear from Toy Story has actually been to outer space!",
  "There is a planet half the radius of the Earth with a surface made up of diamonds. Find it in Google.",
  "Halley’s Comet will pass over Earth again on 26th July 2061.",
  "Mars is the most likely planet in our solar system to be hospitable to life.",
  "There are 5 Dwarf Planets recognized in our Solar System.",
  "In 2006, the International Astronomical Union reclassified Pluto as a dwarf planet.",
  "As early as 240BC the Chinese began to document the appearance of Halley’s Comet.",
  "The center of a comet is called a “nucleus”.",
  "There are 88 recognized star constellations in our night sky.",
  "On average it takes the light only 1.3 seconds to travel from the Moon to Earth.",
  "As space has no gravity, pens won’t work.",
]

choice = random.choice

def facts():
  all = [
    choice(computerFacts),
    choice(emojiFacts),
    choice(foodFacts),
    choice(spaceFacts)
  ]

  return {
    "all": choice(all),
    "computer": choice(computerFacts),
    "emoji": choice(emojiFacts),
    "food": choice(foodFacts),
    "space": choice(spaceFacts)
  }

PACKAGE = 'factful'
__version__ = '0.0.7'