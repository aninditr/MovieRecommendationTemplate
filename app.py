from flask import Flask
import random
from flask import make_response

app = Flask(__name__)

user_list = ["1","2","3","10","65"]
popular_movies = ["Movie_82","Movie_32","Movie_76","Movie_41","Movie_39"]

def predict(userid):
    print(userid,type(userid))
    if userid in user_list:
        randomlist = random.sample(range(25, 75), 5)
        print(randomlist,type(randomlist))
        rec_list = ["Movie_"+str(i) for i in randomlist]
    else:
        rec_list = popular_movies
    return rec_list

@app.route("/recommend/<userid>", methods=["GET"])
def recommend(userid):
    """
    Given a userid, recommend movies to the user.
    Return:
        - a list of movie IDs
    """
    #checks whether the user id is valid (integer)
    try: 
        type(int(userid)) == int 
    except: 
        validUserId = False
        return make_response({"error": "Invalid user ID - must be a number"}, 400)

    movie_recommendations = predict(userid)
    print(movie_recommendations,type(movie_recommendations))

    output = ','.join(movie_recommendations)
    return make_response({"message": "OK", "recommendations": output}, 200)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
    

# To run: flask run -h 0.0.0.0 -p 8082