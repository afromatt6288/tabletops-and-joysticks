#!/usr/bin/env python3

import datetime
from random import randint, choice as rc
from faker import Faker
from faker.providers.internet import *
from app import app
from models import db, User, Game, Inventory, Swap, Message, Review, Chat_Room, Chat_Message

fake = Faker()

with app.app_context():

    print("Deleting User data...")
    User.query.delete()
    print("Deleting Game data...")
    Game.query.delete()
    print("Deleting Inventory data...")
    Inventory.query.delete()
    print("Deleting Swap data...")
    Swap.query.delete()
    print("Deleting Message data...")
    Message.query.delete()
    print("Deleting Review data...")
    Review.query.delete()
    print("Deleting Chat_Room data...")
    Chat_Room.query.delete()
    print("Deleting Chat_Message data...")
    Chat_Message.query.delete()
    
##########################################################

    print("Creating User data...")
    new_user_1 = User(username="Admin", email="Admin@flatironschool.com", address="2228 Blake St. Denver, CO 80205", avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
    # avatar_blob="TBD", 
    stars=3, travel_distance=5, is_active = False, is_admin=True)
    new_user_1.password_hash = "Admin"
    new_user_2 = User(username="Matthew", email="Matthew@flatironschool.com", address="2228 Blake St. Denver, CO 80205", avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
    # avatar_blob="TBD", 
    stars=5, travel_distance=25, is_active = False, is_admin=True)
    new_user_2.password_hash = "Matthew" 
    new_user_3 = User(username="Preston", email="Preston@flatironschool.com", address="2282 Blake St. Denver, CO 80205", avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
    # avatar_blob="TBD", 
    stars=3, travel_distance=5, is_active = False, is_admin=False)
    new_user_3.password_hash = "Preston"
    new_user_4 = User(username="Dylan", email="Dylan@flatironschool.com", address="2822 Blake St. Denver, CO 80205", avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
    # avatar_blob="TBD", 
    stars=3, travel_distance=5, is_active = False, is_admin=False)
    new_user_4.password_hash = "Dylan"
    new_user_5 = User(username="Sarah", email="Sarah@flatironschool.com", address="8222 Blake St. Denver, CO 80205", avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
    # avatar_blob="TBD", 
    stars=3, travel_distance=5, is_active = False, is_admin=False)
    new_user_5.password_hash = "Sarah"
    users = [new_user_1,new_user_2,new_user_3,new_user_4,new_user_5]
    usernames = ['Admin', 'Matthew', 'Preston', 'Dylan', 'Sarah']
    for n in range(20):
        username=fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)
        password = username
        new_user = User(username=username, email=fake.email(), address=fake.address(), avatar_url='https://cdn-icons-png.flaticon.com/512/8053/8053055.png', 
            # avatar_blob="TBD", 
            stars=3, travel_distance=5, is_active = False, is_admin=False)
        new_user.password_hash = password
        users.append(new_user)
    print('Adding User objects...')
    db.session.add_all(users)
    db.session.commit()

##########################################################

    print("Creating Game data...")
    games = [
        Game(title='Settlers of Catan', type='Board Games', genres='Trading, Resource Management', platforms='Tabletop', player_num_min=3, player_num_max=4, image_url='https://example.com/settlers-of-catan.jpg', description='Settlers of Catan is a popular strategy board game where players build settlements and trade resources to become the dominant civilization.'),
        Game(title='Risk', type='Board Games', genres='War, Dice Rolling', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/risk.jpg', description='Risk is a classic war board game where players conquer territories and engage in battles to become the dominant world power.'),
        Game(title='Scrabble', type='Board Games', genres='Word, Tile Placement', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/scrabble.jpg', description='Scrabble is a popular word board game where players create words using letter tiles and score points based on the letters used and the placement of their words on the board.'),
        Game(title='Monopoly', type='Board Games', genres='Economic, Trading', platforms='Tabletop, Digital', player_num_min=2, player_num_max=8, image_url='https://example.com/monopoly.jpg', description='Monopoly is a classic economic board game where players buy, sell, and trade properties and businesses to become the wealthiest player.'),
        Game(title='Pandemic', type='Board Games', genres='Cooperative, Strategy', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/pandemic.jpg', description='Pandemic is a cooperative board game where players work together to stop the spread of infectious diseases around the world.'),
        Game(title='Azul', type='Board Games', genres='Abstract, Tile Placement', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/azul.jpg', description='Azul is an abstract board game where players compete to decorate the walls of a royal palace with beautiful tiles.'),
        Game(title='Codenames', type='Board Games', genres='Word, Party', platforms='Tabletop, Digital', player_num_min=2, player_num_max=8, image_url='https://example.com/codenames.jpg', description='Codenames is a party game where players work in teams to guess the identities of secret agents based on one-word clues given by a spymaster.'),
        Game(title='Betrayal at Baldur\'s Gate', type='Board Games', genres='Horror, Adventure', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/betrayal-at-baldurs-gate.jpg', description='Betrayal at Baldur\'s Gate is a horror board game where players explore a haunted city and uncover the dark secrets hidden within.'),
        Game(title='Splendor', type='Board Games', genres='Economic, Card Drafting', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/splendor.jpg', description='Splendor is an economic board game where players collect gems and use them to purchase cards that grant them points and special abilities.'),
        Game(title='Twilight Imperium', type='Board Games', genres='Strategy, Epic', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/twilight-imperium.jpg', description='Twilight Imperium is an epic sci-fi board game where players lead their civilizations in a quest for galactic domination through politics, diplomacy, and warfare.'),
        Game(title='Carcassonne', type='Board Games', genres='Strategy, Medieval', platforms='Tabletop, Digital', player_num_min=2, player_num_max=5, image_url='https://example.com/carcassonne.jpg', description='Carcassonne is a tile-based board game where players build a medieval landscape and score points by claiming cities, roads, and farms.'),
        Game(title='Dead of Winter', type='Board Games', genres='Cooperative, Horror, Survival', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/dead-of-winter.jpg', description='Dead of Winter is a horror board game where players work together to survive a zombie apocalypse while dealing with traitors and personal objectives.'),
        Game(title='Dominion', type='Card Games', genres='Strategy, Card Drafting', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/dominion.jpg', description='Dominion is a deck-building board game where players build their own decks of cards and use them to gain victory points and outscore their opponents.'),
        Game(title='Gloomhaven', type='Board Games', genres='Adventure, Campaign, Fantasy', platforms='Tabletop, Digital', player_num_min=1, player_num_max=4, image_url='https://example.com/gloomhaven.jpg', description='Gloomhaven is an adventure board game where players embark on a campaign to save a fantasy world, battling monsters and discovering treasures along the way.'),
        Game(title='King of Tokyo', type='Board Games', genres='Party, Battle, Dice Rolling', platforms='Tabletop, Digital', player_num_min=2, player_num_max=6, image_url='https://example.com/king-of-tokyo.jpg', description='King of Tokyo is a party game where players take on the roles of giant monsters and battle for control of Tokyo, rolling dice to attack and heal.'),
        Game(title='Ticket to Ride', type='Board Games', genres='Strategy, Trains, Route Building', platforms='Tabletop, Digital', player_num_min=2, player_num_max=5, image_url='https://example.com/ticket-to-ride.jpg', description='Ticket to Ride is a route-building board game where players collect and play matching train cards to claim railway routes and connect cities.'),
        Game(title='Scythe', type='Board Games', genres='Strategy, Alternate History, Engine Building', platforms='Tabletop, Digital', player_num_min=1, player_num_max=5, image_url='https://example.com/scythe.jpg', description='Scythe is a strategy board game set in an alternate-history 1920s Europe, where players build their factions and gather resources to expand their territories and gain power.'),
        Game(title='7 Wonders', type='Card Games', genres='Civilization, Drafting', platforms='Tabletop, Digital', player_num_min=2, player_num_max=7, image_url='https://example.com/7-wonders.jpg', description='7 Wonders is a card-based board game where players lead one of seven ancient civilizations and compete to build the most impressive city across three ages.'),
        Game(title='Mansions of Madness', type='Board Games', genres='Horror, Cooperative, Investigation', platforms='Tabletop', player_num_min=1, player_num_max=5, image_url='https://example.com/mansions-of-madness.jpg', description='Mansions of Madness is a horror board game where players investigate supernatural mysteries and fight monsters in a haunted mansion, using an app to control the game.'),
        Game(title='Terraforming Mars', type='Board Games', genres='Strategy, Science Fiction, Engine Building', platforms='Tabletop, Digital', player_num_min=1, player_num_max=5, image_url='https://example.com/terraforming-mars.jpg', description='Terraforming Mars is a strategy game where players take on the role of corporations and compete to terraform the planet Mars, using resources and technology to raise the planet\'s temperature, oxygen level, and ocean coverage.'),
        Game(title='Through the Ages', type='Tabletop', genres='Civilization, Card Game, Strategy', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/through-the-ages.jpg', description='Through the Ages is a civilization-building game where players lead their nations from antiquity to modern times, managing resources, developing technologies, and waging wars to become the greatest civilization in history.'),
        Game(title='Deadwood 1876', type='Card Games', genres='Deduction, Western', platforms='Tabletop', player_num_min=2, player_num_max=9, image_url='https://example.com/deadwood-1876.jpg', description='Deadwood 1876 is a card game where players take on the roles of famous cowboys and outlaws in the wild west, engaging in shootouts and trying to be the last one standing.'),
        Game(title='Forbidden Island', type='Tabletop', genres='Adventure, Cooperative, Exploration', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/forbidden-island.jpg', description='Forbidden Island is a cooperative board game where players work together to collect treasures and escape from a sinking island before it\'s too late.'),
        Game(title='Dominant Species', type='Tabletop', genres='Area Control, Evolution, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/dominant-species.jpg', description='Dominant Species is a strategy board game where players lead their animal species in a fight for survival and dominance, adapting to changing environmental conditions and outcompeting other species for resources.'),
        Game(title='Root', type='Strategy', genres='Asymmetric, War', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/root.jpg', description='Root is an asymmetric strategy game where players take on different roles with unique abilities, competing for control of a forest and its resources.'),
        Game(title='Arkham Horror: The Card Game', type='Card Games', genres='Horror, Adventure, Deck Building', platforms='Tabletop, Digital', player_num_min=1, player_num_max=4, image_url='https://example.com/arkham-horror-card-game.jpg', description='Arkham Horror: The Card Game is a horror-themed card game where players take on the roles of investigators, fighting monsters and uncovering the mysteries of Lovecraftian horror.'),
        Game(title='Agricola', type='Strategy', genres='Farming, Worker Placement', platforms='Tabletop, Digital', player_num_min=1, player_num_max=5, image_url='https://example.com/agricola.jpg', description='Agricola is a farming strategy board game where players manage their own farms and families, raising animals, growing crops, and renovating their homes to earn points.'),
        Game(title='The Resistance', type='Social Deduction', genres='Party, Espionage', platforms='Tabletop', player_num_min=5, player_num_max=10, image_url='https://example.com/the-resistance.jpg', description='The Resistance is a social deduction party game where players take on the roles of resistance fighters or spies, trying to outmaneuver each other and complete missions in a dystopian future.'),
        Game(title='Photosynthesis', type='Board Games', genres='Abstract, Nature', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/photosynthesis.jpg', description='Photosynthesis is an abstract strategy board game where players grow and harvest trees, using the sun\'s energy to score points and outcompete their opponents.'),
        Game(title='Gloom', type='Card Games', genres='Horror, Storytelling', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/gloom.jpg', description='Gloom is a storytelling card game where players control a family of misfits, trying to make them as miserable as possible before killing them off.'),
        Game(title='Spyfall', type='Party Games', genres='Deduction, Social Deduction', platforms='Tabletop', player_num_min=3, player_num_max=8, image_url='https://example.com/spyfall.jpg', description='Spyfall is a party game where players are all given a location except for one spy, who has to figure out where they are based on the conversation.'),
        Game(title='Onitama', type='Board Games', genres='Strategy, Abstract', platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/onitama.jpg', description='Onitama is an abstract strategy game where players move their pieces around the board, trying to capture their opponent\'s pieces or move their own to their opponent\'s temple.'),
        Game(title='Love Letter', type='Card Games', genres='Deduction, Card Game', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/love-letter.jpg', description='Love Letter is a card game where players try to deliver a love letter to the princess while avoiding the other players trying to intercept it.'),
        Game(title='Santorini', type='Board Games', genres='Abstract, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/santorini.jpg', description='Santorini is an abstract strategy game where players build a beautiful island while trying to outmaneuver their opponent and reach the top of a tower.'),
        Game(title='Sheriff of Nottingham', type='Board Games', genres='Deduction, Bluffing', platforms='Tabletop', player_num_min=3, player_num_max=5, image_url='https://example.com/sheriff-of-nottingham.jpg', description='Sheriff of Nottingham is a game of bluffing and deception, where players take turns being the sheriff and inspecting each other\'s bags of goods to see who is telling the truth.'),
        Game(title='The Mind', type='Card Games', genres='Cooperative, Deduction', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/the-mind.jpg', description='The Mind is a cooperative card game where players try to play their cards in ascending order without communicating.'),
        Game(title='Ticket to Ride: Europe', type='Board Games', genres='Strategy, Route Building', platforms='Tabletop, Digital', player_num_min=2, player_num_max=5, image_url='https://example.com/ticket-to-ride-europe.jpg', description='Ticket to Ride: Europe is a strategy board game where players build train routes across Europe, trying to connect different cities and complete their secret routes before their opponents do.'),
        Game(title='Sushi Go!', type='Card Games', genres='Drafting, Set Collection', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/sushi-go.jpg', description='Sushi Go! is a card drafting game where players try to collect the best combinations of sushi cards for points.'),
        Game(title='Hanabi', type='Card Games', genres='Cooperative, Deduction', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/hanabi.jpg', description='Hanabi is a cooperative card game where players work together to create the perfect fireworks show, without being able to see their own cards.'),
        Game(title='Blokus', type='Board Games', genres='Abstract, Strategy', platforms='Tabletop, Mobile Games', player_num_min=2, player_num_max=4, image_url='https://example.com/blokus.jpg', description='Blokus is an abstract strategy game where players take turns placing their colored pieces on a board, attempting to cover as much space as possible while blocking their opponents.'),
        Game(title='Munchkin', type='Card Games', genres='Fantasy, Role-playing', platforms='Tabletop, Digital', player_num_min=3, player_num_max=6, image_url='https://example.com/munchkin.jpg', description='Munchkin is a humorous card game where players play as characters exploring a dungeon, trying to gain levels and defeat monsters to become the ultimate hero.'),
        Game(title='Dixit', type='Party Games', genres='Abstract, Deduction', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/dixit.jpg', description='Dixit is a party game where players take turns being the storyteller, creating a sentence or phrase that describes one of their cards. Other players then choose a card from their hand that matches the sentence, and the group tries to guess which card was the storyteller\'s.'),
        Game(title='Wavelength', type='Party Games', genres='Deduction, Social Deduction', platforms='Tabletop', player_num_min=2, player_num_max=20, image_url='https://example.com/wavelength.jpg', description='Wavelength is a party game where players take turns giving clues to help their team guess a range on a spectrum. The catch is that the clue giver can only give a single word, and their team has to figure out where on the spectrum that word falls.'),
        Game(title='Betrayal Legacy', type='Board Games', genres='Horror, Campaign', platforms='Tabletop', player_num_min=3, player_num_max=5, image_url='https://example.com/betrayal-legacy.jpg', description='Betrayal Legacy is a horror-themed board game where players play through a campaign, uncovering the dark secrets of a haunted house. The twist is that halfway through the campaign, one of the players becomes the traitor, and the game changes drastically.'),
        Game(title='Dominion: Intrigue', type='Deck Building', genres='Strategy, Card Game', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/dominion-intrigue.jpg', description='Dominion: Intrigue is a deck-building game where players start with a small deck of cards and gradually add more powerful cards to it over the course of the game. Players compete to have the most victory points at the end of the game.'),
        Game(title='Hive', type='Board Games', genres='Abstract, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/hive.jpg', description='Hive is an abstract strategy game where players take turns placing hexagonal tiles representing different insects on a board, with the goal of surrounding their opponent\'s queen bee.'),
        Game(title='Terra Mystica', type='Board Games', genres='Fantasy, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/terra-mystica.jpg', description='Terra Mystica is a strategy game where players represent different fantasy races trying to terraform and expand their own territories while limiting others.'),
        Game(title='Lovecraft Letter', type='Card Games', genres='Horror, Deduction', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/lovecraft-letter.jpg', description='Lovecraft Letter is a card game based on the classic game Love Letter, with added elements of horror and deduction as players try to survive in a world inspired by the works of H.P. Lovecraft.'),
        Game(title='Gloomhaven: Jaws of the Lion', type='Board Games', genres='Fantasy, Adventure', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/gloomhaven-jaws-of-the-lion.jpg', description='Gloomhaven: Jaws of the Lion is a standalone game in the Gloomhaven series, featuring a new storyline and beginner-friendly rules for players to experience the world of Gloomhaven.'),
        Game(title='Ticket to Ride: Nordic Countries', type='Board Games', genres='Strategy, Route Building', platforms='Tabletop, Digital', player_num_min=2, player_num_max=3, image_url='https://example.com/ticket-to-ride-nordic-countries.jpg', description='Ticket to Ride: Nordic Countries is a variant of the popular Ticket to Ride game, set in the Nordic countries of Europe and featuring unique gameplay elements.'),
        Game(title='Dungeons & Dragons', type='Tabletop Role-playing Games', genres='Fantasy, Role-playing', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/dungeons-and-dragons.jpg', description='Dungeons & Dragons is a classic tabletop role-playing game where players create their own characters and embark on epic adventures in a world of swords and sorcery.'),
        Game(title='Rising Sun', type='Board Games', genres='Strategy, Battle', platforms='Tabletop', player_num_min=3, player_num_max=5, image_url='https://example.com/rising-sun.jpg', description='Rising Sun is a game of politics and war set in feudal Japan, where players lead their clans to victory by mastering the arts of negotiation, combat, and diplomacy.'),
        Game(title='Gwent: The Witcher Card Game', type='Card Games', genres='Fantasy, Strategy', platforms='Mobile Games, PC, PlayStation, Xbox', player_num_min=2, player_num_max=2, image_url='https://example.com/gwent.jpg', description='Gwent: The Witcher Card Game is a digital card game set in the world of The Witcher, where players collect and use cards featuring characters, spells, and artifacts from the popular fantasy series.'),
        Game(title='The Castles of Burgundy', type='Board Games', genres='Dice Rolling, Strategy', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/castles-of-burgundy.jpg', description='In The Castles of Burgundy, players take on the roles of medieval princes competing to build the most prosperous and well-fortified estates in the region.'),
        Game(title='Blood Rage', type='Board Games', genres='Strategy, Miniature, Fantasy', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/blood-rage.jpg', description='Blood Rage is a Viking-themed strategy game where players control rival clans vying for control of the mythical land of Yggdrasil.'),
        Game(title='Sagrada', type='Board Games', genres='Dice Rolling, Puzzle', platforms='Tabletop, Digital', player_num_min=1, player_num_max=4, image_url='https://example.com/sagrada.jpg', description='Sagrada is a game of stained glass window crafting where players draft colorful dice and strategically place them on their personal player boards.'),
        Game(title='Spirit Island', type='Board Games', genres='Cooperative, Strategy, Fantasy', platforms='Tabletop, Digital', player_num_min=1, player_num_max=4, image_url='https://example.com/spirit-island.jpg', description='In Spirit Island, players take on the roles of powerful spirits defending their island home from invading colonizers.'),
        Game(title='Betrayal at House on the Hill', type='Board Games', genres='Horror, Adventure, Cooperative', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/betrayal-at-house-on-the-hill.jpg', description='Betrayal at House on the Hill is a spooky cooperative game where players explore a haunted house and uncover the secrets lurking within.'),
        Game(title='One Night Ultimate Werewolf', type='Party Games', genres='Social Deduction, Fantasy', platforms='Tabletop', player_num_min=3, player_num_max=10, image_url='https://example.com/one-night-ultimate-werewolf.jpg', description='One Night Ultimate Werewolf is a fast-paced social deduction game where players take on the roles of villagers trying to identify the werewolves among them.'),
        Game(title='Lords of Waterdeep', type='Board Games', genres='Worker Placement, Fantasy', platforms='Tabletop, Digital', player_num_min=2, player_num_max=5, image_url='https://example.com/lords-of-waterdeep.jpg', description='Lords of Waterdeep is a game of political intrigue and economic manipulation set in the Dungeons & Dragons universe.'),
        Game(title='Gloomhaven: Forgotten Circles', type='Board Games', genres='Adventure, Fantasy, Fighting', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/gloomhaven-forgotten-circles.jpg', description='Gloomhaven: Forgotten Circles is the first expansion for Gloomhaven that adds twenty new scenarios and more than twenty new enemies. It also includes new character classes and a new boss monster, the Aesther Diviner.'),
        Game(title='Machi Koro', type='Board Games', genres='City-building, Dice Rolling', platforms='Tabletop, Mobile Games', player_num_min=2, player_num_max=4, image_url='https://example.com/machi-koro.jpg', description='Machi Koro is a fast-paced city-building game where players roll dice to collect coins and purchase buildings that earn income. The first player to build all of their landmarks wins the game.'),
        Game(title='Mysterium', type='Board Games', genres='Cooperative, Deduction', platforms='Tabletop, Digital', player_num_min=2, player_num_max=7, image_url='https://example.com/mysterium.jpg', description='Mysterium is a cooperative deduction game where players work together to solve the mystery of a ghost\'s murder. One player plays as the ghost and can only communicate with the other players through visions.'),
        Game(title='Race for the Galaxy', type='Card Games', genres='Strategy, Science Fiction', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/race-for-the-galaxy.jpg', description='Race for the Galaxy is a fast-paced card game where players build their own galactic civilizations by playing cards that represent different technologies and developments.'),
        Game(title='Secret Hitler', type='Party Games', genres='Social Deduction , Politics', platforms='Tabletop', player_num_min=5, player_num_max=10, image_url='https://example.com/secret-hitler.jpg', description='Secret Hitler is a social deduction game where players try to figure out who among them is the secret Hitler. Players take turns passing laws that may or may not benefit Hitler, and the game ends when either Hitler is elected Chancellor or the Liberals pass enough laws to win.'),
        Game(title='Talisman', type='Board Games', genres='Adventure, Fantasy, Role-playing', platforms='Tabletop, Digital', player_num_min=2, player_num_max=6, image_url='https://example.com/talisman.jpg', description='Talisman is a fantasy adventure game where players journey through a magical realm to reach the Crown of Command and claim ultimate power. Along the way, players must defeat monsters, collect treasure, and gain experience points to level up their characters.'),
        Game(title='The Crew: The Quest for Planet Nine', type='Card Games', genres='Cooperative, Trick-taking', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/the-crew.jpg', description='The Crew: The Quest for Planet Nine is a cooperative trick-taking game where players work together to complete missions and reach the mysterious Planet Nine. Each mission has specific tasks that must be completed, and players must strategize and communicate to win the game.'),
        Game(title='Viticulture', type='Board Games', genres='Strategy, Worker Placement', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/viticulture.jpg', description='Viticulture is a game about running a vineyard and making wine. Players plant vines, harvest grapes, make wine, and sell their product to gain victory points.'),
        Game(title='Tzolk\'in: The Mayan Calendar', type='Board Games', genres='Strategy, Worker Placement', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/tzolkin.jpg', description='Tzolk\'in is a game where players place workers on a rotating gear to take actions and gain resources. As the game progresses, the gear rotates and the value of the actions change.'),
        Game(title='Escape Room: The Game', type='Escape Room', genres='Puzzle', platforms='Tabletop', player_num_min=3, player_num_max=5, image_url='https://example.com/escape-room-the-game.jpg', description='Escape Room: The Game is a boxed escape room game where players must solve puzzles and riddles to escape from a locked room before time runs out.'),
        Game(title='Just Dance 2022', type='Video Games', genres='Music', platforms='Nintendo Switch, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S', player_num_min=1, player_num_max=6, image_url='https://example.com/just-dance-2022.jpg', description='Just Dance 2022 is a rhythm game where players dance along to popular songs and try to match the movements of the on-screen characters. The game can be played with a smartphone app or a motion controller.'),
        Game(title='Ticket to Ride: London', type='Board Games', genres='Family, Route Building', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/ticket-to-ride-london.jpg', description='Ticket to Ride: London is a quick and easy-to-learn version of the popular Ticket to Ride game, set in the bustling city of London.'),
        Game(title='Clank! In! Space!', type='Deck Building', genres='Adventure, Sci-Fi', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/clank-in-space.jpg', description='Clank! In! Space! is a deck-building board game where players take on the role of thieves breaking into a space station to steal valuable artifacts.'),
        Game(title='Aeon\'s End: Legacy', type='Deck Building', genres='Fantasy, Cooperative', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/aeons-end-legacy.jpg', description='Aeon\'s End: Legacy is a deck-building game that tells a unique story with each playthrough, as players work together to defend their city from a horde of powerful monsters.'),
        Game(title='Coup', type='Card Games', genres='Bluffing, Deduction', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/coup.jpg', description='Coup is a fast-paced card game of deduction and bluffing, where players take on the roles of powerful figures in a dystopian society and attempt to eliminate their opponents.'),
        Game(title='Kingdomino', type='Board Games', genres='Abstract, Tile Placement', platforms='Tabletop, Digital', player_num_min=2, player_num_max=4, image_url='https://example.com/kingdomino.jpg', description='Kingdomino is a family-friendly board game where players build their own kingdoms by strategically placing domino-like tiles with different terrain types.'),
        Game(title='Dead Man\'s Cabal', type='Board Games', genres='Fantasy, Worker Placement', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/dead-mans-cabal.jpg', description='Dead Man\'s Cabal is a worker placement game where players take on the role of necromancers trying to raise the most powerful army of undead.'),
        Game(title='Catan: Starfarers', type='Board Games', genres='Science Fiction, Strategy', platforms='Tabletop', player_num_min=3, player_num_max=4, image_url='https://example.com/catan-starfarers.jpg', description='Catan: Starfarers is a board game where players explore and settle new planets while managing resources and building infrastructure to become the dominant civilization in the galaxy.'),
        Game(title='Werewolf', type='Social Deduction ', genres='Party', platforms='Tabletop', player_num_min=7, player_num_max=75, image_url='https://example.com/werewolf.jpg', description='Werewolf is a party game where players take on the roles of villagers and werewolves in a battle for survival.'),
        Game(title='Super Mario Party', type='Party Games', genres='Platformer, Mini-games', platforms='Nintendo Switch', player_num_min=1, player_num_max=4, image_url='https://example.com/super-mario-party.jpg', description='Super Mario Party is a party game where players compete in various mini-games and challenges using characters from the Mario franchise.'),
        Game(title='Magic: The Gathering Arena', type='Trading Card', genres='Strategy, Fantasy', platforms='PC, Mac', player_num_min=1, player_num_max=2, image_url='https://example.com/magic-the-gathering-arena.jpg', description='Magic: The Gathering Arena is a digital version of the popular trading card game, allowing players to build and customize their own decks and compete against others online.'),
        Game(title='Civilization VI', type='Strategy', genres='City-building, Civilization', platforms='PC, Nintendo Switch', player_num_min=1, player_num_max=12, image_url='https://example.com/civilization-vi.jpg', description='Civilization VI is a turn-based strategy game where players lead their civilizations through history, building cities, managing resources, and waging wars.'),
        Game(title='Red Dead Redemption 2', type='Video Games', genres='Western, Action', platforms='PlayStation 4, Xbox One, PC', player_num_min=1, player_num_max=32, image_url='https://example.com/red-dead-redemption-2.jpg', description='Red Dead Redemption 2 is an open-world action game set in the Wild West, where players take on the role of an outlaw and navigate the dangers of the frontier.'),
        Game(title='Escape Room: The Game 2', type='Escape Room', genres='Puzzle, Cooperative', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/escape-room-the-game-2.jpg', description='Escape Room: The Game 2 is a board game where players work together to solve puzzles and escape from a series of themed rooms before time runs out.'),
        Game(title='Clank!', type='Deck Building', genres='Adventure, Fantasy', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/clank.jpg', description='In Clank!, players delve into a dungeon to steal treasure and avoid detection by a dragon.'),
        Game(title='Poker', type='Casino Games', genres='Gambling, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=10, image_url='https://example.com/poker.jpg', description='Poker is a classic casino game where players bet on the strength of their hand and try to outsmart their opponents.'),
        Game(title='Super Smash Bros. Ultimate', type='Video Games', genres='Fighting, Multiplayer', platforms='Nintendo Switch', player_num_min=1, player_num_max=8, image_url='https://example.com/smash-ultimate.jpg', description='Super Smash Bros. Ultimate is a fighting game featuring a wide range of Nintendo characters, items, and stages.'),
        Game(title='T.I.M.E Stories', type='Board Games', genres='Adventure, Cooperative', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/time-stories.jpg', description='In T.I.M.E Stories, players travel through time to solve mysteries and prevent temporal anomalies from occurring.'),
        Game(title='The Resistance: Avalon', type='Party Games', genres='Deduction, Social Deduction', platforms='Tabletop', player_num_min=5, player_num_max=10, image_url='https://example.com/resistance-avalon.jpg', description='The Resistance: Avalon is a social deduction game where players try to identify who among them are loyal servants of King Arthur and who are minions of Mordred.'),
        Game(title='Ticket to Ride: Rails and Sails', type='Board Games', genres='Route Building, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/ticket-to-ride-rails-and-sails.jpg', description='Ticket to Ride: Rails and Sails is a train and ship route-building game where players compete to connect cities across the world.'),
        Game(title='The Sims 4', type='Video Games', genres='Life Simulator, Simulation', platforms='PC, Mac, Xbox One, PlayStation 4', player_num_min=1, player_num_max=1, image_url='https://example.com/the-sims-4.jpg', description='The Sims 4 is a life simulation game where players create and control virtual people and help them navigate through their daily lives.'),
        Game(title='Codenames Duet', type='Party Games', genres='Word, Deduction', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/codenames-duet.jpg', description='Codenames Duet is a cooperative word game where players try to identify secret agents based on one-word clues given by their partner.'),
        Game(title='Ticket to Ride: New York', type='Board Games', genres='Strategy, Family', platforms='Tabletop, Mobile Games', player_num_min=2, player_num_max=4, image_url='https://example.com/ticket-to-ride-new-york.jpg', description='Ticket to Ride: New York is a quick, light version of the classic Ticket to Ride game, set in 1960s New York City.'),
        Game(title='Pandemic Legacy: Season 1', type='Board Games', genres='Cooperative, Campaign, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/pandemic-legacy-season-1.jpg', description='Pandemic Legacy is a cooperative game that takes players on a journey through a year-long campaign to save the world from a deadly pandemic.'),
        Game(title='Terraforming Mars: Ares Expedition', type='Board Games', genres='Strategy, Science Fiction', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/terraforming-mars-ares-expedition.jpg', description='Terraforming Mars: Ares Expedition is a card-driven strategy game set in a future where humanity is attempting to terraform the red planet.'),
        Game(title='Werewolf: The Apocalypse - Heart of the Forest', type='Video Games', genres='Adventure, Interactive Fiction, Role-playing', platforms='PC', player_num_min=1, player_num_max=1, image_url='https://example.com/werewolf-heart-of-the-forest.jpg', description='Werewolf: The Apocalypse - Heart of the Forest is a narrative adventure game where players take on the role of a young woman discovering her connection to the world of werewolves.'),
        Game(title='Magic Maze', type='Board Games', genres='Cooperative, Real-time', platforms='Tabletop', player_num_min=1, player_num_max=8, image_url='https://example.com/magic-maze.jpg', description='Magic Maze is a cooperative game where players must work together to guide their characters through a maze, with each player only able to move the characters in certain directions.'),
        Game(title='Ticket to Ride: Amsterdam', type='Board Games', genres='Strategy, Family', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/ticket-to-ride-amsterdam.jpg', description='Ticket to Ride: Amsterdam is a quick, light version of the classic Ticket to Ride game, set in the Dutch capital in the early 20th century.'),
        Game(title='Dungeons & Dragons: The Legend of Drizzt', type='Tabletop Role-playing Games', genres='Adventure, Fantasy', platforms='Tabletop', player_num_min=1, player_num_max=5, image_url='https://example.com/dungeons-and-dragons-the-legend-of-drizzt.jpg', description='Dungeons & Dragons: The Legend of Drizzt is a cooperative adventure game based on the popular fantasy novels by R.A. Salvatore.'),
        Game(title='Twilight Struggle', type='Board Games', genres='Strategy', platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/twilight-struggle.jpg', description='Twilight Struggle is a two-player game simulating the forty-five year dance of intrigue, prestige, and occasional flares of warfare between the Soviet Union and the United States.'),
        Game(title='7 Wonders Duel', type='Board Games', genres='Strategy', platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/7-wonders-duel.jpg', description='7 Wonders Duel is a two-player civilization building game set in the 7 Wonders universe. Players compete to build the most magnificent civilization and earn victory points by building structures and wonders, mastering military conflicts, and developing commercial networks.'),
        Game(title='Pandemic Legacy: Season 2', type='Board Games', genres='Cooperative, Campaign', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/pandemic-legacy-season-2.jpg', description='Pandemic Legacy: Season 2 is a cooperative campaign game where players must work together to survive in a world ravaged by a deadly pandemic.'),
        Game(title='Ticket to Ride: Asia', type='Board Games', genres='Strategy, Route Building', platforms='Tabletop', player_num_min=2, player_num_max=6, image_url='https://example.com/ticket-to-ride-asia.jpg', description='Ticket to Ride: Asia is a board game where players build train routes across Asia to score points.'),
        Game(title='Gizmos', type='Board Games', genres='Engine Building, Family', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/gizmos.jpg', description='Gizmos is a family board game where players build machines and collect energy marbles to earn points.'),
        Game(title='Cards Against Humanity', type='Card Games', genres='Party, Adult', platforms='Tabletop', player_num_min=3, player_num_max=20, image_url='https://example.com/cards-against-humanity.jpg', description='Cards Against Humanity is a party game where players complete fill-in-the-blank statements using raunchy or politically incorrect words and phrases.'),
        Game(title='Exploding Kittens', type='Card Games', genres='Family, Party', platforms='Tabletop, Mobile Games', player_num_min=2, player_num_max=5, image_url='https://example.com/exploding-kittens.jpg', description='Exploding Kittens is a family-friendly party game where players draw cards until someone draws an exploding kitten and loses the game.'),
        Game(title='Bandido', type='Card Games', genres='Cooperative, Puzzle', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/bandido.jpg', description='Bandido is a cooperative card game where players must work together to stop a prisoner from escaping through a network of tunnels.'),
        Game(title='Boss Monster: The Dungeon Building Card Game', type='Card Games', genres='Fantasy, Deck Building', platforms='Tabletop', player_num_min=2, player_num_max=4, image_url='https://example.com/boss-monster.jpg', description='Boss Monster is a dungeon-building card game where players compete to build the most enticing dungeon to lure in and defeat unsuspecting adventurers.'),
        Game(title='Burgle Bros.', type='Board Games', genres='Cooperative, Heist', platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/burgle-bros.jpg', description='Burgle Bros. is a cooperative game where players work together to plan and execute a heist in a high-security building.'),
        Game(title='Captain Sonar', type='Board Games', genres='Real-time, Strategy', platforms='Tabletop', player_num_min=2, player_num_max=8, image_url='https://example.com/captain-sonar.jpg', description='Captain Sonar is a real-time game where two teams of players take on different roles on a submarine and try to take out the other team.'),
        Game(title='Century: Spice Road', type='Board Games', genres='Economic, Engine Building', platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/century-spice-road.jpg', description='Century: Spice Road is an engine-building game where players trade spices to fulfill contracts and upgrade their caravans.'),
        Game(title='Concept', type='Board Games', genres='Party, Word', platforms='Tabletop', player_num_min=4, player_num_max=12, image_url='https://example.com/concept.jpg', description='Concept is a party game where players use icons to communicate and guess words or phrases.'),
        Game(title='Coup: Rebellion G54', type='Card Games', genres='Bluffing, Social Deduction', platforms='Tabletop', player_num_min=3, player_num_max=6, image_url='https://example.com/coup-rebellion.jpg', description='Coup: Rebellion G54 is a social deduction game where players are members of different factions trying to overthrow the government.'),
        Game(title='Diamant', type='Board Games', genres='Push Your Luck, Adventure', platforms='Tabletop', player_num_min=3, player_num_max=8, image_url='https://example.com/diamant.jpg', description='Diamant is a push-your-luck game where players explore a mine for treasure while trying to avoid dangerous obstacles.'),
        Game(title='Dobble/Spot It!', type='Card Games', genres='Pattern Building, Party', platforms='Tabletop', player_num_min=2, player_num_max=8, image_url='https://example.com/dobble.jpg', description='Dobble/Spot It! is a pattern-building game where players try to match symbols on cards.'),
        Game(title="Don't Mess with Cthulhu", type="Card Games", genres="Deduction, Horror", platforms='Tabletop', player_num_min=4, player_num_max=8, image_url='https://example.com/dont-mess-with-cthulhu.jpg', description="Don't Mess with Cthulhu is a social deduction game where players take on the roles of investigators or cultists and try to either uncover or hide the eldritch horrors that lurk among them."),
        Game(title="Forbidden Desert", type="Board Games", genres="Cooperative, Adventure", platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/forbidden-desert.jpg', description="Forbidden Desert is a cooperative game where players work together to survive a deadly desert and find the parts they need to repair their airship and escape."),
        Game(title="Forbidden Sky", type="Board Games", genres="Cooperative, Adventure", platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/forbidden-sky.jpg', description="Forbidden Sky is a cooperative game where players work together to explore a mysterious floating platforms and assemble a rocket to escape before it's too late."),
        Game(title="Fury of Dracula", type="Board Games", genres="Deduction, Horror", platforms='Tabletop', player_num_min=2, player_num_max=5, image_url='https://example.com/fury-of-dracula.jpg', description="Fury of Dracula is a deduction game where one player takes on the role of Dracula and tries to elude and outwit the other players, who are hunters trying to find and defeat him."),
        Game(title="Ganz schön clever/That's Pretty Clever", type="Dice", genres="Roll-and-Write, Puzzle", platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/ganz-schon-clever.jpg', description="Ganz schön clever/That's Pretty Clever is a roll-and-write game where players try to score as many points as possible by filling out their score sheets strategically with the numbers they roll on six dice."),
        Game(title="Hanamikoji", type="Card Games", genres="Abstract, Strategy", platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/hanamikoji.jpg', description="Hanamikoji is an abstract strategy game where players try to win the favor of geishas by playing cards with different abilities to win their support and ultimately gain the most points."),
        Game(title="Ingenious", type="Board Games", genres="Abstract, Tile Placement", platforms='Tabletop', player_num_min=1, player_num_max=4, image_url='https://example.com/ingenious.jpg', description="Ingenious is an abstract tile-placement game where players score points by creating lines of matching colored tiles and trying to score in each of the six different colors."),
        Game(title="Jaipur", type="Card Games", genres="Set Collection, Economic", platforms='Tabletop', player_num_min=2, player_num_max=2, image_url='https://example.com/jaipur.jpg', description="Jaipur is a set collection game where players trade goods and camels to earn money and buy victory points, with the goal of becoming the best trader in the city of Jaipur."),
        Game(title="K2", type="Board Games", genres="Adventure, Strategy", platforms="Tabletop", player_num_min=1, player_num_max=5, image_url="https://example.com/k2.jpg", description="K2 is a competitive game about mountaineering where players must balance risks and rewards to reach the summit of the mountain."),
        Game(title="Kanagawa", type="Board Games", genres="Family, Set Collection", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="https://example.com/kanagawa.jpg", description="Kanagawa is a game where players paint the beautiful landscape of Japan in the 19th century, while trying to balance different themes and techniques."),
        Game(title="Kingdom Builder", type="Board Games", genres="City-building, Strategy", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="https://example.com/kingdom-builder.jpg", description="Kingdom Builder is a strategic game where players create their own kingdoms by placing settlements, while trying to fulfill different objectives."),
        Game(title="Machi Koro: Bright Lights, Big City", type="Card Games", genres="Economic, City-building", platforms="Tabletop", player_num_min=2, player_num_max=5, image_url="https://example.com/machi-koro-bright-lights-big-city.jpg", description="Machi Koro: Bright Lights, Big City is a fast-paced game where players build their own cities and try to attract tourists by creating different landmarks and attractions."),
        Game(title="Mint Works", type="Board Games", genres="Economic, Resource Management", platforms="Tabletop", player_num_min=1, player_num_max=4, image_url="https://example.com/mint-works.jpg", description="Mint Works is a worker-placement game where players manage their own mint factory, trying to create the most efficient production line."),
        Game(title="Onirim", type="Card Games", genres="Cooperative, Deduction", platforms="Tabletop", player_num_min=1, player_num_max=2, image_url="https://example.com/onirim.jpg", description="Onirim is a solitaire or cooperative game where players try to escape from a mysterious labyrinth, by finding the eight doors that lead outside."),
        Game(title="Pandemic: Reign of Cthulhu", type="Board Games", genres="Cooperative, Horror", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="https://example.com/pandemic-reign-of-cthulhu.jpg", description="Pandemic: Reign of Cthulhu is a cooperative game where players must stop the spread of the Lovecraftian monsters that threaten to take over the world."),
        Game(title="The Quacks of Quedlinburg", type="Board Games", genres="Press Your Luck, Bag Building", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="https://example.com/quacks-of-quedlinburg.jpg", description="The Quacks of Quedlinburg is a game about alchemists trying to brew the most powerful potions, by drawing random ingredients from their own bags."),
        Game(title="Specter Ops", type="Board Games", genres="Deduction, Miniature, Stealth", platforms="Tabletop", player_num_min=2, player_num_max=5, image_url="", description="Specter Ops is a tactical board game of hidden movement and deduction."),
        Game(title="Tales of the Arabian Nights", type="Board Games", genres="Adventure, Storytelling", platforms="Tabletop", player_num_min=1, player_num_max=6, image_url="", description="Tales of the Arabian Nights is an adventure game where players embark on a journey through a mystical world, making choices that determine their fate."),
        Game(title="Takenoko", type="Board Games", genres="Family, Strategy", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="", description="Takenoko is a cute and colorful game where players cultivate a bamboo garden and tend to a hungry panda."),
        Game(title="Time's Up!", type="Party Games", genres="Word", platforms="Tabletop", player_num_min=4, player_num_max=12, image_url="", description="Time's Up! is a fast-paced word-guessing game that will have you laughing and shouting with your friends."),
        Game(title="Tiny Epic Galaxies", type="Board Games", genres="Dice Rolling, Strategy", platforms="Tabletop", player_num_min=1, player_num_max=5, image_url="", description="Tiny Epic Galaxies is a compact strategy game where players compete to build the greatest galactic empire."),
        Game(title="Tokaido", type="Board Games", genres="Family, Strategy", platforms="Tabletop", player_num_min=2, player_num_max=5, image_url="", description="Tokaido is a peaceful journey through Japan where players collect experiences and meet new people along the way."),
        Game(title="Ultimate Werewolf", type="Party Games", genres="Social Deduction ", platforms="Tabletop", player_num_min=5, player_num_max=68, image_url="", description="Ultimate Werewolf is a classic social deduction game where players work to identify the werewolf among them."),
        Game(title="Unstable Unicorns", type="Card Games", genres="Family, Strategy", platforms="Tabletop", player_num_min=2, player_num_max=8, image_url="", description="Unstable Unicorns is a whimsical card game where players collect and protect a menagerie of magical unicorns."),
        Game(title="Valley of the Kings", type="Card Games", genres="Deck Building", platforms="Tabletop", player_num_min=2, player_num_max=4, image_url="", description="Valley of the Kings is a deck-building game where players compete to build the most impressive tomb and earn the favor of the Pharaoh."),
        Game(title="Villages of Valeria", type="Card Games", genres="City-building, Resource Management", platforms="Tabletop", player_num_min=1, player_num_max=5, image_url="", description="Villages of Valeria is a strategic card game where players compete to build the most prosperous village in the land."),
        Game(title='Wingspan', type='Board Games', genres='Educational, Family', platforms='Tabletop, Digital', player_num_min=1, player_num_max=5, image_url='https://example.com/wingspan.jpg', description='Wingspan is a competitive bird-collection, engine-building game. You are bird enthusiasts—researchers, bird watchers, ornithologists, and collectors— seeking to discover and attract the best birds to your network of wildlife preserves. Each bird extends a chain of powerful combinations in one of your habitats (actions). These habitats focus on several key aspects of growth:'),
        Game(title='Zombie Dice', type='Dice', genres='Party, Horror', platforms='Tabletop', player_num_min=2, player_num_max=99, image_url='https://example.com/zombie-dice.jpg', description="Zombie Dice is a quick game for any zombie fan (or the whole zombie family). The 13 custom dice are your victims. Push your luck to eat their brains, but stop before the shotgun blasts end your turn! It's a great game for parties and for introducing friends to board games."),
    ]
    types = [
        "Board Games", "Card Games", "Casino Games", "Deck Building", "Dice", "Escape Room", 
        "Miniature", "Mobile Games", "Party Games", "Puzzles", "Social Deduction ", "Sports Games", 
        "Tabletop Role-playing Games", "Virtual Reality", "Video Games", "Word"
        ]
    genres = [
        "Abstract", "Action", "Adult", "Adventure", "Alternate History", "Battle", "Battle Royale", 
        "Campaign", "Card Drafting", "Card Game", "City-building", "Civilization", "Cooperative", 
        "Deduction", "Dice Rolling", "Drafting", "Economic", "Educational", "Engine Building", 
        "Epic", "Escape Room", "Family", "Fantasy", "Fighting", "Gambling", "Horror", "Incremental/Idle", 
        "Interactive Fiction", "Investigation", "JRPG", "Life Simulator", "Management", 
        "Massively Multiplayer Online Role Playing Game (MMORPG)", "Multiplayer Online Battle Arena (MOBA)", 
        "First-Person Shooter (FPS)", "Music", "Other", "Party", "Pattern Building", "Platformer", 
        "Puzzle", "Racing", "Resource Management", "Role-playing", "Roguelike", "Route Building", "Rhythm", 
        "Sandbox", "Science Fiction", "Shooter", "Simulation", "Sports", "Stealth", "Strategy", "Storytelling", 
        "Survival", "Tactical", "Tile Placement", "Trading", "Trading Card", "Trains", "Trivia", 
        "Vehicle Simulator", "Visual Novel", "Vocabulary", "War", "Word"
        ]
    platforms = ["NES", "SNES", "Digital", "Nintendo 64", "GameCube", "Wii",
        "Wii U", "Nintendo Switch", "GameBoy", "GameBoy Advance",
        "Nintendo DS", "Nintendo 3DS", "XBox", "XBox 360",
        "XBox One", "XBox Series X/S", "Other", "PlayStation", "PlayStation 2",
        "PlayStation 3", "PlayStation 4", "PlayStation 5", "PSP",
        "PS Vita", "Genesis", "DreamCast", "PC", "Table Top"]
    for n in range(100):
        game = Game(
            title=fake.word(),
            type=rc(types),
            genres=f"{rc(genres)}, {rc(genres)}",
            platforms=f"{rc(platforms)}, {rc(platforms)}",
            player_num_min=randint(1,4),
            player_num_max=randint(5,10),
            image_url=fake.image_url(200,200),
            # image_blob="TBD",
            description=fake.paragraph(nb_sentences=3),
        )
        games.append(game)
    print('Adding Game objects...')
    db.session.add_all(games)
    db.session.commit()

##########################################################

    print("Creating Inventory data...")
    inventories = []
    for user in users:
        for n in range(randint(1, 10)):
            inventory = Inventory(
                user=user,
                game=rc(games))
            inventories.append(inventory)
    print('Adding Inventory objects...')
    db.session.add_all(inventories)
    db.session.commit()

##########################################################

    print("Creating Swap data...")
    swaps = []
    statuses = ["Pending", "In Progess", "Completed"]
    for user in users:
        for n in range(randint(1,10)):
            borrow_date_str = fake.date()
            borrow_date = datetime.datetime.strptime(borrow_date_str, '%Y-%m-%d')
            swap = Swap(
                swap_status=rc(statuses), 
                borrow_date=borrow_date,
                due_date=borrow_date + datetime.timedelta(days=7),
                loaning_user_id=user.id,
                borrowing_user_id=rc(users).id,
                game_swapped_id=rc(games).id)
            swaps.append(swap)
    print('Adding Swap objects...')
    db.session.add_all(swaps)
    db.session.commit()

##########################################################

    print("Creating Message data...")
    messages = []
    for user in users:
        for n in range(randint(1, 10)):
            message = Message(
                message_text=f"{fake.sentence()}",
                sender_user_id=user.id,
                receiver_user_id=rc(users).id)
            messages.append(message)
    print('Adding Message objects...')
    db.session.add_all(messages)
    db.session.commit()

##########################################################

    print("Creating Review data...")
    reviews = []
    for user in users:
        for n in range(randint(1, 10)):
            review = Review(
                review_content=f"{fake.sentence()}",
                review_stars=randint(1,5),
                review_sender_user_id=user.id,
                review_receiver_user_id=rc(users).id)
            reviews.append(review)
    print('Adding Review objects...')
    db.session.add_all(reviews)
    db.session.commit()

##########################################################

    print("Creating Chat_Room data...")
    chat_rooms = []
    for n in range(randint(1, 10)):
        chat_room = Chat_Room(
            chat_room_name=f"{fake.word()}",
            chat_room_creator_user_id=rc(users).id)
        chat_rooms.append(chat_room)

    print('Adding Chat_Room objects...')
    db.session.add_all(chat_rooms)
    db.session.commit()

##########################################################

    print("Creating Chat Message data...")
    chat_messages = []
    for user in users:
        for n in range(randint(1, 10)):
            chat_message = Chat_Message(
                chat_message_text=f"{fake.sentence()}",
                chat_sender_user_id=user.id,
                chat_room_id=rc(chat_rooms).id)
            chat_messages.append(chat_message)
    print('Adding Chat Message objects...')
    db.session.add_all(chat_messages) 
    db.session.commit()   

##########################################################
    
    print("Just collating Data, as they say...")
    for user in users:
        review= rc(reviews)
        user.review = review
        reviews.remove(review)
        swap= rc(swaps)
        user.swap = swap
        swaps.remove(swap)

    print('Committing Seed...')
    db.session.commit()

    print("Seeding Complete!")