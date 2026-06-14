"""
AI Movie Recommendation System
A rule-based recommendation system that suggests movies based on user preferences.

Author: Pratisha Macha
Project: DecodeLabs Internship - Project 3
Date: June 2026
"""

# ============================================================================
# STEP 1: CREATE MOVIE DATABASE
# ============================================================================

def create_movie_database():
    """
    Create a comprehensive movie database with genres and ratings.

    Each movie has:
    - Name
    - Genres (list) - can have multiple genres
    - Rating (1-5)
    - Year

    Returns:
        list: List of movie dictionaries
    """
    movies = [
        # Action Movies
        {
            "title": "The Dark Knight",
            "genres": ["action", "thriller", "crime"],
            "rating": 5,
            "year": 2008
        },
        {
            "title": "Mad Max: Fury Road",
            "genres": ["action", "adventure", "sci-fi"],
            "rating": 5,
            "year": 2015
        },
        {
            "title": "John Wick",
            "genres": ["action", "thriller"],
            "rating": 4,
            "year": 2014
        },
        {
            "title": "Mission Impossible",
            "genres": ["action", "thriller", "adventure"],
            "rating": 4,
            "year": 2018
        },

        # Comedy Movies
        {
            "title": "The Hangover",
            "genres": ["comedy"],
            "rating": 4,
            "year": 2009
        },
        {
            "title": "Superbad",
            "genres": ["comedy"],
            "rating": 4,
            "year": 2007
        },
        {
            "title": "Deadpool",
            "genres": ["comedy", "action", "adventure"],
            "rating": 5,
            "year": 2016
        },
        {
            "title": "The Grand Budapest Hotel",
            "genres": ["comedy", "drama"],
            "rating": 5,
            "year": 2014
        },

        # Drama Movies
        {
            "title": "The Shawshank Redemption",
            "genres": ["drama"],
            "rating": 5,
            "year": 1994
        },
        {
            "title": "Forrest Gump",
            "genres": ["drama", "romance"],
            "rating": 5,
            "year": 1994
        },
        {
            "title": "The Pursuit of Happyness",
            "genres": ["drama"],
            "rating": 5,
            "year": 2006
        },
        {
            "title": "12 Years a Slave",
            "genres": ["drama", "history"],
            "rating": 5,
            "year": 2013
        },

        # Thriller Movies
        {
            "title": "Inception",
            "genres": ["thriller", "sci-fi", "action"],
            "rating": 5,
            "year": 2010
        },
        {
            "title": "The Silence of the Lambs",
            "genres": ["thriller", "crime"],
            "rating": 5,
            "year": 1991
        },
        {
            "title": "Gone Girl",
            "genres": ["thriller", "drama"],
            "rating": 4,
            "year": 2014
        },
        {
            "title": "Shutter Island",
            "genres": ["thriller", "mystery"],
            "rating": 4,
            "year": 2010
        },

        # Sci-Fi Movies
        {
            "title": "Interstellar",
            "genres": ["sci-fi", "drama", "adventure"],
            "rating": 5,
            "year": 2014
        },
        {
            "title": "The Matrix",
            "genres": ["sci-fi", "action"],
            "rating": 5,
            "year": 1999
        },
        {
            "title": "Blade Runner 2049",
            "genres": ["sci-fi", "thriller"],
            "rating": 4,
            "year": 2017
        },
        {
            "title": "Arrival",
            "genres": ["sci-fi", "drama"],
            "rating": 4,
            "year": 2016
        },

        # Romance Movies
        {
            "title": "The Notebook",
            "genres": ["romance", "drama"],
            "rating": 4,
            "year": 2004
        },
        {
            "title": "La La Land",
            "genres": ["romance", "drama", "musical"],
            "rating": 5,
            "year": 2016
        },
        {
            "title": "Eternal Sunshine of the Spotless Mind",
            "genres": ["romance", "drama", "sci-fi"],
            "rating": 5,
            "year": 2004
        },
        {
            "title": "Pride and Prejudice",
            "genres": ["romance", "drama"],
            "rating": 4,
            "year": 2005
        },

        # Horror Movies
        {
            "title": "Get Out",
            "genres": ["horror", "thriller"],
            "rating": 5,
            "year": 2017
        },
        {
            "title": "A Quiet Place",
            "genres": ["horror", "thriller", "sci-fi"],
            "rating": 4,
            "year": 2018
        },
        {
            "title": "The Conjuring",
            "genres": ["horror"],
            "rating": 4,
            "year": 2013
        },

        # Adventure Movies
        {
            "title": "The Lord of the Rings",
            "genres": ["adventure", "fantasy"],
            "rating": 5,
            "year": 2001
        },
        {
            "title": "Indiana Jones",
            "genres": ["adventure", "action"],
            "rating": 5,
            "year": 1981
        },
        {
            "title": "Jurassic Park",
            "genres": ["adventure", "sci-fi", "thriller"],
            "rating": 5,
            "year": 1993
        }
    ]

    return movies


def get_available_genres(movies):
    """
    Extract all unique genres from the movie database.

    Args:
        movies: List of movie dictionaries

    Returns:
        set: Set of unique genres
    """
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return sorted(genres)


# ============================================================================
# STEP 2: DISPLAY WELCOME MESSAGE
# ============================================================================

def display_welcome():
    """Display welcome message and available genres."""
    print("\n")
    print("=" * 70)
    print("           AI MOVIE RECOMMENDATION SYSTEM")
    print("              Personalized Movie Suggestions")
    print("=" * 70)
    print()
    print("Welcome! I'll recommend movies based on your preferences.")
    print()


def display_available_genres(genres):
    """
    Display all available genres to the user.

    Args:
        genres: List of genre names
    """
    print("=" * 70)
    print("AVAILABLE GENRES")
    print("=" * 70)
    print()

    # Display genres in columns
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre.capitalize():<15}", end="")
        if i % 4 == 0:
            print()

    print("\n")
    print("Tip: You can enter multiple genres separated by commas")
    print("Example: action, comedy, thriller")
    print()


# ============================================================================
# STEP 3: GET USER PREFERENCES
# ============================================================================

def get_user_preferences():
    """
    Ask user for their movie preferences.

    Returns:
        list: List of preferred genres (lowercase)
    """
    print("=" * 70)
    print("YOUR PREFERENCES")
    print("=" * 70)
    print()

    user_input = input("Enter your favorite genre(s): ").strip()

    # Handle empty input
    if not user_input:
        print("No preferences entered. Showing all genres...")
        return []

    # Split by comma and clean up
    preferences = [genre.strip().lower() for genre in user_input.split(",")]

    print(f"\n[OK] Your preferences: {', '.join([p.capitalize() for p in preferences])}")
    print()

    return preferences


# ============================================================================
# STEP 4: RECOMMENDATION LOGIC
# ============================================================================

def calculate_match_score(movie, preferences):
    """
    Calculate how well a movie matches user preferences.

    Args:
        movie: Movie dictionary
        preferences: List of user preferred genres

    Returns:
        int: Match score (0-100)
    """
    if not preferences:
        return 50  # Neutral score if no preferences

    # Count matching genres
    matching_genres = sum(1 for genre in movie["genres"] if genre in preferences)

    # Calculate percentage match
    score = (matching_genres / len(preferences)) * 100

    # Bonus for high-rated movies
    score += (movie["rating"] * 2)

    return min(score, 100)  # Cap at 100


def get_recommendations(movies, preferences, min_score=30, limit=10):
    """
    Generate movie recommendations based on preferences.

    Args:
        movies: List of all movies
        preferences: List of user preferred genres
        min_score: Minimum match score to include
        limit: Maximum number of recommendations

    Returns:
        list: List of recommended movies with scores
    """
    recommendations = []

    for movie in movies:
        score = calculate_match_score(movie, preferences)

        if score >= min_score:
            recommendations.append({
                "movie": movie,
                "score": score
            })

    # Sort by score (highest first)
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    # Limit results
    return recommendations[:limit]


def get_alternative_recommendations(movies, preferences, limit=5):
    """
    Get alternative recommendations with lower match scores.

    Args:
        movies: List of all movies
        preferences: List of user preferred genres
        limit: Maximum number of alternatives

    Returns:
        list: List of alternative movies
    """
    alternatives = []

    for movie in movies:
        score = calculate_match_score(movie, preferences)

        # Look for movies with moderate scores
        if 20 <= score < 30:
            alternatives.append({
                "movie": movie,
                "score": score
            })

    # Sort by score
    alternatives.sort(key=lambda x: x["score"], reverse=True)

    return alternatives[:limit]


# ============================================================================
# STEP 5: DISPLAY RECOMMENDATIONS
# ============================================================================

def display_recommendations(recommendations, title="RECOMMENDED MOVIES"):
    """
    Display movie recommendations in a formatted way.

    Args:
        recommendations: List of recommendation dictionaries
        title: Title for the recommendations section
    """
    if not recommendations:
        print("=" * 70)
        print(title)
        print("=" * 70)
        print()
        print("Sorry, no movies found matching your preferences.")
        print("Try different genres or check available genres above.")
        print()
        return

    print("=" * 70)
    print(title)
    print("=" * 70)
    print()

    for i, rec in enumerate(recommendations, 1):
        movie = rec["movie"]
        score = rec["score"]

        print(f"{i}. {movie['title']}")
        print(f"   Genres: {', '.join([g.capitalize() for g in movie['genres']])}")
        print(f"   Rating: {'*' * movie['rating']}{'-' * (5 - movie['rating'])} ({movie['rating']}/5)")
        print(f"   Year: {movie['year']}")
        print(f"   Match Score: {score:.0f}%")
        print()


def display_statistics(recommendations):
    """
    Display recommendation statistics.

    Args:
        recommendations: List of recommendation dictionaries
    """
    if not recommendations:
        return

    print("=" * 70)
    print("RECOMMENDATION STATISTICS")
    print("=" * 70)
    print()

    total = len(recommendations)
    avg_score = sum(r["score"] for r in recommendations) / total
    avg_rating = sum(r["movie"]["rating"] for r in recommendations) / total

    print(f"Total Recommendations: {total}")
    print(f"Average Match Score: {avg_score:.1f}%")
    print(f"Average Movie Rating: {avg_rating:.1f}/5.0")
    print()


# ============================================================================
# STEP 6: HANDLE NO MATCHES
# ============================================================================

def handle_no_matches(movies, preferences):
    """
    Handle cases where no exact matches are found.

    Args:
        movies: List of all movies
        preferences: User preferences
    """
    print("=" * 70)
    print("NO EXACT MATCHES FOUND")
    print("=" * 70)
    print()
    print("Don't worry! Here are some alternatives you might enjoy:")
    print()

    # Get alternative recommendations with lower threshold
    alternatives = get_recommendations(movies, preferences, min_score=10, limit=5)

    if alternatives:
        display_recommendations(alternatives, "ALTERNATIVE SUGGESTIONS")
    else:
        # Show top-rated movies if still no matches
        print("Here are some highly-rated movies across all genres:")
        print()

        top_rated = sorted(movies, key=lambda x: x["rating"], reverse=True)[:5]
        display_recommendations(
            [{"movie": m, "score": 50} for m in top_rated],
            "TOP-RATED MOVIES"
        )


# ============================================================================
# STEP 7: MAIN RECOMMENDATION LOOP
# ============================================================================

def run_recommender():
    """Main function to run the recommendation system."""

    # Display welcome message
    display_welcome()

    # Create movie database
    movies = create_movie_database()
    genres = get_available_genres(movies)

    print(f"[OK] Loaded {len(movies)} movies across {len(genres)} genres")
    print()

    # Main loop
    while True:
        # Display available genres
        display_available_genres(genres)

        # Get user preferences
        preferences = get_user_preferences()

        # Generate recommendations
        recommendations = get_recommendations(movies, preferences)

        # Display results
        if recommendations:
            display_recommendations(recommendations)
            display_statistics(recommendations)

            # Get alternatives
            alternatives = get_alternative_recommendations(movies, preferences)
            if alternatives:
                display_recommendations(alternatives, "YOU MIGHT ALSO LIKE")
        else:
            handle_no_matches(movies, preferences)

        # Ask if user wants more recommendations
        print("=" * 70)
        choice = input("Would you like more recommendations? (yes/no): ").strip().lower()

        if choice in ["no", "n", "exit", "quit"]:
            print()
            print("=" * 70)
            print("Thank you for using AI Movie Recommender!")
            print("Enjoy your movies! [Movies]")
            print("=" * 70)
            print()
            break

        print("\n")


# ============================================================================
# RUN THE PROGRAM
# ============================================================================

if __name__ == "__main__":
    run_recommender()
