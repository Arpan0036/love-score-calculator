def calculate_Love_Score(name1,name2):
    combine_name=name1+name2
    lower_combine_name=combine_name.lower()

    t=lower_combine_name.count("t")
    r=lower_combine_name.count("r")
    u=lower_combine_name.count("u")
    e=lower_combine_name.count("e")
    
    digit1=t+r+u+e

    l=lower_combine_name.count("l")
    o=lower_combine_name.count("o")
    v=lower_combine_name.count("v")
    e=lower_combine_name.count("e")

    digit2=l+o+v+e

    love_score=int(str(digit1)+str(digit2))
    print(f"Your Love score is {love_score}!")

    if love_score<30:
        print("Your divorce is going to happen soon.🫂")
    elif love_score<=70:
        print("You are going to get married soon.👰🏼‍♀️")
    else:
        print("💗 A perfect match! True Soulmates!")


calculate_Love_Score(name1="Ahaan Roy",name2="Radhika Agarwal")
