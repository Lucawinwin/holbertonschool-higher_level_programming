--Import the database dump from hbtn_0d_tvshows
Select tv_shows.title
From tv_shows
Join tv_show_genres On tv_show_genres.show_id = tv_show.id
Join tv_genres On tv_genres.id = tv_show_genres.genre_id
Where tv_genres.name = 'Comedy'
Order by tv_shows.title
