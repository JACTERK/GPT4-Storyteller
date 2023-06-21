# Made with <3 by Jacob Terkuc


# --------- Name that will trigger bot in discord -------- #

trigger_name = "john"

# --- Character reference for bot to function properly --- #

prompt = "Your name is Todd Howard. You are a video game developer at Bethesda who will respond to questions in an " \
         "egotistical, arrogant, short and witty manner. You like to use the phrase 'it just works', when in reality, " \
         "you know it does not 'just work' like you said. You like to overemphasise the successes of the video games " \
         "you have created. You lie about most things you talk about, and become angry and defensive when people try " \
         "to push back on you."
prompt = "Your name is " + trigger_name + ". you are a good person who will respond to questions in a kind, " \
         "understanding, and helpful manner. You "
default_response = "It just works..."

# ----------------- Text Queue Settings ------------------ #

# Number of human and ai responses that will be queued. (Note: Higher values will consume more credits)

q_len = 3
q_expire = 10  # 5 minutes (time in seconds) (TODO: IMPLEMENT)

# ------- Sleep settings for bot typing indicator. ------- #   TODO: FIX

# Min/max time before typing indicator (in seconds)

time_to_wait_min = 0
time_to_wait_max = 1

# Time multiplier bot will send typing indicator (in seconds)
# The calculation is done by taking the length of the message and dividing it by this value

t_speed_multiplier = 2

# ---------- Configuration for the OpenAI Model ---------- #

# Advanced users only: If you don't know what these do it's best to leave them.

model_checker = "gpt-3.5-turbo"
model_gen = "gpt-4"

# --------------- Image Generation Settings -------------- #

# True: Generate images
# False: Disable image generation

generate_images = True

# -------------------------------------------------------- #

debug_mode = True
