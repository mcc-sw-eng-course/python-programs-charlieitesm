import logging
from abc import ABC

from L8.game.game import Game

# Create a logger for later troubleshooting
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='tictectoe-engine_network.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.getLogger(__name__).addHandler(console)


class ClientGame(Game, ABC):

    LOGGER = logging.getLogger(__name__)

    def initialize_resources(self):
        pass

    # noinspection PyBroadException
    def release_resources(self):
        ClientGame.LOGGER.info(f"Releasing server resources for port... {self.port}")

        for mr in self.managed_resources:
            if mr:
                try:
                    mr.close()
                except:
                    ClientGame.LOGGER.error(f"There was a problem trying to close resoure {str(mr)}")
                    ClientGame.LOGGER.exception("Exception thrown")
