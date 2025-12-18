class Cleaner:
    '''
    Represents text cleaning utilities
    Attributes:
        categories: dictionary of word categories for analysis
    '''

    def __init__(self):
        # define categories as attribute so other methods can use them
        self.categories = {
            "beat": {"beat", "fight"},
            "weapon": {"pistol","pistols","ak","gat", "gats", "gun", "guns", "shot", "shots", "gunshot", "gunshots"},
            "lawenforcer": {"police", "cop", "fbi"},
            "fox": {"fox", "foxs"},
            "murder": {"murder", "murders", "murderers", "murdered", "die", "dies", "kill", "killing"},
            "color": {"black", "brown", "color"}
        }

    def get_categories(self):
        '''
        Returns the categories dictionary
        '''
        return self.categories

    # You could add more cleaning functions here later, e.g., text cleaning
    # def clean_text(self, text):
    #     """Example: remove punctuation, lowercase, replace words, etc."""
