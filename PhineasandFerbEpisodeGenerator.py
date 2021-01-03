import random

epi_list = ["S01E01 : Rollercoaster/Candace Loses Her Head",
            "S01E02 : The Fast and the Phineas/Lawn Gnome Beach Party of Terror!",
            "S01E03 : The Magnificent Few/S'Winter",
            "S01E04 : Are You My Mummy?/Flop Starz",
            "S01E05 : Raging Bully/ Lights, Candace, Action!",
            "S01E06 : Get That Bigfoot Outa My Face!/Tree to Get Ready",
            "S01E07 : It's About Time!",
            "S01E08 : Jerk De Soleil/Toy to the World",
            "S01E09 : One Good Scare Ought To Do It!",
            "S01E10 : A Hard Day's Knight/ I, Brobot", 
            "S01E11 : Mom's Birthday/ Journey to the Center of Candace",
            "S01E12 : Run Away Runway/ I Scream, You Scream",
            "S01E13 : It's a Mud, Mud, Mud, Mud World/The Ballad of Badbeard",
            "S01E14 : Dude, We're Gettin' the Band Back Together!",
            "S01E15 : Ready For the Bettys/ The Flying Fishmonger",
            "S01E16 : Phineas and Ferb Get Busted!",
            "S01E17 : Greece Lightning/Leave the Busting to Us!",
            "S01E18 : Crack That Whip/ The Best Lazy Day Ever",
            "S01E19 : Boyfriend from 27,000 B.C./Voyage to the Bottom of Buford",
            "S01E20 : Put that Putter Away/ Does This Duckbill Make Ne Look Fat?",
            "S01E21 : Traffic Cam Caper/ Bowl-R-Rama Drama",
            "S01E22 : The Monster of Phineas-n-Ferbenstein/ Oil on Candace",
            "S01E23 : Unfair Science Fair/ Unfair Science Fair",
            "S01E24 : Out to Launch",
            "S01E25 : Got Game?/Comet Kermilian ",
            "S01E26 : Out of Toon/Hail Doofania!",
            "S02E01 : The Lake Nose Monster (Part 1 and 2)",
            "S02E02 : Interview with a Platypus/ Tip of the Day",
            "S02E03 : Attack of the 50-Foot Sister/Backyard Aquarium",
            "S02E04 : Day of the Living Gelatin!/Elementary, My Dear Stacy",
            "S02E05 : Don't Even Blink/Chez Platypus",
            "S02E06 : Perry Lays an Egg/Gaming the System",
            "S02E07 : The Chronicles of Meap",
            "S02E08 : Thaddeus and Thor/De Plane! De Plane!",
            "S02E09 : Let's Take a Quiz/At the Car Wash",
            "S02E10 : Oh, There You Are, Perry/Swiss Family Phineas",
            "S02E11 : Phineas and Ferb's Musical Cliptastic Countdown",
            "S02E12 : Phineas and Ferb's Quantum Boogaloo",
            "S02E13 : Hide and Seek/That Sinking Feeling",
            "S02E14 : The Baljeatles/Vanessassary Roughness",
            "S02E15 : No More Bunny Business/Spa Day",
            "S02E16 : Bubble Boys/Isabella and the Temple of Sap",
            "S02E17 : Cheer Up, Candace/Fireside Girl Jamboree",
            "S02E18 : The Bully Code/Finding Mary McGuffin",
            "S02E19 : What Do It Do?/ Atlantis",
            "S02E20 : Picture This/Nerdy Dancin'",
            "S02E21 : I Was a Middle-Aged Robot/Suddenly Suzy",
            "S02E22 : Phineas and Ferb Christmas Vacation!",
            "S02E23 : Undercover Carl/Hip Hop Parade",
            "S02E24 : Just Passing Through/Candace's Big day",
            "S02E25 : Invasion of the Ferb Snatchers/Ain't No Kiddie Ride",
            "S02E26 : Wizard of Odd (Part 1 and 2)",
            "S02E27 : The Beak (Part 1 and 2)",
            "S02E28 : Not Phineas and Ferb/Phineas and Ferb-Busters!",
            "S02E29 : The Lizard Whisperer/Robot Rodeo",
            "S02E30 : The Secret of Success/The Doof Side of the Moon",
            "S02E31 : She's the Mayor/The Lemonade Stand",
            "S02E32 : We Call It Maze/Ladies and Gentlemen, Meet Max Modem!",
            "S02E33 : Nerds of a Feather (Part 1 and 2)",
            "S02E34 : Phineas and Ferb Hawaiian Vacation (Part 1 and 2)",
            "S02E35 : Split Personality/ Brain Drain",
            "S02E36 : Make Play/Candace Gets Busted",
            "S02E37 : Summer Belongs to You! (Part 1 and 2)",
            "S02E38 : Summer Belongs to You! (Part 3 and 4)",
            "S02E39 : Rollercoaster: The Musical! (Part I and II)",
            "S03E01 : Run, Candace, Run/ Last Train to Bustville",
            "S03E02 : The Great Indoors/Canderemy",
            "S03E03 : The Belly of the Beast/ Moon Farm",
            "S03E04 : Phineas' Birthday Clip-O-Rama! (Part 1 and 2)",
            "S03E05 : Ask a Foolish Question/Misperceived Monotreme",
            "S03E06 : Candace Disconnected/Magic Carpet Ride",
            "S03E07 : Bad Hair Day/Meatloaf Surprise",
            "S03E08 : Tri-Stone Area/Doof Dynasty",
            "S03E09 : Supermollusk/The Necklace",
            "S03E10 : Mommy Can You Hear Me?/Road Trip",
            "S03E11 : Skiddley Whiffers/Tour de Ferb",
            "S03E12 : My Fair Goalie (Parts 1 and 2)",
            "S03E13 : Perry the Actorpus/Bullseye!",
            "S03E14 : That's the Spirit!/The Curse of Candace",
            "S03E15 : Escape from Phineas Tower/The Remains of the Platypus",
            "S03E16 : Ferb Latin/ Lotsa Latkes",
            "S03E17 : Phineas and Ferb Family Christmas, a/S'Winter",
            "S03E18 : What a Croc!/Ferb TV",
            "S03E19 : Mom's in the House/Minor Monogram",
            "S03E20 : Excaliferb (Parts 1 and 2)",
            "S03E21 : Monster from ID/Gi-Ants",
            "S03E22 : Agent Doof/Phineas and Ferb and the Temple of Juatchadoon",
            "S03E23 : Delivery of Destiny/Let's Bounce",
            "S03E24 : Quietest Day Ever/Bully Bromance Breakup",
            "S03E25 : The Doonkelberry Imperative/Buford Confidential",
            "S03E26 : Sleepwalk Surprise/Sci-Fi Pie Fly",
            "S03E27 : Meapless in Seattle (Parts 1 and 2)",
            "S03E28 : The Mom Attractor/Cranius Maximus",
            "S03E29 : Sipping with the Enemy/Tri-State Treasure: Boot of Secrets",
            "S03E30 : Doofapus/Norm Unleashed",
            "S03E31 : When World's Collide/Road to Danville",
            "S03E32 : Where;s Perry? (Part I)(Part 1 of 2)",
            "S03E33 : WWhere;s Perry? (Part II)(Part 2 of 2)",
            "S03E34 : Blackout!/ What'd I Miss?",
            "S03E35 : This Is Your Backstory (Part 1 and 2)",
            "S04E01 : Fly on the Wall/ y Sweet Ride",
            "S04E02 : For Your Ice Only/Happy New Year!",
            "S04E03 : Bully Bust/Backyard Hodge Podge",
            "S04E04 : Der Kinderlumper/Just Desserts",
            "S04E05 : Bee Day/Bee Story",
            "S04E06 : Sidetracked (Part 1 and 2)",
            "S04E07 : Knot My Problem/Mind Share",
            "S04E08 : Primal Perry (Part 1 and 2)",
            "S04E09 : La Candace-Cabra/Happy Birthday Isabella",
            "S04E10 : Great Balls of Water/Where's Pinky?",
            "S04E11 : Phineas and Ferb: Mission Marvel, Part I (Part 1 of 2)",
            "S04E12 : Phineas and Ferb: Mission Marvel, Part II (Part 2 of 2)",
            "S04E13 : Thank But No Thanks/Troy Story",
            "S04E14 : Love at First Byte/One Good Turn",
            "S04E15 : Cheers for Fears/Just Our Luck",
            "S04E16 : Return Policy/Imperfect Storm",
            "S04E17 : Streampunx/It's No Picnic",
            "S04E18 : Terrifying Tri-State Trilogy of Terror (Part 1 and 2)",
            "S04E19 : Druselsteinoween/Face Your Fear",
            "S04E20 : The Klimpaloon Ultimatum",
            "S04E21 : Doof 101/Father's Day",
            "S04E22 : Operation Crumb Cake/Mandace",
            "S04E23 : Tales from the Resistance (Part 1 and 2)",
            "S04E24 : The Return of the Rogue Rabbit/Live and Let Drive",
            "S04E25 : Lost in Dancille/ he Inator Method",
            "S04E26 : Act Your Age (Part 1 and 2)",
            "S04E27 : Phineas and Ferb Save Summer Part 1 (Part 1 of 2)",
            "S04E28 : Phineas and Ferb Save Summer Part 2 (Part 2 of 2)",
            "S04E29 : Night of the Living Phramacists Part 1 (Part 1 of 2)",
            "S04E30 : Night of the Living Pharmacists Part 2 (Part 2 of 2)",
            "S04E31 : Phineas and Ferb Star Wars Part I (Part 1 of 2)",
            "S04E32 : Phineas and Ferb Star Wars Part II (Part 2 of 2)",
            "S04E33 : Last Day of Summer Part I (Part 1 of 2)",
            "S04E34 : Last Day of Summer Part II (Part 2 of 2)",
            "S04E35 : The O.W.C.A. Files, Part I (Part 1 of 2)",
            "S04E36 : The O.W.C.A. Files, Part II (Part 2 of 2)"]

def pandf_episode():
    value = random.randint (0, len(epi_list)-1)
    print("The episode you will be watching is " + epi_list[value])

pandf_episode()    
    
    
            
            
            