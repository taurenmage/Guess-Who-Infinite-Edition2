import random
import sys
import names
import weighted_random_choice as wrc

# Quick functions

# 1  breathing room
def broom():
    print("\n\t", "#" * 20, "\n")


def get_seed():
    broom()
    print("With the ability of random seeds, it is possible to re-visit past games featuring the same characters as during the original game. \nSimply enter the same number each time you are prompted and you will be met with the same faces as before. \n")
    choice = input("Enter a seed number: ")
    return choice


# Guess Who Parameters

AMOUNT_OF_FACES = 24
PERCENTAGE_CONSTANT = 100
random.seed(get_seed())

# input prompt ----------- input(">>")

# Face/person attributes

face_shape = ["square", "round", "pear", "oblong", "oval", "rectangle", "triangle", "diamond", "heart", "heptagon"]
eyes = ["upturned", "round", "monolid", "downturned", "hooded", "almond"]
eye_color = ["amber", "blue", "brown", "gray", "green", "hazel", "red"]
eyebrows = ["none", "unibrow", "thin", "bushy", "arched", "rounded", "straight"]
nose_shape = ["straight", "convex", "concave", "wavy", "button", "beak", "bulb", "schnoz", "dainty"]
lips = ["full", "heavy upper", "wide", "round", "heavy lower", "thin", "bow-shaped", "heart shaped", "downward-turned"]
cheeks = ["high", "low"]
hair_style = ["undercut", "bun", "pompadour", "comb-over", "bald", "balding", "caesar", "side-part", "buzz-cut",
              "spiky", "flat-top", "cornrows", "braids", "pony-tail", "mohawk", "mullet", "afro", "power bob", "pixie",
              "lob", "shag", "bangs", "midi", "waves"]
hair_color = ["blonde", "brown", "red", "black", "green", "blue", "purple", "rainbow", "white", "gray", "pink"]
hat = ["none", "baseball", "visor", "bucket", "cowboy", "fedora", "cloche", "beret", "fez", "pillbox", "straw",
       "sailor", "top hat", "chef", "hard hat", "coonskin"]
glasses = ["none", "round", "cat eye", "goggles", "heart", "mirrored", "biker", "oval", "pilot", "brow-line",
           "oversized", "square"]
beard = ["none", "stubble", "mutton chops", "full", "pointy", "long", "patchy", "viking"]
mustache = ["none", "pringles", "Dali", "pencil", "Hitler", "handlebar", "horsehoe", "walrus", "pyramidal", "fu manchu",
            "zappa"]
skin_color = ["white", "black", "olive", "pink", "yellow", "brown", "red", "green", "purple", "gray", "blue"]
gender_appearance = ["feminine", "masculine", "androgynous"]
shirt = ["none", "button-down", "crew-neck", "v-neck", "tank-top", "sleeveless", "jersey", "t-shirt", "smock", "sailor",
         "sweatshirt", "sweater", "turtleneck", "tuxedo", "tube top"]
shirt_color = ["yellow", "brown", "red", "black", "green", "blue", "purple", "rainbow", "white", "gray", "pink",
               "translucent", "tie-dye"]

# lists & dictionaries

face_shape_dict = [
    {"feature": "square",
    "probability": 1},
    {"feature": "round",
     "probability": 10},
    {"feature": "pear",
     "probability": 1},
    {"feature": "oblong",
     "probability": 10},
    {"feature": "oval",
     "probability": 1},
    {"feature": "rectangle",
     "probability": 1},
    {"feature": "triangle",
     "probability": 1},
    {"feature": "diamond",
     "probability": 1},
    {"feature": "heart",
     "probability": 1},
    {"feature": "heptagon",
     "probability": 1},
]

eyes_dict = [
    {"feature": "upturned",
    "probability": 1},
    {"feature": "round",
     "probability": 1},
    {"feature": "monolid",
     "probability": 1},
    {"feature": "downturned",
     "probability": 1},
    {"feature": "hooded",
     "probability": 1},
    {"feature": "almond",
     "probability": 1},
]

eye_color_dict = [
    {"feature": "amber",
    "probability": 15},
    {"feature": "blue",
     "probability": 25},
    {"feature": "brown",
     "probability": 50},
    {"feature": "gray",
     "probability": 1},
    {"feature": "green",
     "probability": 5},
    {"feature": "hazel",
     "probability": 15},
    {"feature": "red",
     "probability": 1},
]

eyebrows_dict = [
    {"feature": "none",
    "probability": 1},
    {"feature": "unibrow",
     "probability": 5},
    {"feature": "thin",
     "probability": 15},
    {"feature": "bushy",
     "probability": 20},
    {"feature": "arched",
     "probability": 10},
    {"feature": "rounded",
     "probability": 20},
    {"feature": "straight",
     "probability": 20},
]

nose_shape_dict = [
    {"feature": "straight",
    "probability": 25},
    {"feature": "convex",
     "probability": 15},
    {"feature": "concave",
     "probability": 15},
    {"feature": "wavy",
     "probability": 15},
    {"feature": "button",
     "probability": 1},
    {"feature": "beak",
     "probability": 2},
    {"feature": "bulb",
     "probability": 10},
    {"feature": "schnoz",
     "probability": 2},
    {"feature": "dainty",
     "probability": 10},
]

lips_dict = [
    {"feature": "full",
    "probability": 1},
    {"feature": "heavy upper",
     "probability": 1},
    {"feature": "wide",
     "probability": 1},
    {"feature": "round",
     "probability": 1},
    {"feature": "heavy lower",
     "probability": 1},
    {"feature": "thin",
     "probability": 1},
    {"feature": "bow-shaped",
     "probability": 1},
    {"feature": "heart-shaped",
     "probability": 1},
    {"feature": "downward-turned",
     "probability": 1},
]

cheeks_dict = [
    {"feature": "high",
    "probability": 1},
    {"feature": "low",
     "probability": 1},
]

hair_style_dict = [
    {"feature": "undercut",
    "probability": 10},
    {"feature": "bun",
     "probability": 10},
    {"feature": "pompadour",
     "probability": 2},
    {"feature": "comb-over",
     "probability": 5},
    {"feature": "bald",
     "probability": 14},
    {"feature": "balding",
     "probability": 8},
    {"feature": "caesar",
     "probability": 5},
    {"feature": "side-part",
     "probability": 20},
    {"feature": "buzz-cut",
     "probability": 15},
    {"feature": "spiky",
     "probability": 10},
    {"feature": "flat-top",
     "probability": 1},
    {"feature": "cornrows",
     "probability": 5},
    {"feature": "braids",
     "probability": 5},
    {"feature": "pony-tail",
     "probability": 5},
    {"feature": "mohawk",
     "probability": 1},
    {"feature": "mullet",
     "probability": 1},
    {"feature": "afro",
     "probability": 4},
    {"feature": "power bob",
     "probability": 4},
    {"feature": "pixie",
     "probability": 3},
    {"feature": "lob",
     "probability": 10},
    {"feature": "shag",
     "probability": 5},
    {"feature": "bangs",
     "probability": 20},
    {"feature": "midi",
     "probability": 10},
    {"feature": "waves",
     "probability": 5},
]

hair_color_dict = [
    {"feature": "blonde",
    "probability": 10},
    {"feature": "brown",
     "probability": 40},
    {"feature": "red",
     "probability": 5},
    {"feature": "black",
     "probability": 40},
    {"feature": "green",
     "probability": 1},
    {"feature": "blue",
     "probability": 1},
    {"feature": "purple",
     "probability": 1},
    {"feature": "rainbow",
     "probability": 1},
    {"feature": "white",
     "probability": 5},
    {"feature": "gray",
     "probability": 5},
    {"feature": "pink",
     "probability": 1},
]

hat_dict = [
    {"feature": "none",
    "probability": 30},
    {"feature": "baseball",
     "probability": 3},
    {"feature": "visor",
     "probability": 1},
    {"feature": "bucket",
     "probability": 1},
    {"feature": "cowboy",
     "probability": 1},
    {"feature": "fedora",
     "probability": 1},
    {"feature": "cloche",
     "probability": 1},
    {"feature": "beret",
     "probability": 1},
    {"feature": "fez",
     "probability": 1},
    {"feature": "pillbox",
     "probability": 1},
    {"feature": "straw",
     "probability": 2},
    {"feature": "sailor",
     "probability": 1},
    {"feature": "top hat",
     "probability": 1},
    {"feature": "chef",
     "probability": 1},
    {"feature": "hard hat",
     "probability": 1},
    {"feature": "coonskin",
     "probability": 1},
]

glasses_dict = [
    {"feature": "none",
    "probability": 25},
    {"feature": "round",
     "probability": 5},
    {"feature": "cat eye",
     "probability": 2},
    {"feature": "goggles",
     "probability": 1},
    {"feature": "heart",
     "probability": 2},
    {"feature": "mirrored",
     "probability": 1},
    {"feature": "biker",
     "probability": 1},
    {"feature": "oval",
     "probability": 2},
    {"feature": "pilot",
     "probability": 1},
    {"feature": "brow-line",
     "probability": 1},
    {"feature": "oversized",
     "probability": 1},
    {"feature": "square",
     "probability": 2},
]

beard_dict = [
    {"feature": "none",
    "probability": 88},
    {"feature": "stubble",
     "probability": 5},
    {"feature": "mutton chops",
     "probability": 1},
    {"feature": "full",
     "probability": 15},
    {"feature": "pointy",
     "probability": 1},
    {"feature": "long",
     "probability": 2},
    {"feature": "patchy",
     "probability": 3},
    {"feature": "viking",
     "probability": 1},
]

mustache_dict = [
    {"feature": "none",
    "probability": 90},
    {"feature": "pringles",
     "probability": 1},
    {"feature": "Dali",
     "probability": 1},
    {"feature": "pencil",
     "probability": 1},
    {"feature": "Hitler",
     "probability": 1},
    {"feature": "handlebar",
     "probability": 1},
    {"feature": "horseshoe",
     "probability": 1},
    {"feature": "walrus",
     "probability": 1},
    {"feature": "pyramidal",
     "probability": 1},
    {"feature": "fu manchu",
     "probability": 1},
    {"feature": "Zappa",
     "probability": 1},
]

skin_color_dict = [
    {"feature": "white",
    "probability": 40},
    {"feature": "black",
     "probability": 40},
    {"feature": "olive",
     "probability": 20},
    {"feature": "pink",
     "probability": 20},
    {"feature": "yellow",
     "probability": 40},
    {"feature": "brown",
     "probability": 40},
    {"feature": "red",
     "probability": 15},
    {"feature": "green",
     "probability": 1},
    {"feature": "purple",
     "probability": 1},
    {"feature": "gray",
     "probability": 1},
    {"feature": "blue",
     "probability": 1},
]

gender_appearance_dict = [
    {"feature": "feminine",
    "probability": 12},
    {"feature": "masculine",
     "probability": 12},
    {"feature": "androgynous",
     "probability": 1},
]

shirt_dict = [
    {"feature": "none",
    "probability": 3},
    {"feature": "button-down",
     "probability": 2},
    {"feature": "crew-neck",
     "probability": 5},
    {"feature": "v-neck",
     "probability": 7},
    {"feature": "tank-top",
     "probability": 5},
    {"feature": "sleeveless",
     "probability": 5},
    {"feature": "jersey",
     "probability": 2},
    {"feature": "t-shirt",
     "probability": 10},
    {"feature": "smock",
     "probability": 1},
    {"feature": "sailor",
     "probability": 1},
    {"feature": "sweatshirt",
     "probability": 5},
    {"feature": "sweater",
     "probability": 5},
    {"feature": "turtleneck",
     "probability": 2},
    {"feature": "tuxedo",
     "probability": 1},
    {"feature": "tube top",
     "probability": 5},
]

shirt_color_dict = [
    {"feature": "white",
    "probability": 5},
    {"feature": "black",
     "probability": 5},
    {"feature": "translucent",
     "probability": 1},
    {"feature": "pink",
     "probability": 5},
    {"feature": "yellow",
     "probability": 5},
    {"feature": "brown",
     "probability": 5},
    {"feature": "red",
     "probability": 5},
    {"feature": "green",
     "probability": 5},
    {"feature": "purple",
     "probability": 5},
    {"feature": "gray",
     "probability": 5},
    {"feature": "blue",
     "probability": 5},
    {"feature": "rainbow",
     "probability": 1},
    {"feature": "tie-dye",
     "probability": 1},
]

attributes_list = [face_shape, eyes, eye_color, eyebrows, nose_shape, lips, cheeks, hair_style, hair_color, hat, glasses, beard,
                   mustache, skin_color, gender_appearance, shirt, shirt_color]
categories_list = ["face shape", "eyes", "eye color", "eyebrows", "nose", "lip shape", "cheekbones", "hair style", "hair color",
                   "hat", "glasses", "beard", "mustache", "skin color", "gender appearance", "shirt", "shirt color"]

dict_list = [face_shape_dict, eyes_dict, eye_color_dict, eyebrows_dict, nose_shape_dict, lips_dict, cheeks_dict, hair_style_dict, hair_color_dict, hat_dict, glasses_dict, beard_dict, mustache_dict, skin_color_dict, gender_appearance_dict, shirt_dict, shirt_color_dict]

class Face:
    def __init__(self, name, face_shape, eyes, eye_color, eyebrows, nose_shape, lips, cheeks, hair_style, hair_color, hat,
                 glasses, beard, mustache, skin_color, gender_appearance, shirt, shirt_color):
        self.name = name
        self.face_shape = face_shape
        self.eyes = eyes
        self.eye_color = eye_color
        self.eyebrows = eyebrows
        self.nose_shape = nose_shape
        self.lips = lips
        self.cheeks = cheeks
        self.hair_style = hair_style
        self.hair_color = hair_color
        self.hat = hat
        self.glasses = glasses
        self.beard = beard
        self.mustache = mustache
        self.skin_color = skin_color
        self.gender_appearance = gender_appearance
        self.shirt = shirt
        self.shirt_color = shirt_color

    def self_list(self):
        return [self.face_shape, self.eyes, self.eye_color, self.eyebrows, self.nose_shape, self.lips, self.cheeks, self.hair_style,
                self.hair_color, self.hat, self.glasses, self.beard, self.mustache, self.skin_color,
                self.gender_appearance, self.shirt, self.shirt_color]

    def self_details_gen(self, attr_list):
        broom()

        print(f'\n\tName: {self.name}')

        for i, j in zip(range(len(categories_list)), range(len(attr_list))):
            print(f'\t{categories_list[i].capitalize()}: {attr_list[j].capitalize()}')

    def name_get(self):
        return self.name

    def name_list(self):

        for i in range(len(instances_list)):
            print(f'{i + 1}. {instances_list[i].name_get()}')

    def display_instance_details(self, attr_list):
        broom()
        print(f'\n\tName: {self.name}')

        for i, j in zip(range(len(categories_list)), range(len(attr_list))):
            print(f'\t{categories_list[i].capitalize()}: {attr_list[j].capitalize()}')

        what_do_next()


# how each feature is randomly generated
def random_feature_gen(feature_list):
    return feature_list[random.randrange(0, len(feature_list))]


def random_instance_gen():
    return Face(names.get_first_name(), random_feature_gen(face_shape), random_feature_gen(eyes),
                random_feature_gen(eye_color), random_feature_gen(eyebrows), random_feature_gen(nose_shape), random_feature_gen(lips),
                random_feature_gen(cheeks), random_feature_gen(hair_style), random_feature_gen(hair_color),
                random_feature_gen(hat), random_feature_gen(glasses), random_feature_gen(beard),
                random_feature_gen(mustache), random_feature_gen(skin_color),
                random_feature_gen(gender_appearance), random_feature_gen(shirt),
                random_feature_gen(shirt_color))

# probablistic generation
def weighted_instance_gen():
    return Face(names.get_first_name(), wrc.weighted_choice([dict_list[0][i]["feature"] for i in range(len(face_shape))], [dict_list[0][i]["probability"] for i in range(len(face_shape))]), wrc.weighted_choice([dict_list[1][i]["feature"] for i in range(len(eyes))], [dict_list[1][i]["probability"] for i in range(len(eyes))]), wrc.weighted_choice([dict_list[2][i]["feature"] for i in range(len(eye_color))], [dict_list[2][i]["probability"] for i in range(len(eye_color))]), wrc.weighted_choice([dict_list[3][i]["feature"] for i in range(len(eyebrows))], [dict_list[3][i]["probability"] for i in range(len(eyebrows))]), wrc.weighted_choice([dict_list[4][i]["feature"] for i in range(len(nose_shape))], [dict_list[4][i]["probability"] for i in range(len(nose_shape))]), wrc.weighted_choice([dict_list[5][i]["feature"] for i in range(len(lips))], [dict_list[5][i]["probability"] for i in range(len(lips))]), wrc.weighted_choice([dict_list[6][i]["feature"] for i in range(len(cheeks))], [dict_list[6][i]["probability"] for i in range(len(cheeks))]), wrc.weighted_choice([dict_list[7][i]["feature"] for i in range(len(hair_style))], [dict_list[7][i]["probability"] for i in range(len(hair_style))]), wrc.weighted_choice([dict_list[8][i]["feature"] for i in range(len(hair_color))], [dict_list[8][i]["probability"] for i in range(len(hair_color))]), wrc.weighted_choice([dict_list[9][i]["feature"] for i in range(len(hat))], [dict_list[9][i]["probability"] for i in range(len(hat))]), wrc.weighted_choice([dict_list[10][i]["feature"] for i in range(len(glasses))], [dict_list[10][i]["probability"] for i in range(len(glasses))]), wrc.weighted_choice([dict_list[11][i]["feature"] for i in range(len(beard))], [dict_list[11][i]["probability"] for i in range(len(beard))]), wrc.weighted_choice([dict_list[12][i]["feature"] for i in range(len(mustache))], [dict_list[12][i]["probability"] for i in range(len(mustache))]), wrc.weighted_choice([dict_list[13][i]["feature"] for i in range(len(skin_color))], [dict_list[13][i]["probability"] for i in range(len(skin_color))]), wrc.weighted_choice([dict_list[14][i]["feature"] for i in range(len(gender_appearance))], [dict_list[14][i]["probability"] for i in range(len(gender_appearance))]), wrc.weighted_choice([dict_list[15][i]["feature"] for i in range(len(shirt))], [dict_list[15][i]["probability"] for i in range(len(shirt))]), wrc.weighted_choice([dict_list[16][i]["feature"] for i in range(len(shirt_color))], [dict_list[16][i]["probability"] for i in range(len(shirt_color))]))


# random instace generation
# instances_list = []
# for i in range(AMOUNT_OF_FACES):
#     instances_list.append(random_instance_gen())


# weighted instance generation
instances_list = []
for i in range(AMOUNT_OF_FACES):
    instances_list.append(weighted_instance_gen())


def title_screen() -> object:
    broom()
    print("\tWelcome to Guess Who: Infinite Edition!\n\n")
    input(">>")

def selection_screen():
    broom()

    instances_list[0].name_list()
    broom()
    choice = int(input("Select the person you want to read more about.\n>> "))
    while True:
        try:
            if choice - 1 in range(len(instances_list)):
                instances_list[choice - 1].display_instance_details(instances_list[choice - 1].self_list())
                break
            else:
                print(f'Invalid input. Input must be a number between 1 and {len(instances_list)}')
                input(">>")
                selection_screen()
                break
        except ValueError:
            print(f'Invalid input. Input must be a number between 1 and {len(instances_list)}')
            input(">>")
            selection_screen()
            break


def what_do_next():
    broom()
    choice = int(input("Return to the list? \n1. Yes \n2. No \n>> "))
    while True:
        try:
            if choice == 1:
                selection_screen()
                break
            elif choice == 2:
                broom()
                print("Thank you for using the program! ")
                sys.exit()
            else:
                print(f'Invalid input. Input must be a number between 1 and 2')
                input(">>")
                what_do_next()
                break
        except ValueError:
            print(f'Invalid input. Input must be a number between 1 and 2')
            input(">>")
            what_do_next()
            break


title_screen()
selection_screen()


