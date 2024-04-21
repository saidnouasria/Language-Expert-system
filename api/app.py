from flask import Flask, render_template, request , session , redirect
from knowledge import language, description

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
# Define a dictionary to hold questions and their corresponding options
initial_question = "Why do you want to learn programming?"
questions = {
    "Why do you want to learn programming?": ["For my kids", "I don't know", "Make money", "Just for fun", "Im interested", "Improve myself"],
    "Which platform do you want to work on?": ["Doesn't matter", "Gaming", "Mobile", "Facebook", "Google", "Microsoft", "Apple", "Web", "Enterprise"],
    "Which mobile OS do you prefer?": ["iOS", "Android"],
    "Which web development role do you prefer?": ["Front-end", "Back-end"],
    "Do you want to work in a corporate environment or a startup?": ["Corporate", "Startup"],
    "What do you think about Microsoft?": ["I'm a fan", "Not bad", "Suck"],
    "Do you want to try something new?": ["Yes", "No"],
    "What is your favourite toy?": ["Lego", "Play-doh", "Old ugly"],
    "How would you prefer to learn?": ["Easy way", "Best way", "Harder way", "Hardest way"],
    "What is your favourite car?": ["Auto", "Manual"],
}

params = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        next_question, options = determine_next_question(user_answer)
        if next_question is None:
            print(params)
            result_language, result_description = language(params)
            params.clear()
            return render_template('results.html', language=result_language, description=result_description)
        return render_template('query_form.html', question=next_question, options=options,)
    else:
        next_question, options = get_initial_question()
        return render_template('query_form.html', question=next_question, options=options,)



def get_initial_question():
    initial_options = questions[initial_question]
    return initial_question, initial_options

def determine_next_question(answer):
    next_question = None
    options = None
    if answer == "For my kids":
        params.append("Why(John)")
        params.append("For_my_kids(John)")
    elif answer == "I don't know":
        params.append("Why(John)")
        params.append("I_dont_know(John)")
    elif answer == "Make money":
        params.append("Why(John)")
        params.append("Make_money(John)")
        next_question = "Which platform do you want to work on?"
        options = questions[next_question]
    elif answer == "Just for fun":
        params.append("Why(John)")
        params.append("Just_for_fun(John)")
        next_question = "How would you prefer to learn?"
        options = questions[next_question]
    elif answer == "Im interested":
        params.append("Why(John)")
        params.append("Im_interested(John)")
        next_question = "How would you prefer to learn?"
        options = questions[next_question]
    elif answer == "Improve myself":
        params.append("Why(John)")
        params.append("Improve_myself(John)")
        next_question = "How would you prefer to learn?"
        options = questions[next_question]
    elif answer == "Doesn't matter":
        params.append("WhichPlatform(John)")
        params.append("Does_t_matter(John)")
    elif answer == "Gaming":
        params.append("WhichPlatform(John)")
        params.append("Gaming(John)")
    elif answer == "Mobile":
        params.append("WhichPlatform(John)")
        params.append("Mobile(John)")
        next_question = "Which mobile OS do you prefer?"
        options = questions[next_question]
    elif answer == "IOS":
        params.append("WhichMobileOS(John)")
        params.append("Ios(John)")
    elif answer == "Android":
        params.append("WhichMobileOS(John)")
        params.append("Android(John)")
    elif answer == "Facebook":
        params.append("WhichPlatform(John)")
        params.append("Facebook(John)")
    elif answer == "Google":
        params.append("WhichPlatform(John)")
        params.append("Google(John)")
    elif answer == "Microsoft":
        params.append("WhichPlatform(John)")
        params.append("Microsoft(John)")
        next_question = "What do you think about Microsoft?"
        options = questions[next_question]
    elif answer == "I'm a fan":
        params.append("ThinkAboutMicrosoft(John)")
        params.append("Im_a_fan(John)")
    elif answer == "Not bad":
        params.append("ThinkAboutMicrosoft(John)")
        params.append("Not_bad(John)")
    elif answer == "Suck":
        params.append("ThinkAboutMicrosoft(John)")
        params.append("Suck(John)")
    elif answer == "Apple":
        params.append("WhichPlatform(John)")
        params.append("Apple(John)")
    elif answer == "Web":
        params.append("WhichPlatform(John)")
        params.append("Wweb(John)")
        next_question = "Which web development role do you prefer?"
        options = questions[next_question]
    elif answer == "Front-end":
        params.append("Web(John)")
        params.append("Front_end(John)")
    elif answer == "Back-end":
        params.append("Web(John)")
        params.append("Back_end(John)")
        next_question = "Do you want to work in a corporate environment or a startup?"
        options = questions[next_question]
    elif answer == "Corporate":
        params.append("WantToWorkFor(John)")
        params.append("Corporate(John)")
        next_question = "What do you think about Microsoft?"
        options = questions[next_question]
    elif answer == "Startup":
        params.append("WantToWorkFor(John)")
        params.append("Startup(John)")
        next_question = "Do you want to try something new?"
        options = questions[next_question]
    elif answer == "Yes":
        params.append("TrySomethingNew(John)")
        params.append("Yes(John)")
    elif answer == "No":
        params.append("TrySomethingNew(John)")
        params.append("No(John)")
        next_question = "What is your favourite toy?"
        options = questions[next_question]
    elif answer == "Lego":
        params.append("FavouriteToy(John)")
        params.append("Lego(John)")
    elif answer == "Play-doh":
        params.append("FavouriteToy(John)")
        params.append("Play_doh(John)")
    elif answer == "Old ugly":
        params.append("FavouriteToy(John)")
        params.append("Old_ugly(John)")
    elif answer == "Easy way":
        params.append("PreferToLearn(John)")
        params.append("Easy_way(John)")
    elif answer == "Best way":
        params.append("PreferToLearn(John)")
        params.append("Best_way(John)")
    elif answer == "Harder way":
        params.append("PreferToLearn(John)")
        params.append("Harder_way(John)")
        next_question = "What is your favourite car?"
        options = questions[next_question]
    elif answer == "Manual":
        params.append("Car(John)")
        params.append("Manual(John)")
    elif answer == "Auto": 
        params.append("Car(John)")
        params.append("Auto(John)")
    elif answer == "Hardest way":
        params.append("PreferToLearn(John)")
        params.append("Hardest_way(John)")
    else:
        next_question, options = get_initial_question()
    if next_question is None:
        return None, None
    return next_question, options

if __name__ == '__main__':
    app.run(debug=True)
