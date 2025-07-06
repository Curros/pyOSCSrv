import logging
from logger import log
from config import get_config
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class SpotifyHandler():
    def __init__(self):
        for noisy_logger in ["spotipy", "urllib3", "requests"]:
            logger = logging.getLogger(noisy_logger)
            logger.setLevel(logging.CRITICAL)
            logger.propagate = False
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

        self.spotify_client_id = get_config("spotify_client_id")
        if not self.spotify_client_id:
            log.error(f"SPOTIFY_CLIENTID could not be loaded.")
            raise ValueError("SPOTIFY_CLIENTID could not be loaded.")

        self.spotify_client_secret = get_config("spotify_client_secret")
        if not self.spotify_client_id:
            log.error(f"SPOTIFY_CLIENT_SECRET could not be loaded.")
            raise ValueError("SPOTIFY_CLIENT_SECRET could not be loaded.")

        self.spotify = Spotify(auth_manager=SpotifyOAuth(
            client_id = self.spotify_client_id,
            client_secret=self.spotify_client_secret,
            redirect_uri=get_config("spotify_redirect_uri"),
            scope=get_config("spotify_scope")
        ))

    def handle(self, address, *args):

        devices = self.spotify.devices()
        if devices['devices']:
            device_id = devices['devices'][0]['id']
            log.info(f"Spotify device loaded Id: [{device_id}]")
        else:
            log.info(f"Spotify doesn't seams to have any device loaded")

        playback = self.spotify.current_playback()
        if playback and playback['device']:
            current_volume = playback['device']['volume_percent']
            log.info(f"Spotify current volume: [{current_volume}]")

        if address == "/spotify/play":
            self.spotify.start_playback()
        elif address == "/spotify/pause":
            self.spotify.pause_playback()
        elif address == "/spotify/next":
            self.spotify.next_track()
        elif address == "/spotify/volume" and args:
            volume = int(args[0])
            self.spotify.volume(volume)
        elif address == "/spotify/volume/increase":
            new_volume = min(current_volume + 5, 100)
            self.spotify.volume(new_volume)
        elif address == "/spotify/volume/decrease":
            new_volume = min(current_volume - 5, 100)
            self.spotify.volume(new_volume)
        else:
            print(f"[SpotifyHandler] Unknown command: {address}")