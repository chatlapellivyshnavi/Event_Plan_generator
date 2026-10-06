'''import streamlit as st
import torch
import random
from diffusers import StableDiffusionPipeline


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Event Plan Generator",
    page_icon="🎉",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #FFF0F5;
}

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎉 Event Plan Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create a complete event plan and generate an AI event poster ✨</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# LOAD AI IMAGE MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():

    pipe = StableDiffusionPipeline.from_pretrained(
        "segmind/tiny-sd",
        torch_dtype=torch.float32
    )

    return pipe


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

st.session_state.setdefault("surprise_prompt", "")
st.session_state.setdefault("generated_plan", "")
st.session_state.setdefault("generated_image", None)


# --------------------------------------------------
# RANDOM EVENT PROMPTS
# --------------------------------------------------

random_events = [
    "College Cultural Fest",
    "Technology Fest",
    "Hackathon",
    "Birthday Party",
    "College Farewell",
    "Freshers Party",
    "Sports Day",
    "Music Festival",
    "Science Exhibition",
    "Startup Event"
]

random_themes = [
    "Futuristic",
    "Elegant",
    "Colorful",
    "Technology",
    "Retro",
    "Nature",
    "Neon",
    "Minimal",
    "Royal",
    "Space"
]


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Event Settings")

    event_type = st.selectbox(
        "🎪 Event Type",
        random_events
    )

    attendees = st.number_input(
        "👥 Number of Attendees",
        min_value=10,
        max_value=5000,
        value=100,
        step=10
    )

    duration = st.slider(
        "⏰ Event Duration (hours)",
        min_value=1,
        max_value=12,
        value=4
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1000,
        max_value=1000000,
        value=50000,
        step=5000
    )

    theme = st.selectbox(
        "🎨 Event Theme",
        random_themes
    )

    st.divider()

    surprise = st.button(
        "✨ Surprise Me"
    )


# --------------------------------------------------
# SURPRISE ME
# --------------------------------------------------

if surprise:

    random_event = random.choice(random_events)
    random_theme = random.choice(random_themes)

    st.session_state.surprise_prompt = (
        f"{random_event} with a {random_theme} theme"
    )

    st.info(
        f"🎲 Random Event: {st.session_state.surprise_prompt}"
    )


# --------------------------------------------------
# MAIN INPUT AREA
# --------------------------------------------------

left, right = st.columns(2)


with left:

    st.subheader("📝 Event Details")

    event_name = st.text_input(
        "Event Name",
        placeholder="Example: Technova 2026"
    )

    location = st.text_input(
        "📍 Location",
        placeholder="Example: College Auditorium"
    )

    organizer = st.text_input(
        "👤 Organizer",
        placeholder="Example: Data Science Department"
    )

    activities = st.text_area(
        "🎯 Special Activities",
        placeholder="Example: Coding competition, music, dance, games..."
    )

    generate_plan = st.button(
        "🚀 Generate Event Plan",
        use_container_width=True
    )


# --------------------------------------------------
# EVENT PLAN GENERATOR
# --------------------------------------------------

if generate_plan:

    if event_name == "":
        event_name = event_type

    if location == "":
        location = "College Campus"

    if organizer == "":
        organizer = "Event Organizing Team"

    if activities == "":
        activities = "Games, music, cultural activities and networking"


    # -----------------------------
    # BUDGET CALCULATION
    # -----------------------------

    food_budget = int(budget * 0.30)
    decoration_budget = int(budget * 0.15)
    venue_budget = int(budget * 0.20)
    entertainment_budget = int(budget * 0.15)
    marketing_budget = int(budget * 0.10)
    emergency_budget = int(budget * 0.10)


    # -----------------------------
    # EVENT SCHEDULE
    # -----------------------------

    schedule = []

    schedule.append("09:00 AM - Guest Registration")

    if duration >= 2:
        schedule.append("10:00 AM - Welcome and Opening Ceremony")

    if duration >= 3:
        schedule.append("11:00 AM - Main Event Activities")

    if duration >= 4:
        schedule.append("12:00 PM - Interactive Games / Competitions")

    if duration >= 5:
        schedule.append("01:00 PM - Lunch / Refreshments")

    if duration >= 6:
        schedule.append("02:00 PM - Cultural and Entertainment Activities")

    if duration >= 7:
        schedule.append("03:00 PM - Special Guest Session")

    schedule.append("Final Session - Prize Distribution and Vote of Thanks")


    # -----------------------------
    # EVENT PLAN
    # -----------------------------

    plan = f"""
# 🎉 {event_name}

## 📌 Event Overview

**Event Type:** {event_type}

**Theme:** {theme}

**Location:** {location}

**Organizer:** {organizer}

**Expected Attendees:** {attendees}

**Duration:** {duration} hours

**Total Budget:** ₹{budget:,}


## 🕒 Event Schedule

"""

    for item in schedule:
        plan += f"- {item}\n"

    plan += f"""

## 🎯 Activities

{activities}


## 🎨 Decoration Plan

- {theme} themed entrance
- Stage decoration
- Welcome banner
- Photo booth
- LED / lighting setup
- Direction boards
- Seating arrangement


## 🍴 Food Plan

- Welcome drinks
- Snacks
- Main course
- Dessert
- Water stations


## 🎤 Entertainment

- Music system
- DJ / live music
- Interactive games
- Cultural performances
- Audience activities


## 📢 Marketing Plan

- Social media promotion
- Posters around campus
- WhatsApp announcements
- Registration form
- Digital invitation


## 💰 Estimated Budget

| Category | Estimated Cost |
|---|---:|
| 🍴 Food | ₹{food_budget:,} |
| 🎨 Decoration | ₹{decoration_budget:,} |
| 🏢 Venue | ₹{venue_budget:,} |
| 🎤 Entertainment | ₹{entertainment_budget:,} |
| 📢 Marketing | ₹{marketing_budget:,} |
| 🛟 Emergency | ₹{emergency_budget:,} |
| **Total** | **₹{budget:,}** |


## 👥 Organizing Team

- Event Coordinator
- Registration Team
- Decoration Team
- Food Management Team
- Technical Team
- Photography Team
- Security Team
- Volunteer Team


## ✅ Final Checklist

- [ ] Venue booked
- [ ] Guest list prepared
- [ ] Invitations sent
- [ ] Decorations arranged
- [ ] Food confirmed
- [ ] Sound system checked
- [ ] Volunteers assigned
- [ ] Emergency arrangements ready
- [ ] Certificates / prizes prepared
- [ ] Event schedule printed
"""

    st.session_state.generated_plan = plan


# --------------------------------------------------
# DISPLAY EVENT PLAN
# --------------------------------------------------

with right:

    st.subheader("📋 Generated Event Plan")

    if st.session_state.generated_plan:

        st.markdown(
            st.session_state.generated_plan
        )

    else:

        st.info(
            "Your generated event plan will appear here."
        )


# --------------------------------------------------
# AI EVENT POSTER
# --------------------------------------------------

st.divider()

st.header("🖼️ AI Event Poster Generator")

poster_prompt = st.text_input(
    "Enter a poster idea",
    value=(
        f"{event_type}, {theme} theme, "
        "beautiful college event, colorful decorations, "
        "professional event poster"
    )
)


generate_image = st.button(
    "🎨 Generate AI Event Poster"
)


if generate_image:

    try:

        with st.spinner(
            "🤖 AI is creating your event poster..."
        ):

            pipe = load_model()

            image = pipe(
                poster_prompt,
                num_inference_steps=25
            ).images[0]

            st.session_state.generated_image = image

    except Exception as e:

        st.error(
            "Unable to generate the image. "
            "Please make sure the required libraries and model are installed."
        )

        st.write(e)


# --------------------------------------------------
# DISPLAY IMAGE
# --------------------------------------------------

if st.session_state.generated_image is not None:

    st.subheader("✨ Generated Event Poster")

    st.image(
        st.session_state.generated_image,
        caption="AI Generated Event Poster",
        use_container_width=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🎉 Event Plan Generator | Powered by Streamlit + Stable Diffusion"
)'''




import streamlit as st
import torch
import random

from diffusers import StableDiffusionPipeline, DDIMScheduler


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Event Plan Generator",
    page_icon="🎉",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #FFF0F5;
}

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🎉 Event Plan Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create a complete event plan and generate an AI event poster ✨'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOAD AI IMAGE MODEL
# ============================================================

@st.cache_resource
def load_model():

    pipe = StableDiffusionPipeline.from_pretrained(
        "segmind/tiny-sd",
        torch_dtype=torch.float32
    )

    # Change scheduler to DDIM
    # This avoids the DPM Solver error
    pipe.scheduler = DDIMScheduler.from_config(
        pipe.scheduler.config
    )

    return pipe


# ============================================================
# SESSION STATE
# ============================================================

st.session_state.setdefault(
    "surprise_prompt",
    ""
)

st.session_state.setdefault(
    "generated_plan",
    ""
)

st.session_state.setdefault(
    "generated_image",
    None
)


# ============================================================
# RANDOM EVENT OPTIONS
# ============================================================

random_events = [
    "College Cultural Fest",
    "Technology Fest",
    "Hackathon",
    "Birthday Party",
    "College Farewell",
    "Freshers Party",
    "Sports Day",
    "Music Festival",
    "Science Exhibition",
    "Startup Event"
]


random_themes = [
    "Futuristic",
    "Elegant",
    "Colorful",
    "Technology",
    "Retro",
    "Nature",
    "Neon",
    "Minimal",
    "Royal",
    "Space"
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Event Settings")

    event_type = st.selectbox(
        "🎪 Event Type",
        random_events
    )

    attendees = st.number_input(
        "👥 Number of Attendees",
        min_value=10,
        max_value=5000,
        value=100,
        step=10
    )

    duration = st.slider(
        "⏰ Event Duration (hours)",
        min_value=1,
        max_value=12,
        value=4
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1000,
        max_value=1000000,
        value=50000,
        step=5000
    )

    theme = st.selectbox(
        "🎨 Event Theme",
        random_themes
    )

    st.divider()

    surprise = st.button(
        "✨ Surprise Me",
        use_container_width=True
    )


# ============================================================
# SURPRISE ME
# ============================================================

if surprise:

    random_event = random.choice(
        random_events
    )

    random_theme = random.choice(
        random_themes
    )

    st.session_state.surprise_prompt = (
        f"{random_event} with a {random_theme} theme"
    )

    st.info(
        f"🎲 Random Event: "
        f"{st.session_state.surprise_prompt}"
    )


# ============================================================
# MAIN INPUT AREA
# ============================================================

left, right = st.columns(2)


with left:

    st.subheader("📝 Event Details")

    event_name = st.text_input(
        "Event Name",
        placeholder="Example: Technova 2026"
    )

    location = st.text_input(
        "📍 Location",
        placeholder="Example: College Auditorium"
    )

    organizer = st.text_input(
        "👤 Organizer",
        placeholder="Example: Data Science Department"
    )

    activities = st.text_area(
        "🎯 Special Activities",
        placeholder=(
            "Example: Coding competition, "
            "music, dance, games..."
        )
    )

    generate_plan = st.button(
        "🚀 Generate Event Plan",
        use_container_width=True
    )


# ============================================================
# EVENT PLAN GENERATOR
# ============================================================

if generate_plan:

    if event_name == "":
        event_name = event_type

    if location == "":
        location = "College Campus"

    if organizer == "":
        organizer = "Event Organizing Team"

    if activities == "":
        activities = (
            "Games, music, cultural activities "
            "and networking"
        )


    # --------------------------------------------------------
    # BUDGET
    # --------------------------------------------------------

    food_budget = int(budget * 0.30)
    decoration_budget = int(budget * 0.15)
    venue_budget = int(budget * 0.20)
    entertainment_budget = int(budget * 0.15)
    marketing_budget = int(budget * 0.10)
    emergency_budget = int(budget * 0.10)


    # --------------------------------------------------------
    # SCHEDULE
    # --------------------------------------------------------

    schedule = []

    schedule.append(
        "09:00 AM - Guest Registration"
    )

    if duration >= 2:
        schedule.append(
            "10:00 AM - Welcome and Opening Ceremony"
        )

    if duration >= 3:
        schedule.append(
            "11:00 AM - Main Event Activities"
        )

    if duration >= 4:
        schedule.append(
            "12:00 PM - Interactive Games / Competitions"
        )

    if duration >= 5:
        schedule.append(
            "01:00 PM - Lunch / Refreshments"
        )

    if duration >= 6:
        schedule.append(
            "02:00 PM - Cultural and Entertainment Activities"
        )

    if duration >= 7:
        schedule.append(
            "03:00 PM - Special Guest Session"
        )

    schedule.append(
        "Final Session - Prize Distribution and Vote of Thanks"
    )


    # --------------------------------------------------------
    # CREATE EVENT PLAN
    # --------------------------------------------------------

    plan = f"""
# 🎉 {event_name}

## 📌 Event Overview

**Event Type:** {event_type}

**Theme:** {theme}

**Location:** {location}

**Organizer:** {organizer}

**Expected Attendees:** {attendees}

**Duration:** {duration} hours

**Total Budget:** ₹{budget:,}


## 🕒 Event Schedule

"""

    for item in schedule:
        plan += f"- {item}\n"


    plan += f"""

## 🎯 Activities

{activities}


## 🎨 Decoration Plan

- {theme} themed entrance
- Stage decoration
- Welcome banner
- Photo booth
- LED / lighting setup
- Direction boards
- Seating arrangement


## 🍴 Food Plan

- Welcome drinks
- Snacks
- Main course
- Dessert
- Water stations


## 🎤 Entertainment

- Music system
- DJ / live music
- Interactive games
- Cultural performances
- Audience activities


## 📢 Marketing Plan

- Social media promotion
- Posters around campus
- WhatsApp announcements
- Registration form
- Digital invitation


## 💰 Estimated Budget

| Category | Estimated Cost |
|---|---:|
| 🍴 Food | ₹{food_budget:,} |
| 🎨 Decoration | ₹{decoration_budget:,} |
| 🏢 Venue | ₹{venue_budget:,} |
| 🎤 Entertainment | ₹{entertainment_budget:,} |
| 📢 Marketing | ₹{marketing_budget:,} |
| 🛟 Emergency | ₹{emergency_budget:,} |
| **Total** | **₹{budget:,}** |


## 👥 Organizing Team

- Event Coordinator
- Registration Team
- Decoration Team
- Food Management Team
- Technical Team
- Photography Team
- Security Team
- Volunteer Team


## ✅ Final Checklist

- [ ] Venue booked
- [ ] Guest list prepared
- [ ] Invitations sent
- [ ] Decorations arranged
- [ ] Food confirmed
- [ ] Sound system checked
- [ ] Volunteers assigned
- [ ] Emergency arrangements ready
- [ ] Certificates / prizes prepared
- [ ] Event schedule printed
"""

    st.session_state.generated_plan = plan


# ============================================================
# DISPLAY EVENT PLAN
# ============================================================

with right:

    st.subheader("📋 Generated Event Plan")

    if st.session_state.generated_plan:

        st.markdown(
            st.session_state.generated_plan
        )

    else:

        st.info(
            "Your generated event plan will appear here."
        )


# ============================================================
# AI EVENT POSTER
# ============================================================

st.divider()

st.header("🖼️ AI Event Poster Generator")

poster_prompt = st.text_input(
    "Enter your poster idea",
    value=(
        f"{event_type}, {theme} theme, "
        "beautiful college event, "
        "colorful decorations, "
        "professional event poster"
    )
)


# ============================================================
# GENERATE IMAGE BUTTON
# ============================================================

generate_image = st.button(
    "🎨 Generate AI Event Poster",
    use_container_width=True
)


# ============================================================
# IMAGE GENERATION
# ============================================================

if generate_image:

    if poster_prompt.strip() == "":
        st.warning(
            "Please enter a poster idea first."
        )

    else:

        try:

            with st.spinner(
                "🤖 AI is generating your event poster..."
            ):

                # Load Stable Diffusion
                pipe = load_model()

                # Generate image
                result = pipe(
                    prompt=poster_prompt,
                    num_inference_steps=20,
                    guidance_scale=7.5
                )

                image = result.images[0]

                # Store image
                st.session_state.generated_image = image


            st.success(
                "🎉 Event poster generated successfully!"
            )

        except Exception as e:

            st.error(
                "❌ Image generation failed."
            )

            st.write(
                "Error details:"
            )

            st.code(
                str(e)
            )


# ============================================================
# DISPLAY GENERATED IMAGE
# ============================================================

if st.session_state.generated_image is not None:

    st.subheader(
        "✨ Your AI Generated Event Poster"
    )

    st.image(
        st.session_state.generated_image,
        caption="AI Generated Event Poster",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎉 Event Plan Generator | "
    "Powered by Streamlit + Stable Diffusion"
)