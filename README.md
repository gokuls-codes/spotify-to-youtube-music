# Migrate tracks from spotify playlist to youtube music playlist

### Steps:

1. Install python.
2. Clone this repository into your system.
3. (Optional but **RECOMMENDED**) Create a new virtual environment in python for this project and activate it.
4. Get client-id, client-secret from spotify developer portal.
5. In the file main.py and modify the lines 7,8 as follows with your client id and client secret:
   ```
   client_id='<Your client id>'
   client_secret='<your client secret>'
   ```
6. Install the required libraries using the command `pip install -r requirements.txt`.
7. Run the command `ytmusicapi oauth` and authorize it in browser choosing whichever google account you want the playlist to be created in.
8. Run the file main.py using the command `python main.py`.
9. Further instructions will be provided while running the file main.py.
10. You'll be prompted to login to spotify and authorize the app to perform various actions when running the main file.
11. Due to some technical reasons, it may be unable to add some of the songs from the spotify playlist. Such songs are printed to the terminal in the end.
