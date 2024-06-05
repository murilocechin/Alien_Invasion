class GameStats:
    """
    Track statistics for Alien Invasion
    """

    def __init__(self, ai_game):
        """
        Inicialize statistics
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """
        Initialize statistics that can change during game
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0