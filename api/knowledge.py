from aima3 import logic
from aima3.logic import *


def language(list):
    kb = FolKB()
    #rules
    
    kb.tell(expr("Why(X) & For_my_kids(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & I_dont_know(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Does_t_matter(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Gaming(X) ==> Cpp(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Mobile(X) & WhichMobileOS(X) & Ios(X) ==> Objectivec(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Mobile(X) & WhichMobileOS(X) & Android(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Facebook(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Google(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Microsoft(X) ==> Csharp(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Apple(X) ==> Objectivec(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Front_end(X) ==> JavaScript(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Corporate(X) & ThinkAboutMicrosoft(X) & Im_a_fan(X) ==> Csharp(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Corporate(X) & ThinkAboutMicrosoft(X) & Not_bad(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Corporate(X) & ThinkAboutMicrosoft(X) & Suck(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Startup(X) & TrySomethingNew(X) & Yes(X) ==> JavaScript(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Startup(X) & TrySomethingNew(X) & No(X) & FavouriteToy(X) & Lego(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Startup(X) & TrySomethingNew(X) & No(X) & FavouriteToy(X) & Play_doh(X) ==> Ruby(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Wweb(X) & Web(X) & Back_end(X) & WantToWorkFor(X) & Startup(X) & TrySomethingNew(X) & No(X) & FavouriteToy(X) & Old_ugly(X) ==> Php(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WhichPlatform(X) & Enterprise(X) & ThinkAboutMicrosoft(X) & Im_a_fan(X) ==> Csharp(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WantToWorkFor(X) & Enterprise(X) & ThinkAboutMicrosoft(X) & Not_bad(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Make_money(X) & WantToWorkFor(X) & Enterprise(X) & ThinkAboutMicrosoft(X) & Suck(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Just_for_fun(X) & PreferToLearn(X) & Easy_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Just_for_fun(X) & PreferToLearn(X) & Best_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Just_for_fun(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Auto(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Just_for_fun(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Manual(X) ==> C(X)"))
    kb.tell(expr("Why(X) & Just_for_fun(X) & PreferToLearn(X) & Hardest_way(X) ==> Cpp(X)"))
    kb.tell(expr("Why(X) & Im_interested(X) & PreferToLearn(X) & Easy_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Im_interested(X) & PreferToLearn(X) & Best_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Im_interested(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Auto(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Im_interested(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Manual(X) ==> C(X)"))
    kb.tell(expr("Why(X) & Im_interested(X) & PreferToLearn(X) & Hardest_way(X) ==> Cpp(X)"))
    kb.tell(expr("Why(X) & Improve_myself(X) & PreferToLearn(X) & Easy_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Improve_myself(X) & PreferToLearn(X) & Best_way(X) ==> Python(X)"))
    kb.tell(expr("Why(X) & Improve_myself(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Auto(X) ==> Java(X)"))
    kb.tell(expr("Why(X) & Improve_myself(X) & PreferToLearn(X) & Harder_way(X) & Car(X) & Manual(X) ==> C(X)"))
    kb.tell(expr("Why(X) & Improve_myself(X) & PreferToLearn(X) & Hardest_way(X) ==> Cpp(X)"))


    memory = {}


    agenda = []
    for p in list:
        agenda.append(expr(p))
    # Run the expert system
    seen = set()  # Keep track of the conditions already processed
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue  # Skip the condition if it has already been processed
        seen.add(p)
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
        else:
            print(f'{p} is false.')
            memory[p] = False

        if memory.get(expr('Why(John)'), False) and memory.get(expr('For_my_kids(John)'), False) :
            return "you should learn python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('I_dont_know(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Does_t_matter(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Gaming(John)'), False) :
            return "you should learn C++", description('Cpp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Mobile(John)'), False) and memory.get(expr('WhichMobileOS(John)'), False) and memory.get(expr('Ios(John)'), False) :
            return "you should learn Objective-C", description('Objectivec')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Mobile(John)'), False) and memory.get(expr('WhichMobileOS(John)'), False) and memory.get(expr('Android(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Facebook(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Google(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Microsoft(John)'), False) :
            return "you should learn C#", description('Csharp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Apple(John)'), False) :
            return "you should learn Objective-C", description('Objectivec')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Front_end(John)'), False) :
            return "you should learn JavaScript", description('JavaScript')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Corporate(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Im_a_fan(John)'), False) :
            return "you should learn C#", description('Csharp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Corporate(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Not_bad(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Corporate(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Suck(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Startup(John)'), False) and memory.get(expr('TrySomethingNew(John)'), False) and memory.get(expr('Yes(John)'), False) :
            return "you should learn JavaScript", description('JavaScript')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Startup(John)'), False) and memory.get(expr('TrySomethingNew(John)'), False) and memory.get(expr('No(John)'), False) and memory.get(expr('FavouriteToy(John)'), False) and memory.get(expr('Lego(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Startup(John)'), False) and memory.get(expr('TrySomethingNew(John)'), False) and memory.get(expr('No(John)'), False) and memory.get(expr('FavouriteToy(John)'), False) and memory.get(expr('Play_doh(John)'), False) :
            return "you should learn Ruby", description('Ruby')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Wweb(John)'), False) and memory.get(expr('Web(John)'), False) and memory.get(expr('Back_end(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Startup(John)'), False) and memory.get(expr('TrySomethingNew(John)'), False) and memory.get(expr('No(John)'), False) and memory.get(expr('FavouriteToy(John)'), False) and memory.get(expr('Old_ugly(John)'), False) :
            return "you should learn Php", description('Php')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WhichPlatform(John)'), False) and memory.get(expr('Enterprise(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Im_a_fan(John)'), False) :
            return "you should learn C#", description('Csharp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Enterprise(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Not_bad(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Make_money(John)'), False) and memory.get(expr('WantToWorkFor(John)'), False) and memory.get(expr('Enterprise(John)'), False) and memory.get(expr('ThinkAboutMicrosoft(John)'), False) and memory.get(expr('Suck(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Just_for_fun(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Easy_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Just_for_fun(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Best_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Just_for_fun(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Auto(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Just_for_fun(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Manual(John)'), False) :
            return "you should learn C", description('C')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Just_for_fun(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Hardest_way(John)'), False) :
            return "you should learn C++", description('Cpp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Im_interested(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Easy_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Im_interested(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Best_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Im_interested(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Auto(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Im_interested(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Manual(John)'), False) :
            return "you should learn C", description('C')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Im_interested(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Hardest_way(John)'), False) :
            return "you should learn C++", description('Cpp')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Improve_myself(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Easy_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Improve_myself(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Best_way(John)'), False) :
            return "you should learn Python", description('Python')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Improve_myself(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Auto(John)'), False) :
            return "you should learn Java", description('Java')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Improve_myself(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Harder_way(John)'), False) and memory.get(expr('Car(John)'), False) and memory.get(expr('Manual(John)'), False) :
            return "you should learn C", description('C')
        if memory.get(expr('Why(John)'), False) and memory.get(expr('Improve_myself(John)'), False) and memory.get(expr('PreferToLearn(John)'), False) and memory.get(expr('Hardest_way(John)'), False) :
            return "you should learn C++", description('Cpp')
        

def description(lang):
    switch_case = {
        'Python': 'Python is a versatile and powerful programming language that is widely used in various domains such as web development, data analysis, artificial intelligence, and more. It has a simple and readable syntax, making it easy to learn and write.',
        'Java': 'Java is a popular programming language known for its platform independence and wide range of applications. It is commonly used for building enterprise-level applications, Android apps, and large-scale systems. Java offers strong support for object-oriented programming and has a vast ecosystem of libraries and frameworks.',
        'Cpp': 'C++ is a powerful programming language that is widely used for system-level programming, game development, and performance-critical applications. It provides low-level control over hardware resources and supports both procedural and object-oriented programming paradigms.',
        'Objectivec': 'Objective-C is a programming language used primarily for developing applications on Apple platforms, including iOS and macOS. It is an extension of the C programming language and provides additional features for object-oriented programming.',
        'JavaScript': 'JavaScript is a versatile scripting language that is primarily used for web development. It enables interactive and dynamic behavior on web pages and is supported by all modern web browsers. JavaScript can be used for both front-end and back-end development.',
        'Csharp': 'C# (pronounced C sharp) is a modern programming language developed by Microsoft. It is widely used for building Windows applications, web services, and game development using the Unity engine. C# combines the power of C++ with the simplicity of Visual Basic.',
        'Ruby': 'Ruby is a dynamic, object-oriented programming language known for its simplicity and productivity. It has an elegant syntax and focuses on developer happiness. Ruby is commonly used for web development, scripting, and automation tasks.',
        'Php': 'PHP is a popular server-side scripting language used for web development. It is widely supported and has a large community of developers. PHP is known for its simplicity and integration with databases, making it a popular choice for building dynamic websites.',
        'C': 'C is a general-purpose programming language known for its efficiency and low-level control. It is widely used for system programming, embedded systems, and developing high-performance applications. C serves as the foundation for many other programming languages.',
    }

    language_description = switch_case.get(lang, 'Language not found')
    return language_description