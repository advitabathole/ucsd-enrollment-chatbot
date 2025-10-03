def get_response(user_input):
    user_input = user_input.lower()
    if "pass 1" in user_input:
        return "📅 Pass 1 enrollment usually happens about a week before Pass 2."
    elif "pass 2" in user_input:
        return "⏰ Pass 2 enrollment opens after Pass 1 ends. Check TritonLink for exact time."
    elif "units" in user_input:
        return "🎓 First-years can enroll in up to 19.5 units after enrollment begins."
    elif "hello" in user_input or "hi" in user_input:
        return "Hey Triton 🐬! Need help with enrollment?"
    else:
        return "🤔 I’m not sure yet. Try asking about pass times, units, or prerequisites."
