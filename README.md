# Spotify Playlist Editor
Flask based website utilizing the python Spotify library "Spotipy". This website allows a user to shuffle their existing playlists in a true-random fashion, or combine multiple playlists into a new playlist.

# Home Page
Here is the login page, utilizing a bootstrap jumbotron. Each page will also have a bootstrap NavBar, with  four options. Clicking the Spotify logo will redirect the user to Spotify.com. Clicking "Home" will bring the user back to this page. Clicking "Shuffle" will redirect the user to the "Shuffle" page, and "Combine" will redirect the user to the "Combine" page. This is also the case for clicking "Shuffle Playlist" and "Combine Playlist" respectively. On first visit, clicking any button other than home will open a new tab at Spotify, asking for authentication for the app.

![image](https://media.discordapp.net/attachments/404431223860232203/1075636366861410304/Screen_Shot_2023-02-15_at_3.49.21_PM.png?width=1775&height=903)

# Shuffle Page
This is the shuffle page. This page utilizes the Spotify to pull the user's playlist information, displaying the playlist names and images on a responsive grid. For this page, the playlists function as a radio input, meaning only one playlist can be selected at a time. Once a  playlist is selected, the user can either shuffle the original playlist, or create a new one. The new playlist will be named "Original playlist name" + "Shuffle". The method of shuffling uses Python's Random Shuffle() method to shuffle the list of tracks from the playlist.

![image](https://media.discordapp.net/attachments/404431223860232203/1075636367771582546/Screen_Shot_2023-02-15_at_3.50.36_PM.png?width=1232&height=676)

After shuffling the playlist, the user will be redirected to this success page. Here, the cover of the title and the playlist cover will be displayed. The user can click on the playlist cover to be redirected to the playlist page on Spotify.

![image](https://media.discordapp.net/attachments/404431223860232203/1075636368392331314/Screen_Shot_2023-02-15_at_3.51.09_PM.png?width=1646&height=904)

# Combine Page
Similar to the "Shuffle" page, the "Combine" page utilizes the Spotify to pull the user's playlist information, displaying the playlist names and images on a responsive grid. On this page, the playlists act as a checkbox input, where the user can select as many playlists as they would like combined. After selecting their playlists, the user will put in the name of the new playlist and click the "Combine Playlists" button.

![image](https://media.discordapp.net/attachments/404431223860232203/1075636368933408768/Screen_Shot_2023-02-15_at_3.51.42_PM.png?width=1646&height=904)

Similar to the "Shuffle" page, the user will be redirected to this success page. Here, the cover of the title and the playlist cover will be displayed. The user can click on the playlist cover to be redirected to the playlist page on Spotify.

![image](https://media.discordapp.net/attachments/404431223860232203/1075636369440907324/Screen_Shot_2023-02-15_at_3.52.08_PM.png?width=1641&height=904)
