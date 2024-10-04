from db.models import Movie


def get_movies(genres_ids: int = None, actors_ids: int = None) -> None:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None
) -> str:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
        genres_ids=genres_ids,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie