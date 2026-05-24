from app.models.schemas import AnalysisResult, ScreenTimeInput


PROMPT_VERSION = "v1"

ALTERNATE_REALITY_INSTRUCTIONS = """
You are the cinematic narrator and behavioral coach inside Doomscroll Reverser.
Your job is to show the user the opportunity cost of doomscrolling without shaming them.
Tone: emotional, cinematic, motivational, slightly scary, realistic, Gen Z-aware.
Avoid: medical diagnosis, hopelessness, insults, fake certainty, toxic productivity.
Make the future feel tangible. Balance the warning with a clear next move.
Return valid JSON only with these keys:
headline, cinematic_summary, alternate_career, skills_learned, income_potential,
projects_built, fitness_transformation, confidence_level, first_30_days,
warning, action_plan.
Lists must contain 3 to 5 concise strings.
"""


def build_alternate_reality_prompt(screen_time: ScreenTimeInput, analysis: AnalysisResult) -> str:
    goals = screen_time.daily_goals.strip() or "career growth, better health, and focused creative work"
    return f"""
Create an alternate reality report for a user with these daily habits:
- Instagram: {screen_time.instagram_hours} hours
- YouTube: {screen_time.youtube_hours} hours
- Reels/Shorts/TikTok: {screen_time.short_form_hours} hours
- Gaming: {screen_time.gaming_hours} hours
- Sleep: {screen_time.sleep_hours} hours
- Goals: {goals}

Computed annual opportunity cost:
- Yearly hours wasted: {analysis.yearly_hours_wasted}
- Estimated money equivalent lost: ${analysis.money_lost}
- Books not read: {analysis.books_not_read}
- Workouts skipped: {analysis.workouts_skipped}
- Projects not completed: {analysis.projects_not_completed}
- Interview prep sessions lost: {analysis.interview_prep_sessions_lost}
- Brain rot percentage: {analysis.brain_rot_percentage}%
- Doom level: {analysis.doom_level}

Write as if a Netflix documentary freeze-frame revealed the user's better timeline.
Keep it specific and plausible for the next 12 months.
"""

