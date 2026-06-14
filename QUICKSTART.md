# Quick Start Guide

## ⚡ Run in 2 Minutes!

---

## Step 1: Check Python

```bash
python --version
```

Should show: Python 3.6 or higher

---

## Step 2: Navigate to Project

```bash
cd D:\DecodeLabs\Project-3-Recommendation-System
```

---

## Step 3: Run the Recommender

```bash
python movie_recommender.py
```

---

## 🎬 How to Use

### 1. View Available Genres
The system will show all available genres automatically.

### 2. Enter Your Preferences
```
Enter your favorite genre(s): action
```

Or multiple genres:
```
Enter your favorite genre(s): action, comedy, thriller
```

### 3. Get Recommendations
The system will show:
- Top matching movies
- Match scores (0-100%)
- Movie ratings
- Year of release
- Alternative suggestions

### 4. Get More Recommendations
```
Would you like more recommendations? (yes/no): yes
```

---

## 📝 Sample Session

```
======================================================================
           AI MOVIE RECOMMENDATION SYSTEM
              Personalized Movie Suggestions
======================================================================

Welcome! I'll recommend movies based on your preferences.

[OK] Loaded 30 movies across 13 genres

======================================================================
AVAILABLE GENRES
======================================================================

1. Action         2. Adventure      3. Comedy         4. Crime          
5. Drama          6. Fantasy        7. History        8. Horror         
9. Musical        10. Mystery        11. Romance        12. Sci-fi         
13. Thriller       

======================================================================
YOUR PREFERENCES
======================================================================

Enter your favorite genre(s): sci-fi

[OK] Your preferences: Sci-fi

======================================================================
RECOMMENDED MOVIES
======================================================================

1. Interstellar
   Genres: Sci-fi, Drama, Adventure
   Rating: ***** (5/5)
   Year: 2014
   Match Score: 100%

2. The Matrix
   Genres: Sci-fi, Action
   Rating: ***** (5/5)
   Year: 1999
   Match Score: 100%

3. Blade Runner 2049
   Genres: Sci-fi, Thriller
   Rating: ****- (4/5)
   Year: 2017
   Match Score: 100%

======================================================================
RECOMMENDATION STATISTICS
======================================================================

Total Recommendations: 8
Average Match Score: 92.5%
Average Movie Rating: 4.6/5.0

======================================================================
Would you like more recommendations? (yes/no): no

======================================================================
Thank you for using AI Movie Recommender!
Enjoy your movies!
======================================================================
```

---

## 💡 Tips

### Multiple Genres
```
Enter your favorite genre(s): action, comedy
```
Will find movies that match EITHER genre.

### Case Insensitive
```
ACTION = action = Action = AcTiOn
```
All work the same!

### Empty Input
Pressing Enter without typing shows all genres.

### Exit
Type any of these to exit:
- `no`
- `n`
- `exit`
- `quit`

---

## 🎯 Understanding Results

### Match Score
- **100%**: Perfect match (all your genres present)
- **60-99%**: Good match (some genres match + high rating)
- **30-59%**: Moderate match (alternative suggestions)
- **0-29%**: Low match (not shown unless no alternatives)

### Rating
```
***** = 5/5 (Excellent)
****- = 4/5 (Great)
***-- = 3/5 (Good)
**--- = 2/5 (Fair)
*---- = 1/5 (Poor)
```

---

## ⏱️ Time Required

- **First run**: 1 minute
- **Per recommendation**: 10 seconds
- **Learning the system**: 5 minutes

**Total**: ~5 minutes to full proficiency!

---

## ❓ Troubleshooting

### Issue: "python is not recognized"
**Solution**: Try `python3`
```bash
python3 movie_recommender.py
```

### Issue: No recommendations shown
**Solution**: Try broader genres
```
Instead of: musical
Try: comedy, drama
```

### Issue: Want to exit
**Solution**: Type `no` or `quit` when asked for more recommendations

---

## 🚀 What's Next?

After running successfully:

1. **Try different genres** - Experiment with combinations
2. **Check match scores** - See how the algorithm works
3. **Read the code** - Open `movie_recommender.py`
4. **Modify movies** - Add your favorite movies to the database

---

**Ready to run? Just type:**
```bash
python movie_recommender.py
```

**Enjoy your personalized movie recommendations! 🎬**
