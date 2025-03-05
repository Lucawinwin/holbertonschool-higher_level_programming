--Import the database dump from hbtn_0d_tvshows
Select tv_genres.name
From tv_genres
Join tv_show_genres On tv_genres.id = tv_show_genres.genre.id
Join tv_shows On tv_show_genres.show_id = tv_shows.id
Where tv_shows.title = 'Dexter'
Order by tv_genres.name
