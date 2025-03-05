-- Import from database dump of hbnt_0d_tvshows
Select tv_show.title, tv_show_genres.genre_id
From tv_show
Left Join tv_show_genres On tv_shows.id = tv_show_genres.show_id
Order BY tv_shows.title, tv_show_genres.genre_id;
