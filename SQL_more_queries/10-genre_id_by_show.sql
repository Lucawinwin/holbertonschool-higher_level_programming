-- Import the database dump from "htbn_0d_tvshows"
Select tv_shows.title, tv_show_genre.genre.id
From tv_shows
Join tv_show_genres On tv_shows.id = tv_show_genres.show_id
Order by tv_show.title, tv_show_genre.genre_id;
